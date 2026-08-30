#!/usr/bin/env python3
"""CLI entry for GitHub Actions gate job (and local simulation)."""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

# Allow running from repo without install
_BRIDGE_ROOT = Path(__file__).resolve().parents[1]
if str(_BRIDGE_ROOT) not in sys.path:
    sys.path.insert(0, str(_BRIDGE_ROOT))

from ksb_issue_bridge.gate import GateReject, gate_issue_event  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description="KSB Issue-bridge gate")
    parser.add_argument("--event-json", required=True, help="Path to GitHub event JSON")
    parser.add_argument("--out", required=True, help="Path to write normalized request JSON")
    parser.add_argument(
        "--idempotency-store",
        default="",
        help="Optional path to idempotency JSON store",
    )
    parser.add_argument(
        "--github-output",
        default="",
        help="Optional path to append GitHub Actions outputs",
    )
    args = parser.parse_args()

    event = json.loads(Path(args.event_json).read_text(encoding="utf-8"))
    store = Path(args.idempotency_store) if args.idempotency_store else None

    try:
        normalized = gate_issue_event(
            event,
            authorized_actors=None,  # from env AUTHORIZED_KSB_RENDER_ACTORS
            allowed_shas=None,  # from env ALLOWED_KSB_CANONICAL_SHAS
            idempotency_store=store,
            record_success=False,
        )
    except GateReject as exc:
        print(f"GATE REJECT {exc.code}: {exc.message}", file=sys.stderr)
        if args.github_output:
            with open(args.github_output, "a", encoding="utf-8") as fh:
                fh.write("authorized=false\n")
                fh.write(f"reject_code={exc.code}\n")
                fh.write(f"reject_message={exc.message}\n")
        return 2

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(normalized.to_dict(), indent=2) + "\n", encoding="utf-8")

    if args.github_output:
        with open(args.github_output, "a", encoding="utf-8") as fh:
            fh.write("authorized=true\n")
            fh.write(f"request_id={normalized.request_id}\n")
            fh.write(f"canonical_sha={normalized.canonical_sha}\n")
            fh.write(f"issue_number={normalized.issue_number}\n")
            fh.write(f"artifact_name=ksb-render-{normalized.request_id}\n")

    print(f"GATE PASS request_id={normalized.request_id}")
    return 0


if __name__ == "__main__":
    # Ensure env vars present in Actions; local CLI may set them.
    if not os.environ.get("AUTHORIZED_KSB_RENDER_ACTORS"):
        print("WARNING: AUTHORIZED_KSB_RENDER_ACTORS unset", file=sys.stderr)
    if not os.environ.get("ALLOWED_KSB_CANONICAL_SHAS"):
        print("WARNING: ALLOWED_KSB_CANONICAL_SHAS unset", file=sys.stderr)
    raise SystemExit(main())
