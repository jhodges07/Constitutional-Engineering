"""
NON-PRODUCTION test suite for KSB Status deterministic renderer (CWC-CE-097).

Run:
  python Engineering-Office/publication/weekly-status/renderer/tests/run_tests.py
"""

from __future__ import annotations

import json
import sys
import traceback
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]  # weekly-status/
RENDERER_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RENDERER_ROOT))

from ksb_renderer.antidrift import authorized_rects_from_regions, validate_anti_drift  # noqa: E402
from ksb_renderer.contract import InputValidationError, format_status_date, validate_and_normalize  # noqa: E402
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
FIX = Path(__file__).resolve().parent / "fixtures"


def _load_fixture(name: str) -> dict:
    raw = json.loads((FIX / name).read_text(encoding="utf-8"))
    raw.pop("_comment", None)
    return raw


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    regions = load_regions()
    baseline = ROOT / regions["baseline_relpath"]
    master = ROOT / regions["clean_master_relpath"]
    rects = authorized_rects_from_regions(regions)
    results = []

    def check(name: str, ok: bool, detail: str = "") -> None:
        results.append((name, ok, detail))
        status = "PASS" if ok else "FAIL"
        print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))

    try:
        start_sha = verify_baseline_immutable(baseline)
        check("baseline_start_integrity", start_sha == EXPECTED_BASELINE_SHA256, start_sha)
        msha = verify_clean_master(master)
        check("clean_master_start_integrity", msha == EXPECTED_CLEAN_MASTER_SHA256, msha)
    except Exception as exc:
        check("baseline_start_integrity", False, str(exc))
        _print_summary(results)
        return 1

    try:
        inp = _load_fixture("A_placeholder_equivalent.json")
        p1 = OUT / "A_run1.png"
        p2 = OUT / "A_run2.png"
        img1, norm, _ = render_ksb_status(inp, output_path=p1)
        img2, _, _ = render_ksb_status(inp, output_path=p2)
        s1, s2 = sha256_file(p1), sha256_file(p2)
        check("determinism_sha_identity", s1 == s2, f"run1={s1} run2={s2}")
        a = list(img1.getdata())
        b = list(img2.getdata())
        pixdiff = sum(1 for i in range(len(a)) if a[i] != b[i])
        check("determinism_pixel_identity", pixdiff == 0, f"pixdiff={pixdiff}")
        ad = validate_anti_drift(master, p1, rects)
        check("antidrift_A", ad.pass_ok, ad.message)
        check(
            "status_date_compact_A",
            norm.status_date_compact == format_status_date(norm.calendar_date),
            norm.status_date_compact,
        )
        check("status_date_expected_A", norm.status_date_compact == "2026.08.35", norm.status_date_compact)
        check("dims_A", img1.size == (1536, 912), str(img1.size))
    except Exception:
        check("fixture_A_block", False, traceback.format_exc())

    try:
        inp = _load_fixture("B_different_valid.json")
        p = OUT / "B_different.png"
        img, norm, _ = render_ksb_status(inp, output_path=p)
        ad = validate_anti_drift(master, p, rects)
        check("antidrift_B", ad.pass_ok, ad.message)
        check("dims_B", img.size == (1536, 912), str(img.size))
        check("status_date_B", norm.status_date_compact == "2026.01.03", norm.status_date_compact)
    except Exception:
        check("fixture_B_block", False, traceback.format_exc())

    try:
        inp = _load_fixture("D_boundary_values.json")
        p = OUT / "D_boundary.png"
        _, norm, _ = render_ksb_status(inp, output_path=p)
        ad = validate_anti_drift(master, p, rects)
        check("antidrift_D", ad.pass_ok, ad.message)
        check("boundary_percents", norm.bill_a_percent == 0 and norm.bill_b_percent == 100, str(norm))
    except Exception:
        check("fixture_D_block", False, traceback.format_exc())

    try:
        validate_and_normalize(
            {"status_date": "not-a-date", "bill_a_percent": 1, "bill_b_percent": 1, "bill_c_percent": 1}
        )
        check("invalid_date", False, "should have raised")
    except InputValidationError as exc:
        check("invalid_date", True, str(exc))

    try:
        validate_and_normalize({"status_date": "2026-08-30", "bill_a_percent": 1, "bill_b_percent": 1})
        check("missing_percent", False, "should have raised")
    except InputValidationError as exc:
        check("missing_percent", True, str(exc))

    try:
        validate_and_normalize(
            {"status_date": "2026-08-30", "bill_a_percent": -1, "bill_b_percent": 1, "bill_c_percent": 1}
        )
        check("below_range", False, "should have raised")
    except InputValidationError as exc:
        check("below_range", True, str(exc))

    try:
        validate_and_normalize(
            {"status_date": "2026-08-30", "bill_a_percent": 101, "bill_b_percent": 1, "bill_c_percent": 1}
        )
        check("above_range", False, "should have raised")
    except InputValidationError as exc:
        check("above_range", True, str(exc))

    try:
        validate_and_normalize(
            {
                "status_date": "2026-08-30",
                "bill_a_percent": 10.5,
                "bill_b_percent": 1,
                "bill_c_percent": 1,
            }
        )
        check("fractional_reject", False, "should have raised")
    except InputValidationError as exc:
        check("fractional_reject", True, str(exc))

    try:
        validate_and_normalize(
            {
                "status_date": "2026-08-30",
                "bill_a_percent": 1,
                "bill_b_percent": 1,
                "bill_c_percent": 1,
                "extra": 1,
            }
        )
        check("no_fifth_variable", False, "should have raised")
    except InputValidationError as exc:
        check("no_fifth_variable", True, str(exc))

    try:
        inp = _load_fixture("A_placeholder_equivalent.json")
        p = OUT / "J_mutated_fixed.png"
        img, _, _ = render_ksb_status(inp, output_path=p)
        pix = img.load()
        pix[100, 100] = (255, 0, 0)
        img.save(p, format="PNG", compress_level=9, optimize=False)
        ad = validate_anti_drift(master, p, rects)
        check(
            "negative_fixed_mutation_rejects",
            (not ad.pass_ok) and ad.unauthorized_changed > 0,
            ad.message,
        )
    except Exception:
        check("negative_fixed_mutation_rejects", False, traceback.format_exc())

    end_sha = sha256_file(baseline)
    check("baseline_end_immutability", end_sha == EXPECTED_BASELINE_SHA256, end_sha)
    check("clean_master_end_immutability", sha256_file(master) == EXPECTED_CLEAN_MASTER_SHA256)

    return _print_summary(results)


def _print_summary(results) -> int:
    failed = [r for r in results if not r[1]]
    print("\n=== SUMMARY ===")
    print(f"total={len(results)} pass={len(results)-len(failed)} fail={len(failed)}")
    for name, ok, detail in failed:
        print(f"  FAIL {name}: {detail}")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main())
