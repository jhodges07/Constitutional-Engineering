#!/usr/bin/env python3
"""Render job helper: verify clean master, invoke renderer, write RESULT.json.

Consumes ONLY gate-normalized JSON — never raw Issue text.
CWC-CE-097: clean master is ordinary render input; baseline is historical integrity only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

_BRIDGE_ROOT = Path(__file__).resolve().parents[1]
_WEEKLY = _BRIDGE_ROOT.parent
_RENDERER_ROOT = _WEEKLY / "renderer"
if str(_BRIDGE_ROOT) not in sys.path:
    sys.path.insert(0, str(_BRIDGE_ROOT))
if str(_RENDERER_ROOT) not in sys.path:
    sys.path.insert(0, str(_RENDERER_ROOT))

from ksb_issue_bridge.constants import (  # noqa: E402
    BASELINE_HEIGHT,
    BASELINE_ID,
    BASELINE_SHA256,
    BASELINE_WIDTH,
    CLEAN_MASTER_HEIGHT,
    CLEAN_MASTER_SHA256,
    CLEAN_MASTER_WIDTH,
)
from ksb_issue_bridge.result import build_result, write_result  # noqa: E402


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def main() -> int:
    parser = argparse.ArgumentParser(description="KSB Issue-bridge render helper")
    parser.add_argument("--normalized", required=True)
    parser.add_argument("--baseline", required=True)
    parser.add_argument("--out-dir", required=True)
    parser.add_argument("--run-id", type=int, default=0)
    args = parser.parse_args()

    request = json.loads(Path(args.normalized).read_text(encoding="utf-8-sig"))
    baseline = Path(args.baseline)
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    if not baseline.is_file():
        print("BASELINE missing", file=sys.stderr)
        return 3

    digest = _sha256_file(baseline)
    if digest != BASELINE_SHA256:
        print(f"BASELINE HASH MISMATCH got={digest}", file=sys.stderr)
        return 4

    from PIL import Image

    with Image.open(baseline) as im:
        w, h = im.size
    if (w, h) != (BASELINE_WIDTH, BASELINE_HEIGHT):
        print(f"BASELINE DIM MISMATCH {w}x{h}", file=sys.stderr)
        return 5

    from ksb_renderer.antidrift import authorized_rects_from_regions, validate_anti_drift
    from ksb_renderer.render import load_regions, render_ksb_status

    payload = {
        "status_date": request["status_date"],
        "bill_a_percent": request["bill_a_percent"],
        "bill_b_percent": request["bill_b_percent"],
        "bill_c_percent": request["bill_c_percent"],
    }
    out_png = out_dir / "ksb-status.png"
    regions = load_regions()
    clean_master = _WEEKLY / regions["clean_master_relpath"]

    if not clean_master.is_file():
        print("CLEAN MASTER missing", file=sys.stderr)
        return 3
    if _sha256_file(clean_master) != CLEAN_MASTER_SHA256:
        print(f"CLEAN MASTER HASH MISMATCH got={_sha256_file(clean_master)}", file=sys.stderr)
        return 4
    with Image.open(clean_master) as im:
        if im.size != (CLEAN_MASTER_WIDTH, CLEAN_MASTER_HEIGHT):
            print(f"CLEAN MASTER DIM MISMATCH {im.size}", file=sys.stderr)
            return 5

    try:
        img, _norm, _msha = render_ksb_status(
            payload, baseline_path=baseline, output_path=out_png
        )
    except Exception as exc:
        print(f"RENDER FAILED: {exc}", file=sys.stderr)
        result = build_result(
            request=request,
            run_id=args.run_id or None,
            output_filename="ksb-status.png",
            output_sha256="",
            output_width=0,
            output_height=0,
            renderer_test_result="FAIL",
            anti_drift_result="FAIL",
            execution_result="FAILED",
            baseline_sha256=BASELINE_SHA256,
        )
        write_result(out_dir / "RESULT.json", result)
        return 6

    out_digest = _sha256_file(out_png)
    ow, oh = img.size

    rects = authorized_rects_from_regions(regions)
    ad = validate_anti_drift(clean_master, out_png, rects)
    anti = "PASS" if ad.pass_ok else "FAIL"
    if not ad.pass_ok:
        print(f"ANTI-DRIFT FAILED: {ad.message}", file=sys.stderr)
        result = build_result(
            request=request,
            run_id=args.run_id or None,
            output_filename=out_png.name,
            output_sha256=out_digest,
            output_width=ow,
            output_height=oh,
            renderer_test_result="PASS",
            anti_drift_result=anti,
            execution_result="FAILED",
            baseline_sha256=BASELINE_SHA256,
        )
        write_result(out_dir / "RESULT.json", result)
        return 8

    result = build_result(
        request=request,
        run_id=args.run_id or None,
        output_filename=out_png.name,
        output_sha256=out_digest,
        output_width=ow,
        output_height=oh,
        renderer_test_result="PASS",
        anti_drift_result=anti,
        execution_result="SUCCEEDED",
        baseline_sha256=BASELINE_SHA256,
    )
    write_result(out_dir / "RESULT.json", result)
    print(f"RENDER PASS sha256={out_digest} baseline_id={BASELINE_ID}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
