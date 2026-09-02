# WD-BILL-A-009 — H.R. 25 FairTax Evidence Crosswalk (Working)

**Document ID:** WD-BILL-A-009  
**Title:** H.R. 25 FairTax Evidence Crosswalk — Kansas Mirror Trace Surface  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-121 (Definition workspace origin); Human Q-BILL-A-002 reply 2026-09-01; CWC-CE-123 (exception boundary); CWC-CE-127; CWC-CE-128; CWC-CE-133; CWC-CE-134  
**Governing LOU candidate:** LOU-004 Draft 1.3 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / INCOMPLETE — NOT ACCEPTED — NOT PRIMARY EVIDENCE BY ITSELF  
**Version:** 0.7.0  
**Effective Date:** 2026-09-01  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-009-HR25-FairTax-Evidence-Crosswalk.md  
**Source ID:** SRC-BILL-A-014 (this register); primary text = SRC-BILL-A-015  

```text
PRIMARY EVIDENCE = CONGRESSIONAL H.R. 25 TEXT
AI SUMMARY IS NON-AUTHORITATIVE
DO NOT SILENTLY ALTER H.R. 25 ECONOMIC STANDARDS
DO NOT INVENT KANSAS TAX INVENTORY OR CLASSIFICATIONS
KANSAS EQUIVALENT COLUMNS ARE TRACE WORK — NOT LAW
THIS CROSSWALK DOES NOT ADVANCE ANY HUMAN GATE
```

---

## 1. Primary-source pin

| Field | Value |
|---|---|
| Measure | H.R. 25 — FairTax Act of 2025 |
| Congress | 119th Congress (2025–2026) |
| Version pinned for this Definition cycle | **Introduced in House (IH)** — as retrieved 2026-09-01 |
| Authoritative locator (HTML bill page) | https://www.congress.gov/bill/119th-congress/house-bill/25 |
| Authoritative locator (IH PDF) | https://www.congress.gov/119/bills/hr25/BILLS-119hr25ih.pdf |
| File designation | `BILLS-119hr25ih.pdf` |
| Latest action (as of retrieval) | 2025-01-03: Introduced; referred to House Ways and Means — **[VERIFY on congress.gov before SPEC use]** |
| Source class | **PRIMARY-LEGAL** (U.S. congressional bill text) |
| Authority status for Kansas law | **NON-AUTHORITATIVE** as Kansas law; **PRIMARY** as federal FairTax model text for Human Intent mirror |
| AI-synthesis status | **FORBIDDEN as primary evidence** |

If a later Congress version (reported, engrossed, enrolled, or enacted) supersedes this IH text, Engineering SHALL re-pin and re-trace before treating any Kansas mirror row as complete.

---

## 2. Crosswalk schema

Each row SHALL eventually contain:

| Column | Meaning |
|---|---|
| Crosswalk ID | Stable Bill A row ID |
| H.R. 25 provision | Act section / proposed IRC subtitle section |
| Exact operative language | Verbatim excerpt or pinpoint cite into IH PDF (not paraphrase for meaning-critical rules) |
| Economic function | What economic boundary the provision creates |
| Proposed Kansas equivalent | Mirror / adapt / deviate / out-of-scope — **working only** |
| Federal-specific language requiring adaptation | Secretary, United States, federal agencies, SSNs, federal rates, federal sunset, etc. |
| Kansas constitutional/statutory issue | `[CITATION/TEXT NEEDED]` / `[LEGAL EFFECT UNKNOWN]` until verified |
| Human-authorized Kansas deviation | Only if Human expressly authorized (see WD-BILL-A-008 §§8–10) |
| Trace status | NOT STARTED / PARTIAL / TRACED / CONFLICT / BLOCKED |

CWC-CE-123 required chain (must be filled before drafting; paraphrase into Kansas law is forbidden):

```text
H.R. 25 provision
→ operative concept
→ Kansas mirror candidate
→ Kansas jurisdictional adaptation required?
→ express Human deviation?
→ evidence/legal question
→ status
```

Where exact H.R. 25 language is intended for later reuse, preserve the provision locator so Legislative Engineering can retrieve and verify the authoritative text. **This CWC does not draft Kansas statutory adaptation.**

---

## 3. Priority rows opened by Q-BILL-A-002 Human Intent

Status as of 2026-09-01: **PARTIAL locator open**. Full verbatim attachment and Kansas adaptation remain incomplete. Do not treat this table as a finished legal crosswalk.

| Crosswalk ID | H.R. 25 provision (IH) | Economic function (working) | Proposed Kansas equivalent | Federal-specific adaptation needed | KS issue | Human deviation | Trace status |
|---|---|---|---|---|---|---|---|
| XW-HR25-001 | Proposed IRC §2(14) — Taxable property or service | Defines taxable property/services; excludes intangible property and used property from “property”; services include/exclude certain wage cases | **KANSAS MIRROR** of economic definition | “United States,” federal employer classes, §801 financial intermediation | `[LEGAL EFFECT UNKNOWN]` KS constitutional tax uniformity / classification | None (intent = mirror) | PARTIAL — locator opened |
| XW-HR25-002 | Proposed IRC §2(16) — Used property | Prevents re-tax of property already taxed under §101 (or held non-business as of 2026-12-31 under federal text) | **KANSAS MIRROR** — do not invent title-based Kansas definition | Federal date “December 31, 2026”; credit cross-refs §§202/203/205 | Kansas transition start date **OPEN HUMAN / EVIDENCE** | None | PARTIAL — locator opened |
| XW-HR25-003 | Proposed IRC §101 — Imposition of sales tax | Imposes tax on taxable property/services (final-consumption architecture) | **KANSAS MIRROR** of taxable-event architecture; **rate not adopted by this Human reply** | Federal rate machinery; federal administration | Rate, base, remittance authority `[LEGAL EFFECT UNKNOWN]` | None on base architecture | PARTIAL |
| XW-HR25-004 | Proposed IRC §102 — Intermediate and export sales; business purpose; investment purpose | Business-purpose and investment-purpose purchases not taxed as final consumption | **KANSAS MIRROR** exact economic standard | “Export,” federal trade definitions | KS nexus / sourcing `[LEGAL EFFECT UNKNOWN]` | None | PARTIAL |
| XW-HR25-005 | Proposed IRC §103 / conversion rules; §202 business-use conversion credit | Business↔personal conversion taxation/credit | **KANSAS MIRROR** | Federal credit administration | KS credit/admin `[LEGAL EFFECT UNKNOWN]` | None | NOT STARTED (locator known) |
| XW-HR25-006 | Proposed IRC §705 — Mixed use property | Allocation for mixed business/personal use | **KANSAS MIRROR** — do not invent separate KS allocation system | Federal computation month rules | `[LEGAL EFFECT UNKNOWN]` | None | PARTIAL |
| XW-HR25-007 | Proposed IRC §702 — Gaming activities (chance; chances not taxable property/service; tax on taxable gaming services of gaming sponsor) | Chance (lottery/raffle/chips/wagers) not §101 taxable property/service; separate tax on taxable gaming services of gaming sponsor | **KANSAS MIRROR** classification for KS Lottery, casino, horse-racing, sports wager, raffle, etc. | “Secretary,” federal 23% gaming-services rate, federal remittance | **CWC-CE-128:** Kansas lottery/casino is a **state-owned** lottery gaming operation with a contracted manager (74-8734 / 74-8711). Pathway classified as enterprise / governmental share of gaming revenue and **referred to Domain 08** (privilege fee to Domain 05). Not forced into Domain 01. H.R. 25 remains federal model only. KS Lottery / Racing & Gaming Kansas-mirror drafting still `[TO BE VERIFIED]`; rate adaptation OPEN | None on classification; rate not Human-set here | PARTIAL — IH index/cross-ref may say §701(a) for gaming sponsor while gaming body text is §702 — **VERIFY against IH PDF**. Current-state Kansas mechanism evidenced; not a Bill A gaming disposition |
| XW-HR25-008 | Proposed IRC §§201–207 credits/refunds; registration/documentation elsewhere in subtitle | Credits, refunds, anti-avoidance/support mechanisms preserving economic boundary | **KANSAS MIRROR** where economic; adapt administration | Federal Sales Tax Bureau / Secretary / administration credit | KS DOR / constitutional `[LEGAL EFFECT UNKNOWN]` | None yet | NOT STARTED |
| XW-HR25-009 | Family consumption allowance / rebate (§§301 et seq.) | Federal prebate / poverty-level rebate | **NOT DISPOSED by Human reply** — OPEN HUMAN DECISION | SSN / lawful-resident / federal poverty metrics | KS constitutional gift/rebate issues `[LEGAL EFFECT UNKNOWN]` | None authorized | CONFLICT / UNKNOWN — Human silent |
| XW-HR25-010 | Act Title I repeals (income, payroll, estate/gift); Title IV Sixteenth Amendment sunset | Federal repeal / sunset architecture | **OUT OF SCOPE as federal repeal**; KS income/other tax disposition via Kansas inventory classification — **not invented** | Entirely federal constitutional/machinery | KS income-tax repeal is CURRENT KANSAS LAW question + Human disposition | Not a FairTax-base deviation | BLOCKED pending KS inventory evidence |
| XW-HR25-011 | Human-authorized KS surviving-excise non-stacking (motor fuel as **example**) | If a surviving excise applies to a transaction, Kansas FairTax shall not also apply unless Human later expressly authorizes stacking; surviving excise applies to personal **and** business purchases | **EXPRESS KANSAS DEVIATION / CONTROL** (WD-BILL-A-008 §8; WD-BILL-A-012 §3 F–G) | N/A (Kansas-authored) | Existing KS motor-fuel (and other excise) statutes `[TO BE VERIFIED]` | **YES — uniform surviving-excise rule; motor fuel is the example, not a Human RETAIN** | INTENT RECORDED; statute text NOT YET TRACED; **no individual tax RETAINED** |
| XW-HR25-012 | Excise purpose-control chain | Any surviving excise → express purpose → restricted pool → direct purpose execution; no admin overhead against pool (uniform standard A–E, H) | **EXPRESS KANSAS DEVIATION / CONTROL** (WD-BILL-A-008 §9; WD-BILL-A-012 §3 A–E, H) | N/A | KS fund/constitutional dedication `[LEGAL EFFECT UNKNOWN]` | **YES — purpose control for all surviving excises** | INTENT RECORDED; engineering test for DIRECT vs ADMIN **NOT YET BUILT**; no individual RETAIN |
| XW-HR25-013 | Proposed IRC §702 — Gaming activities (chance not §101 taxable property/service) | Chance (lottery ticket / raffle / chips / wagers) classification vs tax on taxable gaming services of gaming sponsor | **KANSAS MIRROR** of chance classification; Human presently classifies **state-operated lottery ticket sales as not a Kansas FairTax taxable transaction** (CWC-CE-123 N) — must still VERIFY against IH PDF before drafting | “Secretary,” federal gaming-services rate | KS Lottery law `[TO BE VERIFIED]`; do not paraphrase H.R. 25 into Kansas statute | None on chance classification unless Human later deviates from H.R. 25 | PARTIAL — Human Intent recorded; PDF VERIFY still required (also CF-BILL-A-007) |

---

## 4. Work remaining (required; not optional)

1. Attach verbatim operative excerpts (or PDF pinpoint cites with line-stable quotes) for every priority row from `BILLS-119hr25ih.pdf` — not from AI paraphrase.  
2. Resolve IH internal cross-reference inconsistency (gaming sponsor §701(a) vs §702 body) against the PDF.  
3. Enumerate remaining H.R. 25 subtitle sections (financial intermediation, government enterprises, not-for-profits, imports, housing, etc.) into additional XW rows.  
4. Build Kansas revenue-claim inventory from PRIMARY-LEGAL / GOV-DATA only — **do not invent**. **CWC-CE-134:** Domain 01 working inventory exists in WD-BILL-A-022 (14 rows); Domain 02 in WD-BILL-A-031 (16 rows); Domain 03 in WD-BILL-A-040 (5 rows after closure); remaining domains empty.  
5. Classify each inventoried Kansas claim under Human disposition vocabulary: REMAIN / TRANSFORM / DISAPPEAR / REQUIRES HUMAN DECISION / EVIDENCE INSUFFICIENT. **CWC-CE-134: all Domain 01, 02, and 03 field 25 values remain BLANK. Do not fill this step from existence.**  
6. Surface every federal-only mechanism (rate formula, prebate, IRS abolition, Sixteenth Amendment sunset, federal administration fee) as ADAPT / OUT-OF-SCOPE / REQUIRES HUMAN DECISION — never silent change.  
7. Open Human questions for unused excise balances, sinking funds, rate reductions, refunds, credits, and other undisposed excise mechanisms (WD-BILL-A-008 §10).  
8. Fill EV-KS-REV-001–012 (WD-BILL-A-013) without inventing Kansas claims; map each inventoried claim against XW rows for stack/duplicate. Audit **not executed** in this cycle.

---

## 5. Explicitly empty / forbidden

| Item | Status |
|---|---|
| Complete Kansas tax-class inventory | **PARTIAL** — Domain 01 in WD-BILL-A-022; Domain 02 in WD-BILL-A-031; Domain 03 in WD-BILL-A-040; Domains 04–12 EMPTY |
| Kansas excise / excise-type audit findings | **DOMAIN 01 EXECUTED** in WD-BILL-A-023 — dispositions **BLANK**; not LOU-accepted |
| REMAIN/TRANSFORM/DISAPPEAR classifications | **EMPTY** except architecture rule; no class-level dispositions asserted; motor fuel is **not** a RETAIN |
| Kansas FairTax rate | **NOT SET** by Q-BILL-A-002 reply |
| Prebate / family allowance Kansas adoption | **OPEN HUMAN DECISION** |
| AI summary of H.R. 25 as primary evidence | **FORBIDDEN** |

---

## 6. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-09-01 | Opened after Q-BILL-A-002 Human Intent. Pinned H.R. 25 IH (119th). Priority rows locator-opened. Inventory not invented. |
| 0.2.0 | 2026-09-01 | CWC-CE-123: CWC chain documented; XW-HR25-013 lottery-ticket Human classification + PDF VERIFY. No Kansas inventory invented. |
| 0.3.0 | 2026-09-01 | Q-BILL-A-003: XW-HR25-011/012 motor fuel = example of uniform surviving-excise standard, **not** Human RETAIN. Audit not executed. |
| 0.4.0 | 2026-09-02 | CWC-CE-127: Domain 01 overlap/stack observations recorded in WD-BILL-A-023 §K. No RETAIN. H.R. 25 still not Kansas law. |
| 0.5.0 | 2026-09-02 | CWC-CE-128: XW-HR25-007 Kansas lottery/casino mechanism evidenced and referred off Domain 01. H.R. 25 still not Kansas law. PDF VERIFY still required. |
| 0.6.0 | 2026-09-02 | CWC-CE-133: Domain 03 income/privilege claims classified STRUCTURALLY OUTSIDE H.R. 25 FINAL-CONSUMPTION EVENT in WD-BILL-A-044. No RETAIN/DISAPPEAR. H.R. 25 still not Kansas law. |
| 0.7.0 | 2026-09-02 | CWC-CE-134: Domain 03 closure does not change H.R. 25 classifications. Count remains 5. No RETAIN/DISAPPEAR. H.R. 25 still not Kansas law. |
