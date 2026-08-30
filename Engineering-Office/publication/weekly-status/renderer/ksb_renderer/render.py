"""Deterministic KSB Status image renderer (baseline + four variables only)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Mapping, Tuple

import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

from .contract import InputValidationError, NormalizedInput, validate_and_normalize

RENDERER_VERSION = "1.0.0-CWC-CE-084"

EXPECTED_BASELINE_SHA256 = (
    "17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9"
)


def _repo_weekly_status_root() -> Path:
    # .../publication/weekly-status/renderer/ksb_renderer/render.py
    return Path(__file__).resolve().parents[2]


def default_regions_path() -> Path:
    return Path(__file__).resolve().parents[1] / "regions.json"


def load_regions(path: Path | None = None) -> Dict[str, Any]:
    p = path or default_regions_path()
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def verify_baseline_immutable(baseline_path: Path) -> str:
    got = sha256_file(baseline_path)
    if got != EXPECTED_BASELINE_SHA256:
        raise RuntimeError(
            f"BASELINE INTEGRITY FAILURE: expected {EXPECTED_BASELINE_SHA256} got {got}"
        )
    return got


def _load_font(regions: Dict[str, Any], size: int) -> ImageFont.FreeTypeFont:
    typo = regions["typography"]
    font_path = Path(typo.get("font_path_windows", r"C:\Windows\Fonts\arialbd.ttf"))
    if not font_path.is_file():
        raise RuntimeError(
            f"Authorized font not found at {font_path}. "
            "CWC-CE-084 requires Arial Bold (arialbd.ttf) as deterministic substitute."
        )
    return ImageFont.truetype(str(font_path), size=size)


def _clear_region_inpaint(rgb: np.ndarray, x: int, y: int, w: int, h: int) -> None:
    """Deterministically clear text/ink in a region via Telea inpaint (baseline-local)."""
    h_img, w_img = rgb.shape[:2]
    x0, y0 = max(0, x), max(0, y)
    x1, y1 = min(w_img, x + w), min(h_img, y + h)
    crop = rgb[y0:y1, x0:x1]
    if crop.size == 0:
        return
    # Anomaly vs median of crop luminance → ink / antialias
    lum = crop.astype(np.float32).mean(axis=2)
    med = float(np.median(lum))
    mask = (np.abs(lum - med) >= 14).astype(np.uint8) * 255
    if int(mask.sum()) == 0:
        return
    kernel = np.ones((2, 2), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)
    bgr = cv2.cvtColor(crop, cv2.COLOR_RGB2BGR)
    out = cv2.inpaint(bgr, mask, inpaintRadius=3, flags=cv2.INPAINT_TELEA)
    rgb[y0:y1, x0:x1] = cv2.cvtColor(out, cv2.COLOR_BGR2RGB)


def _draw_bar(
    draw: ImageDraw.ImageDraw,
    bar: Dict[str, Any],
    percent: int,
) -> None:
    x, y, w, h = bar["x"], bar["y"], bar["w"], bar["h"]
    track = tuple(bar["track_rgb"])
    fill = tuple(bar["fill_rgb"])
    # Full track restore
    draw.rounded_rectangle([x, y, x + w - 1, y + h - 1], radius=h // 2, fill=track)
    fill_w = int(round(w * (percent / 100.0)))
    if fill_w <= 0:
        return
    if fill_w >= w:
        draw.rounded_rectangle([x, y, x + w - 1, y + h - 1], radius=h // 2, fill=fill)
        return
    # Draw fill as rounded on left; square cut on right of fill segment
    draw.rounded_rectangle([x, y, x + fill_w - 1, y + h - 1], radius=h // 2, fill=fill)
    # Cover right round of short fill if fill_w small — acceptable mechanical approximation


def render_ksb_status(
    raw_input: Mapping[str, Any],
    *,
    baseline_path: Path | None = None,
    regions_path: Path | None = None,
    output_path: Path | None = None,
) -> Tuple[Image.Image, NormalizedInput, str]:
    """
    Render from accepted baseline + Human-approved variables.

    Returns (RGB image, normalized input, baseline_sha).
    Raises InputValidationError on bad input (fail closed).
    """
    root = _repo_weekly_status_root()
    regions = load_regions(regions_path)
    pct = regions["percent_range"]
    normalized = validate_and_normalize(
        raw_input, percent_min=int(pct["min"]), percent_max=int(pct["max"])
    )

    bpath = baseline_path or (root / regions["baseline_relpath"])
    bsha = verify_baseline_immutable(bpath)

    base = Image.open(bpath).convert("RGB")
    exp_w = int(regions["canvas"]["width"])
    exp_h = int(regions["canvas"]["height"])
    if base.size != (exp_w, exp_h):
        raise RuntimeError(f"baseline dimensions {base.size} != {(exp_w, exp_h)}")

    rgb = np.array(base)
    v = regions["variables"]

    # Clear variable text regions (runtime plates from baseline; not stored visual authority)
    _clear_region_inpaint(rgb, **v["STATUS_DATE"]["region"])
    for bill in ("BILL_A_PERCENT", "BILL_B_PERCENT", "BILL_C_PERCENT"):
        _clear_region_inpaint(rgb, **v[bill]["text_region"])
        # Clear bar area to track color before redraw (deterministic rectangle restore)
        bar = v[bill]["bar"]
        x, y, w, h = bar["x"], bar["y"], bar["w"], bar["h"]
        rgb[y : y + h, x : x + w] = np.array(bar["track_rgb"], dtype=np.uint8)

    img = Image.fromarray(rgb, mode="RGB")
    draw = ImageDraw.Draw(img)
    typo = regions["typography"]
    date_font = _load_font(regions, int(typo["date_font_size_px"]))
    pct_font = _load_font(regions, int(typo["percent_font_size_px"]))

    # STATUS_DATE
    date_text = v["STATUS_DATE"]["display_prefix"] + normalized.status_date_compact
    dx, dy = v["STATUS_DATE"]["text_xy"]
    draw.text((dx, dy), date_text, font=date_font, fill=tuple(typo["date_color_rgb"]))

    # Percentages + bars
    bills = [
        ("BILL_A_PERCENT", normalized.bill_a_percent, "bill_a_color_rgb"),
        ("BILL_B_PERCENT", normalized.bill_b_percent, "bill_b_color_rgb"),
        ("BILL_C_PERCENT", normalized.bill_c_percent, "bill_c_color_rgb"),
    ]
    for key, pct_val, color_key in bills:
        spec = v[key]
        label = f"{pct_val}%"
        # right-align to text_right_xy
        rx, ry = spec["text_right_xy"]
        bbox = draw.textbbox((0, 0), label, font=pct_font)
        tw = bbox[2] - bbox[0]
        draw.text((rx - tw, ry), label, font=pct_font, fill=tuple(typo[color_key]))
        _draw_bar(draw, spec["bar"], pct_val)

    if output_path is not None:
        output_path = Path(output_path)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        # Deterministic PNG encoding parameters
        img.save(output_path, format="PNG", compress_level=9, optimize=False)

    # Ending baseline immutability check
    verify_baseline_immutable(bpath)
    return img, normalized, bsha


def production_output_name(calendar_date) -> str:
    """Controlled weekly filename contract (STD-011); not renamed by KSB terminology."""
    return f"{calendar_date.isoformat()}-BlueprintLiberty-Weekly-Status.png"
