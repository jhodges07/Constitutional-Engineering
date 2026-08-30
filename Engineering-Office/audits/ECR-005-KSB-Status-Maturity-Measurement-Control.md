# ECR-005 — KSB Status Maturity Measurement Control

**Document ID:** ECR-005  
**Title:** KSB Status Maturity Measurement Control  
**Classification:** Engineering Change Request  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Governing Standards:** STD-001; STD-011; STD-014; WF-001  
**Governing Work Card:** CWC-CE-085 — Bounded Continuation — KSB Maturity Control Authorization Package; CWC-CE-085 — ECR-005 Human Acceptance Implementation / Bill Identity Reconciliation / First Authoritative Recalculation  
**Related Prior Work:** CWC-CE-076 (WSGAP / GAP-WS-007 deferred); CWC-CE-078 / ECR-004 (STD-011 Part B packaging); CWC-CE-081–084 (date/baseline/renderer); CWC-CE-085 Outcome B (WSMAT-001-PROPOSED); CWC-CE-085 authorization package (OUTCOME A)  
**Status:** Implemented  
**Disposition:** HUMAN ACCEPTED — LOCALLY IMPLEMENTED UNDER CWC-CE-085 (Verified-Closed / Git canonicalization pending separate Human Git gate; Human maturity certification pending)  
**Implementation State:** IMPLEMENTED LOCALLY — STD-011 Version 1.3.0; WSMAT-001 Active locally; LOU-001 Draft 0.3 identity reconciled; first authoritative recalculation performed; CERTIFIED KSB MATURITY pending Human Engineer  
**Operative Authority:** Locally Active under Human-accepted ECR-005 / CWC-CE-085 implementation (not yet on origin/main until Human Git gates)  
**Version:** 1.0.0  
**Effective Date:** 2026-08-30  
**Primary Category:** STD  
**Secondary Categories:** ADM, BL (measurement model), COR (Bill identity integrity)  
**Requestor:** Human Engineer  
**Preparing Agent:** CE-Engineer  
**Acceptance Recording Agent:** CE-Engineer  
**Implementation Agent:** CE-Engineer  

---

## 0. Activation Banner

```text
HUMAN ACCEPTED
APPROVED FOR CONTROL IMPLEMENTATION
IMPLEMENTED LOCALLY UNDER CWC-CE-085
STD-011 VERSION 1.3.0 ACTIVE LOCALLY
WSMAT-001 ACTIVE LOCALLY
LOU-001 BILL A/B IDENTITY RECONCILED (DRAFT 0.3 — NOT ACCEPTED)
FIRST AUTHORITATIVE RECALCULATION COMPLETED
CERTIFIED KSB MATURITY PENDING HUMAN ENGINEER
GIT NOT ADVANCED — NOT CANONICAL ON origin/main UNTIL HUMAN GIT GATES
KSB RENDER / PUBLICATION NOT AUTHORIZED BY THIS ECR ALONE
```

Human Engineer acceptance under CWC-CE-085 authorized controlled implementation of the maturity-measurement architecture.  
Local implementation establishes STD-011 v1.3.0 and Active WSMAT-001 for deterministic CALCULATED MATURITY.  
Human CERTIFIED KSB MATURITY for Bill percentages remains a separate Human gate.  
Package generation, phone POC, and social-media publication remain separately authorized.  
Git stage/commit/push remain Human-gated (WF-001 HG-4 / HG-5).

---

## 1. Purpose

Authorize establishment of an Active deterministic **KSB Status engineering-maturity measurement** system for BlueprintLiberty Weekly Public Engineering Status Bill percentages, while preserving Human Engineer certification authority.

This ECR proposes:

1. adoption of **WSMAT-001 — KSB Status Maturity Measurement** as the subordinate Active maturity algorithm CONTROL (upon approval/implementation);  
2. amendment of **STD-011 Part B** (proposed Version **1.3.0**) to authorize deterministic calculation under WSMAT-001 and to distinguish CALCULATED vs CERTIFIED maturity;  
3. controlled disposition of **GAP-WS-007**;  
4. Bill A/B identity integrity rules aligning LOU/SPEC/CWC/maturity/KSB public pins;  
5. first authoritative recalculation procedure (no grandfathering of provisional 27/27/8).

This ECR does **not** by itself:

- certify Bill A/B/C percentages;  
- accept any LOU (HG-D1);  
- generate weekly Markdown/PNG;  
- authorize phone POC / publication;  
- stage/commit/push.

---

## 2. Reason for Change

### 2.1 Problem

STD-011 §27 and WSGAP-001 **GAP-WS-007** record that no Active CONTROL authorizes deterministic Bill maturity-percentage formulas. Percentages remain HUMAN-SUPPLIED / HUMAN-APPROVED only.

CWC-CE-085 discovered that Human-invented percentages are not the intended steady-state authority model. Human Engineer accepted the WSMAT measurement *concept* subject to controlled implementation, but did **not** certify provisional values 27/27/8.

Without an Active algorithm CONTROL, AI-proposed maturity cannot become authoritative KSB maturity without risking accidental undocumented convention.

### 2.2 Human decision (architecture accepted; values not certified)

Under CWC-CE-085 maturity control authorization continuation, the Human Engineer ACCEPTS for v1.0 (subject to this ECR implementation):

1. 13-stage KSB Value Stream Map as maturity spine;  
2. equal weighting;  
3. bounded partial-stage credit;  
4. hard mandatory-gate ceilings;  
5. current-stage work may earn bounded credit;  
6. downstream work SHALL NOT earn credit while a required predecessor Human Gate is unsatisfied;  
7. AI/ChatGPT as MEASURER / PROPOSER;  
8. Human Engineer as CERTIFIER;  
9. Bill A/B identity discrepancy must be resolved before the algorithm becomes Active.

Provisional calculated samples **27% / 27% / 8%** remain **NON-AUTHORITATIVE** and are **not grandfathered**.

### 2.3 Current control gap

| Element | State |
|---|---|
| STD-011 §27 | No automatic formula; HE-supplied/approved only |
| STD-011 §2.2 item 7 | Automated formulas out of scope unless later Active CONTROL |
| GAP-WS-007 | Deferred / may remain Human-gated during POC |
| WSMAT-001-PROPOSED | Informational proposal only (`0.1.0-PROPOSED`) |
| Dedicated Active maturity CONTROL | **Absent** |

---

## 3. Description of Change

### 3.1 Architecture (smallest proper placement)

| Layer | Role |
|---|---|
| **STD-011 Part B (proposed §27 rewrite)** | Normative packaging authority: CALCULATED vs CERTIFIED; pointer to WSMAT-001; Bill identity integrity; first-recalculation rule |
| **WSMAT-001** | Subordinate Active specification: stage model, evidence criteria, hard gates, rounding, evidence snapshot, AI/HE roles |
| **STD-001 / WF-001** | Unchanged operational gate authority (HG-D1, HG-D2, HG-1…HG-8) |
| **Visual baseline VSM** | Public maturity spine labels (FIXED composition); does **not** alone declare stage complete |
| **WSMAT-001-PROPOSED** | Historical proposal evidence after concepts incorporated |

Do **not** promote WSPC-001 to operative CONTROL. Do **not** invent a parallel percentage system outside STD-011 / WSMAT-001.

### 3.2 Proposed STD-011 amendment

Exact proposed text is filed at:

`Engineering-Office/standards/proposed/STD-011-v1.3.0-Maturity-Amendment-PROPOSED-ECR-005.md`

Summary:

1. Amend §2.2 item 7 to recognize WSMAT-001 once Active.  
2. Replace/expand §27 Percentage Authority to authorize deterministic calculation under Active WSMAT-001, require certification before operative weekly VARIABLE use, and forbid grandfathering provisional values.  
3. Advance STD-011 to Version **1.3.0** upon implementation.  
4. Record ECR-005 / CWC-CE-085 in governing metadata / version history.

### 3.3 Proposed WSMAT-001

Candidate control filed at:

`Engineering-Office/publication/weekly-status/WSMAT-001-KSB-Status-Maturity-Measurement.md`

Status at filing: **Proposed / Not Operative**. Becomes Active only after Human approval of this ECR and controlled implementation.

### 3.4 Bill identity integrity (required before Active)

Public KSB pins (STD-011 §26) are authoritative for weekly-status Bill identity:

| Public Bill | Public FIXED title |
|---|---|
| Bill A | COMPREHENSIVE KANSAS TAX-SYSTEM REPLACEMENT |
| Bill B | KANSAS PROPERTY-TAX ELIMINATION |
| Bill C | KANSAS NBEF ACT |

LOU-001 Draft 0.2 currently reverses internal Bill A/B labels relative to those pins.

**Disposition (proposed):** Correct LOU-001 Draft labels to match public pins **before** WSMAT-001 becomes Active. Because LOU-001 is Draft / NOT ACCEPTED / local untracked working draft, correction is permitted as Engineering Definition draft repair under Human direction and does **not** constitute HG-D1 acceptance. This ECR does **not** itself edit LOU-001; a separate bounded Human-authorized draft correction is required.

Bill C legislative maturity requires Bill C Engineering Definition evidence. NBEF framework repository maturity ≠ Bill C legislative maturity.

### 3.5 GAP-WS-007 disposition

GAP-WS-007 remains in its current deferred / Human-gated state during this proposal.

**Closure is not authorized by drafting this ECR.**

Proposed lifecycle after approval/implementation:

```text
OPEN / DEFERRED
 → CONTROL AUTHORIZED (ECR-005 Approved)
 → IMPLEMENTED (STD-011 v1.3.0 + WSMAT-001 Active)
 → VALIDATED (first authoritative recalculation + certification record)
 → CLOSED
```

### 3.6 First authoritative recalculation

After WSMAT-001 becomes Active:

1. Recalculate Bills A/B/C from zero under Active rules + reconciled identities + current evidence + gate states.  
2. Provisional 27/27/8 are **not** inherited.  
3. Equality to provisional values is permitted only if recalculation produces them.  
4. Results remain CALCULATED until Human CERTIFIES.

### 3.7 Explicit non-effects

- No LOU acceptance.  
- No maturity certification of 27/27/8.  
- No KSB render / phone POC / publication under this ECR alone.

---

## 4. Change Category

**Primary:** STD  
**Secondary:** ADM; COR (identity integrity); BL (measurement model as controlled weekly-status measurement baseline)

---

## 5. Impact Analysis

| Area | Impact |
|---|---|
| STD-011 | Part B percentage authority change (proposed 1.3.0) |
| Weekly-status packaging | Calculated maturity becomes eligible after certification; renderer contract unchanged (still integer VARIABLE percents) |
| STD-001 / WF-001 | No gate semantics change; maturity references existing Human Gates |
| Visual baseline | Unchanged; stage identifiers map to public labels |
| GAP-WS-007 | Closure criteria defined; not closed by this proposal |
| LOU-001 | Requires label reconciliation before Active algorithm |
| Git / publication | Unchanged WF-001 HG-4/5/6 |
| Prior provisional calc | Non-authoritative; not grandfathered |

**Backward compatibility:** Existing weekly packages (if any) remain historical. Future packages require Active WSMAT calculation + Human certification when using algorithm path.

---

## 6. Documents and Repositories Affected

| Artifact | Action |
|---|---|
| `Engineering-Office/audits/ECR-005-…` | This ECR (Proposed) |
| `Engineering-Office/publication/weekly-status/WSMAT-001-…` | Create (Proposed → later Active) |
| `Engineering-Office/standards/proposed/STD-011-v1.3.0-…` | Proposed amendment text |
| `Engineering-Office/standards/STD-011-Public-Documentation.md` | Amend only after ECR approval + implementation authorization |
| `Engineering-Office/publication/weekly-status/GAP-CLOSURE-MATRIX-CWC-CE-076.md` | Update GAP-WS-007 row only after authorized state transitions |
| `Engineering-Office/publication/weekly-status/PROPOSED-MATURITY-MEASUREMENT-CWC-CE-085.md` | Retain as historical proposal evidence |
| `Engineering-Office/definition/LOU-001-…` | Separate draft identity correction (not performed by this ECR filing) |
| Constitutional-Engineering repository | Local proposal only until Human Git gates |

---

## 7. Proposed Resolution / Implementation Plan

1. Human Engineer reviews this ECR + WSMAT-001 + STD-011 proposed amendment.  
2. Human Engineer ACCEPTS / MODIFIES / REJECTS the package.  
3. If accepted: Human authorizes LOU-001 Bill A/B label correction (still Draft / NOT ACCEPTED).  
4. Implementation CWC applies STD-011 → 1.3.0 and activates WSMAT-001.  
5. Perform first authoritative recalculation (A/B/C from zero).  
6. Human CERTIFIES or MODIFIES calculated values for the target KSB cycle.  
7. Validate GAP-WS-007 closure criteria; close only when met.  
8. Separate CWC resumes CWC-CE-085 render path if/when authorized.

---

## 8. Approval Record

| Decision | Authority | State |
|---|---|---|
| Architecture concept acceptance | Human Engineer (CWC-CE-085) | ACCEPTED |
| ECR-005 approval | Human Engineer (HG-2) via CWC-CE-085 implementation continuation | **ACCEPTED** |
| STD-011 v1.3.0 activation | Human Engineer authorized implementation | **IMPLEMENTED LOCALLY** |
| WSMAT-001 Active | Human Engineer authorized implementation | **ACTIVE LOCALLY** |
| LOU-001 Bill A/B identity reconciliation | Human Engineer authorized (Draft only) | **COMPLETED (Draft 0.3)** |
| Maturity % certification | Human Engineer | **PENDING** (first authoritative recalculation returned) |
| LOU HG-D1 (any bill) | Human Engineer | **NOT PASSED** (preserved) |
| Git canonicalization (HG-4/HG-5) | Human Engineer | **PENDING** |

Silence is not approval.

---

## 9. Verification Record

| Check | State |
|---|---|
| ECR identifier = next sequential (ECR-005) | Verified |
| Human acceptance recorded under CWC-CE-085 | Yes |
| STD-011 locally advanced to 1.3.0 | Yes |
| WSMAT-001 Active locally (1.0.0) | Yes |
| LOU-001 Draft 0.3 identity aligned to STD-011 §26 | Yes |
| LOU Acceptance Status remains NOT ACCEPTED | Yes |
| First authoritative recalculation from zero | Yes (see maturity ledger artifact) |
| Provisional 27/27/8 not grandfathered | Yes |
| Baseline SHA unchanged | Required |
| No Git stage/commit/push under this CWC | Required |
| No KSB render under this CWC | Required |
| GAP-WS-007 closed | **NO** — Human certification remains |

---

## 10. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0-PROPOSED | 2026-08-30 | Initial Proposed ECR under CWC-CE-085 maturity control authorization package. |
| 1.0.0 | 2026-08-30 | Human-accepted and locally implemented under CWC-CE-085: STD-011 v1.3.0; WSMAT-001 Active; LOU-001 Draft 0.3 identity reconciliation; first authoritative recalculation; certification pending. |
