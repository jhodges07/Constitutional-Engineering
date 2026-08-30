#!/usr/bin/env python3
"""Write a fence-safe KSB Issue body file (CWC-CE-102).

Usage (from repository root or any cwd — paths may be absolute):

  python Engineering-Office/publication/weekly-status/issue-bridge/scripts/write_ksb_issue_body.py \\
    --request path/to/request.json \\
    --out path/to/issue-body.md

Then (future hosted CWC only — NOT executed by CWC-CE-102):

  gh issue create -R jhodges07/Constitutional-Engineering \\
    --title \"[KSB-RENDER] ...\" \\
    --body-file path/to/issue-body.md

Do NOT embed triple-backtick fences in PowerShell `python -c` strings.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_BRIDGE = Path(__file__).resolve().parents[1]
if str(_BRIDGE) not in sys.path:
    sys.path.insert(0, str(_BRIDGE))

from ksb_issue_bridge.constants import BASELINE_ID, CLEAN_MASTER_ID, RENDERER_ID  # noqa: E402
from ksb_issue_bridge.issue_body import (  # noqa: E402
    assert_literal_fences,
    pre_submit_validate,
    write_issue_body_file,
)


def main() -> int:
    parser = argparse.ArgumentParser(description="Fence-safe KSB Issue body writer")
    parser.add_argument("--request", required=True, help="Path to request JSON object")
    parser.add_argument("--out", required=True, help="Path to write Issue body markdown")
    parser.add_argument(
        "--allowed-sha",
        action="append",
        default=[],
        help="Canonical SHA allowlist entry (repeatable). If omitted, skip full gate.",
    )
    parser.add_argument(
        "--preface",
        default=None,
        help="Optional preface text before the fenced block",
    )
    args = parser.parse_args()

    req_path = Path(args.request)
    request = json.loads(req_path.read_text(encoding="utf-8-sig"))
    if not isinstance(request, dict):
        print("request root must be a JSON object", file=sys.stderr)
        return 2

    # Soft guardrails (do not replace gate)
    if request.get("baseline_id") == CLEAN_MASTER_ID:
        print(
            "REFUSING: baseline_id must not be clean-master identity "
            f"(expected {BASELINE_ID!r})",
            file=sys.stderr,
        )
        return 3
    if request.get("baseline_id") and request["baseline_id"] != BASELINE_ID:
        print(
            f"WARNING: baseline_id={request['baseline_id']!r} "
            f"(canonical expected {BASELINE_ID!r})",
            file=sys.stderr,
        )
    if request.get("renderer_id") and request["renderer_id"] != RENDERER_ID:
        print(
            f"WARNING: renderer_id={request['renderer_id']!r} "
            f"(canonical expected {RENDERER_ID!r})",
            file=sys.stderr,
        )

    out = write_issue_body_file(request, args.out, preface=args.preface)
    body = out.read_text(encoding="utf-8").replace("\r\n", "\n")
    assert_literal_fences(body)

    if args.allowed_sha:
        pre_submit_validate(body, allowed_shas=args.allowed_sha)
        print("PRE_SUBMISSION: PASS")
    else:
        print("PRE_SUBMISSION: fence+roundtrip only (no SHA allowlist provided)")

    print(f"WROTE {out.resolve()}")
    fence_line = next(line for line in body.splitlines() if line.startswith(chr(96)))
    print(f"OPENING_FENCE_REPR={fence_line!r}")
    print(f"OPENING_BACKTICK_COUNT={fence_line.count(chr(96))}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
