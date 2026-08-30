#!/usr/bin/env python3
"""Successor-compatible composition checks under CWC-CE-097 clean-template architecture."""

from __future__ import annotations

import sys
from pathlib import Path

RENDERER_ROOT = Path(__file__).resolve().parents[1]
WEEKLY = RENDERER_ROOT.parent
sys.path.insert(0, str(RENDERER_ROOT))

from ksb_renderer.antidrift import authorized_rects_from_regions, validate_anti_drift  # noqa: E402
from ksb_renderer.render import (  # noqa: E402
    EXPECTED_BASELINE_SHA256,
    EXPECTED_CLEAN_MASTER_SHA256,
    load_regions,
    render_ksb_status,
    sha256_file,
    verify_baseline_immutable,
    verify_clean_master,
)

OUT = Path(__file__).resolve().parent / "_non_production_output"
FIX_A = {"status_date": "2026-08-30", "bill_a_percent": 25, "bill_b_percent": 35, "bill_c_percent": 10}
FIX_B = {"status_date": "2026-08-30", "bill_a_percent": 19, "bill_b_percent": 19, "bill_c_percent": 4}


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        raise SystemExit(1)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    regions = load_regions()
    baseline = WEEKLY / regions["baseline_relpath"]
    master = WEEKLY / regions["clean_master_relpath"]
    verify_baseline_immutable(baseline)
    verify_clean_master(master)
    check("baseline_unchanged", sha256_file(baseline) == EXPECTED_BASELINE_SHA256)
    check("clean_master_present", sha256_file(master) == EXPECTED_CLEAN_MASTER_SHA256)

    p1 = OUT / "ce094_B_run1.png"
    p2 = OUT / "ce094_B_run2.png"
    render_ksb_status(FIX_B, output_path=p1)
    render_ksb_status(FIX_B, output_path=p2)
    check("double_render_determinism_B", sha256_file(p1) == sha256_file(p2))

    pA = OUT / "ce094_A.png"
    pB_after_A = OUT / "ce094_B_after_A.png"
    pB_clean = OUT / "ce094_B_clean.png"
    render_ksb_status(FIX_A, output_path=pA)
    render_ksb_status(FIX_B, output_path=pB_after_A)
    render_ksb_status(FIX_B, output_path=pB_clean)
    check("clean_start_byte_identity", sha256_file(pB_after_A) == sha256_file(pB_clean))
    check("variable_change_A_ne_B", sha256_file(pA) != sha256_file(pB_clean))

    rects = authorized_rects_from_regions(regions)
    adA = validate_anti_drift(master, pA, rects)
    adB = validate_anti_drift(master, pB_clean, rects)
    check("antidrift_A", adA.pass_ok, adA.message)
    check("antidrift_B", adB.pass_ok, adB.message)

    src = (RENDERER_ROOT / "ksb_renderer" / "render.py").read_text(encoding="utf-8")
    check("no_ordinary_inpaint", "INPAINT_TELEA" not in src)
    check("clean_master_architecture", "verify_clean_master" in src and ".copy()" in src)
    print("\nce094 successor-compatible tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
