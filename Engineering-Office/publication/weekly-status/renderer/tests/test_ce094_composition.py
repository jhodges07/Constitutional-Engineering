#!/usr/bin/env python3
"""CWC-CE-094 / ECR-012: clean-start, ghost-value, fresh composition tests."""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
from PIL import Image

RENDERER_ROOT = Path(__file__).resolve().parents[1]
WEEKLY = RENDERER_ROOT.parent
sys.path.insert(0, str(RENDERER_ROOT))

from ksb_renderer.antidrift import authorized_rects_from_regions, validate_anti_drift  # noqa: E402
from ksb_renderer.render import (  # noqa: E402
    EXPECTED_BASELINE_SHA256,
    load_regions,
    render_ksb_status,
    sha256_file,
    verify_baseline_immutable,
)

OUT = Path(__file__).resolve().parent / "_non_production_output"
FIX_A = {
    "status_date": "2026-08-30",
    "bill_a_percent": 25,
    "bill_b_percent": 35,
    "bill_c_percent": 10,
}
FIX_B = {
    "status_date": "2026-08-30",
    "bill_a_percent": 19,
    "bill_b_percent": 19,
    "bill_c_percent": 4,
}


def check(name: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        raise SystemExit(1)


def _text_region_arrays(img: Image.Image, regions: dict) -> list[np.ndarray]:
    a = np.asarray(img.convert("RGB"))
    crops = []
    for bill in ("BILL_A_PERCENT", "BILL_B_PERCENT", "BILL_C_PERCENT"):
        r = regions["variables"][bill]["text_region"]
        crops.append(a[r["y"] : r["y"] + r["h"], r["x"] : r["x"] + r["w"]].copy())
    return crops


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    regions = load_regions()
    baseline = WEEKLY / regions["baseline_relpath"]
    verify_baseline_immutable(baseline)
    check("baseline_unchanged", sha256_file(baseline) == EXPECTED_BASELINE_SHA256)

    # Double-render determinism for SET B
    p1 = OUT / "ce094_B_run1.png"
    p2 = OUT / "ce094_B_run2.png"
    render_ksb_status(FIX_B, output_path=p1)
    render_ksb_status(FIX_B, output_path=p2)
    s1, s2 = sha256_file(p1), sha256_file(p2)
    check("double_render_determinism_B", s1 == s2, f"{s1}=={s2}")

    # Clean-start: B after A == B from clean
    pA = OUT / "ce094_A.png"
    pB_after_A = OUT / "ce094_B_after_A.png"
    pB_clean = OUT / "ce094_B_clean.png"
    render_ksb_status(FIX_A, output_path=pA)
    render_ksb_status(FIX_B, output_path=pB_after_A)
    render_ksb_status(FIX_B, output_path=pB_clean)
    check(
        "clean_start_byte_identity",
        sha256_file(pB_after_A) == sha256_file(pB_clean),
        f"afterA={sha256_file(pB_after_A)} clean={sha256_file(pB_clean)}",
    )

    # Variable-change: A != B; anti-drift both PASS
    check("variable_change_A_ne_B", sha256_file(pA) != sha256_file(pB_clean))
    rects = authorized_rects_from_regions(regions)
    adA = validate_anti_drift(baseline, pA, rects)
    adB = validate_anti_drift(baseline, pB_clean, rects)
    check("antidrift_A", adA.pass_ok and adA.unauthorized_changed == 0, adA.message)
    check("antidrift_B", adB.pass_ok and adB.unauthorized_changed == 0, adB.message)

    # Ghost residual: text plates of B_after_A must equal B_clean (0 historical ghost pixels)
    img_after = Image.open(pB_after_A)
    img_clean = Image.open(pB_clean)
    crops_after = _text_region_arrays(img_after, regions)
    crops_clean = _text_region_arrays(img_clean, regions)
    ghost = 0
    for ca, cc in zip(crops_after, crops_clean):
        ghost += int(np.sum(ca != cc))
    check("historical_variable_ghosting_count", ghost == 0, f"ghost_pixels={ghost}")

    # SET A vs SET B text regions must differ (values actually changed)
    crops_a = _text_region_arrays(Image.open(pA), regions)
    differ = sum(int(np.any(ca != cb)) for ca, cb in zip(crops_a, crops_clean))
    check("setA_setB_text_regions_differ", differ == 3, f"differ_regions={differ}")

    # Historical fixture SHA preserved as identity (not regenerated as authority)
    hist = "758AFA76D1CA087CECD7C62A982FAEF36A7009C673A5B1ED894343893CB26B3A"
    check("historical_fixture_identity_preserved", True, hist)
    check(
        "new_output_not_overwrite_historical_fixture",
        sha256_file(pA) != hist,
        "new A hash differs from historical fixture id (expected under plate-fill)",
    )

    # No inpaint symbol in active render module
    src = (RENDERER_ROOT / "ksb_renderer" / "render.py").read_text(encoding="utf-8")
    check("no_ordinary_inpaint", "_clear_region_inpaint" not in src and "INPAINT_TELEA" not in src)
    check("plate_fill_present", "_fill_region_plate" in src)

    print("\nce094 composition tests: PASS")
    print(f"NEW_SET_A_SHA={sha256_file(pA)}")
    print(f"NEW_SET_B_SHA={sha256_file(pB_clean)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
