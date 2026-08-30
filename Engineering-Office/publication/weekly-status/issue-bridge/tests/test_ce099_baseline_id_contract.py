#!/usr/bin/env python3
"""CWC-CE-099 — reproduce Issue #6 baseline_id mismatch and prove corrected contract."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

_BRIDGE = Path(__file__).resolve().parents[1]
_WEEKLY = _BRIDGE.parent
_RENDERER = _WEEKLY / "renderer"
sys.path.insert(0, str(_BRIDGE))
sys.path.insert(0, str(_RENDERER))

from ksb_issue_bridge.constants import (  # noqa: E402
    BASELINE_ID,
    CLEAN_MASTER_ID,
    CLEAN_MASTER_SHA256,
    RENDERER_ID,
)
from ksb_issue_bridge.gate import GateReject, build_issue_body, gate_issue_event  # noqa: E402
from ksb_renderer.render import (  # noqa: E402
    EXPECTED_CLEAN_MASTER_SHA256,
    render_ksb_status,
    sha256_file,
)

OUT = Path(__file__).resolve().parent / "_non_production_output"
CANON = "87e48e631edbc21cc64d96cc2095a0b2703d63d0"
ACTOR = "jhodges07"
ACCEPTED_VISUAL_SHA = "78D5E2E1CA11078106DC4585867651915490E2B8745B7E2A08CDB3D303A111DD"


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        raise SystemExit(1)


def _req(**overrides):
    base = {
        "request_schema_version": "1.0.0",
        "publication_request_type": "KSB_WEEKLY_STATUS",
        "request_id": "KSB-RENDER-2026-08-30-005",
        "canonical_sha": CANON,
        "baseline_id": BASELINE_ID,
        "renderer_id": RENDERER_ID,
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


def _event(req: dict, number: int = 6):
    return {
        "action": "opened",
        "issue": {
            "number": number,
            "title": f"[KSB-RENDER] 2026-08-30 {req['request_id']}",
            "body": build_issue_body(req),
            "user": {"login": ACTOR},
            "author_association": "OWNER",
        },
    }


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    master = _WEEKLY / "templates" / "BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE.png"
    sha_before = sha256_file(master)

    check("expected_baseline_id", BASELINE_ID == "BL-WEEKLY-STATUS-BASELINE-v1.0")
    check("clean_master_not_baseline_field", CLEAN_MASTER_ID != BASELINE_ID)
    check("renderer_id", RENDERER_ID == "ksb_renderer@2.0.0-CWC-CE-097-CANDIDATE")

    # --- Reproduce Issue #6 ---
    bad = _req(baseline_id=CLEAN_MASTER_ID)
    try:
        gate_issue_event(
            _event(bad),
            authorized_actors=[ACTOR],
            allowed_shas=[CANON],
        )
        check("issue6_reproduced_reject", False, "should have rejected")
    except GateReject as exc:
        check(
            "issue6_reproduced_reject",
            exc.code == "INVALID_INPUT" and "baseline_id" in exc.message,
            f"{exc.code}: {exc.message}",
        )
        check(
            "issue6_reason_identifies_expectation",
            BASELINE_ID in exc.message or "mismatch" in exc.message,
            exc.message,
        )

    # --- Correct contract ACCEPT ---
    good = _req(request_id="KSB-RENDER-2026-08-30-099")
    try:
        n = gate_issue_event(
            _event(good, number=99),
            authorized_actors=[ACTOR],
            allowed_shas=[CANON],
        )
        check("correct_request_authorized", n.baseline_id == BASELINE_ID and n.renderer_id == RENDERER_ID)
    except Exception as exc:
        check("correct_request_authorized", False, str(exc))

    # --- Negatives ---
    cases = [
        ("wrong_clean_master_as_baseline", _req(baseline_id=CLEAN_MASTER_ID), "INVALID_INPUT"),
        ("wrong_baseline_other", _req(baseline_id="BL-WEEKLY-STATUS-BASELINE-v9.9"), "INVALID_INPUT"),
        ("wrong_renderer", _req(renderer_id="ksb_renderer@2.0.0-CWC-CE-096-CANDIDATE"), "INVALID_INPUT"),
        ("wrong_sha", _req(canonical_sha="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), "UNAUTHORIZED_SHA"),
        (
            "extra_field",
            _req(
                render_payload={
                    "status_date": "2026-08-30",
                    "bill_a_percent": 19,
                    "bill_b_percent": 19,
                    "bill_c_percent": 4,
                    "prompt": "x",
                }
            ),
            "INVALID_INPUT",
        ),
        (
            "malformed_missing_percent",
            _req(
                render_payload={
                    "status_date": "2026-08-30",
                    "bill_a_percent": 19,
                    "bill_b_percent": 19,
                }
            ),
            "INVALID_INPUT",
        ),
    ]
    for name, req, code in cases:
        try:
            gate_issue_event(_event(req, number=100), authorized_actors=[ACTOR], allowed_shas=[CANON])
            check(name, False, "should reject")
        except GateReject as exc:
            check(name, exc.code == code, f"{exc.code}: {exc.message}")

    try:
        gate_issue_event(
            _event(good),
            authorized_actors=[ACTOR],
            allowed_shas=[CANON],
            # attacker
        )
    except Exception:
        pass
    try:
        gate_issue_event(
            {
                "action": "opened",
                "issue": {
                    "number": 101,
                    "title": f"[KSB-RENDER] 2026-08-30 {good['request_id']}",
                    "body": build_issue_body(good),
                    "user": {"login": "attacker"},
                    "author_association": "NONE",
                },
            },
            authorized_actors=[ACTOR],
            allowed_shas=[CANON],
        )
        check("unauthorized_actor", False)
    except GateReject as exc:
        check("unauthorized_actor", exc.code == "AUTHORIZATION_FAILED", exc.code)

    # --- Local render (clean master path unchanged) ---
    payload = good["render_payload"]
    p1 = OUT / "ce099_B_run1.png"
    p2 = OUT / "ce099_B_run2.png"
    render_ksb_status(payload, output_path=p1)
    render_ksb_status(payload, output_path=p2)
    s1, s2 = sha256_file(p1), sha256_file(p2)
    check("determinism", s1 == s2, f"{s1}")
    check("visual_sha_matches_ce097_accepted", s1 == ACCEPTED_VISUAL_SHA, f"got={s1}")
    sha_after = sha256_file(master)
    check("master_immutable", sha_before == sha_after == CLEAN_MASTER_SHA256 == EXPECTED_CLEAN_MASTER_SHA256)
    check("clean_master_sha_constant", CLEAN_MASTER_SHA256 == EXPECTED_CLEAN_MASTER_SHA256)

    # Write machine-usable example for ChatGPT
    example = {
        "request_schema_version": "1.0.0",
        "publication_request_type": "KSB_WEEKLY_STATUS",
        "request_id": "KSB-RENDER-YYYY-MM-DD-NNN",
        "canonical_sha": CANON,
        "baseline_id": BASELINE_ID,
        "renderer_id": RENDERER_ID,
        "render_payload": {
            "status_date": "2026-08-30",
            "bill_a_percent": 19,
            "bill_b_percent": 19,
            "bill_c_percent": 4,
        },
        "_contract_notes": {
            "baseline_id_meaning": "HISTORICAL visual baseline identity (NOT clean master)",
            "clean_master_identity": CLEAN_MASTER_ID,
            "clean_master_selected_by": "renderer_id → repository renderer config (regions.json)",
            "do_not_put_clean_master_in_baseline_id": True,
        },
    }
    ex_path = OUT / "CWC-CE-099-CORRECTED-REQUEST-EXAMPLE.json"
    ex_path.write_text(json.dumps(example, indent=2) + "\n", encoding="utf-8")
    print(f"EXAMPLE={ex_path}")
    print(f"PNG_SHA={s1}")
    print("\nce099 baseline_id contract tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
