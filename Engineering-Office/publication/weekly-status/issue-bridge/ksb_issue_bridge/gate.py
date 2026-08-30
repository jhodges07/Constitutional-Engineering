"""Fail-closed gate validation for KSB Issue-trigger render requests."""

from __future__ import annotations

import json
import os
import re
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path
from typing import Any, Mapping, Optional, Sequence

from .constants import (
    BASELINE_ID,
    BODY_FENCE_END,
    BODY_FENCE_START,
    CLEAN_MASTER_ID,
    ENVELOPE_KEYS,
    PUBLICATION_REQUEST_TYPE,
    RENDER_PAYLOAD_KEYS,
    RENDERER_ID,
    REQUEST_ID_RE,
    REQUEST_SCHEMA_VERSION,
    SHA40_RE,
    TITLE_PREFIX,
    TRUSTED_ASSOCIATIONS,
)

_HOSTILE_RE = re.compile(
    r"[;`|$]|\$\(|&&|\|\||\.\./|\.\.\\|\\\\|/bin/|/usr/bin/|"
    r"powershell|cmd\.exe|Invoke-Expression|Start-Process|"
    r"https?://|git@|file://",
    re.IGNORECASE,
)


class GateReject(Exception):
    """Authorization or validation failure — fail closed."""

    def __init__(self, code: str, message: str) -> None:
        self.code = code
        self.message = message
        super().__init__(f"{code}: {message}")


@dataclass(frozen=True)
class NormalizedRequest:
    request_schema_version: str
    publication_request_type: str
    request_id: str
    canonical_sha: str
    baseline_id: str
    renderer_id: str
    status_date: str
    bill_a_percent: int
    bill_b_percent: int
    bill_c_percent: int
    issue_number: int
    actor_login: str
    author_association: str
    title: str

    def to_dict(self) -> dict[str, Any]:
        return asdict(self)

    def render_payload(self) -> dict[str, Any]:
        return {
            "status_date": self.status_date,
            "bill_a_percent": self.bill_a_percent,
            "bill_b_percent": self.bill_b_percent,
            "bill_c_percent": self.bill_c_percent,
        }

    def idempotency_key(self) -> str:
        return "|".join(
            [
                self.request_id,
                self.canonical_sha,
                self.status_date,
                str(self.bill_a_percent),
                str(self.bill_b_percent),
                str(self.bill_c_percent),
            ]
        )


def parse_authorized_actors(raw: Optional[str] = None) -> frozenset[str]:
    if raw is None:
        raw = os.environ.get("AUTHORIZED_KSB_RENDER_ACTORS", "")
    return frozenset(p.strip() for p in raw.split(",") if p.strip())


def parse_allowed_shas(raw: Optional[str] = None) -> frozenset[str]:
    if raw is None:
        raw = os.environ.get("ALLOWED_KSB_CANONICAL_SHAS", "")
    return frozenset(p.strip().lower() for p in raw.split(",") if p.strip())


def extract_request_json(issue_body: str) -> dict[str, Any]:
    if not isinstance(issue_body, str):
        raise GateReject("INVALID_INPUT", "issue body must be a string")
    start = issue_body.find(BODY_FENCE_START)
    if start < 0:
        raise GateReject("INVALID_INPUT", "missing ```ksb-render-request fence")
    start = issue_body.find("\n", start)
    if start < 0:
        raise GateReject("INVALID_INPUT", "malformed ksb-render-request fence")
    start += 1
    end = issue_body.find(BODY_FENCE_END, start)
    if end < 0:
        raise GateReject("INVALID_INPUT", "unclosed ksb-render-request fence")
    blob = issue_body[start:end].strip()
    try:
        data = json.loads(blob)
    except json.JSONDecodeError as exc:
        raise GateReject("INVALID_INPUT", f"malformed JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise GateReject("INVALID_INPUT", "request root must be a JSON object")
    return data


def _reject_hostile_string(field: str, value: str) -> None:
    if _HOSTILE_RE.search(value):
        raise GateReject("HOSTILE_INPUT", f"field {field} contains disallowed patterns")


def _parse_percent(name: str, value: Any) -> int:
    if isinstance(value, bool) or not isinstance(value, int):
        raise GateReject("INVALID_INPUT", f"{name} must be an integer")
    if value < 0 or value > 100:
        raise GateReject("INVALID_INPUT", f"{name} out of range 0–100")
    return value


def validate_envelope(
    data: Mapping[str, Any],
    *,
    allowed_shas: Sequence[str] | frozenset[str],
) -> NormalizedRequest:
    """Validate envelope+payload; issue metadata filled by caller via replace fields.

    Returns a NormalizedRequest with issue_number=0 and empty actor fields;
    gate_issue_event overwrites those from the Issue event.
    """
    unknown = set(data.keys()) - ENVELOPE_KEYS
    if unknown:
        raise GateReject("INVALID_INPUT", f"unknown envelope fields: {sorted(unknown)}")
    for key in ENVELOPE_KEYS:
        if key not in data:
            raise GateReject("INVALID_INPUT", f"missing envelope field: {key}")

    if data["request_schema_version"] != REQUEST_SCHEMA_VERSION:
        raise GateReject("INVALID_INPUT", "unsupported request_schema_version")
    if data["publication_request_type"] != PUBLICATION_REQUEST_TYPE:
        raise GateReject("INVALID_INPUT", "unsupported publication_request_type")

    request_id = data["request_id"]
    if not isinstance(request_id, str) or not REQUEST_ID_RE.match(request_id):
        raise GateReject("INVALID_INPUT", "invalid request_id")
    _reject_hostile_string("request_id", request_id)

    canonical_sha = data["canonical_sha"]
    if not isinstance(canonical_sha, str) or not SHA40_RE.match(canonical_sha.lower()):
        raise GateReject("INVALID_INPUT", "canonical_sha must be 40-char hex SHA")
    canonical_sha = canonical_sha.lower()
    allowed = {s.lower() for s in allowed_shas}
    if not allowed:
        raise GateReject("CONFIG", "ALLOWED_KSB_CANONICAL_SHAS is empty")
    if canonical_sha not in allowed:
        raise GateReject("UNAUTHORIZED_SHA", "canonical_sha not in allowlist")

    if data["baseline_id"] != BASELINE_ID:
        raise GateReject(
            "INVALID_INPUT",
            f"baseline_id mismatch: got={data['baseline_id']!r} expected={BASELINE_ID!r} "
            f"(baseline_id is HISTORICAL visual baseline; clean master "
            f"{CLEAN_MASTER_ID!r} is selected by renderer_id, not baseline_id)",
        )
    if data["renderer_id"] != RENDERER_ID:
        raise GateReject(
            "INVALID_INPUT",
            f"renderer_id mismatch: got={data['renderer_id']!r} expected={RENDERER_ID!r}",
        )

    payload = data["render_payload"]
    if not isinstance(payload, dict):
        raise GateReject("INVALID_INPUT", "render_payload must be object")
    unknown_p = set(payload.keys()) - RENDER_PAYLOAD_KEYS
    if unknown_p:
        raise GateReject(
            "INVALID_INPUT", f"unauthorized renderer fields: {sorted(unknown_p)}"
        )
    for key in RENDER_PAYLOAD_KEYS:
        if key not in payload:
            raise GateReject("INVALID_INPUT", f"missing render_payload field: {key}")

    # Reject alternate path / renderer selectors if smuggled as strings elsewhere — already
    # blocked by unknown field rules. Extra hostile check on status_date.
    status_date = payload["status_date"]
    if not isinstance(status_date, str):
        raise GateReject("INVALID_INPUT", "status_date must be string YYYY-MM-DD")
    _reject_hostile_string("status_date", status_date)
    try:
        date.fromisoformat(status_date)
    except ValueError as exc:
        raise GateReject("INVALID_INPUT", "status_date not YYYY-MM-DD") from exc

    a = _parse_percent("bill_a_percent", payload["bill_a_percent"])
    b = _parse_percent("bill_b_percent", payload["bill_b_percent"])
    c = _parse_percent("bill_c_percent", payload["bill_c_percent"])

    return NormalizedRequest(
        request_schema_version=REQUEST_SCHEMA_VERSION,
        publication_request_type=PUBLICATION_REQUEST_TYPE,
        request_id=request_id,
        canonical_sha=canonical_sha,
        baseline_id=BASELINE_ID,
        renderer_id=RENDERER_ID,
        status_date=status_date,
        bill_a_percent=a,
        bill_b_percent=b,
        bill_c_percent=c,
        issue_number=0,
        actor_login="",
        author_association="",
        title="",
    )


def authorize_actor(
    *,
    actor_login: str,
    author_association: str,
    authorized_actors: Sequence[str] | frozenset[str],
) -> None:
    if not actor_login or not isinstance(actor_login, str):
        raise GateReject("AUTHORIZATION_FAILED", "missing actor login")
    if actor_login not in set(authorized_actors):
        raise GateReject("AUTHORIZATION_FAILED", "actor not on allowlist")
    if author_association not in TRUSTED_ASSOCIATIONS:
        raise GateReject("AUTHORIZATION_FAILED", "author_association not trusted")


def authorize_title(title: str) -> None:
    if not isinstance(title, str) or not title.startswith(TITLE_PREFIX):
        raise GateReject("INVALID_INPUT", "title must start with [KSB-RENDER] ")


def check_idempotency(store_path: Path, key: str) -> None:
    store_path.parent.mkdir(parents=True, exist_ok=True)
    prior: set[str] = set()
    if store_path.is_file():
        try:
            prior = set(json.loads(store_path.read_text(encoding="utf-8")))
        except json.JSONDecodeError as exc:
            raise GateReject("CONFIG", f"corrupt idempotency store: {exc}") from exc
    if key in prior:
        raise GateReject("DUPLICATE", "identical request already succeeded")


def record_idempotency(store_path: Path, key: str) -> None:
    store_path.parent.mkdir(parents=True, exist_ok=True)
    prior: set[str] = set()
    if store_path.is_file():
        prior = set(json.loads(store_path.read_text(encoding="utf-8")))
    prior.add(key)
    store_path.write_text(json.dumps(sorted(prior), indent=2) + "\n", encoding="utf-8")


def gate_issue_event(
    event: Mapping[str, Any],
    *,
    authorized_actors: Optional[Sequence[str]] = None,
    allowed_shas: Optional[Sequence[str]] = None,
    idempotency_store: Optional[Path] = None,
    record_success: bool = False,
) -> NormalizedRequest:
    """Full gate: EVENT → AUTHORIZED → VALIDATED (+ optional idempotency)."""
    action = event.get("action")
    if action is not None and action != "opened":
        raise GateReject("EVENT_FILTER", "only issues opened are accepted")

    issue = event.get("issue")
    if not isinstance(issue, dict):
        raise GateReject("INVALID_INPUT", "missing issue object")

    title = issue.get("title", "")
    body = issue.get("body") or ""
    number = issue.get("number")
    user = issue.get("user") or {}
    actor_login = user.get("login", "")
    association = issue.get("author_association") or ""

    if not isinstance(number, int):
        raise GateReject("INVALID_INPUT", "issue number required")

    actors = (
        frozenset(authorized_actors)
        if authorized_actors is not None
        else parse_authorized_actors(None)
    )
    if not actors:
        raise GateReject("CONFIG", "AUTHORIZED_KSB_RENDER_ACTORS is empty")

    authorize_actor(
        actor_login=actor_login,
        author_association=str(association),
        authorized_actors=actors,
    )
    authorize_title(str(title))

    shas = (
        frozenset(allowed_shas) if allowed_shas is not None else parse_allowed_shas(None)
    )
    data = extract_request_json(str(body))
    base = validate_envelope(data, allowed_shas=shas)

    normalized = NormalizedRequest(
        request_schema_version=base.request_schema_version,
        publication_request_type=base.publication_request_type,
        request_id=base.request_id,
        canonical_sha=base.canonical_sha,
        baseline_id=base.baseline_id,
        renderer_id=base.renderer_id,
        status_date=base.status_date,
        bill_a_percent=base.bill_a_percent,
        bill_b_percent=base.bill_b_percent,
        bill_c_percent=base.bill_c_percent,
        issue_number=number,
        actor_login=actor_login,
        author_association=str(association),
        title=str(title),
    )

    if idempotency_store is not None:
        check_idempotency(idempotency_store, normalized.idempotency_key())
        if record_success:
            record_idempotency(idempotency_store, normalized.idempotency_key())

    return normalized


def build_issue_body(request: Mapping[str, Any]) -> str:
    return (
        "KSB render execution request (non-canonical).\n\n"
        f"{BODY_FENCE_START}\n"
        f"{json.dumps(request, indent=2)}\n"
        f"{BODY_FENCE_END}\n"
    )
