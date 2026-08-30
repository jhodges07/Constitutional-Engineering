#!/usr/bin/env python3
"""Local security/schema tests for KSB Issue-bridge gate (not remote Actions proof)."""

from __future__ import annotations

import json
import sys
import tempfile
from pathlib import Path

_BRIDGE_ROOT = Path(__file__).resolve().parents[1]
if str(_BRIDGE_ROOT) not in sys.path:
    sys.path.insert(0, str(_BRIDGE_ROOT))

from ksb_issue_bridge.gate import GateReject, build_issue_body, gate_issue_event
from ksb_issue_bridge.result import build_result

CANON = "4aeaf60b330ad41b5750ce523ad850a75325aa78"
ACTOR = "jhodges07"


def _request(**overrides):
    base = {
        "request_schema_version": "1.0.0",
        "publication_request_type": "KSB_WEEKLY_STATUS",
        "request_id": "KSB-RENDER-2026-08-30-001",
        "canonical_sha": CANON,
        "baseline_id": "BL-WEEKLY-STATUS-BASELINE-v1.0",
        "renderer_id": "ksb_renderer@2.0.0-CWC-CE-097-CANDIDATE",
        "render_payload": {
            "status_date": "2026-08-30",
            "bill_a_percent": 19,
            "bill_b_percent": 19,
            "bill_c_percent": 4,
        },
    }
    base.update(overrides)
    if "render_payload" in overrides:
        base["render_payload"] = overrides["render_payload"]
    return base


def _event(login=ACTOR, association="OWNER", title=None, body=None, number=2):
    req = _request()
    title = title or f"[KSB-RENDER] 2026-08-30 {req['request_id']}"
    body = body if body is not None else build_issue_body(req)
    return {
        "action": "opened",
        "issue": {
            "number": number,
            "title": title,
            "body": body,
            "user": {"login": login},
            "author_association": association,
        },
    }


def expect_reject(code: str, **kwargs) -> None:
    try:
        gate_issue_event(
            _event(**kwargs) if "login" in kwargs or "association" in kwargs or "title" in kwargs or "body" in kwargs else _event(),
            authorized_actors=[ACTOR],
            allowed_shas=[CANON],
        )
        raise AssertionError(f"expected reject {code}")
    except GateReject as exc:
        assert exc.code == code, f"expected {code} got {exc.code}: {exc.message}"


def main() -> int:
    results = []

    def check(name: str, ok: bool, detail: str = "") -> None:
        results.append((name, ok))
        print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))

    # Authorized
    try:
        n = gate_issue_event(
            _event(), authorized_actors=[ACTOR], allowed_shas=[CANON]
        )
        check("authorized_actor", n.request_id == "KSB-RENDER-2026-08-30-001")
        check("four_variable_payload", n.bill_a_percent == 19 and n.bill_c_percent == 4)
        check("sha_binding", n.canonical_sha == CANON)
    except Exception as exc:
        check("authorized_actor", False, str(exc))

    # Unauthorized actor (public copy)
    try:
        gate_issue_event(
            _event(login="attacker", association="NONE"),
            authorized_actors=[ACTOR],
            allowed_shas=[CANON],
        )
        check("unauthorized_actor", False, "should reject")
    except GateReject as exc:
        check("unauthorized_actor", exc.code == "AUTHORIZATION_FAILED", exc.code)

    # COLLABORATOR without allowlist membership
    try:
        gate_issue_event(
            _event(login="random-collab", association="COLLABORATOR"),
            authorized_actors=[ACTOR],
            allowed_shas=[CANON],
        )
        check("copied_request_collab", False)
    except GateReject as exc:
        check("copied_request_collab", exc.code == "AUTHORIZATION_FAILED", exc.code)

    # Fifth field
    req = _request()
    req["render_payload"]["prompt"] = "make it pretty"
    try:
        gate_issue_event(
            _event(body=build_issue_body(req)),
            authorized_actors=[ACTOR],
            allowed_shas=[CANON],
        )
        check("fifth_field", False)
    except GateReject as exc:
        check("fifth_field", exc.code == "INVALID_INPUT", exc.message)

    # Malformed JSON
    try:
        gate_issue_event(
            _event(body="```ksb-render-request\n{not json\n```\n"),
            authorized_actors=[ACTOR],
            allowed_shas=[CANON],
        )
        check("malformed_json", False)
    except GateReject as exc:
        check("malformed_json", exc.code == "INVALID_INPUT")

    # Missing field
    req = _request()
    del req["render_payload"]["bill_c_percent"]
    try:
        gate_issue_event(
            _event(body=build_issue_body(req)),
            authorized_actors=[ACTOR],
            allowed_shas=[CANON],
        )
        check("missing_field", False)
    except GateReject as exc:
        check("missing_field", exc.code == "INVALID_INPUT")

    # Percent bounds / types
    for label, payload, expect in [
        ("pct_neg", {**_request()["render_payload"], "bill_a_percent": -1}, "INVALID_INPUT"),
        ("pct_hi", {**_request()["render_payload"], "bill_a_percent": 101}, "INVALID_INPUT"),
        ("pct_str", {**_request()["render_payload"], "bill_a_percent": "19"}, "INVALID_INPUT"),
    ]:
        req = _request(render_payload=payload)
        try:
            gate_issue_event(
                _event(body=build_issue_body(req)),
                authorized_actors=[ACTOR],
                allowed_shas=[CANON],
            )
            check(label, False)
        except GateReject as exc:
            check(label, exc.code == expect, exc.code)

    # Hostile / path / shell
    for label, mutate in [
        (
            "shell_meta",
            lambda r: r.update({"request_id": "KSB-RENDER-2026-08-30-001; rm -rf /"}),
        ),
        (
            "path_traversal",
            lambda r: r.__setitem__(
                "canonical_sha", "4aeaf60b330ad41b5750ce523ad850a75325aa78"
            )
            or r.update({"baseline_id": "../etc/passwd"}),
        ),
        (
            "alt_renderer",
            lambda r: r.update({"renderer_id": "evil.py"}),
        ),
        (
            "http_url",
            lambda r: (
                r.update({"request_id": "KSB-RENDER-2026-08-30-001"}),
                r.__setitem__("canonical_sha", CANON),
                r.update({"baseline_id": "http://evil.example/x"}),
            ),
        ),
    ]:
        req = _request()
        mutate(req)
        # Fix request_id if shell_meta broke regex — expect INVALID or HOSTILE
        try:
            gate_issue_event(
                _event(body=build_issue_body(req)),
                authorized_actors=[ACTOR],
                allowed_shas=[CANON],
            )
            check(label, False, "should reject")
        except GateReject as exc:
            check(label, exc.code in {"INVALID_INPUT", "HOSTILE_INPUT", "UNAUTHORIZED_SHA"}, exc.code)

    # Unauthorized SHA
    req = _request(canonical_sha="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
    try:
        gate_issue_event(
            _event(body=build_issue_body(req)),
            authorized_actors=[ACTOR],
            allowed_shas=[CANON],
        )
        check("unauthorized_sha", False)
    except GateReject as exc:
        check("unauthorized_sha", exc.code == "UNAUTHORIZED_SHA", exc.code)

    # Title routing only — wrong title rejected even if actor ok
    try:
        gate_issue_event(
            _event(title="Please render"),
            authorized_actors=[ACTOR],
            allowed_shas=[CANON],
        )
        check("title_prefix", False)
    except GateReject as exc:
        check("title_prefix", exc.code == "INVALID_INPUT")

    # Idempotency
    with tempfile.TemporaryDirectory() as td:
        store = Path(td) / "idem.json"
        n1 = gate_issue_event(
            _event(),
            authorized_actors=[ACTOR],
            allowed_shas=[CANON],
            idempotency_store=store,
            record_success=True,
        )
        try:
            gate_issue_event(
                _event(),
                authorized_actors=[ACTOR],
                allowed_shas=[CANON],
                idempotency_store=store,
            )
            check("idempotency", False)
        except GateReject as exc:
            check("idempotency", exc.code == "DUPLICATE" and n1.request_id.startswith("KSB-RENDER-"), exc.code)

    # RESULT contract shape
    n = gate_issue_event(_event(), authorized_actors=[ACTOR], allowed_shas=[CANON])
    result = build_result(
        request=n.to_dict(),
        run_id=123,
        output_filename="ksb-status.png",
        output_sha256="ABC",
        output_width=1536,
        output_height=912,
        renderer_test_result="PASS",
        anti_drift_result="PASS",
        execution_result="SUCCEEDED",
        baseline_sha256="17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9",
    )
    required = {
        "schema_version",
        "request_id",
        "issue_number",
        "run_id",
        "canonical_sha",
        "status_date",
        "bill_a_percent",
        "bill_b_percent",
        "bill_c_percent",
        "baseline_id",
        "baseline_sha256",
        "renderer_identity",
        "output_filename",
        "output_sha256",
        "output_width",
        "output_height",
        "renderer_test_result",
        "anti_drift_result",
        "execution_result",
    }
    check("result_contract", required <= set(result.keys()))

    failed = [n for n, ok in results if not ok]
    print(f"\n{len(results) - len(failed)}/{len(results)} PASS")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
