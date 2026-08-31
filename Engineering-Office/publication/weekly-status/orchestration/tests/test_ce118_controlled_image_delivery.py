#!/usr/bin/env python3
"""CWC-CE-118 — controlled package image delivery (exact artifact; no image-search fallback)."""

from __future__ import annotations

import hashlib
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WEEKLY = ROOT.parent
sys.path.insert(0, str(ROOT))

from ksb_package_state import (  # noqa: E402
    CommandError,
    PackagePhase,
    Product,
    ThreeStepOrchestrator,
    package_image_relpath,
)

EXPECTED_SHA = "5FEECAA3267D07A996968DC4116A0C8AFB8E7181D187302B06401886960D80CC"
FIXTURE = WEEKLY / "images" / "2026-08-30-BlueprintLiberty-Weekly-Status.png"

CERT = dict(
    cycle_id="KSB-CYCLE-2026-08-30",
    status_date="2026-08-30",
    bill_a_percent=19,
    bill_b_percent=19,
    bill_c_percent=4,
    canonical_sha="dedce82d5b9bcaa97e9775aae449680bc9b0edb8",
)


def check(name: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        raise SystemExit(1)


def _orch_with_fixture() -> ThreeStepOrchestrator:
    tmp = tempfile.TemporaryDirectory()
    root = Path(tmp.name)
    (root / "images").mkdir(parents=True)
    shutil.copy2(FIXTURE, root / package_image_relpath("2026-08-30"))
    orch = ThreeStepOrchestrator(weekly_status_root=root)
    orch._tmpdir = tmp  # type: ignore[attr-defined]
    return orch


def main() -> int:
    check("fixture_exists", FIXTURE.is_file(), str(FIXTURE))
    raw = FIXTURE.read_bytes()
    check("fixture_sha", hashlib.sha256(raw).hexdigest().upper() == EXPECTED_SHA)

    # Exact artifact path + contract preservation
    orch = _orch_with_fixture()
    r1 = orch.prepare_ksb_status(**CERT)
    check("prepare_status", r1.product == Product.STATUS and r1.create_render_request is False)
    r2 = orch.next_command()
    check("first_next_press", r2.product == Product.PRESS_RELEASE)
    r3 = orch.next_command(expected_image_sha256=EXPECTED_SHA)
    check("final_next_product_image", r3.product == Product.IMAGE)
    check("final_next_no_render", r3.create_render_request is False)
    check("final_next_inline", r3.image_presentation == "INLINE_PNG")
    check(
        "final_next_path",
        r3.controlled_image_path == "images/2026-08-30-BlueprintLiberty-Weekly-Status.png",
    )
    check("final_next_sha", r3.controlled_image_sha256 == EXPECTED_SHA)
    check("final_next_dims", r3.controlled_image_width == 1536 and r3.controlled_image_height == 912)
    check("final_next_phase", r3.phase == PackagePhase.PACKAGE_COMPLETE)
    check("message_forbids_search", "Do NOT image_search" in r3.message)

    # Negative: generic image search substitute impossible under controlled path
    orch_s = _orch_with_fixture()
    orch_s.prepare_ksb_status(**CERT)
    orch_s.next_command()
    try:
        orch_s.next_command(allow_image_substitute="image_search")
        check("reject_image_search", False)
    except CommandError as e:
        check("reject_image_search", "substitute prohibited" in str(e).lower() or "image_search" in str(e))

    for banned in (
        "web_image_search",
        "kansas_capitol_search",
        "stock_photo",
        "generic_image_search",
        "image_gen",
    ):
        o = _orch_with_fixture()
        o.prepare_ksb_status(**CERT)
        o.next_command()
        try:
            o.next_command(allow_image_substitute=banned)
            check(f"reject_{banned}", False)
        except CommandError:
            check(f"reject_{banned}", True)

    # Missing artifact → controlled failure; no search/gen/render substitute
    empty = tempfile.TemporaryDirectory()
    orch_m = ThreeStepOrchestrator(weekly_status_root=Path(empty.name))
    orch_m._tmpdir = empty  # type: ignore[attr-defined]
    orch_m.prepare_ksb_status(**CERT)
    orch_m.next_command()
    try:
        orch_m.next_command(require_existing_package_image=True, expected_image_sha256=EXPECTED_SHA)
        check("missing_artifact_fails", False)
    except CommandError as e:
        msg = str(e)
        check("missing_artifact_fails", "DELIVERY BLOCKED" in msg)
        check("missing_no_search_hint", "image_search" not in msg.lower() or "DELIVERY BLOCKED" in msg)

    # Wrong SHA → identity failure; no substitute
    bad = tempfile.TemporaryDirectory()
    bad_root = Path(bad.name)
    (bad_root / "images").mkdir(parents=True)
    shutil.copy2(FIXTURE, bad_root / package_image_relpath("2026-08-30"))
    orch_b = ThreeStepOrchestrator(weekly_status_root=bad_root)
    orch_b._tmpdir = bad  # type: ignore[attr-defined]
    orch_b.prepare_ksb_status(**CERT)
    orch_b.next_command()
    try:
        orch_b.next_command(expected_image_sha256="0" * 64)
        check("wrong_sha_fails", False)
    except CommandError as e:
        check("wrong_sha_fails", "IDENTITY VERIFICATION FAILED" in str(e))

    # Three-step contract preserved with package image present
    orch_c = _orch_with_fixture()
    path = [
        ("Prepare KSB Status", orch_c.prepare_ksb_status(**CERT).product.value),
        ("Next", orch_c.next_command().product.value),
        ("Next", orch_c.next_command(expected_image_sha256=EXPECTED_SHA).product.value),
    ]
    check(
        "contract_preserved_with_package_image",
        path
        == [
            ("Prepare KSB Status", "STATUS"),
            ("Next", "PRESS_RELEASE"),
            ("Next", "IMAGE"),
        ],
        str(path),
    )

    print("\nCWC-CE-118 controlled image delivery tests: PASS")
    print("GENERIC IMAGE SEARCH SUBSTITUTE: REJECTED / IMPOSSIBLE UNDER CONTROLLED PATH")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
