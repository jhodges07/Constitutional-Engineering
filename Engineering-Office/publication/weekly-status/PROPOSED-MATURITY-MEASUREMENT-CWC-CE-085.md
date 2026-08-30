# PROPOSED — KSB Status VSM Maturity Measurement (NON-AUTHORITATIVE)

**Document ID:** WSMAT-001-PROPOSED  
**Title:** Proposed KSB Status VSM Maturity Measurement Model  
**Classification:** Informational Proposal — Not Operative CONTROL  
**Governing Work Card:** CWC-CE-085 Bounded Continuation — VSM Maturity Measurement Authority and First Measurement  
**Status:** PROPOSED / NON-AUTHORITATIVE  
**Version:** 0.1.0-PROPOSED  
**Effective Date:** *none — not Active*  
**Preparing Agent:** CE-Engineer  

```text
NOT OPERATIVE CONTROL
NOT AN ACTIVE MATURITY ALGORITHM
PROVISIONAL / SAMPLE CALCULATIONS ONLY
REQUIRES HUMAN ENGINEER ACCEPTANCE + ECR / STD AMENDMENT BEFORE AUTHORITY
```

### Disposition (CWC-CE-085 control authorization package)

Human Engineer accepted the measurement **concept** subject to controlled implementation (ECR-005).

**Proposed disposition (Option C + B):**

1. Retain this file as **historical proposal evidence**.  
2. Promote accepted concepts into candidate Active control **WSMAT-001** (`WSMAT-001-KSB-Status-Maturity-Measurement.md`) via **ECR-005** + proposed STD-011 v1.3.0 amendment.  
3. Do **not** make this PROPOSED file operative.

Successor candidate: `WSMAT-001-KSB-Status-Maturity-Measurement.md` (Proposed / Not Operative until ECR-005 approved and implemented).

---

## 1. Why this exists

STD-011 §27 and WSGAP-001 GAP-WS-007 record that **no Active CONTROL** presently authorizes deterministic automated Bill maturity-percentage formulas.

CWC-CE-085 requires evidence-based PROPOSED percentages for Human certification, without inventing permanent accidental policy.

This document is the **smallest candidate measurement model** for Human decision. It does **not** amend STD-011.

---

## 2. Authority sources inspected

| Artifact | Role | Maturity algorithm? |
|---|---|---|
| STD-011 v1.2.1 §27 | Percentages HUMAN-SUPPLIED/APPROVED until later CONTROL; AI-proposed non-operative until HE approval; **no automatic formula** | **NO** |
| STD-011 §2 Out of Scope item 7 | Automated Bill maturity formulas excluded unless later Active CONTROL | **NO** |
| WSPC-001 / WSGAP GAP-WS-007 | Automated % = deferred production maturity item | **NO** |
| STD-001 §4.1 | Operational Engineering Definition process (LOU → HG-D1 → SPEC → HG-D2 → Controlled Execution…) | Gate rules **YES**; % formula **NO** |
| STD-008 | Legislative Manager artifact lifecycle states (Proposed→…→Published) | Post-LOU legislative artifact states; **not** KSB % formula |
| BL-WEEKLY-STATUS-BASELINE-v1.0 | **Visual** FIXED VSM layout (public composition) | Design/projection **YES**; operational gate completion **NO** |
| Dedicated VSM control file | **NONE FOUND** | — |

---

## 3. Visual VSM vs operational Process

**Visual VSM (baseline FIXED layout) — 13 stages (public composition):**

1. Citizen Problem / Political Idea  
2. Human Engineering Intent  
3. Research & Evidence  
4. Letter of Understanding (LOU)  
5. Requirements / SPEC  
6. Constitutional & AGCL Control Evaluation  
7. Legislative Engineering  
8. Engineering & Legal Review  
9. Public Review & Signal  
10. Human Acceptance  
11. Controlled Git Version  
12. Publication  
13. Future Runtime Republic Digital Twin  

**Operational Process (STD-001 §4.1) — Engineering Definition → Controlled Execution:**

Human Engineering Intent → Research → LOU → HG-D1 → SPEC → HG-D2 → CWC-CE → … → Git → Publication  

**Relationship (proposed):**

- Visual VSM is the **public maturity spine** for KSB Status percentages.  
- STD-001 / HG-D1 / HG-D2 supply **mandatory gate rules** (especially LOU acceptance).  
- A visual diagram alone **SHALL NOT** declare a gate complete.  
- Gate completion requires controlled evidence + applicable Human acceptance.

---

## 4. Proposed measurement rules (candidate)

### 4.1 Equal stage weights (simplest auditable)

- 13 stages; each full stage = `100/13` percentage points.  
- Display as nearest integer: `round(100 * credited_units / 13)` with half-up.  
- No false-precision decimals on the public image.

### 4.2 Hard-gate ceiling

A bill **SHALL NOT** receive maturity credit for stages whose controlled authority requires a predecessor mandatory gate that is unsatisfied.

For Engineering Definition bills, **LOU HG-D1 acceptance** is a mandatory gate before SPEC and downstream engineering stages earn maturity credit.

### 4.3 LOU stage states (candidate)

| LOU state | Stage-4 credit |
|---|---|
| NOT STARTED | 0.0 |
| IN DEVELOPMENT (controlled draft exists; HG-D1 not accepted) | 0.5 |
| READY FOR HUMAN REVIEW (explicitly declared) | 0.75 |
| HUMAN-ACCEPTED (HG-D1) | 1.0 |

`IN DEVELOPMENT ≠ PASSED`. Silence ≠ acceptance.

### 4.4 Partial credit for stages 1–3

Only when controlled evidence supports defined exit criteria (to be finalized in Active CONTROL).  
Until Active CONTROL defines exit criteria, provisional measurement shall use conservative binary or half-stage credits and label them **PROVISIONAL**.

### 4.5 Human certification

```text
CALCULATED MATURITY  ≠  CERTIFIED KSB MATURITY
```

AI/ChatGPT/CE-Engineer **measures and proposes**.  
Human Engineer **ACCEPT / MODIFY / REJECT**.

---

## 5. Recommended control placement (Human decision)

Smallest durable path:

1. **ECR** (new or extension of ECR-004) authorizing a KSB maturity-measurement CONTROL; then  
2. Amend **STD-011 Part B** (new section after §27) **or** adopt a dedicated Active SPEC/STD under STD-014;  
3. Close / recharacterize **GAP-WS-007** when Active.

Do **not** treat WSPC-001 or this PROPOSED file as operative CONTROL.

---

## 6. Public Bill pin ↔ LOU-001 internal naming (audit note)

STD-011 §26 public FIXED titles **do not match** LOU-001 Draft 0.2 internal Bill A/B labels:

| Public KSB Status pin (authoritative for weekly titles) | LOU-001 Draft 0.2 internal label |
|---|---|
| Bill A — COMPREHENSIVE KANSAS TAX-SYSTEM REPLACEMENT | LOU-001 **Bill B** (elimination + replacement architecture) |
| Bill B — KANSAS PROPERTY-TAX ELIMINATION | LOU-001 **Bill A** (elimination mandate) |
| Bill C — KANSAS NBEF ACT | *no bill LOU found* |

Measurement SHALL use public pins for Bill identity and LOU-001 for shared two-bill tax Engineering Definition evidence.

---

## 7. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0-PROPOSED | 2026-08-30 | Initial NON-AUTHORITATIVE proposal under CWC-CE-085 maturity continuation. |
