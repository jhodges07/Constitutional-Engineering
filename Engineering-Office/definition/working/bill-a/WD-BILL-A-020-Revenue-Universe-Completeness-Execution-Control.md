# WD-BILL-A-020 — Kansas Government Revenue Universe Completeness and Execution Control

**Document ID:** WD-BILL-A-020  
**Title:** Kansas Government Revenue Universe — Completeness Methodology and Evidence-Execution Control  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-125 (defines method; does **not** certify completeness); CWC-CE-127 (applies method to Domain 01 only); CWC-CE-128 (Domain 01 closure; completeness **not** upgraded); CWC-CE-130 (applies method to Domain 02); CWC-CE-131 (Domain 02 closure reassessment; statewide completeness **not** certified)  
**Governing Human Intent:** WD-BILL-A-018 / Q-BILL-A-005 Option (a)  
**Governing schema:** WD-BILL-A-019  
**Governing LOU candidate:** LOU-004 Draft 1.1 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / METHOD DEFINED — DOMAIN 01 **SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS** — DOMAIN 02 **SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS** — STATEWIDE COMPLETENESS **NOT CERTIFIED** — NOT ACCEPTED  
**Version:** 0.5.0  
**Effective Date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-020-Revenue-Universe-Completeness-Execution-Control.md  
**Source ID:** SRC-BILL-A-023  

```text
COMPLETENESS METHODOLOGY / EXECUTION CONTROL
NO STATEWIDE COMPLETENESS CERTIFICATION
DOMAIN 01 APPLIED UNDER CWC-CE-127 (WD-BILL-A-025)
DOMAIN 02 APPLIED UNDER CWC-CE-130 (WD-BILL-A-033)
DOMAIN 02 CLOSURE REASSESSED UNDER CWC-CE-131 (WD-BILL-A-037)
AI SYNTHESIS IS NOT KANSAS-LAW EVIDENCE
BLANK ≠ RETAIN
NOT A SPEC
NOT HG-D1 / HG-D2
```

---

## 1. Purpose

Define what evidence sweeps and reconciliations must later be completed before the project may make a **controlled completeness claim** that the current-state Kansas Government Revenue Universe has been reasonably identified.

Completeness SHALL NOT mean absolute omniscience.

**No completeness certification occurs under this CWC.** **Audit execution is not authorized.**

---

## 2. Source hierarchy (execution rules)

| Class | Use | Forbidden use |
|---|---|---|
| PRIMARY-LEGAL | Legal authority: Kansas Constitution; Kansas Statutes Annotated; session laws; legally material administrative regulations; controlling Kansas judicial authority **if located** (do not invent holdings); local ordinances/resolutions where necessary | Inventing section numbers, holdings, or legal effect |
| GOV-DATA | Fiscal/current-state evidence: KDOR; KLRD; Kansas Department of Administration; official Kansas budget materials; Kansas ACFR / official financial statements; Consensus Revenue Estimates; official agency revenue/fee schedules; official local-government financial materials; official bond/debt materials; other official government fiscal sources discovered during execution | Inventing rates, collections, or quantities |
| FEDERAL MODEL | H.R. 25 IH (SRC-BILL-A-015) for Kansas FairTax economic-model crosswalk **only** | Treating H.R. 25 as Kansas law |
| CONTROL-DOC | AGCL 00A–00J classification | Marking any control SATISFIED by audit |
| AI-SYNTHESIS | May assist discovery, indexing, query generation, or comparison | Establishing current Kansas law, legal authority, tax classification, rate, collections, statutory purpose, fund destination, debt obligation, fiscal quantity, or legal effect |

Exact titles, editions, articles, and section numbers remain `[TO BE VERIFIED]` / `[CITATION/TEXT NEEDED]` until an execution CWC retrieves them.

---

## 3. Candidate completeness protocol

A later controlled completeness claim would require documented completion (or documented gap) of:

| ID | Sweep / reconciliation |
|---|---|
| CMP-A | Kansas constitutional authority sweep |
| CMP-B | Kansas statutory title / chapter sweep |
| CMP-C | Session-law / recent-change check |
| CMP-D | KDOR revenue / tax source reconciliation |
| CMP-E | KLRD tax / revenue publication reconciliation |
| CMP-F | State budget revenue-source reconciliation |
| CMP-G | State ACFR / financial-statement reconciliation |
| CMP-H | Agency fee / revenue authority reconciliation |
| CMP-I | Local-government authority sweep |
| CMP-J | County revenue-authority reconciliation |
| CMP-K | City revenue-authority reconciliation |
| CMP-L | School-district revenue-authority reconciliation |
| CMP-M | Township / special-district / authority reconciliation |
| CMP-N | Bond / debt revenue-source reconciliation |
| CMP-O | Duplicate / alias normalization |
| CMP-P | Economic-function normalization |
| CMP-Q | Unexplained-receipt report |
| CMP-R | Unmatched-legal-authority report |
| CMP-S | Source-gap report |
| CMP-T | Domain-coverage matrix (Domains 01–12 vs sweeps) |
| CMP-U | Final exception / unknown register |

Do **not** declare the universe complete because one source found no additional claims.

Maps to WD-BILL-A-016 CMP-KLRS-001–010 (those remain nested; this protocol is the locked execution-control expansion).

---

## 4. Execution order (recommended; not self-authorized)

```text
CWC-CE-125 (this card)
= schema + domains + evidence rules + completeness method
= DONE AS DEFINITION ONLY

CWC-CE-127
= DOMAIN 01 EXCISE / EXCISE-TYPE EXECUTED
  → WD-BILL-A-022 execution instance (schema remains WD-BILL-A-019)
  → beyond-motor-fuel question: YES — VERIFIED
  → disposition field 25 remains BLANK
  → no RETAIN of motor fuel

CWC-CE-130
= DOMAIN 02 PROPERTY-BASED CLAIMS EXECUTED
  → WD-BILL-A-031 execution instance (schema remains WD-BILL-A-019)
  → 15 claim-category rows at execution; dispositions BLANK
  → completeness: SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS (WD-BILL-A-033)
  → no property-tax elimination design

CWC-CE-131
= DOMAIN 02 EVIDENCE CLOSURE / RECONCILIATION
  → WD-BILL-A-037; WD-BILL-A-031 count **16**
  → KRU-D02-016 added; KRU-D02-010/011 TY 2026 mill NOT CURRENT
  → completeness **not upgraded**: SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS
  → dispositions BLANK; Domain 03 not executed

NEXT (Human-authorized; number not assigned)
= residual Domain 02 gaps, then remaining domains 03–12
  against the SAME master register
  still no invented dispositions
THEN
= Human disposition CWC(s)
```

CWC-CE-125 did not execute the audit. CWC-CE-127 executed Domain 01 only. Statewide Universe remains uncertified.

---

## 5. Acceptance criteria for a future Domain 01 execution CWC (not this CWC)

1. Writes only Domain 01 rows into the master schema; no pre-invented claim list.  
2. WD-BILL-A-012 §2 and WD-BILL-A-013 satisfied for those rows.  
3. Beyond-motor-fuel question answered from PRIMARY-LEGAL / GOV-DATA or marked `[TO BE VERIFIED]` with locators — **not** from AI memory.  
4. Compulsory status YES / NO / UNCERTAIN; KLRS candidacy per Option (a); field 25 BLANK.  
5. Motor fuel not converted to RETAIN.  
6. AI synthesis not used as Kansas-law or fiscal evidence.  
7. No HG-D1, SPEC, HG-D2, criminal statute, publication, maturity change, commit, or push unless a later CWC separately authorizes Git.  
8. Unrelated working-tree files not staged.

CWC-CE-125 does **not** pass those criteria because execution is **not** authorized.

**CWC-CE-127:** Domain 01 execution status is recorded in WD-BILL-A-025. Statewide Universe completeness remains **not certified**.  
**CWC-CE-128:** Domain 01 completeness **reassessed, not upgraded**. WD-BILL-A-025 v0.2.0 / WD-BILL-A-028. Statewide Universe completeness remains **not certified**.  
**CWC-CE-130:** Domain 02 completeness recorded in WD-BILL-A-033 as **SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS**. Statewide Universe completeness remains **not certified**.  
**CWC-CE-131:** Domain 02 completeness **reassessed** in WD-BILL-A-033 / WD-BILL-A-037 as **SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS** (not upgraded). Statewide Universe completeness remains **not certified**.

---

## 6. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-09-02 | CWC-CE-125: locked candidate completeness protocol CMP-A–U and Domain 01-first execution order. Not certified. Not executed. |
| 0.2.0 | 2026-09-02 | CWC-CE-127: Domain 01 execution status only. Universe not certified. |
| 0.3.0 | 2026-09-02 | CWC-CE-128: Domain 01 closure status; completeness not upgraded. Universe not certified. |
| 0.4.0 | 2026-09-02 | CWC-CE-130: Domain 02 applied; substantially complete with explicit gaps. Universe not certified. |
| 0.5.0 | 2026-09-02 | CWC-CE-131: Domain 02 closure reassessed; completeness not upgraded. Universe not certified. |
