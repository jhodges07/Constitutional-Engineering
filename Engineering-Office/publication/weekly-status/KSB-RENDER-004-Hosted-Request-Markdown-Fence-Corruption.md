# KSB-RENDER-004 — Hosted Request Markdown Fence Corruption

**Defect ID:** KSB-RENDER-004  
**Title:** HOSTED REQUEST MARKDOWN FENCE CORRUPTION  
**Classification:** HOSTED BRIDGE / REQUEST-CONSTRUCTION DEFECT  
**Governing Work Card:** CWC-CE-102  
**Related:** CWC-CE-101 (hosted Outcome B); Issue #7; run 33339896335  

**Not:** KSB-RENDER-003 (baseline_id contract semantics).  
**Not:** a baseline_id regression — correct historical baseline was present in JSON text.

---

## Failed hosted evidence (immutable)

| Field | Value |
|---|---|
| Request | KSB-RENDER-2026-08-30-006 |
| Issue | #7 |
| Workflow run | 33339896335 |
| Canonical SHA | 037e81143c3b56c624d67b2ab5e28963a3d4a3d3 |
| Intended baseline_id | BL-WEEKLY-STATUS-BASELINE-v1.0 |
| Intended renderer_id | ksb_renderer@2.0.0-CWC-CE-097-CANDIDATE |
| Gate | REJECT |
| Code | INVALID_INPUT |
| Reason | missing ```ksb-render-request fence |
| baseline_id gate | NOT REACHED |
| Windows renderer | SKIPPED |
| PNG | NONE |
| Artifact | NONE |

Do not reopen Issue #7. Do not edit Issue #7. Do not rerun workflow 33339896335.

---

## Root cause (proven)

CWC-CE-101 constructed the Issue body via PowerShell-invoked `python -c` with the markdown opening fence embedded in a PowerShell double-quoted / escape-sensitive context.

PowerShell treats backtick (U+0060) as the escape character. A literal triple-backtick fence therefore collapses:

| Stage | Opening fence |
|---|---|
| Intended | ```ksb-render-request (3 backticks) |
| After PowerShell expansion | `ksb-render-request (1 backtick) |
| Observed on Issue #7 | single-backtick open/close |

Live local PowerShell proof (CWC-CE-102):

```text
INTENDED=```ksb-render-request
EXPANDED=`ksb-render-request
INTENDED_BT_COUNT=3
EXPANDED_BT_COUNT=1
```

Corruption occurred **before** `gh issue create` / during shell interpolation of the body text — not inside the GitHub gate parser, and not because of baseline_id semantics.

---

## Canonical parser contract (unchanged / authoritative)

| Item | Requirement |
|---|---|
| Opening fence | exactly ```ksb-render-request |
| Closing fence | exactly ``` |
| Newline | required after opening fence before JSON |
| Extraction | `gate.extract_request_json` finds `BODY_FENCE_START`, then first newline, then JSON until `BODY_FENCE_END` |
| Malformed fences | REJECT `INVALID_INPUT` |
| Parser weakening | FORBIDDEN |

---

## Remediation (CWC-CE-102)

Fence-safe construction:

1. Write request JSON to a UTF-8 file (no fence in shell).  
2. Run `issue-bridge/scripts/write_ksb_issue_body.py --request … --out … --allowed-sha …`  
3. Module uses `build_issue_body` / `BODY_FENCE_*` constants in Python only.  
4. Pre-submit: `pre_submit_validate` (fence → JSON → envelope).  
5. Create Issue with `gh … --body-file <path>` only (never `--body` with interpolated fences).  
6. Post-create: read back Issue body and re-parse before trusting workflow.

See: `issue-bridge/FENCE-SAFE-HOSTED-REQUEST-PROCEDURE.md`

---

## Hosted acceptance disposition (CWC-CE-105)

**Status:** CLOSED BY HOSTED TEST  

| Field | Value |
|---|---|
| Acceptance CWC | CWC-CE-104 |
| Closure CWC | CWC-CE-105 |
| Request | KSB-RENDER-2026-08-30-007 |
| Issue | #8 |
| Run | 33340965250 |
| Pre-submit / readback | PASS (OPENING_BACKTICK_COUNT=3) |
| Hosted gate | PASS |

Immutable failure evidence (Issue #7 / run 33339896335) remains preserved.
