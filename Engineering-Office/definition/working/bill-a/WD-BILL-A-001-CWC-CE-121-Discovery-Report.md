# WD-BILL-A-001 — CWC-CE-121 Discovery Report

**Document ID:** WD-BILL-A-001  
**Title:** CWC-CE-121 Bill A LOU Discovery Report  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-121  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / CANDIDATE — NOT ACCEPTED — NOT AUTHORIZED  
**Version:** 0.1.0  
**Effective Date:** 2026-08-30  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-001-CWC-CE-121-Discovery-Report.md  

**Authority Effect:** Discovery only. Does not accept any LOU. Does not assign HG-D1. Does not create a SPEC.

---

## 1. Repository authority

| Check | Result |
|---|---|
| Expected repository | `jhodges07/Constitutional-Engineering` |
| CWC expected canonical path | `X:\GitHub\Constitutional-Engineering` |
| Alternate clone observed | `D:\Constitutional-Engineering` — **behind origin/main by 27 commits at discovery**; not used for writes |
| Canonical workspace used | `X:\GitHub\Constitutional-Engineering` |
| Branch | `main` |
| Starting canonical SHA | `32bd7c3c627187ab470ac7ff2ede68651ac3b6a7` |
| `origin/main` | `32bd7c3c627187ab470ac7ff2ede68651ac3b6a7` |
| HEAD == origin/main | **YES** |
| Remote | `https://github.com/jhodges07/Constitutional-Engineering.git` |

CWC-CE-121 stop condition (“origin/main unexpectedly advanced”) applied to the stale `D:\` clone. The CWC-specified `X:\` clone matched `origin/main`. Work proceeded on `X:\`. No reset, clean, stash, rebase, or overwrite of unrelated Human work.

---

## 2. Existing LOU identity / numbering

| Document ID | Title | Version / status | Git posture | Role |
|---|---|---|---|---|
| LOU-001 | Kansas Two-Bill Tax Engineering Project | Draft 0.3 / NOT ACCEPTED / HG-D1 PENDING | Tracked (canonical) | Shared Bill A **and** Bill B candidate. CWC-CE-085 reconciled labels to public pins. |
| LOU-002 | Constitutional Engineering Master Plan | Draft 0.5 / HG-D1 ACCEPTED | Tracked (canonical) | Master Plan. Does not accept Bill A. |
| LOU-003 | Kansas NBEF Act | Draft 0.1 / NOT ACCEPTED / HG-D1 PENDING | **Untracked** | Bill C. Occupies `LOU-003`. Out of CWC-CE-121 scope. |
| LOU-004 | — | **Did not exist at discovery** | — | Next unused sequential identity |

Numbering authority (TMP-002 / IDX-001 / README-DEF-001): `LOU-NNN` sequential integers; numbers never reused.

**Numbering decision (not an invention of a skipped number):** LOU-001 and LOU-002 exist as committed identities. LOU-003 exists as a Bill C candidate file. The next unused sequential identity is **LOU-004**. CWC-CE-121 forbids assuming a new number and forbids overwriting an existing LOU. Using LOU-001 or LOU-003 for Bill A would overwrite or collide.

---

## 3. Bill A / Bill A-B shared-LOU issue (required report)

### 3.1 Finding

No dedicated accepted or draft **Bill A–only** LOU existed. Bill A Definition currently lives inside **LOU-001**, a shared two-bill candidate.

CWC-CE-086 Option 3 (Human-accepted locally): retain LOU-001 as **master** Engineering Definition for coordinated Bill A/B; use bill-specific **public-review packets**; optional later separation into independent bill-specific LOUs only if subsequently justified and authorized. Option 3 explicitly does **not** split LOU-001 into separate normative LOUs.

CWC-CE-121 subsequently authorizes a Bill A Engineering Definition workspace and contemplates:

- A. continue an existing Bill A LOU;  
- B. separate Bill A from an existing shared Bill A/B draft LOU;  
- C. create a new Bill A LOU candidate under the next authorized LOU identity;  
- D. STOP if identity/numbering is ambiguous.

### 3.2 Disposition under CWC-CE-121 (not silent resolution)

| Option | Result |
|---|---|
| A — continue LOU-001 as the Bill A LOU | **Rejected for this CWC.** Continuing LOU-001 as Bill A–only work would mix Bill B content and risk rewriting Bill B Definition. CWC-CE-121 forbids modifying Bill B artifacts and forbids merging Bill B into Bill A. |
| B — separate Bill A from the shared draft | **Selected as process.** LOU-001 left unmodified. |
| C — new LOU under next identity | **Selected as artifact.** New candidate = **LOU-004**. |
| D — STOP | **Not required.** Identity of Bill A is aligned to STD-011 / CWC-CE-085 / CWC-CE-121 public pin. Numbering next-unused is LOU-004. Shared-LOU **relationship** remains UNRESOLVED (no supersession claimed). |

**Reported issue:** A Bill A–only working LOU now exists **alongside** unmodified shared LOU-001. That is working separation, not Human-accepted supersession, and not a rewrite of Bill B.

---

## 4. Identity history (retained)

| Era | Bill A meaning | Bill B meaning | Authority |
|---|---|---|---|
| NOTE-PKG-KS-TAX-001 / OPT-KS-TAX-05 | Comprehensive replacement (Bill 1) | Property-tax elimination (Bill 2) | Informational pack |
| LOU-001 Draft 0.2 (CWC-CE-059) | Five-year elimination mandate only | Elimination **plus** replacement | Human-directed revision; **NOT HG-D1 accepted** |
| LOU-001 Draft 0.3 (CWC-CE-085) | Comprehensive replacement **plus** same five-year elimination destination | Five-year elimination mandate (not comprehensive replacement) | Label reconciliation to public KSB pins; **NOT HG-D1 accepted** |
| CWC-CE-121 | Comprehensive Kansas tax-system replacement | Kansas property-tax elimination (referenced only) | This CWC working identity |

Draft 0.2 inverted labels are **retained in LOU-001 history** and are **not** used as this CWC’s Bill A identity.

---

## 5. Other Bill A Definition surfaces (not overwritten)

| Path | Role | Action |
|---|---|---|
| `Engineering-Office/publication/definition/public-review-candidates/BILL-A/PRC-BILL-A-2026-08-30.md` | Public-review packet; master = LOU-001; NOT RELEASED | Unmodified |
| `Bill_A/grok/2026-08-30-GROK-Bill-A-Research-Scout-Round-01.md` | Untracked Grok AI-SYNTHESIS scout | Unmodified; cited as non-authoritative evidence |
| `Engineering-Office/publication/weekly-status/KSB-MATURITY-CERT-001-CWC-CE-085.md` | Bill A maturity 19% Human-certified | Unmodified; maturity unchanged |
| `Engineering-Office/definition/working/WD-MP-001` … `WD-MP-003` | Master Plan working artifacts (CWC-CE-070) | Unmodified |
| TMP-002, STD-001, WF-001, definition/README.md (dirty) | Unrelated / prior Human local work | Unmodified |

CWC-CE-085 / CWC-CE-086 evidence used: identity reconciliation, maturity 19/19/4, Option 3, PRC-BILL-A, LOU-003 Bill C occupancy. CWC-CE-086 public review remains PARKED / NOT RELEASED. This CWC does not start public review.

---

## 6. Template / Engineering-Office structure

| Item | Result |
|---|---|
| LOU template | TMP-002 (working tree v1.1.0; Public Review metadata). Instance uses required sections. Candidate authority banner per CWC-CE-121 (not “accepted understanding”). |
| LOU storage | `Engineering-Office/definition/` |
| Working Definition surface | `Engineering-Office/definition/working/` already exists (CWC-CE-070). Bill A working files placed in `working/bill-a/` so Master Plan WD-MP-* is not mixed or rewritten. |
| Evidence taxonomy | PRIMARY-LEGAL / GOV-DATA / SECONDARY-ANALYSIS / TESTIMONY / HISTORICAL / SCRIPTURE / AI-SYNTHESIS / CONTROL-DOC |

---

## 7. Discovery conclusion

**Action taken:** B + C — separate Bill A working Definition from shared LOU-001; create **LOU-004** as Draft / Candidate / NOT HUMAN-ACCEPTED.

**Not taken:** overwrite LOU-001; occupy LOU-003; invent LOU-005; pass HG-D1; change maturity; publish; commit; push.
