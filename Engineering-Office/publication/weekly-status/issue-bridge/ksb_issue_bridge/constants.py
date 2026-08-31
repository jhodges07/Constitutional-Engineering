"""KSB Issue-bridge controlled constants (ECR-009 / KSB-ISSUE-BRIDGE-001).

CWC-CE-099 identity contract (authoritative for hosted Issues):

  baseline_id
      = HISTORICAL Human-accepted visual baseline identity
      = BL-WEEKLY-STATUS-BASELINE-v1.0
      ≠ clean master / render-source template

  CLEAN_MASTER_ID
      = active pristine render-source template identity
      = BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.1-CWC-CE-107-CANDIDATE
      Selected by renderer_id → renderer regions.json (NOT by baseline_id field)

  renderer_id
      = ksb_renderer@2.1.0-CWC-CE-107-CANDIDATE
      Binds the clean-master composition path (CWC-CE-107 public-image cleanup candidate)

Do NOT place CLEAN_MASTER_ID in the Issue baseline_id field (KSB-RENDER-003 / Issue #6).
"""

from __future__ import annotations

import re

REQUEST_SCHEMA_VERSION = "1.0.0"
PUBLICATION_REQUEST_TYPE = "KSB_WEEKLY_STATUS"

# HISTORICAL visual baseline — Issue envelope baseline_id MUST equal this value.
BASELINE_ID = "BL-WEEKLY-STATUS-BASELINE-v1.0"
BASELINE_SHA256 = "17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9"
BASELINE_WIDTH = 1536
BASELINE_HEIGHT = 912

# Active clean master (render source). NOT a baseline_id value.
CLEAN_MASTER_ID = "BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.1-CWC-CE-107-CANDIDATE"
CLEAN_MASTER_SHA256 = "29E243233AB0872FFF2323ACC882FC477F71865CE072C4416EEFBDEC8F8576E0"
CLEAN_MASTER_WIDTH = 1536
CLEAN_MASTER_HEIGHT = 912

# Historical CE-097 clean master (immutable evidence; not ordinary input under CE-107)
HISTORICAL_CE097_CLEAN_MASTER_ID = "BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE"
HISTORICAL_CE097_CLEAN_MASTER_SHA256 = (
    "01C29A8A20CA4D1798E4A407431B0A7FA1BD58F798D5837AD2A1CC1BF9E1D05C"
)

# Public-image cleanup candidate renderer (CWC-CE-107). Human visual PENDING.
RENDERER_ID = "ksb_renderer@2.1.0-CWC-CE-107-CANDIDATE"

TITLE_PREFIX = "[KSB-RENDER] "
REQUEST_ID_RE = re.compile(r"^KSB-RENDER-\d{4}-\d{2}-\d{2}-\d{3}$")
SHA40_RE = re.compile(r"^[0-9a-f]{40}$")

TRUSTED_ASSOCIATIONS = frozenset({"OWNER", "MEMBER", "COLLABORATOR"})

ENVELOPE_KEYS = frozenset(
    {
        "request_schema_version",
        "publication_request_type",
        "request_id",
        "canonical_sha",
        "baseline_id",
        "renderer_id",
        "render_payload",
    }
)

RENDER_PAYLOAD_KEYS = frozenset(
    {"status_date", "bill_a_percent", "bill_b_percent", "bill_c_percent"}
)

# Markers for machine-readable Issue body extraction
BODY_FENCE_START = "```ksb-render-request"
BODY_FENCE_END = "```"

ARTIFACT_NAME_PREFIX = "ksb-render-"

RESULT_SCHEMA_VERSION = "1.0.0"
