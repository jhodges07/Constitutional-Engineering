"""Deterministic KSB Status renderer — clean master + dynamic center panel (CWC-CE-097)."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Dict, Mapping, Sequence, Tuple

from PIL import Image, ImageDraw, ImageFont

from .contract import NormalizedInput, validate_and_normalize

RENDERER_VERSION = "2.1.0-CWC-CE-107-CANDIDATE"
OPERATIONAL_STATUS = "TECHNICAL CANDIDATE — HUMAN VISUAL PENDING (CWC-CE-107)"

EXPECTED_BASELINE_SHA256 = (
    "17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9"
)
EXPECTED_CLEAN_MASTER_SHA256 = (
    "29E243233AB0872FFF2323ACC882FC477F71865CE072C4416EEFBDEC8F8576E0"
)
# Historical CE-097 clean master — preserved; not ordinary input under CE-107
HISTORICAL_CE097_CLEAN_MASTER_SHA256 = (
    "01C29A8A20CA4D1798E4A407431B0A7FA1BD58F798D5837AD2A1CC1BF9E1D05C"
)
# Historical CE-096 asset — must not be used as ordinary render input
PROHIBITED_CE096_FIXED_LAYER_SHA256 = (
    "A445685853095203F4D30941AED33320EF1629E643BA0DA6D8FCF95860787E05"
)


def _repo_weekly_status_root() -> Path:
    return Path(__file__).resolve().parents[2]


def default_regions_path() -> Path:
    return Path(__file__).resolve().parents[1] / "regions.json"


def load_regions(path: Path | None = None) -> Dict[str, Any]:
    p = path or default_regions_path()
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def load_center_content(regions: Dict[str, Any], root: Path | None = None) -> Dict[str, Any]:
    root = root or _repo_weekly_status_root()
    path = root / regions["center_content_relpath"]
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def verify_baseline_immutable(baseline_path: Path) -> str:
    """Historical visual reference integrity only — NOT ordinary render input."""
    got = sha256_file(baseline_path)
    if got != EXPECTED_BASELINE_SHA256:
        raise RuntimeError(
            f"BASELINE INTEGRITY FAILURE: expected {EXPECTED_BASELINE_SHA256} got {got}"
        )
    return got


def verify_clean_master(master_path: Path) -> str:
    got = sha256_file(master_path)
    if got != EXPECTED_CLEAN_MASTER_SHA256:
        raise RuntimeError(
            f"CLEAN MASTER INTEGRITY FAILURE: expected {EXPECTED_CLEAN_MASTER_SHA256} got {got}"
        )
    return got


def _load_font(path: str, size: int) -> ImageFont.FreeTypeFont:
    fp = Path(path)
    if not fp.is_file():
        raise RuntimeError(f"Authorized font not found at {fp}")
    return ImageFont.truetype(str(fp), size=size)


def _wrap_text(text: str, font: ImageFont.ImageFont, max_width: int, draw: ImageDraw.ImageDraw) -> list[str]:
    words = text.split()
    lines: list[str] = []
    cur = ""
    for w in words:
        trial = w if not cur else f"{cur} {w}"
        bbox = draw.textbbox((0, 0), trial, font=font)
        if bbox[2] - bbox[0] <= max_width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def _draw_rounded_rect(
    draw: ImageDraw.ImageDraw,
    xy: Tuple[int, int, int, int],
    radius: int,
    fill: Sequence[int],
) -> None:
    draw.rounded_rectangle(list(xy), radius=radius, fill=tuple(fill))


def _draw_bar(
    draw: ImageDraw.ImageDraw,
    x: int,
    y: int,
    w: int,
    h: int,
    percent: int,
    track_rgb: Sequence[int],
    fill_rgb: Sequence[int],
) -> None:
    draw.rounded_rectangle([x, y, x + w - 1, y + h - 1], radius=h // 2, fill=tuple(track_rgb))
    fill_w = int(round(w * (percent / 100.0)))
    if fill_w <= 0:
        return
    if fill_w >= w:
        draw.rounded_rectangle([x, y, x + w - 1, y + h - 1], radius=h // 2, fill=tuple(fill_rgb))
        return
    draw.rounded_rectangle([x, y, x + fill_w - 1, y + h - 1], radius=h // 2, fill=tuple(fill_rgb))


def _draw_right_text(
    draw: ImageDraw.ImageDraw,
    text: str,
    right_xy: Sequence[int],
    font: ImageFont.ImageFont,
    fill: Sequence[int],
) -> None:
    rx, ry = int(right_xy[0]), int(right_xy[1])
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text((rx - tw, ry), text, font=font, fill=tuple(fill))


def _compose_status_date(
    img: Image.Image,
    regions: Dict[str, Any],
    normalized: NormalizedInput,
) -> None:
    """Draw compact Date: yyyy.mm.ww from status_date (DYNAMIC)."""
    sd = regions["status_date"]
    draw = ImageDraw.Draw(img)
    typo = regions["typography"]
    font = _load_font(typo["font_path_windows"], int(sd["font_size_px"]))
    text = f"{sd['label_prefix']}{normalized.status_date_compact}"
    x, y = int(sd["xy"][0]), int(sd["xy"][1])
    draw.text((x, y), text, font=font, fill=tuple(sd["rgb"]))


def _compose_center_panel(
    img: Image.Image,
    regions: Dict[str, Any],
    content: Dict[str, Any],
    normalized: NormalizedInput,
) -> None:
    draw = ImageDraw.Draw(img)
    typo = regions["typography"]
    title_font = _load_font(typo["font_path_windows"], int(typo["title_font_size_px"]))
    desc_font = _load_font(typo.get("font_path_regular_windows", typo["font_path_windows"]), int(typo["description_font_size_px"]))
    pct_font = _load_font(typo["font_path_windows"], int(typo["percent_font_size_px"]))
    eng_font = _load_font(typo["font_path_windows"], int(typo["engineered_font_size_px"]))
    badge_font = _load_font(typo["font_path_windows"], int(typo["badge_font_size_px"]))
    disc_font = _load_font(
        typo.get("font_path_regular_windows", typo["font_path_windows"]),
        int(regions["center_panel"]["disclaimer_font_size_px"]),
    )
    bottom_font = _load_font(
        typo.get("font_path_italic_windows", typo["font_path_windows"]),
        int(regions["center_panel"]["bottom_statement_font_size_px"]),
    )

    percents = {
        "bill_a": normalized.bill_a_percent,
        "bill_b": normalized.bill_b_percent,
        "bill_c": normalized.bill_c_percent,
    }
    panel_x1 = regions["center_panel"]["bounds"]["x"] + regions["center_panel"]["bounds"]["w"]

    for key in ("bill_a", "bill_b", "bill_c"):
        layout = regions["bills"][key]
        bill = content["bills"][key]
        pct = percents[key]
        b = layout["badge"]
        _draw_rounded_rect(
            draw,
            (b["x"], b["y"], b["x"] + b["w"] - 1, b["y"] + b["h"] - 1),
            int(b["radius"]),
            bill["badge_rgb"],
        )
        # Center badge text
        bb = draw.textbbox((0, 0), bill["badge_text"], font=badge_font)
        bw, bh = bb[2] - bb[0], bb[3] - bb[1]
        draw.text(
            (b["x"] + (b["w"] - bw) // 2, b["y"] + (b["h"] - bh) // 2 - 2),
            bill["badge_text"],
            font=badge_font,
            fill=(255, 255, 255),
        )

        tx, ty = layout["title_xy"]
        draw.text((tx, ty), bill["title"], font=title_font, fill=tuple(bill["title_rgb"]))

        box = layout["description_box"]
        lines = _wrap_text(bill["description"], desc_font, int(box["w"]), draw)
        ly = int(box["y"])
        for line in lines[:4]:
            draw.text((box["x"], ly), line, font=desc_font, fill=tuple(bill["description_rgb"]))
            ly += int(typo["description_font_size_px"]) + 2

        bar = layout["bar"]
        _draw_bar(
            draw,
            bar["x"],
            bar["y"],
            bar["w"],
            bar["h"],
            pct,
            bill["bar_track_rgb"],
            bill["bar_fill_rgb"],
        )

        _draw_right_text(
            draw, f"{pct}%", layout["percent_right_xy"], pct_font, bill["percent_rgb"]
        )
        _draw_right_text(
            draw,
            content["engineered_label"],
            layout["engineered_right_xy"],
            eng_font,
            bill["percent_rgb"],
        )

        sep_y = int(layout["separator_y"])
        draw.line(
            [(b["x"], sep_y), (panel_x1 - 20, sep_y)],
            fill=tuple(bill["separator_rgb"]),
            width=1,
        )

    cp = regions["center_panel"]
    dx, dy = cp["disclaimer_xy"]
    draw.text((dx, dy), content["disclaimer"], font=disc_font, fill=tuple(cp["disclaimer_rgb"]))
    bx, by = cp["bottom_statement_xy"]
    draw.text(
        (bx, by),
        content["bottom_statement"],
        font=bottom_font,
        fill=tuple(cp["bottom_statement_rgb"]),
    )


def render_ksb_status(
    raw_input: Mapping[str, Any],
    *,
    baseline_path: Path | None = None,
    clean_master_path: Path | None = None,
    regions_path: Path | None = None,
    output_path: Path | None = None,
    fixed_layer_path: Path | None = None,
) -> Tuple[Image.Image, NormalizedInput, str]:
    """
    Open pristine clean master → copy → draw current center-panel content → new PNG.

    ``baseline_path`` / historical baseline: integrity only, never canvas.
    ``fixed_layer_path``: accepted for API compatibility; MUST NOT be used (CWC-CE-097).
    Returns (RGB image, normalized input, clean_master_sha).
    """
    if fixed_layer_path is not None:
        raise RuntimeError(
            "CWC-CE-097 PROHIBITS CWC-CE-096 fixed-layer as render input "
            f"(got {fixed_layer_path})"
        )

    root = _repo_weekly_status_root()
    regions = load_regions(regions_path)
    pct = regions["percent_range"]
    normalized = validate_and_normalize(
        raw_input, percent_min=int(pct["min"]), percent_max=int(pct["max"])
    )

    # Historical baseline integrity (not canvas)
    bpath = baseline_path or (root / regions["baseline_relpath"])
    verify_baseline_immutable(bpath)

    master_path = clean_master_path or (root / regions["clean_master_relpath"])
    master_sha = verify_clean_master(master_path)

    # Refuse if caller somehow points master at CE-096 fixed layer
    if master_sha == PROHIBITED_CE096_FIXED_LAYER_SHA256:
        raise RuntimeError("CWC-CE-096 fixed layer SHA prohibited as clean master")

    exp_w = int(regions["canvas"]["width"])
    exp_h = int(regions["canvas"]["height"])

    # Fresh open of pristine clean master — never overwrite master
    with Image.open(master_path) as master_im:
        master_rgb = master_im.convert("RGB")
        if master_rgb.size != (exp_w, exp_h):
            raise RuntimeError(
                f"clean master dimensions {master_rgb.size} != {(exp_w, exp_h)}"
            )
        canvas = master_rgb.copy()

    content = load_center_content(regions, root)
    _compose_status_date(canvas, regions, normalized)
    _compose_center_panel(canvas, regions, content, normalized)

    if output_path is not None:
        output_path = Path(output_path)
        if output_path.resolve() == master_path.resolve():
            raise RuntimeError("REFUSING to overwrite clean master template")
        output_path.parent.mkdir(parents=True, exist_ok=True)
        canvas.save(output_path, format="PNG", compress_level=9, optimize=False)

    # Master immutability check
    verify_clean_master(master_path)
    verify_baseline_immutable(bpath)
    return canvas, normalized, master_sha


def production_output_name(calendar_date) -> str:
    return f"{calendar_date.isoformat()}-BlueprintLiberty-Weekly-Status.png"
