# KSB-RENDER-003 — Clean-Master baseline_id Contract Mismatch

**Defect ID:** KSB-RENDER-003  
**Title:** CLEAN-MASTER BASELINE_ID CONTRACT MISMATCH  
**Classification:** HOSTED BRIDGE / REQUEST CONTRACT DEFECT  
**Governing Work Card:** CWC-CE-099  
**Related:** CWC-CE-097 (visual architecture accepted); CWC-CE-098 (canonicalization); Issue #6  

**Not:** KSB-RENDER-002 (visual overlay/fixed-layer failure).

---

## Failed hosted evidence (immutable)

| Field | Value |
|---|---|
| Request | KSB-RENDER-2026-08-30-005 |
| Issue | #6 |
| Workflow run | 33339179855 |
| Canonical SHA | 87e48e631edbc21cc64d96cc2095a0b2703d63d0 |
| renderer_id | ksb_renderer@2.0.0-CWC-CE-097-CANDIDATE |
| Requested baseline_id | BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE |
| Gate | REJECT |
| Code | INVALID_INPUT |
| Reason | baseline_id mismatch |
| Windows renderer | SKIPPED |
| PNG | NONE |

---

## Root cause

Gate `BASELINE_ID` (and Issue field `baseline_id`) means the **historical** Human-accepted visual baseline:

`BL-WEEKLY-STATUS-BASELINE-v1.0`

Issue #6 placed the **clean master render-source** identity into `baseline_id`:

`BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE`

Comparison: `data["baseline_id"] != BASELINE_ID` → REJECT before render.

Clean-master rendering architecture was not at fault.

---

## Reconciliation (CWC-CE-099 Option A)

- `baseline_id` remains historical baseline ID.  
- Clean master remains bound to `renderer_id` → renderer `regions.json`.  
- No new Issue field.  
- No redefinition of baseline_id to mean clean master.  
- Documentation + gate error message clarified; negative tests added.
