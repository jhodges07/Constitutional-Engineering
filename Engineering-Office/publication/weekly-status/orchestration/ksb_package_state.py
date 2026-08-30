"""KSB three-step Human command contract state machine (ECR-011 / CWC-CE-092).

Human products advance one boundary per command. GitHub render mechanics are
subordinate and MUST NOT start at Step 1 or Step 2.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Mapping, Optional


class PackagePhase(str, Enum):
    STATUS_PENDING = "KSB_STATUS_PENDING"
    STATUS_COMPLETE = "KSB_STATUS_COMPLETE"
    PRESS_RELEASE_COMPLETE = "KSB_PRESS_RELEASE_COMPLETE"
    IMAGE_REQUESTED = "KSB_IMAGE_REQUESTED"
    IMAGE_IN_PROGRESS = "KSB_IMAGE_IN_PROGRESS"
    IMAGE_COMPLETE = "KSB_IMAGE_COMPLETE"
    PACKAGE_COMPLETE = "KSB_PACKAGE_COMPLETE"
    IMAGE_BLOCKED = "KSB_IMAGE_BLOCKED"


class Product(str, Enum):
    STATUS = "STATUS"
    PRESS_RELEASE = "PRESS_RELEASE"
    IMAGE = "IMAGE"
    IMAGE_IN_PROGRESS = "IMAGE_IN_PROGRESS"
    IMAGE_BLOCKED = "IMAGE_BLOCKED"
    PACKAGE_ALREADY_COMPLETE = "PACKAGE_ALREADY_COMPLETE"
    NONE = "NONE"


class CommandError(ValueError):
    """Fail-closed command / continuity violation."""


@dataclass(frozen=True)
class PackageIdentity:
    cycle_id: str
    status_date: str
    bill_a_percent: int
    bill_b_percent: int
    bill_c_percent: int
    baseline_id: str
    renderer_id: str
    canonical_sha: Optional[str] = None
    certification_state: str = "HUMAN_CERTIFIED"
    evidence_basis: str = "CONTROLLED_REPOSITORY_EVIDENCE"


@dataclass
class PackageState:
    identity: PackageIdentity
    phase: PackagePhase = PackagePhase.STATUS_PENDING
    render_request_id: Optional[str] = None
    render_issue_number: Optional[int] = None
    render_run_id: Optional[int] = None
    artifact_name: Optional[str] = None
    status_returned: bool = False
    press_release_returned: bool = False
    image_returned: bool = False
    blocked_reason: Optional[str] = None
    history: list[str] = field(default_factory=list)

    def snapshot(self) -> dict[str, Any]:
        return {
            "phase": self.phase.value,
            "cycle_id": self.identity.cycle_id,
            "status_date": self.identity.status_date,
            "bill_a_percent": self.identity.bill_a_percent,
            "bill_b_percent": self.identity.bill_b_percent,
            "bill_c_percent": self.identity.bill_c_percent,
            "baseline_id": self.identity.baseline_id,
            "renderer_id": self.identity.renderer_id,
            "canonical_sha": self.identity.canonical_sha,
            "render_request_id": self.render_request_id,
            "render_issue_number": self.render_issue_number,
            "status_returned": self.status_returned,
            "press_release_returned": self.press_release_returned,
            "image_returned": self.image_returned,
            "blocked_reason": self.blocked_reason,
        }


@dataclass(frozen=True)
class CommandResult:
    product: Product
    phase: PackagePhase
    create_render_request: bool
    message: str
    package: Mapping[str, Any]


class ThreeStepOrchestrator:
    """Deterministic Human-facing command interpreter."""

    BASELINE_ID = "BL-WEEKLY-STATUS-BASELINE-v1.0"
    RENDERER_ID = "ksb_renderer@1.0.0-CWC-CE-084"
    FORBIDDEN_IMAGE_SUBSTITUTES = frozenset(
        {"image_gen", "dalle", "generative_infographic", "creative_status_image"}
    )

    def __init__(self) -> None:
        self._active: Optional[PackageState] = None

    @property
    def active(self) -> Optional[PackageState]:
        return self._active

    def prepare_ksb_status(
        self,
        *,
        cycle_id: str,
        status_date: str,
        bill_a_percent: int,
        bill_b_percent: int,
        bill_c_percent: int,
        canonical_sha: Optional[str] = None,
        certification_state: str = "HUMAN_CERTIFIED",
    ) -> CommandResult:
        """Step 1: return STATUS only. MUST NOT create a render Issue."""
        for label, value in (
            ("bill_a_percent", bill_a_percent),
            ("bill_b_percent", bill_b_percent),
            ("bill_c_percent", bill_c_percent),
        ):
            if not isinstance(value, int) or isinstance(value, bool) or not (0 <= value <= 100):
                raise CommandError(f"{label} must be integer percent 0–100")

        identity = PackageIdentity(
            cycle_id=cycle_id,
            status_date=status_date,
            bill_a_percent=bill_a_percent,
            bill_b_percent=bill_b_percent,
            bill_c_percent=bill_c_percent,
            baseline_id=self.BASELINE_ID,
            renderer_id=self.RENDERER_ID,
            canonical_sha=canonical_sha,
            certification_state=certification_state,
        )
        pkg = PackageState(identity=identity, phase=PackagePhase.STATUS_COMPLETE)
        pkg.status_returned = True
        pkg.history.append("PREPARE→STATUS")
        self._active = pkg
        return CommandResult(
            product=Product.STATUS,
            phase=pkg.phase,
            create_render_request=False,
            message="KSB STATUS returned. Stop. Await Next for press release.",
            package=pkg.snapshot(),
        )

    def next_command(
        self,
        *,
        image_execution_status: Optional[str] = None,
        proposed_render_request_id: Optional[str] = None,
        proposed_issue_number: Optional[int] = None,
        allow_image_substitute: Optional[str] = None,
    ) -> CommandResult:
        """Contextual Next: PR → image path → reuse in-progress → completed package."""
        if self._active is None:
            raise CommandError("Next with no active KSB package")

        if allow_image_substitute and allow_image_substitute.lower() in self.FORBIDDEN_IMAGE_SUBSTITUTES:
            raise CommandError("generative/creative image substitution prohibited")

        pkg = self._active
        phase = pkg.phase

        if phase == PackagePhase.STATUS_COMPLETE and not pkg.press_release_returned:
            return self._return_press_release(pkg)

        if phase in (
            PackagePhase.PRESS_RELEASE_COMPLETE,
            PackagePhase.IMAGE_REQUESTED,
            PackagePhase.IMAGE_IN_PROGRESS,
            PackagePhase.IMAGE_BLOCKED,
        ):
            return self._image_path(
                pkg,
                image_execution_status=image_execution_status,
                proposed_render_request_id=proposed_render_request_id,
                proposed_issue_number=proposed_issue_number,
            )

        if phase in (PackagePhase.IMAGE_COMPLETE, PackagePhase.PACKAGE_COMPLETE):
            return CommandResult(
                product=Product.PACKAGE_ALREADY_COMPLETE,
                phase=PackagePhase.PACKAGE_COMPLETE,
                create_render_request=False,
                message=(
                    "KSB PACKAGE COMPLETE — HUMAN REVIEW REQUIRED. "
                    "Next does not start a new weekly cycle; invoke Prepare KSB Status for a new cycle."
                ),
                package=pkg.snapshot(),
            )

        if phase == PackagePhase.STATUS_PENDING:
            raise CommandError("STATUS not yet complete; invoke Prepare KSB Status")

        raise CommandError(f"Next not defined for phase {phase.value}")

    def _return_press_release(self, pkg: PackageState) -> CommandResult:
        # Continuity: values frozen from Step 1 identity
        pkg.press_release_returned = True
        pkg.phase = PackagePhase.PRESS_RELEASE_COMPLETE
        pkg.history.append("NEXT→PRESS_RELEASE")
        return CommandResult(
            product=Product.PRESS_RELEASE,
            phase=pkg.phase,
            create_render_request=False,
            message=(
                "KSB PRESS RELEASE returned (~450–550 words from same status evidence). "
                "Stop. Await Next for controlled image."
            ),
            package=pkg.snapshot(),
        )

    def _image_path(
        self,
        pkg: PackageState,
        *,
        image_execution_status: Optional[str],
        proposed_render_request_id: Optional[str],
        proposed_issue_number: Optional[int],
    ) -> CommandResult:
        status = (image_execution_status or "").strip().upper()

        # Already have a request — never mint another
        if pkg.render_request_id:
            if proposed_render_request_id and proposed_render_request_id != pkg.render_request_id:
                raise CommandError("duplicate render request_id rejected while request active")
            if proposed_issue_number and pkg.render_issue_number and proposed_issue_number != pkg.render_issue_number:
                raise CommandError("duplicate render Issue rejected while request active")

            if status in ("", "QUEUED", "IN_PROGRESS", "RUNNING"):
                pkg.phase = PackagePhase.IMAGE_IN_PROGRESS
                pkg.history.append("NEXT→IMAGE_IN_PROGRESS(reuse)")
                return CommandResult(
                    product=Product.IMAGE_IN_PROGRESS,
                    phase=pkg.phase,
                    create_render_request=False,
                    message="KSB IMAGE: IN PROGRESS — same request retained; no duplicate Issue.",
                    package=pkg.snapshot(),
                )
            if status == "BLOCKED" or status == "FAILED":
                pkg.phase = PackagePhase.IMAGE_BLOCKED
                pkg.blocked_reason = status
                pkg.history.append("NEXT→IMAGE_BLOCKED")
                return CommandResult(
                    product=Product.IMAGE_BLOCKED,
                    phase=pkg.phase,
                    create_render_request=False,
                    message="KSB IMAGE: BLOCKED — no image_gen substitute; no silent rerun.",
                    package=pkg.snapshot(),
                )
            if status == "SUCCEEDED" or status == "COMPLETE":
                pkg.phase = PackagePhase.PACKAGE_COMPLETE
                pkg.image_returned = True
                pkg.history.append("NEXT→IMAGE_COMPLETE")
                return CommandResult(
                    product=Product.IMAGE,
                    phase=pkg.phase,
                    create_render_request=False,
                    message="KSB IMAGE returned. PACKAGE COMPLETE — HUMAN REVIEW REQUIRED. Publication NOT performed.",
                    package=pkg.snapshot(),
                )
            raise CommandError(f"unknown image_execution_status: {image_execution_status}")

        # First entry to image path — authorize at most one render request creation
        if not proposed_render_request_id:
            # Intent recorded; caller/ChatGPT creates Issue only when create_render_request True
            # Use placeholder intent id derived from cycle for continuity tracking before Issue mint
            intent_id = f"INTENT-{pkg.identity.cycle_id}"
            pkg.render_request_id = intent_id
            pkg.phase = PackagePhase.IMAGE_REQUESTED
            pkg.history.append("NEXT→IMAGE_REQUESTED(create_once)")
            return CommandResult(
                product=Product.IMAGE_IN_PROGRESS,
                phase=pkg.phase,
                create_render_request=True,
                message=(
                    "KSB IMAGE path entered — create exactly one controlled render request. "
                    "Do not create duplicates on later Next."
                ),
                package=pkg.snapshot(),
            )

        pkg.render_request_id = proposed_render_request_id
        pkg.render_issue_number = proposed_issue_number
        pkg.artifact_name = f"ksb-render-{proposed_render_request_id}"
        pkg.phase = PackagePhase.IMAGE_IN_PROGRESS
        pkg.history.append("NEXT→IMAGE_REQUESTED(bound)")
        return CommandResult(
            product=Product.IMAGE_IN_PROGRESS,
            phase=pkg.phase,
            create_render_request=False,
            message="KSB IMAGE: IN PROGRESS — request bound; no duplicate.",
            package=pkg.snapshot(),
        )

    def assert_continuity(
        self,
        *,
        status_date: str,
        bill_a_percent: int,
        bill_b_percent: int,
        bill_c_percent: int,
        baseline_id: str,
        renderer_id: str,
        render_request_id: Optional[str] = None,
    ) -> None:
        if self._active is None:
            raise CommandError("no active package")
        idn = self._active.identity
        if status_date != idn.status_date:
            raise CommandError("status_date continuity violation")
        if bill_a_percent != idn.bill_a_percent:
            raise CommandError("bill_a continuity violation")
        if bill_b_percent != idn.bill_b_percent:
            raise CommandError("bill_b continuity violation")
        if bill_c_percent != idn.bill_c_percent:
            raise CommandError("bill_c continuity violation")
        if baseline_id != idn.baseline_id:
            raise CommandError("baseline continuity violation")
        if renderer_id != idn.renderer_id:
            raise CommandError("renderer continuity violation")
        if render_request_id is not None and self._active.render_request_id:
            if render_request_id != self._active.render_request_id:
                raise CommandError("render_request_id continuity violation")

    def mutate_press_release_maturity(self, bill_a_percent: int) -> None:
        """Negative-path helper: press release MUST NOT mutate maturity."""
        raise CommandError("press release must not recalculate or mutate maturity")

    def mutate_image_maturity(self, bill_a_percent: int) -> None:
        raise CommandError("image path must not mutate maturity")
