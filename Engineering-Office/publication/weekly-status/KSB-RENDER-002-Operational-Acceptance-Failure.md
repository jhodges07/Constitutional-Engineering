# KSB-RENDER-002 — Operational Human Acceptance Failure

**Defect ID:** KSB-RENDER-002  
**Classification:** OPERATIONAL HUMAN ACCEPTANCE FAILURE  
**Governing Work Card (remediation):** CWC-CE-096 / ECR-013  
**Predecessor remediation (insufficient):** CWC-CE-094 / ECR-012 / KSB-RENDER-001  

---

## Evidence

| Field | Value |
|---|---|
| Request | KSB-RENDER-2026-08-30-004 |
| Issue | #5 |
| Workflow run | 33336840366 |
| Canonical SHA | ad370c32116973a7f063214cd08f1601bd435c93 |
| Renderer | ksb_renderer@1.1.0-CWC-CE-094 |
| Workflow conclusion | SUCCESS |
| Human image acceptance | **REJECTED** |

## Observed behavior

Newly produced image still visually contained historical raster content associated with a previous KSB state. Most visibly, Bill C showed historical **10%** in the same area as current **4%**.

## Disposition

LOCAL TEST PASS does not override HUMAN OPERATIONAL ACCEPTANCE FAILURE.

**Required:** RENDERER ARCHITECTURE REMEDIATION — true blank-canvas composition (CWC-CE-096).

Plate-fill / larger mask is **not** an acceptable primary correction.
