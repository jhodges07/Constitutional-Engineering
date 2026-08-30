#!/usr/bin/env python3
"""Deterministic tests for KSB three-step Human command contract (CWC-CE-092 / ECR-011)."""

from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from ksb_package_state import (  # noqa: E402
    CommandError,
    PackagePhase,
    Product,
    ThreeStepOrchestrator,
)

CERT = dict(
    cycle_id="KSB-CYCLE-2026-08-30",
    status_date="2026-08-30",
    bill_a_percent=19,
    bill_b_percent=19,
    bill_c_percent=4,
    canonical_sha="87b9657b5f298d4c95b1e3e38de8fea3431d6e43",
)


def check(name: str, ok: bool, detail: str = "") -> None:
    status = "PASS" if ok else "FAIL"
    print(f"[{status}] {name}" + (f" — {detail}" if detail else ""))
    if not ok:
        raise SystemExit(1)


def main() -> int:
    orch = ThreeStepOrchestrator()

    # Prepare → STATUS only; no render
    r1 = orch.prepare_ksb_status(**CERT)
    check("prepare_returns_status", r1.product == Product.STATUS)
    check("prepare_no_render", r1.create_render_request is False)
    check("prepare_phase", r1.phase == PackagePhase.STATUS_COMPLETE)
    check("prepare_maturity_a", r1.package["bill_a_percent"] == 19)

    # First Next → PRESS RELEASE; no render
    r2 = orch.next_command()
    check("first_next_press", r2.product == Product.PRESS_RELEASE)
    check("first_next_no_render", r2.create_render_request is False)
    check("first_next_phase", r2.phase == PackagePhase.PRESS_RELEASE_COMPLETE)
    check("single_copy_box_contract", r2.press_release_presentation == "SINGLE_COPY_BOX")
    check("pr_zip_not_primary", r2.zip_is_primary_human_product is False)

    # Continuity after PR
    orch.assert_continuity(
        status_date="2026-08-30",
        bill_a_percent=19,
        bill_b_percent=19,
        bill_c_percent=4,
        baseline_id="BL-WEEKLY-STATUS-BASELINE-v1.0",
        renderer_id="ksb_renderer@1.1.0-CWC-CE-094",
    )
    check("continuity_after_pr", True)

    # Second Next → image path; at most one create
    r3 = orch.next_command()
    check("second_next_enters_image", r3.create_render_request is True)
    check("second_next_product", r3.product == Product.IMAGE_IN_PROGRESS)
    rid = orch.active.render_request_id
    check("render_request_created_once", bool(rid))

    # Next during IN PROGRESS → reuse; zero duplicate
    r4 = orch.next_command(image_execution_status="IN_PROGRESS")
    check("in_progress_reuse", r4.create_render_request is False)
    check("in_progress_product", r4.product == Product.IMAGE_IN_PROGRESS)
    check("request_id_invariant", orch.active.render_request_id == rid)

    try:
        orch.next_command(
            image_execution_status="IN_PROGRESS",
            proposed_render_request_id="KSB-RENDER-EVIL-999",
        )
        check("reject_duplicate_request_id", False)
    except CommandError:
        check("reject_duplicate_request_id", True)

    # Complete image
    r5 = orch.next_command(image_execution_status="SUCCEEDED")
    check("image_complete_product", r5.product == Product.IMAGE)
    check("package_complete_phase", r5.phase == PackagePhase.PACKAGE_COMPLETE)
    check("image_complete_no_new_render", r5.create_render_request is False)
    check("inline_png_contract", r5.image_presentation == "INLINE_PNG")
    check("image_zip_not_primary", r5.zip_is_primary_human_product is False)

    # Next after complete does not start new cycle
    r6 = orch.next_command()
    check("after_complete_no_new_cycle", r6.product == Product.PACKAGE_ALREADY_COMPLETE)
    check("after_complete_no_render", r6.create_render_request is False)

    # Negative: Next with no package
    orch2 = ThreeStepOrchestrator()
    try:
        orch2.next_command()
        check("reject_next_no_package", False)
    except CommandError:
        check("reject_next_no_package", True)

    # Negative: maturity mutation
    orch3 = ThreeStepOrchestrator()
    orch3.prepare_ksb_status(**CERT)
    try:
        orch3.mutate_press_release_maturity(80)
        check("reject_pr_maturity_mutation", False)
    except CommandError:
        check("reject_pr_maturity_mutation", True)
    try:
        orch3.mutate_image_maturity(80)
        check("reject_image_maturity_mutation", False)
    except CommandError:
        check("reject_image_maturity_mutation", True)

    # Negative: generative substitute
    orch4 = ThreeStepOrchestrator()
    orch4.prepare_ksb_status(**CERT)
    orch4.next_command()
    try:
        orch4.next_command(allow_image_substitute="image_gen")
        check("reject_image_gen", False)
    except CommandError:
        check("reject_image_gen", True)

    # Negative: continuity break
    orch5 = ThreeStepOrchestrator()
    orch5.prepare_ksb_status(**CERT)
    try:
        orch5.assert_continuity(
            status_date="2026-08-30",
            bill_a_percent=80,
            bill_b_percent=19,
            bill_c_percent=4,
            baseline_id="BL-WEEKLY-STATUS-BASELINE-v1.0",
            renderer_id="ksb_renderer@1.1.0-CWC-CE-094",
        )
        check("reject_bill_a_drift", False)
    except CommandError:
        check("reject_bill_a_drift", True)

    # Human simplicity path representation
    orch6 = ThreeStepOrchestrator()
    path = []
    path.append(("Prepare KSB Status", orch6.prepare_ksb_status(**CERT).product.value))
    path.append(("Next", orch6.next_command().product.value))
    path.append(("Next", orch6.next_command().product.value))
    check(
        "human_simplicity_path",
        path
        == [
            ("Prepare KSB Status", "STATUS"),
            ("Next", "PRESS_RELEASE"),
            ("Next", "IMAGE_IN_PROGRESS"),
        ],
        str(path),
    )

    # IMAGE BLOCKED path
    orch7 = ThreeStepOrchestrator()
    orch7.prepare_ksb_status(**CERT)
    orch7.next_command()
    orch7.next_command()
    rb = orch7.next_command(image_execution_status="FAILED")
    check("image_blocked", rb.product == Product.IMAGE_BLOCKED)
    check("blocked_no_rerender", rb.create_render_request is False)

    print("\nthree-step command tests: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
