#!/usr/bin/env python3
"""CWC-CE-107 — public-image cleanup tests (date / breadcrumb / metadata)."""

from __future__ import annotations

import hashlib
import sys
from datetime import date
from pathlib import Path

import numpy as np
from PIL import Image

RENDERER_ROOT = Path(__file__).resolve().parents[1]
WEEKLY = RENDERER_ROOT.parent
sys.path.insert(0, str(RENDERER_ROOT))

from ksb_renderer.antidrift import authorized_rects_from_regions, validate_anti_drift  # noqa: E402
from ksb_renderer.contract import format_status_date, validate_and_normalize  # noqa: E402
from ksb_renderer.render import (  # noqa: E402
    EXPECTED_CLEAN_MASTER_SHA256,
    HISTORICAL_CE097_CLEAN_MASTER_SHA256,
    RENDERER_VERSION,
    load_regions,
    render_ksb_status,
    sha256_file,
    verify_clean_master,
)

OUT = Path(__file__).resolve().parent / "_non_production_output"
CANDIDATE = OUT / "CANDIDATE-CWC-CE-107-PUBLIC-CLEANUP-19-19-4.png"

FORBIDDEN_SUBSTRINGS = (
    "X:\\GitHub",
    "X:/GitHub",
    "Local Template Path",
    "File Name (Local Template)",
    "Date Explanation",
    "yyyy.mm.ww",
    "Live 2026.10.05",
    "(Week 35 of 2026)",
    "(Week ",
)


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        raise SystemExit(1)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    regions = load_regions()
    master = WEEKLY / regions["clean_master_relpath"]
    hist = WEEKLY / regions["historical_clean_master_relpath"]
    rects = authorized_rects_from_regions(regions)

    check("renderer_version", RENDERER_VERSION == "2.1.0-CWC-CE-107-CANDIDATE")
    check("clean_master_id", regions["clean_master_id"].endswith("CWC-CE-107-CANDIDATE"))
    check("canvas_912", regions["canvas"]["height"] == 912 and regions["canvas"]["width"] == 1536)
    verify_clean_master(master)
    check("clean_master_sha", sha256_file(master) == EXPECTED_CLEAN_MASTER_SHA256)
    check("dims", Image.open(master).size == (1536, 912))

    # Historical CE-097 master immutable / not overwritten
    check("historical_master_exists", hist.is_file())
    check(
        "historical_master_sha_immutable",
        sha256_file(hist) == HISTORICAL_CE097_CLEAN_MASTER_SHA256,
    )
    check("successor_is_not_historical_path", master.resolve() != hist.resolve())

    # Date semantics
    check("ordinary_2026-08-30", format_status_date(date(2026, 8, 30)) == "2026.08.35")
    check("month_boundary_2026-09-01", format_status_date(date(2026, 9, 1)) == "2026.09.36")
    # 2026-12-31 is Thursday of ISO week 53 of 2026; calendar year remains 2026
    check("year_boundary_2026-12-31", format_status_date(date(2026, 12, 31)) == "2026.12.53")
    # 2027-01-01 is Friday of ISO week 53 of 2026 — calendar yyyy stays 2027
    check(
        "iso_week_year_divergence_2027-01-01",
        format_status_date(date(2027, 1, 1)) == "2027.01.53",
        format_status_date(date(2027, 1, 1)),
    )
    # 2025-12-29 is Monday of ISO week 1 of 2026 — calendar yyyy stays 2025
    check(
        "iso_week_year_divergence_2025-12-29",
        format_status_date(date(2025, 12, 29)) == "2025.12.01",
        format_status_date(date(2025, 12, 29)),
    )

    # Runtime contract still four keys
    n = validate_and_normalize(
        {
            "status_date": "2026-08-30",
            "bill_a_percent": 19,
            "bill_b_percent": 19,
            "bill_c_percent": 4,
        }
    )
    check("compact_from_status_date", n.status_date_compact == "2026.08.35")

    inp = {
        "status_date": "2026-08-30",
        "bill_a_percent": 19,
        "bill_b_percent": 19,
        "bill_c_percent": 4,
    }
    sha_before = sha256_file(master)
    img1, norm, _ = render_ksb_status(inp, output_path=CANDIDATE)
    img2, _, _ = render_ksb_status(inp, output_path=OUT / "CWC-CE-107-second-render.png")
    check("master_immutable_after_render", sha256_file(master) == sha_before)
    check("candidate_dims", img1.size == (1536, 912))
    s1 = sha256_file(CANDIDATE)
    s2 = sha256_file(OUT / "CWC-CE-107-second-render.png")
    check("determinism", s1 == s2, f"{s1} vs {s2}")
    check("status_date_compact_render", norm.status_date_compact == "2026.08.35")

    ad = validate_anti_drift(master, CANDIDATE, rects, expected_size=(1536, 912))
    check("anti_drift", ad.pass_ok, ad.message)
    check("unauthorized_drift_zero", ad.unauthorized_changed == 0, str(ad.unauthorized_changed))

    # Master must not contain stale/public-prohibited strings (PNG text chunks / pixels via OCR not available —
    # assert via rebuild evidence regions + pixel probes)
    master_arr = np.asarray(Image.open(master).convert("RGB"))
    # Date region should be mostly sky-like (not dark ink block)
    db = regions["status_date"]["authorized_bounds"]
    date_patch = master_arr[db["y"] : db["y"] + db["h"], db["x"] : db["x"] + db["w"]]
    dark_frac = float(np.mean(np.all(date_patch < 80, axis=2)))
    check("master_date_region_blankish", dark_frac < 0.02, f"dark_frac={dark_frac}")

    # Rendered date region should contain dark text ink
    rend = np.asarray(img1)
    date_rend = rend[db["y"] : db["y"] + db["h"], db["x"] : db["x"] + db["w"]]
    dark_rend = float(np.mean(np.all(date_rend < 80, axis=2)))
    check("rendered_date_has_ink", dark_rend > 0.01, f"dark_frac={dark_rend}")

    # Metadata strip removed: height 912; no light gray band below footer
    check("no_metadata_strip_height", img1.size[1] == 912)

    # Center panel maturity pixels exist (non-blank after render)
    b = regions["center_panel"]["bounds"]
    panel = rend[b["y"] : b["y"] + b["h"], b["x"] : b["x"] + b["w"]]
    check("center_panel_drawn", float(np.mean(np.all(panel > 250, axis=2))) < 0.95)

    # Forbidden public strings must not appear as UTF-8 in PNG file bytes (metadata text)
    raw = CANDIDATE.read_bytes()
    for s in FORBIDDEN_SUBSTRINGS:
        check(f"absent_bytes:{s[:24]}", s.encode("utf-8") not in raw)

    # baseline_id semantics untouched in regions
    check("baseline_id_unchanged", regions["baseline_id"] == "BL-WEEKLY-STATUS-BASELINE-v1.0")

    print(f"\nCANDIDATE_PATH={CANDIDATE}")
    print(f"CANDIDATE_SHA={s1}")
    print("ce107 public-image cleanup tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
