#!/usr/bin/env python3
"""CWC-CE-102 — fence-safe Issue body construction tests (KSB-RENDER-004)."""

from __future__ import annotations

import json
import sys
from pathlib import Path

_BRIDGE = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(_BRIDGE))

from ksb_issue_bridge.constants import (  # noqa: E402
    BASELINE_ID,
    BODY_FENCE_END,
    BODY_FENCE_START,
    CLEAN_MASTER_ID,
    RENDERER_ID,
)
from ksb_issue_bridge.gate import GateReject, extract_request_json, validate_envelope  # noqa: E402
from ksb_issue_bridge.issue_body import (  # noqa: E402
    assert_literal_fences,
    gh_issue_create_argv,
    powershell_corruption_demo,
    pre_submit_validate,
    write_issue_body_file,
)

OUT = Path(__file__).resolve().parent / "_non_production_output"
CANON = "037e81143c3b56c624d67b2ab5e28963a3d4a3d3"
# Non-production local test identity (matches REQUEST_ID_RE; not next hosted 007)
TEST_REQUEST_ID = "KSB-RENDER-2026-08-30-900"


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        raise SystemExit(1)


def _request(**overrides):
    base = {
        "request_schema_version": "1.0.0",
        "publication_request_type": "KSB_WEEKLY_STATUS",
        "request_id": TEST_REQUEST_ID,
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


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)

    # --- Parser contract ---
    check("opening_fence_constant", BODY_FENCE_START == chr(96) * 3 + "ksb-render-request")
    check("closing_fence_constant", BODY_FENCE_END == chr(96) * 3)
    check("opening_backtick_count_3", BODY_FENCE_START.count(chr(96)) == 3)
    check("baseline_unchanged", BASELINE_ID == "BL-WEEKLY-STATUS-BASELINE-v1.0")
    check("clean_master_not_baseline", CLEAN_MASTER_ID != BASELINE_ID)
    check("renderer_unchanged", RENDERER_ID == "ksb_renderer@2.0.0-CWC-CE-097-CANDIDATE")

    # --- Reproduce CWC-CE-101 PowerShell corruption ---
    intended = chr(96) * 3 + "ksb-render-request"
    corrupted = powershell_corruption_demo(intended)
    check(
        "ps_corruption_collapses_triple_to_single",
        corrupted == "`ksb-render-request",
        f"intended={intended!r} corrupted={corrupted!r}",
    )
    corrupted_body = (
        "KSB render execution request (non-canonical).\n\n"
        f"{corrupted}\n"
        + json.dumps(_request(), indent=2)
        + "\n`\n"
    )
    try:
        extract_request_json(corrupted_body)
        check("ce101_corrupted_body_rejects", False)
    except GateReject as exc:
        check(
            "ce101_corrupted_body_rejects",
            exc.code == "INVALID_INPUT" and "fence" in exc.message,
            f"{exc.code}: {exc.message}",
        )

    # Issue #7 observed pattern evidence (single-backtick open/close)
    issue7_style = corrupted_body
    check("issue7_style_lacks_triple_open", BODY_FENCE_START not in issue7_style)

    # --- Fence-safe construction ---
    req = _request()
    body_path = OUT / "ce102_fence_safe_body.md"
    write_issue_body_file(req, body_path)
    body = body_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    assert_literal_fences(body)
    check("safe_body_has_triple_open", BODY_FENCE_START in body)
    check("safe_body_open_line", any(line == BODY_FENCE_START for line in body.splitlines()))
    check(
        "safe_open_backtick_count",
        next(line for line in body.splitlines() if "ksb-render-request" in line).count(chr(96))
        == 3,
    )

    # Round-trip identity
    again = body_path.read_text(encoding="utf-8").replace("\r\n", "\n")
    check("round_trip_body_identity", again == body)

    # Canonical parser
    data = extract_request_json(body)
    check("json_extraction", data["request_id"] == TEST_REQUEST_ID)
    check("json_baseline", data["baseline_id"] == BASELINE_ID)
    check("json_renderer", data["renderer_id"] == RENDERER_ID)
    n = validate_envelope(data, allowed_shas=[CANON])
    check("local_gate_accept", n.bill_a_percent == 19 and n.bill_c_percent == 4)
    pre_submit_validate(body, allowed_shas=[CANON])
    check("pre_submission_validate", True)

    # --- Negative fence tests (parser remains strict) ---
    good_json = json.dumps(req, indent=2)

    def reject_body(label: str, text: str) -> None:
        try:
            extract_request_json(text)
            check(label, False, "should reject")
        except GateReject as exc:
            check(label, exc.code == "INVALID_INPUT", f"{exc.code}: {exc.message}")

    reject_body(
        "single_backtick_open",
        f"intro\n\n`ksb-render-request\n{good_json}\n`\n",
    )
    reject_body(
        "double_backtick_open",
        f"intro\n\n``ksb-render-request\n{good_json}\n``\n",
    )
    reject_body(
        "wrong_identifier",
        f"intro\n\n{chr(96)*3}json\n{good_json}\n{chr(96)*3}\n",
    )
    reject_body(
        "missing_closing_fence",
        f"intro\n\n{BODY_FENCE_START}\n{good_json}\n",
    )
    reject_body(
        "malformed_json",
        f"intro\n\n{BODY_FENCE_START}\n{{not json}}\n{BODY_FENCE_END}\n",
    )
    # Correct triple still ACCEPT
    extract_request_json(body)
    check("correct_triple_still_accept", True)
    check("strict_parser_preserved", True)

    # gh argv uses --body-file
    argv = gh_issue_create_argv(
        repo="jhodges07/Constitutional-Engineering",
        title="[KSB-RENDER] 2026-08-30 TEST",
        body_file=body_path,
    )
    check("gh_uses_body_file", "--body-file" in argv and str(body_path) in argv)
    check("gh_no_body_inline", "--body" not in argv)

    # Script CLI path
    req_json = OUT / "ce102_test_request.json"
    req_json.write_text(json.dumps(req, indent=2) + "\n", encoding="utf-8")
    script = _BRIDGE / "scripts" / "write_ksb_issue_body.py"
    import subprocess

    proc = subprocess.run(
        [
            sys.executable,
            str(script),
            "--request",
            str(req_json),
            "--out",
            str(OUT / "ce102_script_body.md"),
            "--allowed-sha",
            CANON,
        ],
        capture_output=True,
        text=True,
        check=False,
    )
    check("write_script_exit0", proc.returncode == 0, proc.stderr or proc.stdout)
    check("write_script_pre_submit", "PRE_SUBMISSION: PASS" in proc.stdout)
    script_body = (OUT / "ce102_script_body.md").read_text(encoding="utf-8")
    check("write_script_fence", BODY_FENCE_START in script_body.replace("\r\n", "\n"))

    # Production request id not consumed
    check("no_production_request_006", TEST_REQUEST_ID != "KSB-RENDER-2026-08-30-006")
    check("no_production_request_007", TEST_REQUEST_ID != "KSB-RENDER-2026-08-30-007")

    print("\nce102 fence-safe construction tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
