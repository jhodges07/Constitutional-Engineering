# BILL IDENTITY RECONCILIATION — PROPOSED DISPOSITION (CWC-CE-085 / ECR-005)

**Document ID:** BILL-ID-RECON-001-PROPOSED  
**Classification:** Informational Proposal — Not Operative; Not HG-D1  
**Governing Work Card:** CWC-CE-085  
**Governing ECR:** ECR-005  
**Status:** RECONCILED in LOU-001 Draft 0.3 under CWC-CE-085 (LOU remains NOT ACCEPTED / HG-D1 PENDING)  
**Preparing Agent:** CE-Engineer  

```text
LOU-001 DRAFT 0.3 IDENTITY RECONCILED TO PUBLIC PINS
NO LOU ACCEPTANCE
NO MATURITY CERTIFICATION BY THIS FILE
```

---

## 1. Authoritative public identities (STD-011 §26)

| Bill | Public FIXED title |
|---|---|
| **Bill A** | COMPREHENSIVE KANSAS TAX-SYSTEM REPLACEMENT |
| **Bill B** | KANSAS PROPERTY-TAX ELIMINATION |
| **Bill C** | KANSAS NBEF ACT *(Node-Based Educational Framework)* |

These pins identify the legislative objects for KSB Status, maturity ledger, and public FIXED copy.

---

## 2. Current LOU-001 Draft 0.2 internal labels (discrepancy)

Path (local / reportedly untracked):  
`Engineering-Office/definition/LOU-001-Kansas-Two-Bill-Tax-Engineering-Project.md`

| LOU-001 Draft label | Draft meaning |
|---|---|
| LOU-001 **Bill A** | Five-year property-tax elimination mandate |
| LOU-001 **Bill B** | Elimination + comprehensive replacement architecture |

Relative to STD-011 §26, this is **reversed**.

---

## 3. Preferred principle

A Bill identifier SHALL identify the **same** legislative object across LOU, SPEC, CWC, drafting, maturity ledger, KSB Status, Git evidence, and publication.

Therefore LOU-001 internal labels SHALL be corrected to match public pins **before** WSMAT-001 becomes Active.

---

## 4. Proposed correction (LOU-001 Draft only)

Because LOU-001 is **Draft / NOT ACCEPTED / HG-D1 PENDING**, correcting labels does **not** accept the LOU and does not pass HG-D1.

**Proposed bounded edit (Human-authorized; not performed in this continuation):**

| After correction | Meaning (unchanged substance) | Aligns to public |
|---|---|---|
| LOU-001 **Bill A** | Elimination + comprehensive replacement architecture | COMPREHENSIVE KANSAS TAX-SYSTEM REPLACEMENT |
| LOU-001 **Bill B** | Five-year property-tax elimination mandate | KANSAS PROPERTY-TAX ELIMINATION |

Also update any internal cross-references, tables, and section headings that encode the old A/B mapping.  
Preserve Acceptance Status = NOT ACCEPTED / HG-D1 PENDING.

**Not modified under this continuation** (existing control does not auto-authorize silent edit of Human drafts outside the ECR package without HE direction). Human Engineer should authorize a separate bounded draft correction CWC or express HE instruction.

---

## 5. Related artifacts to check after LOU-001 correction

Local packages may contain SPEC drafts with legacy naming (e.g., under `Engineering-Office/packages/ChatGPT-Kansas-Tax-Engineering/`). Those are informative/untracked packaging artifacts and SHALL be aligned or clearly labeled non-authoritative after LOU-001 correction. They do not override STD-011 §26.

---

## 6. Bill C rule

Bill C public pin is accepted for weekly FIXED title only.

- NBEF Control Documents / framework repository maturity ≠ Bill C legislative maturity.  
- Bill C requires its own Engineering Definition LOU/SPEC evidence for stages beyond limited S01 credit under WSMAT-001.  
- Current HE fact: Bill C LOU **NOT PASSED**.

---

## 7. Activation precondition

ECR-005 / WSMAT-001: **Do not activate** maturity algorithm until this identity correction is Human-confirmed complete (or Human records an alternate explicit controlled mapping — not recommended).
