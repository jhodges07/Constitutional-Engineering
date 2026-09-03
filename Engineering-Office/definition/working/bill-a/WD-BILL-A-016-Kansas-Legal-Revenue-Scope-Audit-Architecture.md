# WD-BILL-A-016 — Kansas Legal Revenue Scope Audit Architecture

**Document ID:** WD-BILL-A-016  
**Title:** Kansas Legal Revenue Scope — Comprehensive Audit Requirement, Discovery Architecture, and Completeness Controls  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-124 (defines architecture); CWC-CE-125 (Q-BILL-A-005 Option (a); schema locked in WD-BILL-A-019 / WD-BILL-A-020); CWC-CE-127 (Domain 01 executed); CWC-CE-128 (Domain 01 closure); CWC-CE-130 (Domain 02 executed); CWC-CE-131 (Domain 02 closure); CWC-CE-133 (Domain 03 executed); CWC-CE-134 (Domain 03 closure); CWC-CE-136 (Domain 04 executed); CWC-CE-137 (Domain 04 closure); CWC-CE-141 (Domain 05 executed); CWC-CE-144 (Domain 06 executed; remaining domains **not** executed)  
**Governing Human Intent:** WD-BILL-A-015 / Q-BILL-A-004; WD-BILL-A-018 / Q-BILL-A-005 Option (a); subordinate excise intent WD-BILL-A-012 / Q-BILL-A-003  
**Governing LOU candidate:** LOU-004 Draft 1.9 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / ARCHITECTURE DEFINED — SCHEMA LOCKED IN WD-BILL-A-019/020 — DOMAIN 01 **EXECUTED** — DOMAIN 02 **EXECUTED / CLOSURE APPLIED** — DOMAIN 03 **EXECUTED / CLOSURE APPLIED** — DOMAIN 04 **EXECUTED / CLOSURE APPLIED** — DOMAIN 05 **EXECUTED** — DOMAIN 06 **EXECUTED** — REMAINING DOMAINS **NOT PERFORMED** — NOT ACCEPTED  
**Version:** 1.2.0  
**Effective Date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-016-Kansas-Legal-Revenue-Scope-Audit-Architecture.md  
**Source ID:** SRC-BILL-A-020  

```text
KANSAS LEGAL REVENUE SCOPE AUDIT ARCHITECTURE
DOMAIN 01 EXECUTED UNDER CWC-CE-127
DOMAIN 02 EXECUTED UNDER CWC-CE-130
DOMAIN 02 CLOSURE APPLIED UNDER CWC-CE-131
DOMAIN 03 EXECUTED UNDER CWC-CE-133
DOMAIN 03 CLOSURE APPLIED UNDER CWC-CE-134
DOMAIN 04 EXECUTED UNDER CWC-CE-136
DOMAIN 04 CLOSURE APPLIED UNDER CWC-CE-137
DOMAIN 05 EXECUTED UNDER CWC-CE-141
DOMAIN 06 EXECUTED UNDER CWC-CE-144
REMAINING DOMAINS NOT EXECUTED
STATEWIDE UNIVERSE NOT CERTIFIED
NO RETAIN / TRANSFORM / DISAPPEAR DISPOSITIONS
BLANK DISPOSITION ≠ RETAIN
MOTOR FUEL IS NOT RETAINED
CRIMINAL INTENT IS NOT A CRIMINAL STATUTE
NOT A SPEC
NOT HG-D1 / HG-D2
RECOMMENDED NEXT CONTROLLED WORK — NOT SELF-AUTHORIZED
```

---

## 1. Why this artifact exists

Q-BILL-A-004 Human Intent (WD-BILL-A-015) requires an evidenced inventory of **all material governmental revenue claims** of Kansas state and local government before the final post-Bill-A Kansas Legal Revenue Scope can be defined.

Executing that statewide/local audit would materially broaden CWC-CE-124 beyond Definition recording. This file **defines** the audit architecture. It does **not** perform it.

WD-BILL-A-013 remains valid as the **excise-domain** audit requirement and is **subordinate** to this architecture. Do not silently rewrite WD-BILL-A-013 history.

---

## 2. Working Definition — Kansas Government Revenue Universe and Kansas Legal Revenue Scope

**CWC-CE-125 refinement (Q-BILL-A-005 Option (a); does not erase Q-BILL-A-004):**

```text
KANSAS GOVERNMENT REVENUE UNIVERSE
= The complete evidenced universe of material monetary inflows, receipts,
  compulsory claims, transfers, financing proceeds, and other material
  governmental revenue/receipt classes discovered for Kansas state and
  local governmental entities.

KANSAS LEGAL REVENUE SCOPE
= The intended closed post-Bill-A set of COMPULSORY GOVERNMENTAL
  REVENUE CLAIMS that government is affirmatively authorized to impose,
  assess, collect, or otherwise compel from persons or organizations.
```

ALL KLRS CLAIMS ARE WITHIN THE GOVERNMENT REVENUE UNIVERSE. NOT ALL GOVERNMENT RECEIPTS ARE KLRS CLAIMS.

Receipt of money by government does **not** itself create authority to compel payment.

Locked candidate schema: WD-BILL-A-019. Completeness / execution control: WD-BILL-A-020.

Three registers SHALL remain distinct:

| Register | Meaning | Status under CWC-CE-125 |
|---|---|---|
| KANSAS GOVERNMENT REVENUE UNIVERSE (current-state) | All material discovered receipts / claims | **EMPTY** — audit not executed |
| CURRENT COMPULSORY-CLAIM INVENTORY | Current-state subset with compulsory status YES (still not future authority) | **EMPTY** |
| POST-BILL-A KANSAS LEGAL REVENUE SCOPE | Human-controlled closed compulsory demand-authority set | **EMPTY** — no claim authorized |

Current existence does **not** create future authority. Silence does **not** authorize a claim. A blank disposition is **not** RETAIN. Other receipts stay outside the closed demand-authority set unless the Human Engineer later expressly determines otherwise.

Current existence does **not** create future authority. Silence does **not** authorize a claim. A blank disposition is **not** RETAIN.

Candidate closed-authority rule (intent only; not current Kansas law):

```text
IF A GOVERNMENTAL REVENUE CLAIM IS NOT WITHIN THE FINAL
KANSAS LEGAL REVENUE SCOPE, GOVERNMENT HAS NO AUTHORITY
UNDER THE BILL A ARCHITECTURE TO DEMAND IT.
```

---

## 3. Relationship of Q-BILL-A-003 (excise) to this architecture

| Item | Force |
|---|---|
| WD-BILL-A-012 | Controlling Human Intent for **excise** treatment; uniform surviving-excise standard A–J; motor fuel = example, **not RETAIN** |
| WD-BILL-A-013 | Excise / excise-type audit requirement; **subordinate domain** of this architecture |
| Original practical question | Do Kansans currently pay excise or materially equivalent excise-type claims **beyond motor-fuel / gasoline**? — **must be answered by evidence**; **not answered here** |
| Search-surface expansion | Privilege, severance, unlabeled gallonage/pack/unit/volume, license/permit-on-commodity, local-option, and other classes in WD-BILL-A-015 §4 are **audit search surface**, not findings and not automatic RETAIN |

The fourteen excise questions in WD-BILL-A-012 §2 remain required for every in-scope **excise / excise-type** claim. The comprehensive register fields in §6 below apply to **every** material revenue claim, including those excise claims.

---

## 4. Audit universe (intent; not an invented inventory)

### 4.1 Jurisdictions

- State of Kansas.
- Kansas governmental subdivisions/entities with revenue-claim authority, **discovered through primary evidence**, including candidate classes: counties, cities, school districts, townships, special districts, authorities, and other entities possessing material revenue-claim authority.

Do **not** invent the complete entity universe.

### 4.2 Search surface (not findings)

Audit by **legal authority, economic function, and taxable event / trigger** — not merely by government label. A claim shall not escape examination because it is called a fee, assessment, surcharge, license, permit, or other non-“tax” name.

Search surface: WD-BILL-A-015 §4. Listing a class does **not** establish that it presently exists, is legally a tax, or will be retained.

### 4.3 Compulsory vs other governmental receipts — Q-BILL-A-005 Option (a)

**Final KLRS** = compulsory governmental revenue claims only.

**Current-state audit** SHALL still discover and classify all material governmental receipts, including non-compulsory classes. Those receipts are **OTHER RECEIPT** / outside closed demand-authority unless Human later expressly adds them.

Uncertain mixed compulsory/voluntary rows: COMPULSORY STATUS = UNCERTAIN / EVIDENCE REQUIRED; KLRS CANDIDACY = CLASSIFICATION UNRESOLVED. Do not silently resolve.

Locked fields: WD-BILL-A-019 fields 8 and 24.

---

## 5. Discovery method (multiple paths)

A revenue claim cannot be excluded merely because one source class omits it.

| Class | Candidate source types (locators to retrieve in later audit CWC — **not verified here**) |
|---|---|
| PRIMARY-LEGAL | Kansas Constitution; Kansas Statutes Annotated; session laws; administrative regulations where legally material; controlling Kansas cases **if located** (do not invent holdings); local ordinances/resolutions where required |
| GOV-DATA | Kansas Department of Revenue; Kansas Legislative Research Department; Kansas Department of Administration; Kansas ACFR / official financial statements; state budget documents; appropriation acts; Consensus Revenue Estimates; agency fee schedules; county/city/school/special-district official financial materials; official bond documents where necessary; other official governmental fiscal records discovered during the audit |
| CONTROL-DOC | AGCL 00A–00J (classification only; never SATISFIED by audit alone) |
| FEDERAL MODEL | H.R. 25 IH (`BILLS-119hr25ih.pdf`, SRC-BILL-A-015) for Kansas FairTax economic-model crosswalk **only** — not Kansas law |
| AI-SYNTHESIS | May **assist discovery**. SHALL NOT establish current Kansas law, rates, collections, authority, purpose, fund destination, legal effect, or fiscal quantities |

Exact titles, editions, articles, and section numbers remain `[TO BE VERIFIED]` / `[CITATION/TEXT NEEDED]`.

---

## 6. Master register — per-claim fields (minimum)

**CWC-CE-125:** the locked candidate 32-field schema is **WD-BILL-A-019**. Domain labels 01–12 are in that file. Historical A–P fields below remain the CWC-CE-124 minimum and map into WD-BILL-A-019 (they are not a second register).

One master Kansas Government Revenue Universe register. Domain executions write into it. Disposition remains **blank** until Human disposition. KLRS candidacy ≠ final authorization. BLANK ≠ RETAIN.

| Field | Content |
|---|---|
| A. CLAIM IDENTITY | What the claim is called in authoritative sources (verbatim) |
| B. GOVERNMENT ENTITY | Who imposes / receives it |
| C. LEGAL AUTHORITY | Constitutional / statutory / other legal authority — citation or `[CITATION/TEXT NEEDED]` |
| D. TAXABLE EVENT / TRIGGER | Event or condition creating the payment obligation |
| E. LEGALLY OBLIGATED PARTY | Who is legally required to pay |
| F. ECONOMIC FUNCTION | What the claim economically attaches to |
| G. RATE / CALCULATION | How the amount is determined — **do not invent** |
| H. PURPOSE | Legally or publicly stated purpose |
| I. DESTINATION | Where the money goes |
| J. FUND TYPE | General, dedicated, restricted, special, local, trust, enterprise, or other **evidenced** classification |
| K. ADMINISTRATION | Administrative / overhead deductions or transfers |
| L. DEPENDENCIES | Debt, bonds, contracts, federal matching, pensions, or other obligations |
| M. COLLECTIONS | Official reported quantities — `[REVENUE EFFECT UNKNOWN]` until retrieved |
| N. H.R. 25 RELATIONSHIP | Overlap / duplicate / conflict with intended Kansas FairTax mirror (WD-BILL-A-009) |
| O. AGCL RELATIONSHIP | 00A–00J classifications — never SATISFIED by audit alone |
| P. BILL A DISPOSITION | RETAIN / TRANSFORM / DISAPPEAR / HUMAN DECISION REQUIRED / EVIDENCE INSUFFICIENT — **BLANK until Human** |

Excise / excise-type rows SHALL also complete WD-BILL-A-012 §2 questions 1–14.

Stable Claim IDs SHALL be assigned in the later audit CWC. Do not invent claims in order to assign IDs.

---

## 7. Completeness problem and candidate controls

Proving a **closed universe** is more difficult than finding examples. Do **not** declare the audit complete merely because no additional claims were found in one source.

Candidate completeness controls for later Human review (not executed here):

| Control ID | Control |
|---|---|
| CMP-KLRS-001 | Statutory-title sweep |
| CMP-KLRS-002 | Agency revenue-source reconciliation |
| CMP-KLRS-003 | State financial-statement reconciliation |
| CMP-KLRS-004 | Local-government authority sweep |
| CMP-KLRS-005 | Tax/fee publication reconciliation |
| CMP-KLRS-006 | Bond/debt revenue-source reconciliation |
| CMP-KLRS-007 | Duplicate-name normalization |
| CMP-KLRS-008 | Economic-function classification |
| CMP-KLRS-009 | Unexplained-revenue exception report |
| CMP-KLRS-010 | Source-gap report |

Completeness SHALL NOT mean absolute omniscience. **CWC-CE-125 locked expansion:** WD-BILL-A-020 protocol CMP-A–U. No certification under CWC-CE-124 or CWC-CE-125.

---

## 8. Recommended next controlled-work architecture (not self-authorized)

CWC-CE-124 asked whether the next work should (A) execute the entire KLRS audit; (B) establish methodology/register first then execute domain-by-domain; or (C) divide into controlled evidence domains while maintaining one master register.

**Recommendation: C, with B as the mandatory first controlled step.**

| Option | Assessment |
|---|---|
| A. Execute the entire audit in one CWC | **Unsafe.** Completeness problem, state+local entity universe unknown, compulsory-vs-receipt boundary open, would mix Definition with unverified findings, and would silently broaden a single card. |
| B. Methodology/register first, then execute | Necessary first step; insufficient alone if later execution remains one unbounded card. |
| C. Domain-by-domain evidence CWCs against one master register | **Safest execution pattern** after the register exists. |

**CWC-CE-125 status:** Step 1 (methodology / schema lock) is **defined** in WD-BILL-A-019 and WD-BILL-A-020. It is **not** HG-D1 accepted. The register remains **empty**. Audit execution remains **not authorized**.

**Recommended next Human-authorized CWC:** Domain 01 — EXCISE / EXCISE-TYPE execution into the master register (WD-BILL-A-012 / WD-BILL-A-013 / WD-BILL-A-019). Answer the beyond-motor-fuel question from PRIMARY-LEGAL / GOV-DATA. Disposition remains BLANK. Motor fuel is not RETAINED. CWC number **not assigned**. Do **not** execute under CWC-CE-125.

Remaining domains 02–12, then completeness/gap-report, then Human disposition: WD-BILL-A-020 §4.

---

## 9. Acceptance criteria (for a future audit-execution CWC — not this CWC)

PASS of a later **execution** card would require at least:

1. Inventory method documented; no pre-invented claim list.  
2. Multiple discovery paths used; source-gap report produced.  
3. Every in-scope discovered claim has §6 fields A–O with PRIMARY-LEGAL / GOV-DATA locators or explicit unknown notation; P blank.  
4. Excise-domain rows also satisfy WD-BILL-A-013 / WD-BILL-A-012.  
5. Beyond-motor-fuel excise question answered from evidence or marked `[TO BE VERIFIED]` with locators.  
6. AI synthesis not used as Kansas law, rate, collection, purpose, destination, authority, or obligation evidence.  
7. State and local entity universe discovered, not invented; gaps reported.  
8. Current-state inventory distinguished from post-Bill-A KLRS.  
9. No RETAIN/TRANSFORM/DISAPPEAR invented; blank ≠ RETAIN; motor fuel not converted to RETAIN.  
10. No HG-D1, SPEC, HG-D2, criminal statute, publication, maturity change, commit, or push unless a later CWC separately authorizes Git.  
11. Unrelated working-tree files not staged.

This CWC-CE-124 recording does **not** pass those criteria because the audit is **not executed**.

---

## 10. Evidence-need IDs (findings EMPTY)

| ID | Need | Required class |
|---|---|---|
| EV-KLRS-001 | Complete state revenue-authority universe | PRIMARY-LEGAL + GOV-DATA |
| EV-KLRS-002 | Complete local-government revenue-authority universe / entity inventory | PRIMARY-LEGAL + GOV-DATA |
| EV-KLRS-003 | Tax vs fee vs assessment vs service charge vs penalty vs other receipt distinctions as used in Kansas sources | PRIMARY-LEGAL |
| EV-KLRS-004 | Compulsory vs voluntary governmental receipts — Option (a) membership rule recorded; per-row classification still required | HUMAN (recorded) + PRIMARY-LEGAL / GOV-DATA |
| EV-KLRS-005 | Utility / enterprise charges | PRIMARY-LEGAL + GOV-DATA |
| EV-KLRS-006 | Court fines, criminal penalties, restitution, forfeitures, settlements | PRIMARY-LEGAL + GOV-DATA |
| EV-KLRS-007 | Tuition, admission/use charges, regulatory/user fees | PRIMARY-LEGAL + GOV-DATA |
| EV-KLRS-008 | Grants, intergovernmental transfers, federal funds | GOV-DATA + PRIMARY-LEGAL |
| EV-KLRS-009 | Investment earnings, asset sales, donations, unclaimed property | GOV-DATA + PRIMARY-LEGAL |
| EV-KLRS-010 | Bond proceeds / borrowing | PRIMARY-LEGAL + GOV-DATA |
| EV-KLRS-011 | Special assessments / development / exaction charges | PRIMARY-LEGAL |
| EV-KLRS-012 | Local home-rule / existing constitutional revenue authority | PRIMARY-LEGAL |
| EV-KLRS-013 | Debt / bond impairment if sources disappear | PRIMARY-LEGAL + GOV-DATA |
| EV-KLRS-014 | Beyond-motor-fuel excise / excise-type existence | PRIMARY-LEGAL + GOV-DATA (WD-BILL-A-013) |
| EV-KLRS-015 | Completeness-certification methodology | CONTROL-DOC + HUMAN REVIEW |

EV-KS-REV-001–012 (WD-BILL-A-013) remain the **excise-domain** evidence needs and are nested under EV-KLRS-014 / Domain EXCISE.

---

## 11. Conflict / unknown register (surface; do not resolve)

| ID | Unknown / conflict | Status |
|---|---|---|
| CF-BILL-A-010 | Narrow Q-BILL-A-004 (excise-type classes a–g) vs comprehensive Q-BILL-A-004 (KLRS) | **Recorded supersession** — narrow question retained historically; WD-BILL-A-015 governs |
| UNK-KLRS-001 | Complete state revenue-authority universe | UNKNOWN — do not invent |
| UNK-KLRS-002 | Complete local-government revenue-authority / entity universe | UNKNOWN — do not invent |
| UNK-KLRS-003 | Kansas-source distinction among tax, fee, assessment, service charge, penalty, fine, and other receipt | Domain 05/06 bounded doctrine recorded (*Executive Aircraft*; *Heartland*; *Topeka*) — **LEGAL INTERPRETATION REQUIRED** per row; not a statewide resolution |
| UNK-KLRS-004 | Whether every governmental receipt belongs in final KLRS or only compulsory claims | **RECORDED Option (a)** — compulsory only; other receipts remain auditable outside closed demand-authority unless Human later expressly adds (WD-BILL-A-018). Per-row mixed/uncertain classification still OPEN |
| UNK-KLRS-005 | Treatment of voluntary government transactions | OPEN |
| UNK-KLRS-006 | Utility / enterprise charges | OPEN |
| UNK-KLRS-007 | Court fines / criminal penalties / restitution | OPEN |
| UNK-KLRS-008 | Tuition / admission / use charges | OPEN |
| UNK-KLRS-009 | Grants and intergovernmental transfers | OPEN |
| UNK-KLRS-010 | Investment earnings / asset sales / donations | OPEN |
| UNK-KLRS-011 | Federal funds | OPEN |
| UNK-KLRS-012 | Bond proceeds / borrowing | OPEN |
| UNK-KLRS-013 | Unclaimed property / forfeitures / settlements | OPEN |
| UNK-KLRS-014 | Regulatory fees / user fees | Domain 05 **EXECUTED** (WD-BILL-A-060/061) with explicit gaps; Domain 08 user-pay **not executed** |
| UNK-KLRS-015 | Special assessments / development / exaction charges | Domain 06 **EXECUTED** (WD-BILL-A-071/072; 14 rows) with explicit gaps; dispositions **BLANK**; Domain 07/08 referrals **not executed** |
| UNK-KLRS-016 | Local home-rule authority vs closed KLRS | `[LEGAL EFFECT UNKNOWN]` |
| UNK-KLRS-017 | Existing constitutional revenue authority vs closed KLRS | `[CITATION/TEXT NEEDED]` |
| UNK-KLRS-018 | Debt / bond impairment if a source disappears | `[LEGAL EFFECT UNKNOWN]` |
| UNK-KLRS-019 | Criminal-enforcement constitutionality | LEGAL ENGINEERING REQUIRED — not converted to a statute here |
| UNK-KLRS-020 | Official immunity | LEGAL ENGINEERING REQUIRED |
| UNK-KLRS-021 | Prosecutorial authority | LEGAL ENGINEERING REQUIRED |
| UNK-KLRS-022 | Taxpayer remedies | LEGAL ENGINEERING REQUIRED |
| UNK-KLRS-023 | Anti-evasion legal definitions | LEGAL ENGINEERING REQUIRED |
| UNK-KLRS-024 | Completeness certification methodology | OPEN / HUMAN REVIEW |
| UNK-EX-012 | Statewide excise audit required by Q-BILL-A-003 | Domain 01 **EXECUTED** (WD-BILL-A-022/023) with explicit gaps; CWC-CE-128 closure applied (WD-BILL-A-028); remaining Domain 01 residual gaps still open |
| UNK-EX-013 | Historical “materially equivalent” scope | **SUPERSEDED as the complete Q-004 question**; remains live **inside** the excise subordinate domain |

---

## 12. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-09-02 | CWC-CE-124: KLRS working concept; comprehensive audit architecture; WD-BILL-A-013 subordinated; audit not executed; architecture C+B recommended. |
| 0.2.0 | 2026-09-02 | CWC-CE-125: Q-BILL-A-005 Option (a) — KLRS = compulsory demand-authority only; Government Revenue Universe remains auditable; schema/completeness locked in WD-BILL-A-019/020; audit still not executed. |
| 0.3.0 | 2026-09-02 | CWC-CE-127: Domain 01 execution-status cross-reference. Architecture unchanged. Remaining domains not executed. Universe not certified. |
| 0.4.0 | 2026-09-02 | CWC-CE-128: Domain 01 closure-status cross-reference. Architecture unchanged. Remaining domains not executed. Universe not certified. |
| 0.5.0 | 2026-09-02 | CWC-CE-130: Domain 02 execution-status cross-reference. Architecture unchanged. Domains 03–12 not executed. Universe not certified. |
| 0.6.0 | 2026-09-02 | CWC-CE-131: Domain 02 closure-status cross-reference. Architecture unchanged. Domain 03 not executed. Universe not certified. |
| 0.7.0 | 2026-09-02 | CWC-CE-133: Domain 03 execution-status cross-reference. Architecture unchanged. Domains 04–12 not executed. Universe not certified. |
| 0.8.0 | 2026-09-02 | CWC-CE-134: Domain 03 closure-status cross-reference. Architecture unchanged. Domains 04–12 not executed. Universe not certified. |
| 0.9.0 | 2026-09-02 | CWC-CE-136: Domain 04 execution-status cross-reference. Architecture unchanged. Domains 05–12 not executed. Universe not certified. Current Kansas sales/use ≠ H.R. 25. |
| 1.0.0 | 2026-09-02 | CWC-CE-137: Domain 04 closure-status cross-reference. Architecture unchanged. Domains 05–12 not executed. Universe not certified. Completeness not upgraded. |
| 1.1.0 | 2026-09-02 | CWC-CE-141: Domain 05 execution-status cross-reference. Architecture unchanged. Domains 06–12 not executed. Universe not certified. |
| 1.2.0 | 2026-09-02 | CWC-CE-144: Domain 06 execution-status cross-reference. Architecture unchanged. Domains 07–12 not executed. Universe not certified. |
