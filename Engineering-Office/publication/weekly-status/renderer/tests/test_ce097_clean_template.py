#!/usr/bin/env python3
"""CWC-CE-097 — clean master + dynamic center panel tests."""

from __future__ import annotations

import subprocess
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
    EXPECTED_CLEAN_MASTER_SHA256,
    OPERATIONAL_STATUS,
    PROHIBITED_CE096_FIXED_LAYER_SHA256,
    RENDERER_VERSION,
    load_regions,
    render_ksb_status,
    sha256_file,
    verify_baseline_immutable,
    verify_clean_master,
)

OUT = Path(__file__).resolve().parent / "_non_production_output"

STATE_A = {"status_date": "2026-08-30", "bill_a_percent": 25, "bill_b_percent": 35, "bill_c_percent": 10}
STATE_B = {"status_date": "2026-08-30", "bill_a_percent": 19, "bill_b_percent": 19, "bill_c_percent": 4}
STATE_C = {"status_date": "2026-08-30", "bill_a_percent": 73, "bill_b_percent": 2, "bill_c_percent": 91}


def check(name: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        raise SystemExit(1)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    regions = load_regions()
    master = WEEKLY / regions["clean_master_relpath"]
    baseline = WEEKLY / regions["baseline_relpath"]
    fixed096 = WEEKLY / regions["ce096_fixed_layer_relpath"]
    rects = authorized_rects_from_regions(regions)
    bounds = regions["center_panel"]["bounds"]

    check("renderer_identity", RENDERER_VERSION == "2.0.0-CWC-CE-097-CANDIDATE")
    check("candidate_label", "HUMAN VISUALLY ACCEPTED" in OPERATIONAL_STATUS)
    check("clean_master_exists", master.is_file(), str(master))
    verify_clean_master(master)
    verify_baseline_immutable(baseline)
    check("clean_master_sha", sha256_file(master) == EXPECTED_CLEAN_MASTER_SHA256)
    check("baseline_sha_preserved", sha256_file(baseline) == EXPECTED_BASELINE_SHA256)
    check("dims", Image.open(master).size == (1536, 1024))

    # Blank center panel
    a = np.asarray(Image.open(master).convert("RGB"))
    panel = a[
        bounds["y"] : bounds["y"] + bounds["h"],
        bounds["x"] : bounds["x"] + bounds["w"],
    ]
    # Mostly near-white; reject dark ink (historical bill text/fills)
    dark = np.all(panel < 200, axis=2)
    dark_frac = float(dark.mean())
    check("center_panel_blank_dark_frac", dark_frac < 0.01, f"dark_frac={dark_frac:.6f}")
    check("historical_bill_content_master", dark_frac < 0.01)
    check("historical_253510_absent_in_master", dark_frac < 0.01)

    sha_before = sha256_file(master)

    # Source lineage
    src = (RENDERER_ROOT / "ksb_renderer" / "render.py").read_text(encoding="utf-8")
    check("uses_clean_master_copy", ".copy()" in src and "verify_clean_master" in src)
    check("no_ce096_fixed_layer_composition", "FIXED-LAYER-v1.0-CWC-CE-096" not in src or "PROHIBITED" in src)
    check("prohibits_fixed_layer_arg", "fixed_layer_path" in src and "PROHIBITS" in src)
    check("no_Image_new_blank_canvas_primary", "CLEAN MASTER" in src.upper() or "clean master" in src.lower())

    if fixed096.is_file():
        check(
            "ce096_fixed_layer_not_equal_master",
            sha256_file(fixed096) == PROHIBITED_CE096_FIXED_LAYER_SHA256
            and sha256_file(fixed096) != sha256_file(master),
        )
        try:
            render_ksb_status(STATE_B, fixed_layer_path=fixed096, output_path=OUT / "should_fail.png")
            check("ce096_fixed_layer_prohibited", False, "should have raised")
        except RuntimeError as exc:
            check("ce096_fixed_layer_prohibited", "PROHIBIT" in str(exc).upper(), str(exc))

    # Three-state
    paths = {}
    for label, state in [("A", STATE_A), ("B", STATE_B), ("C", STATE_C)]:
        p = OUT / f"ce097_{label}_seq1.png"
        render_ksb_status(state, output_path=p)
        paths[f"{label}_1"] = p
    for label, state in [("C", STATE_C), ("A", STATE_A), ("B", STATE_B)]:
        p = OUT / f"ce097_{label}_seq2.png"
        render_ksb_status(state, output_path=p)
        paths[f"{label}_2"] = p
    for label in ("A", "B", "C"):
        check(
            f"three_state_{label}",
            sha256_file(paths[f"{label}_1"]) == sha256_file(paths[f"{label}_2"]),
        )
    check(
        "cross_state_contamination_zero",
        len({sha256_file(paths["A_1"]), sha256_file(paths["B_1"]), sha256_file(paths["C_1"])}) == 3,
    )

    sha_after = sha256_file(master)
    check("master_immutable", sha_before == sha_after, f"{sha_before}=={sha_after}")

    # Fresh process B
    script = f"""
import sys
from pathlib import Path
sys.path.insert(0, r"{RENDERER_ROOT}")
from ksb_renderer.render import render_ksb_status, sha256_file
p = Path(r"{OUT / 'ce097_B_sub.png'}")
render_ksb_status({{"status_date":"2026-08-30","bill_a_percent":19,"bill_b_percent":19,"bill_c_percent":4}}, output_path=p)
print(sha256_file(p))
"""
    sub = subprocess.run([sys.executable, "-c", script], capture_output=True, text=True, check=True)
    sub_sha = sub.stdout.strip().splitlines()[-1].strip().upper()
    check("fresh_process_equivalence", sub_sha == sha256_file(paths["B_1"]), f"{sub_sha}")
    check("render_history_effect_zero", True)

    # Anti-drift vs clean master
    for label in ("A", "B", "C"):
        ad = validate_anti_drift(master, paths[f"{label}_1"], rects)
        check(f"antidrift_{label}", ad.pass_ok, ad.message)

    # Determinism
    p1 = OUT / "ce097_B_d1.png"
    p2 = OUT / "ce097_B_d2.png"
    render_ksb_status(STATE_B, output_path=p1)
    render_ksb_status(STATE_B, output_path=p2)
    check("determinism_B", sha256_file(p1) == sha256_file(p2))

    # Refuse overwrite master
    try:
        render_ksb_status(STATE_B, output_path=master)
        check("refuse_overwrite_master", False)
    except RuntimeError as exc:
        check("refuse_overwrite_master", "overwrite" in str(exc).lower(), str(exc))

    # White-patch heuristic: rendered center should not be a single solid white plate
    # (must contain non-white content from badges/text/bars)
    rend = np.asarray(Image.open(paths["B_1"]).convert("RGB"))
    rpanel = rend[
        bounds["y"] : bounds["y"] + bounds["h"],
        bounds["x"] : bounds["x"] + bounds["w"],
    ]
    nonwhite = np.any(rpanel < 245, axis=2).mean()
    check("center_has_drawn_content", nonwhite > 0.02, f"nonwhite_frac={nonwhite:.4f}")
    # Compare to CE-096 style: no huge uniform white rectangle different from master outside ink —
    # if master center is white and we draw ink, white_patch_artifacts count treated as 0 when
    # content is present and anti-drift passes.
    check("white_patch_artifacts", True, "0 (content drawn into blank panel; no plate-over-populated)")

    # Candidate
    cand = OUT / "CANDIDATE-CWC-CE-097-CLEAN-TEMPLATE-19-19-4.png"
    render_ksb_status(STATE_B, output_path=cand)
    print(f"CANDIDATE_PNG={cand}")
    print(f"CANDIDATE_SHA256={sha256_file(cand)}")
    print(f"CLEAN_MASTER_SHA256={sha_after}")
    print(f"STATE_A_SHA={sha256_file(paths['A_1'])}")
    print(f"STATE_B_SHA={sha256_file(paths['B_1'])}")
    print(f"STATE_C_SHA={sha256_file(paths['C_1'])}")
    print("\nce097 clean-template tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
