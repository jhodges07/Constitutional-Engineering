# WD-BILL-A-072 — Domain 06 Master Register Execution Instance

**Document ID:** WD-BILL-A-072  
**Title:** Kansas Government Revenue Universe / KLRS Master Register — Domain 06 Execution Instance  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-144  
**Canonical starting SHA:** `19343f33a830b6e2e831c4546f9709fbd1b4e1bb`  
**Schema authority:** WD-BILL-A-019 (this file does **not** replace the schema lock; 32 fields unchanged)  
**Governing LOU candidate:** LOU-004 Draft 1.9 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / DOMAIN 06 ROWS POPULATED FROM EVIDENCE — REGISTER **NOT** STATEWIDE COMPLETE — NOT ACCEPTED  
**Version:** 1.0.0  
**Effective Date:** 2026-09-02  
**Retrieval date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-072-Domain-06-Master-Register-Execution.md  

```text
EXECUTION INSTANCE OF WD-BILL-A-019 SCHEMA
DOMAIN 06 ONLY
HUMAN DISPOSITION = BLANK ON EVERY ROW
BLANK ≠ RETAIN
CURRENT EXISTENCE ≠ POST-BILL-A AUTHORITY
CURRENT RECEIPTS ≠ REQUIRED REPLACEMENT REVENUE
ASSESSMENT ≠ AUTOMATICALLY RETAIN
PROPERTY-RELATED ASSESSMENT ≠ AUTOMATICALLY PROPERTY TAX
ONE CITY / PROJECT / PARCEL ≠ ONE CLAIM
KLRS CANDIDACY ≠ FINAL AUTHORIZATION
STATEWIDE UNIVERSE NOT CERTIFIED
NO FAIRTAX RATE CALCULATION
NO FUTURE DISTRIBUTION DESIGN
```

Narrative audit: WD-BILL-A-071. Sources: WD-BILL-A-073. Completeness: WD-BILL-A-074. Conflicts: WD-BILL-A-075. Classification / referral: WD-BILL-A-076.

Domain 01 rows remain in WD-BILL-A-022. Domain 02: WD-BILL-A-031. Domain 03: WD-BILL-A-040. Domain 04: WD-BILL-A-049. Domain 05: WD-BILL-A-061. They are **not** rewritten here.

Common field values unless a row overrides:

- Field 2 EVIDENCE DOMAIN = 06
- Field 25 HUMAN BILL A DISPOSITION = **BLANK**
- Field 26 POST-BILL-A AUTHORITY STATUS = **NOT DETERMINED**
- Retrieval date = 2026-09-02
- Field 21 default: **OUTSIDE H.R. 25 CONSUMPTION-TAX EVENT AS A CLASS** (property-benefit / district / industry assessment, not retail consumption of new goods). H.R. 25 is **not Kansas law**. Future treatment **NOT DETERMINED**.
- Field 22 default: 00A QUESTION REQUIRED (installment term ≠ self-certified expiration); 00B EVIDENCE REQUIRED / QUESTION REQUIRED (notice/hearing varies); 00C POTENTIAL CONFLICT surface (property-situs/benefit as a claim event vs existence-not-event intent) **and** PROVISIONAL ALIGNMENT surface where the claim is project-benefit rather than general ownership tax; 00D QUESTION REQUIRED (exit often = pay remaining installments or stop the activity); 00E EVIDENCE REQUIRED / POTENTIAL CONFLICT where bonds are secured by assessments; 00G EVIDENCE REQUIRED (destination sometimes specified); 00H QUESTION REQUIRED / LEGAL INTERPRETATION REQUIRED (assessment vs tax vs fee); 00J PROVISIONAL ALIGNMENT (label ≠ function). **Never SATISFIED.**

---

## 1. Index of Domain 06 rows

| Master Record ID | Authoritative name (short) | Compulsory | Verification | Disposition |
|---|---|---|---|---|
| KRU-D06-001 | Municipal special assessments (12-6a01 et seq.) | YES **where levied** | TRACED (architecture); LOCAL IMPLEMENTATION VARIABLE | BLANK |
| KRU-D06-002 | County sewer-district special assessments (19-27a) | YES **where a district exists** | TRACED (architecture) | BLANK |
| KRU-D06-003 | Drainage-district special assessments (ch. 24) | YES **where levied** | TRACED (architecture) | BLANK |
| KRU-D06-004 | Watershed-district special assessments (24-1217) | YES **where used** | TRACED (architecture); mill levies referred to D02 | BLANK |
| KRU-D06-005 | Irrigation-district assessments (42-718) | YES **where a district levies** | TRACED (architecture) | BLANK |
| KRU-D06-006 | County water-supply district special assessments (19-3540) | YES **where levied** | TRACED (architecture) | BLANK |
| KRU-D06-007 | CID / TDD special assessments (12-6a28/29; 12-17,143) | YES **where levied** | TRACED (enabling); distinct from D04 sales tax | BLANK |
| KRU-D06-008 | Nuisance / demolition / service-cost tax-roll assessments | YES **where certified** | TRACED (class); LOCAL IMPLEMENTATION VARIABLE | BLANK |
| KRU-D06-009 | BID annual service fees (12-1791) | YES **where a BID exists** | TRACED (enabling); LOCAL IMPLEMENTATION VARIABLE | BLANK |
| KRU-D06-010 | Insurance guaranty-association assessments (40-2906) | YES when assessed | TRACED (architecture); annual levy EVIDENCE REQUIRED | BLANK |
| KRU-D06-011 | Workers-compensation-fund assessments (44-566a) | YES | TRACED | BLANK |
| KRU-D06-012 | KCC utility/carrier assessments (66-1502 / 66-1503) | YES | TRACED (class; two mechanisms) | BLANK |
| KRU-D06-013 | Grain-commodity first-purchaser assessments (2-3007) | YES (refund architecture) | TRACED | BLANK |
| KRU-D06-014 | Municipal stormwater / drainage utility charges | YES **where imposed** | TRACED (class existence); CLASSIFICATION REQUIRED | BLANK |

Counted Domain 06 verified **claim-category** records: **14**.  
Human dispositions: **ALL BLANK**. Post-Bill-A authority: **NOT DETERMINED** on every row.

Arithmetic with Domains 01–05: **58 + 14 = 72**. **72 ≠ retained claims. 72 ≠ future Bill A claims.**

---

## 2. Thirty-two-field records

### KRU-D06-001 — Municipal special assessments (GIAL)

| # | Field | Value |
|---|---|---|
| 1 | MASTER RECORD ID | KRU-D06-001 |
| 2 | EVIDENCE DOMAIN | 06 |
| 3 | AUTHORITATIVE NAME | Municipal special assessments under the General Improvement and Assessment Law (K.S.A. 12-6a01 et seq.) |
| 4 | COMMON / ALTERNATE NAME | Benefit-district assessments; improvement-district specials; street/sewer/sidewalk assessments |
| 5 | GOVERNMENT LEVEL | local (city) |
| 6 | GOVERNMENT ENTITY / ENTITY CLASS | Cities; county treasurer is a **collection mechanism** |
| 7 | RECEIPT OR CLAIM TYPE | Special assessment / special tax on benefited property. Label is not dispositive. |
| 8 | COMPULSORY STATUS | YES where an assessment ordinance/roll is levied |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 12-6a02, 12-6a08, 12-6a10, 12-6a11. Allied older street method 12-602 / 12-608 **not** a second counted row. Distinct from Domain 02 general ad valorem (KRU-D02 class). |
| 10 | PAYMENT / REVENUE TRIGGER | Levy of special assessments for a municipal improvement conferring special benefit on property in a definable area |
| 11 | LEGALLY OBLIGATED PARTY | Owner of assessed lots/parcels. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Lien; collection as other city taxes (12-6a10). Penalties/interest **REFERRED TO DOMAIN 07** if punitive. 30-day limitation on actions (12-6a11). |
| 13 | ECONOMIC FUNCTION | Allocate improvement cost to specially benefited property; not a general mill levy |
| 14 | RATE / CALCULATION / AMOUNT METHOD | Front foot, square foot, value, or other reasonable plan imposing substantially equal burdens on similarly benefited property (12-6a08). **Do not invent project amounts.** LOCAL IMPLEMENTATION VARIABLE. |
| 15 | STATED PURPOSE | Pay all or part of municipal improvement cost |
| 16 | REVENUE DESTINATION | Separate improvement funds / bond-and-interest (12-6a13 / 12-6a16). LOCAL IMPLEMENTATION VARIABLE. |
| 17 | FUND / POOL TYPE | PROJECT-RESTRICTED / DEBT-SERVICE-RELATED (typical); **EVIDENCE REQUIRED** per project |
| 18 | ADMINISTRATIVE / OVERHEAD TREATMENT | City-at-large share may be apportioned (12-6a04/08). Collection ≠ extra claim. |
| 19 | DEBT / BOND / CONTRACT / FEDERAL-MATCH / OTHER DEPENDENCIES | Bonds authorized (12-6a14/15). **DEPENDENCY VERIFIED** as architecture. Impairment **LEGAL EFFECT UNKNOWN**. Dependency ≠ RETAIN. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Statewide isolated total: **EVIDENCE REQUIRED**. Do not use ACFR charges-for-services as Domain 06 total. **CURRENT RECEIPTS ≠ REQUIRED REPLACEMENT REVENUE.** |
| 21 | H.R. 25 KANSAS-MIRROR RELATIONSHIP | Outside H.R. 25 consumption-tax event as a class. Not Kansas law. Future treatment NOT DETERMINED. |
| 22 | AGCL 00A–00J CLASSIFICATION | Default Domain 06 AGCL (header). 00E EVIDENCE REQUIRED (bonds). **Never SATISFIED.** |
| 23 | CURRENT-STATE STATUS | Evidenced current enabling architecture. **Not** future authorization. One city/project ≠ one row. |
| 24 | KLRS CANDIDACY | CANDIDATE COMPULSORY CLAIM. Not final authorization. |
| 25 | HUMAN BILL A DISPOSITION | **BLANK** |
| 26 | POST-BILL-A AUTHORITY STATUS | **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-278, 279, 280, 281 |
| 28 | GOV-DATA LOCATORS | SRC-BILL-A-297 (do not treat as Domain 06 total) |
| 29 | SOURCE DATE / VERSION | 12-6a retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED (architecture). Exhaustive project inventory **not** performed. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D06-001; CF-D06-002; UNK-D06-001 |
| 32 | NOTES / TRACEABILITY | Collection on the property-tax roll does **not** make this Domain 02. |

### KRU-D06-002 — County sewer-district special assessments

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D06-002 / 06 |
| 3 | AUTHORITATIVE NAME | County sewer-district special assessments (K.S.A. 19-27a01 et seq., especially 19-27a07) |
| 4 | COMMON / ALTERNATE NAME | Sewer-district assessments |
| 5–6 | LEVEL / ENTITY | local / board of county commissioners as sewer-district governing body |
| 7–8 | TYPE / COMPULSORY | Special assessment / lien / YES where levied |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 19-27a02; 19-27a07 |
| 10 | PAYMENT / REVENUE TRIGGER | Assessment resolution after completed sewer improvements; roll, notice, hearing |
| 11 | LEGALLY OBLIGATED PARTY | Landowners made liable on the assessment roll |
| 12 | CONSEQUENCE OF NONPAYMENT | Lien from effective date of resolution; collection as other taxes; 30-day challenge window |
| 13 | ECONOMIC FUNCTION | Allocate sewer-improvement cost to property in the district |
| 14 | RATE / CALCULATION | Method in the assessment resolution. **Do not invent amounts.** |
| 15–17 | PURPOSE / DESTINATION / FUND | Cost of sewer improvements; PROJECT / DEBT-SERVICE typical; **EVIDENCE REQUIRED** per district |
| 19 | DEPENDENCIES | Bonds authorized in 19-27a07 architecture. **POTENTIAL DEPENDENCY**. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Statewide isolated total: **EVIDENCE REQUIRED** |
| 21–26 | H.R. 25 / AGCL / CURRENT / KLRS / DISPOSITION / POST-BILL-A | Default / **Never SATISFIED** / evidenced architecture / CANDIDATE COMPULSORY CLAIM / **BLANK** / **NOT DETERMINED** |
| 27–28 | LOCATORS | SRC-BILL-A-282 / SRC-BILL-A-297 |
| 30 | VERIFICATION STATUS | TRACED (architecture) |
| 31 | CONFLICT / UNKNOWN IDS | UNK-D06-001 |
| 32 | NOTES | One sewer district ≠ one row. |

### KRU-D06-003 — Drainage-district special assessments

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D06-003 / 06 |
| 3 | AUTHORITATIVE NAME | Drainage-district special assessments (K.S.A. 24-422 / 24-424 class) |
| 4 | COMMON / ALTERNATE NAME | Levee / drainage assessments |
| 5–6 | LEVEL / ENTITY | local special district / drainage-district board |
| 7–8 | TYPE / COMPULSORY | Special assessment on benefited lands / YES where levied |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 24-422; 24-424. Other ch. 24 organic acts may be allied; **EVIDENCE REQUIRED** before splitting rows. |
| 10 | PAYMENT / REVENUE TRIGGER | Confirmed assessors’ report charging lands protected/benefited |
| 11 | LEGALLY OBLIGATED PARTY | Owners of described tracts |
| 12 | CONSEQUENCE OF NONPAYMENT | Lien; collected as other taxes; 30-day limitation |
| 13 | ECONOMIC FUNCTION | Charge lands according to overflow-protection / drainage benefit |
| 14 | RATE / CALCULATION | Proportion of estimated cost by benefit on actual view (24-422) |
| 19 | DEPENDENCIES | **POTENTIAL DEPENDENCY** if bonds issued. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | **EVIDENCE REQUIRED** |
| 21–26 | defaults | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL | SRC-BILL-A-283 |
| 30 | VERIFICATION STATUS | TRACED (architecture) |
| 31 | CONFLICT / UNKNOWN IDS | UNK-D06-002 |
| 32 | NOTES | Entity ≠ claim. Count architecture, not each district. |

### KRU-D06-004 — Watershed-district special assessments

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D06-004 / 06 |
| 3 | AUTHORITATIVE NAME | Watershed-district special assessments against especially benefited lands (K.S.A. 24-1217) |
| 4 | COMMON / ALTERNATE NAME | Watershed assessments |
| 5–6 | LEVEL / ENTITY | local special district / watershed-district board |
| 7–8 | TYPE / COMPULSORY | Special assessment / YES where the financing resolution uses special assessment |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 24-1209 (ninth); 24-1217. **General mill levies** of the district **REFERRED TO DOMAIN 02** — not this row. |
| 10 | PAYMENT / REVENUE TRIGGER | Board resolution adopting appraiser-recommended apportionment after hearing |
| 11 | LEGALLY OBLIGATED PARTY | Owners of listed tracts especially benefited |
| 13 | ECONOMIC FUNCTION | Project cost on especially benefited lands; assessment shall not exceed estimated benefits |
| 19 | DEPENDENCIES | Bonds authorized in 24-1209. **POTENTIAL DEPENDENCY**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | **EVIDENCE REQUIRED** |
| 21–26 | defaults | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL | SRC-BILL-A-284, 285 |
| 30 | VERIFICATION STATUS | TRACED (architecture) |
| 31 | CONFLICT / UNKNOWN IDS | CF-D06-003 |
| 32 | NOTES | Do not collapse mill levy into this special-assessment row. |

### KRU-D06-005 — Irrigation-district assessments

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D06-005 / 06 |
| 3 | AUTHORITATIVE NAME | Irrigation-district assessments against district lands (K.S.A. 42-718) |
| 4 | COMMON / ALTERNATE NAME | Irrigation assessments |
| 5–8 | LEVEL / TYPE / COMPULSORY | local irrigation district / assessment certified to tax list / YES where levied |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 42-718; creation 42-357 (historical organic). Water rentals/tolls **REFERRED TO DOMAIN 08**. |
| 10 | PAYMENT / REVENUE TRIGGER | Annual board levy for interest, O&M, salaries, general fund |
| 13 | ECONOMIC FUNCTION | Charge irrigation-district lands for district obligations and operations |
| 16–17 | DESTINATION / FUND | Separate funds per purpose (including “general fund”) (42-718) |
| 19 | DEPENDENCIES | Outstanding indebtedness considered in the levy. **POTENTIAL DEPENDENCY**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | **EVIDENCE REQUIRED**. Existence of active Kansas irrigation districts: **EVIDENCE REQUIRED** for current use (UNK-D06-003). Enabling architecture TRACED. |
| 21–26 | defaults | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL | SRC-BILL-A-286 |
| 30 | VERIFICATION STATUS | TRACED (architecture); current-use **PARTIAL** |
| 31 | CONFLICT / UNKNOWN IDS | UNK-D06-003 |

### KRU-D06-006 — County water-supply district special assessments

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D06-006 / 06 |
| 3 | AUTHORITATIVE NAME | County water-supply / distribution-district cost assessments (K.S.A. 19-3540) |
| 4 | COMMON / ALTERNATE NAME | Water-district special assessments |
| 5–8 | LEVEL / TYPE / COMPULSORY | county district / special assessment or tax on lots exclusive of improvements / YES where levied |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 19-3540. Distinct from rural water districts (82a-619 — **no tax-levy power** → Domain 08). |
| 10 | PAYMENT / REVENUE TRIGGER | Board order placing costs on the tax roll; optional installment/bonds |
| 13 | ECONOMIC FUNCTION | Allocate water-system work cost to lots in the district |
| 14 | RATE / CALCULATION | One tax, area basis if equally benefited, or other reasonable plan |
| 19 | DEPENDENCIES | Improvement bonds authorized. **POTENTIAL DEPENDENCY**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | **EVIDENCE REQUIRED** |
| 21–26 | defaults | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL | SRC-BILL-A-287, 288 |
| 30 | VERIFICATION STATUS | TRACED (architecture) |
| 31 | CONFLICT / UNKNOWN IDS | CF-D06-004 |

### KRU-D06-007 — CID / TDD special assessments

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D06-007 / 06 |
| 3 | AUTHORITATIVE NAME | Community-improvement-district and transportation-development-district **special assessments** (K.S.A. 12-6a28 / 12-6a29; 12-17,143) |
| 4 | COMMON / ALTERNATE NAME | CID assessments; TDD assessments |
| 5–8 | LEVEL / TYPE / COMPULSORY | municipality / special assessments on district property / YES where levied |
| 9 | CURRENT LEGAL AUTHORITY | 12-6a28/29 (assessment method, if any, in CID petition); 12-17,143 (TDD follows 12-6a01 procedures with exceptions). **Distinct from** KRU-D04-005 CID/TDD **sales tax**. |
| 10 | PAYMENT / REVENUE TRIGGER | Ordinance/resolution levying CID/TDD assessments |
| 13 | ECONOMIC FUNCTION | Finance a CID/TDD project from property in the district rather than (or in addition to) a sales-tax overlay |
| 19 | DEPENDENCIES | Project bonds common. TDD 12-17,143 restricts full-faith-and-credit notes in listed cases. **POTENTIAL DEPENDENCY**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Isolated assessment-only statewide dollars: **EVIDENCE REQUIRED**. Do not add to KRU-D04-005. |
| 21–26 | defaults | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL | SRC-BILL-A-289, 290 |
| 30 | VERIFICATION STATUS | TRACED (enabling architecture); per-district inventory not performed |
| 31 | CONFLICT / UNKNOWN IDS | CF-D06-005 |
| 32 | NOTES | STAR increment pledge remains Domain 04, not this row. |

### KRU-D06-008 — Nuisance / demolition / service-cost assessments

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D06-008 / 06 |
| 3 | AUTHORITATIVE NAME | Tax-roll special assessments for nuisance abatement, weed/vegetation, demolition/raze, and city service-cost recovery (K.S.A. 12-1617e; 12-1755; 12-6a17) |
| 4 | COMMON / ALTERNATE NAME | Weed assessments; demolition assessments; dangerous-structure assessments; service assessments |
| 5–8 | LEVEL / TYPE / COMPULSORY | city (and analogous county procedures where evidenced) / cost recovery via special assessment / YES when certified unpaid |
| 9 | CURRENT LEGAL AUTHORITY | 12-1617e; 12-1755; 12-6a17. Distinct from GIAL improvement-benefit assessments (KRU-D06-001). |
| 10 | PAYMENT / REVENUE TRIGGER | Unpaid abatement/demolition/service costs after notice; certification to county clerk |
| 13 | ECONOMIC FUNCTION | Recover police-power / duty-to-perform costs from the subject parcel |
| 14 | RATE / CALCULATION | Actual cost plus authorized notice costs. LOCAL IMPLEMENTATION VARIABLE. |
| 16–17 | DESTINATION / FUND | Reimburse the city fund that paid the work (12-6a17(b) reimbursable credit) |
| 19 | DEPENDENCIES | Generally none as bond architecture; 12-6a17 no-fund warrants possible. **EVIDENCE REQUIRED**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Statewide total **EVIDENCE REQUIRED**. Representative local ordinance: SRC-BILL-A-298 (not statewide). |
| 21–26 | defaults | **BLANK** / **NOT DETERMINED** |
| 27–28 | LOCATORS | SRC-BILL-A-291, 292 / SRC-BILL-A-298 |
| 30 | VERIFICATION STATUS | TRACED (class) |
| 31 | CONFLICT / UNKNOWN IDS | CF-D06-006 |
| 32 | NOTES | Event-triggered. One parcel ≠ one row. |

### KRU-D06-009 — BID annual service fees

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D06-009 / 06 |
| 3 | AUTHORITATIVE NAME | Business-improvement-district annual service fees (K.S.A. 12-1791) |
| 4 | COMMON / ALTERNATE NAME | BID fees; downtown assessment |
| 5–8 | LEVEL / TYPE / COMPULSORY | city BID / annual district levy on businesses / YES where a BID ordinance levies |
| 9 | CURRENT LEGAL AUTHORITY | 12-1788 (creation); 12-1791 (levy). Expressly in addition to occupation licenses (Domain 05 KRU-D05-005). |
| 10 | PAYMENT / REVENUE TRIGGER | Annual ordinance after advisory-board recommended program/budget |
| 11 | LEGALLY OBLIGATED PARTY | Businesses located in the district |
| 13 | ECONOMIC FUNCTION | Fund specified district services; geographic/business-district assessment. Label “fee” not dispositive. |
| 14 | RATE / CALCULATION | Space, front footage, square footage, employees, type of business, or combination deemed reasonable |
| 16–17 | DESTINATION / FUND | Special fund (12-1792) — PROGRAM-RESTRICTED |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED** |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | **EVIDENCE REQUIRED**. LOCAL IMPLEMENTATION VARIABLE. |
| 21–26 | defaults | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL | SRC-BILL-A-293 |
| 30 | VERIFICATION STATUS | TRACED (enabling) |
| 31 | CONFLICT / UNKNOWN IDS | CF-D06-007 |

### KRU-D06-010 — Insurance guaranty-association assessments

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D06-010 / 06 |
| 3 | AUTHORITATIVE NAME | Kansas Insurance Guaranty Association member assessments (K.S.A. 40-2906(1)(3) class) |
| 4 | COMMON / ALTERNATE NAME | KIGA assessments; insolvency assessments |
| 5–8 | LEVEL / TYPE / COMPULSORY | state statutory association / premium-proportion assessment / YES when an assessment is made |
| 9 | CURRENT LEGAL AUTHORITY | 40-2906. Distinct from 40-252 premium **tax** and KRU-D05-016 **fees**. Life/health guaranty allied, not a second counted row. |
| 10 | PAYMENT / REVENUE TRIGGER | Post-insolvency (and authorized expenses) assessment of member insurers |
| 11 | LEGALLY OBLIGATED PARTY | Member insurers |
| 13 | ECONOMIC FUNCTION | Industry assessment to pay covered claims of insolvent insurers |
| 14 | RATE / CALCULATION | Premium proportion; cap **2%** of preceding-year net direct written premiums |
| 16–17 | DESTINATION / FUND | Association obligations — PROGRAM-RESTRICTED |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED** |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Whether a levy occurred in a given year: **EVIDENCE REQUIRED** (UNK-D06-004) |
| 21–26 | defaults | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL | SRC-BILL-A-294 |
| 30 | VERIFICATION STATUS | TRACED (architecture); current-year levy PARTIAL |
| 31 | CONFLICT / UNKNOWN IDS | UNK-D06-004; CF-D06-008 |

### KRU-D06-011 — Workers-compensation-fund assessments

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D06-011 / 06 |
| 3 | AUTHORITATIVE NAME | Workers compensation fund annual assessments (K.S.A. 44-566a) |
| 4 | COMMON / ALTERNATE NAME | WC fund assessments |
| 5–8 | LEVEL / TYPE / COMPULSORY | state / annual assessment by commissioner of insurance / YES |
| 9 | CURRENT LEGAL AUTHORITY | 44-566a(b) |
| 10 | PAYMENT / REVENUE TRIGGER | June 1 imposition; due July 1 |
| 11 | LEGALLY OBLIGATED PARTY | Insurance carriers, self-insurers, group-funded WC pools insuring compensation under the act |
| 13 | ECONOMIC FUNCTION | Fund statutory workers-compensation-fund liabilities |
| 14 | RATE / CALCULATION | Amount sufficient for the fiscal year less unencumbered balance; apportioned by claims paid/payable; experience-based rates authorized |
| 16–17 | DESTINATION / FUND | Workers compensation fund in the state treasury — PROGRAM-RESTRICTED |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED** |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Isolated FY total: **EVIDENCE REQUIRED** |
| 21–26 | defaults | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL | SRC-BILL-A-295 |
| 30 | VERIFICATION STATUS | TRACED |

### KRU-D06-012 — KCC assessments

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D06-012 / 06 |
| 3 | AUTHORITATIVE NAME | State Corporation Commission assessments against public utilities and common carriers (K.S.A. 66-1502 investigation/appraisal; 66-1503 quarterly operating) |
| 4 | COMMON / ALTERNATE NAME | KCC assessments; utility assessments |
| 5–8 | LEVEL / TYPE / COMPULSORY | state / regulatory assessments / YES |
| 9 | CURRENT LEGAL AUTHORITY | 66-1502; 66-1503. Distinct from Domain 05 licenses and from Domain 03 privilege tax. |
| 10 | PAYMENT / REVENUE TRIGGER | Bill after investigation/appraisal; quarterly ascertainment of commission/CURB expenditures |
| 11 | LEGALLY OBLIGATED PARTY | Jurisdictional public utilities and common carriers |
| 13 | ECONOMIC FUNCTION | Recover KCC/CURB regulatory costs from the regulated industry |
| 14 | RATE / CALCULATION | 66-1502 FY cap **0.6%** of intrastate gross operating revenues (exceptions). 66-1503 cap greater of **$100** or **0.2%**. Motor-carrier and oil-conservation fees excluded from 66-1503 base. |
| 16–17 | DESTINATION / FUND | State treasurer credit to KCC / CURB appropriations — REGULATORY |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED** |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | **EVIDENCE REQUIRED** |
| 21–26 | defaults | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL | SRC-BILL-A-296 |
| 30 | VERIFICATION STATUS | TRACED (class; two mechanisms, one row) |

### KRU-D06-013 — Grain-commodity first-purchaser assessments

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D06-013 / 06 |
| 3 | AUTHORITATIVE NAME | Grain sorghum, corn, soybean, wheat, and sunflower first-purchaser assessments (K.S.A. 2-3007) |
| 4 | COMMON / ALTERNATE NAME | Checkoffs; commodity assessments |
| 5–8 | LEVEL / TYPE / COMPULSORY | state / per-unit assessment at commercial marketing / YES (statutory refund procedure) |
| 9 | CURRENT LEGAL AUTHORITY | 2-3007. **Not** Domain 01 gallonage excise. |
| 10 | PAYMENT / REVENUE TRIGGER | First purchase of the commodity from the grower after harvest |
| 11 | LEGALLY OBLIGATED PARTY | Grower (collected by first purchaser). First purchaser is a **collection mechanism**. |
| 13 | ECONOMIC FUNCTION | Industry promotional/research assessment on marketed grain |
| 14 | RATE / CALCULATION | Statutory maxima (examples: sorghum/corn **not more than 10 mills/bushel**; soybeans **not more than 1/2 of 1%** of net market price; wheat **not more than 20 mills/bushel**; sunflowers **not more than $0.06/cwt**). Commission sets rate within cap. |
| 16–17 | DESTINATION / FUND | Commodity commissions via Kansas Department of Agriculture remittance — PROGRAM-RESTRICTED |
| 19 | DEPENDENCIES | None evidenced as bond architecture |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Isolated statewide dollars: **EVIDENCE REQUIRED**. KDA first-purchaser guidance: SRC-BILL-A-299. |
| 21–26 | defaults | **BLANK** / **NOT DETERMINED** |
| 27–28 | LOCATORS | SRC-BILL-A-300 / SRC-BILL-A-299 |
| 30 | VERIFICATION STATUS | TRACED |
| 31 | CONFLICT / UNKNOWN IDS | CF-D06-009 |
| 32 | NOTES | Refund ≥$5 does **not** make the levy non-compulsory at the point of sale. One commodity ≠ extra row. |

### KRU-D06-014 — Municipal stormwater / drainage utility charges

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D06-014 / 06 |
| 3 | AUTHORITATIVE NAME | Municipal stormwater / drainage utility charges (home-rule / ordinance class) |
| 4 | COMMON / ALTERNATE NAME | Stormwater utility fee; drainage fee; TUF-type charges (label not controlling) |
| 5–8 | LEVEL / TYPE / COMPULSORY | city / periodic charge on developed or benefiting property / YES where imposed |
| 9 | CURRENT LEGAL AUTHORITY | Local ordinance + Art. 12 § 5 home rule. **CLASSIFICATION REQUIRED** (fee vs tax vs special assessment). *Heartland* Mission **TUF** held a prohibited **excise tax** (12-194) — **not** counted as a current lawful claim. Kan. Att'y Gen. Op. discussing Topeka stormwater is **not** a judicial holding. |
| 10 | PAYMENT / REVENUE TRIGGER | LOCAL IMPLEMENTATION VARIABLE (typically periodic utility billing and/or tax-roll certification) |
| 13 | ECONOMIC FUNCTION | **CLASSIFICATION REQUIRED** — may resemble user charge, special assessment, or general tax depending on ordinance |
| 14 | RATE / CALCULATION | LOCAL IMPLEMENTATION VARIABLE. Do not invent formulas. |
| 16–17 | DESTINATION / FUND | LOCAL IMPLEMENTATION VARIABLE |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED** |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Statewide total **EVIDENCE REQUIRED**. Do not treat as Domain 06 total. |
| 21–26 | defaults | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL | SRC-BILL-A-253, 254 (doctrine); SRC-BILL-A-252 (home rule); SRC-BILL-A-259 analog |
| 30 | VERIFICATION STATUS | TRACED (class existence / doctrine); classification **CONFLICT** |
| 31 | CONFLICT / UNKNOWN IDS | CF-D06-010; UNK-D06-005 |
| 32 | NOTES | Do not inventory every city ordinance. Do not treat *Heartland* as invalidating every stormwater charge without ordinance-specific analysis. |

---

Libertas sine lapsu — Liberty without drift.
