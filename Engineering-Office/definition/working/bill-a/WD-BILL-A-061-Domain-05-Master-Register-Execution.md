# WD-BILL-A-061 — Domain 05 Master Register Execution Instance

**Document ID:** WD-BILL-A-061  
**Title:** Kansas Government Revenue Universe / KLRS Master Register — Domain 05 Execution Instance  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-141  
**Canonical starting SHA:** `f7c4c80d390cc4b5cdeb6cf9e088d2ed2e775b6c`  
**Schema authority:** WD-BILL-A-019 (this file does **not** replace the schema lock; 32 fields unchanged)  
**Governing LOU candidate:** LOU-004 Draft 1.7 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / DOMAIN 05 ROWS POPULATED FROM EVIDENCE — REGISTER **NOT** STATEWIDE COMPLETE — NOT ACCEPTED  
**Version:** 1.0.0  
**Effective Date:** 2026-09-02  
**Retrieval date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-061-Domain-05-Master-Register-Execution.md  

```text
EXECUTION INSTANCE OF WD-BILL-A-019 SCHEMA
DOMAIN 05 ONLY
HUMAN DISPOSITION = BLANK ON EVERY ROW
BLANK ≠ RETAIN
CURRENT EXISTENCE ≠ POST-BILL-A AUTHORITY
CURRENT RECEIPTS ≠ REQUIRED REPLACEMENT REVENUE
FEE ≠ AUTOMATICALLY COST RECOVERY
GOVERNMENT LABEL ≠ CLASSIFICATION
ONE PROFESSION / FORM / MUNICIPALITY ≠ ONE CLAIM
COLLECTION MECHANISM ≠ ANOTHER CLAIM
KLRS CANDIDACY ≠ FINAL AUTHORIZATION
STATEWIDE UNIVERSE NOT CERTIFIED
NO FAIRTAX RATE CALCULATION
NO FUTURE DISTRIBUTION DESIGN
```

Narrative audit: WD-BILL-A-060. Sources: WD-BILL-A-062. Completeness: WD-BILL-A-063. Conflicts: WD-BILL-A-064. Classification / referral: WD-BILL-A-065.

Domain 01 rows remain in WD-BILL-A-022. Domain 02: WD-BILL-A-031. Domain 03: WD-BILL-A-040. Domain 04: WD-BILL-A-049. They are **not** rewritten here.

Common field values unless a row overrides:

- Field 2 EVIDENCE DOMAIN = 05
- Field 25 HUMAN BILL A DISPOSITION = **BLANK**
- Field 26 POST-BILL-A AUTHORITY STATUS = **NOT DETERMINED**
- Retrieval date = 2026-09-02
- Field 21 default: **OUTSIDE H.R. 25 CONSUMPTION-TAX EVENT AS A CLASS** (authorization/filing charge, not retail consumption of new goods). H.R. 25 is **not Kansas law**. Future treatment **NOT DETERMINED**.
- Field 22 default: 00A QUESTION REQUIRED (renewal/expiration exists for many rows but is not self-certified); 00B EVIDENCE REQUIRED / QUESTION REQUIRED (signal-before-claim varies); 00C POTENTIAL CONFLICT surface (privilege/authorization as a claim event vs Q-001/002 existence-not-event intent) **and** PROVISIONAL ALIGNMENT surface where the person can avoid the claim by not entering the activity; 00D QUESTION REQUIRED (exit often = stop the activity); 00E EVIDENCE REQUIRED where SHF/heritage/bond overlays exist; 00G EVIDENCE REQUIRED (destination sometimes specified); 00H QUESTION REQUIRED / LEGAL INTERPRETATION REQUIRED (fee-vs-tax; home rule); 00J PROVISIONAL ALIGNMENT (label ≠ function). **Never SATISFIED.**

---

## 1. Index of Domain 05 rows

| Master Record ID | Authoritative name (short) | Compulsory | Verification | Disposition |
|---|---|---|---|---|
| KRU-D05-001 | Motor-vehicle registration / license fees (8-143 / 8-145) | YES | TRACED (architecture) | BLANK |
| KRU-D05-002 | Motor-vehicle certificate of title fees (8-135) | YES | TRACED (architecture) | BLANK |
| KRU-D05-003 | Driver's license / CDL / examination fees (8-240 / 8-267) | YES | TRACED (architecture) | BLANK |
| KRU-D05-004 | Professional / occupational licensing (fee-agency class) | YES | TRACED (architecture); one profession ≠ one row | BLANK |
| KRU-D05-005 | Local occupation / business licenses | YES **where imposed** | TRACED (home-rule architecture); LOCAL IMPLEMENTATION VARIABLE | BLANK |
| KRU-D05-006 | SOS entity filing / biennial information-report fees (17-7503 / 17-7506) | YES | TRACED (architecture) | BLANK |
| KRU-D05-007 | Local building / development / inspection permits | YES **where imposed** | TRACED (class); LOCAL IMPLEMENTATION VARIABLE | BLANK |
| KRU-D05-008 | Environmental / health regulatory permits (KDHE class) | YES | TRACED (class architecture); fee schedules PARTIAL | BLANK |
| KRU-D05-009 | Food establishment / food-processing licenses (65-688 / 65-689) | YES | TRACED | BLANK |
| KRU-D05-010 | Alcoholic-liquor licensing (41-310) | YES | TRACED (architecture) | BLANK |
| KRU-D05-011 | Kansas 911 fees (12-5369 monthly; 12-5371 prepaid) | YES | TRACED (architecture); fee-vs-tax LEGAL INTERPRETATION REQUIRED | BLANK |
| KRU-D05-012 | Municipal franchise / telecom access-line or gross-receipts fees (12-2001) | YES **where granted/imposed** | TRACED (enabling); LOCAL IMPLEMENTATION VARIABLE | BLANK |
| KRU-D05-013 | District-court docket / filing fees (60-2001 / 20-362) | YES (poverty-affidavit exception) | TRACED; $22 overlay currentness UNK-D05-007 | BLANK |
| KRU-D05-014 | Register-of-deeds recording fees (28-115) | YES | TRACED | BLANK |
| KRU-D05-015 | Hunting / fishing / wildlife licenses (32-988) | YES as condition of legal take | TRACED (maxima); MIXED classification | BLANK |
| KRU-D05-016 | Insurance licensing / certificate-of-authority **fees** (40-252 fee schedule) | YES | TRACED (fees only); premium **tax** referred | BLANK |
| KRU-D05-017 | Oversize / overweight special permits (8-1911) | YES | TRACED | BLANK |
| KRU-D05-018 | Financial-institution regulatory / examination fees (class; 9-1703 / 75-3170a) | YES | TRACED (architecture); amounts EVIDENCE REQUIRED | BLANK |

Counted Domain 05 verified **claim-category** records: **18**.  
Count follows evidence. Human dispositions: **ALL BLANK**. Post-Bill-A authority: **NOT DETERMINED** on every row.

Arithmetic with Domains 01–04: **40 + 18 = 58** verified claim-category records. **58 ≠ 58 retained claims. 58 ≠ 58 future Bill A claims.**

---

## 2. Thirty-two-field records

### KRU-D05-001 — Motor-vehicle registration / license fees

| # | Field | Value |
|---|---|---|
| 1 | MASTER RECORD ID | KRU-D05-001 |
| 2 | EVIDENCE DOMAIN | 05 |
| 3 | AUTHORITATIVE NAME | Annual vehicle registration / license fees as set in K.S.A. 8-143; collection and remittance K.S.A. 8-145 |
| 4 | COMMON / ALTERNATE NAME | Tag fees; license plate fees; vehicle registration |
| 5 | GOVERNMENT LEVEL | state (county treasurer is a collection mechanism) |
| 6 | GOVERNMENT ENTITY / ENTITY CLASS | State of Kansas; Division of Vehicles; county treasurers; State Treasurer / state highway fund and listed special funds |
| 7 | RECEIPT OR CLAIM TYPE | Motor-vehicle registration / license charge. Label “fee” is not dispositive. |
| 8 | COMPULSORY STATUS | YES — compulsory condition of legal operation of a registrable vehicle |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 8-143; 8-145. Distinct from 79-3408 motor-fuel (Domain 01), 79-5105 motor-vehicle property tax (Domain 02 KRU-D02-012), and Domain 04 vehicle sales/use. |
| 10 | PAYMENT / REVENUE TRIGGER | Annual registration (and stated class exceptions) of a motor vehicle |
| 11 | LEGALLY OBLIGATED PARTY | Registrant / owner. County treasurer collection ≠ second claim. Economic incidence **NOT ESTABLISHED**. Ultimate source (Human intent, crosswalk only): people with money. |
| 12 | CONSEQUENCE OF NONPAYMENT | Unlawful operation without registration (chapter 8 architecture). Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory authorization to operate a registered vehicle on public highways; proceeds materially support highway/transportation funds, not merely a DMV counter cost. |
| 14 | RATE / CALCULATION / AMOUNT METHOD | Statutory class schedule (examples: passenger ≤4,500 lb **$30**; >4,500 lb **$40**; all-electric passenger **$165**; trucks by declared GW up to **$2,070**). Do not invent unlisted classes. |
| 15 | STATED PURPOSE | Vehicle registration / license; electric/hybrid remittances tied to 79-34,142 distribution architecture |
| 16 | REVENUE DESTINATION | State highway fund and listed special funds in 8-145 (including VIPS/CAMA, KHP staffing/training, commercial-vehicle admin; EV/hybrid via 79-34,142 percentages to SHF and special city and county highway fund). County treasurer retains an administrative portion. |
| 17 | FUND / POOL TYPE | Dedicated transportation / special funds + county administrative retainage |
| 18 | ADMINISTRATIVE / OVERHEAD TREATMENT | County treasurer retainage is a **mechanism**, not a second claim. |
| 19 | DEBT / BOND / CONTRACT / FEDERAL-MATCH / OTHER DEPENDENCIES | SHF destination: **DEPENDENCY VERIFIED** (destination). Impairment if disappeared: **LEGAL EFFECT UNKNOWN**. Dependency ≠ RETAIN. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Kansas ACFR FY2024 Transportation Fund budgetary **Vehicle registrations and permits $246,997 thousand**. Aggregates registration **and** permits credited to that presentation. **Not** Domain 05 total. **CURRENT RECEIPTS ≠ REQUIRED REPLACEMENT REVENUE.** |
| 21 | H.R. 25 KANSAS-MIRROR RELATIONSHIP | Outside H.R. 25 consumption-tax event as a class. Not Kansas law. Future treatment NOT DETERMINED. |
| 22 | AGCL 00A–00J CLASSIFICATION | Default Domain 05 AGCL (header). 00E EVIDENCE REQUIRED (SHF). **Never SATISFIED.** |
| 23 | CURRENT-STATE STATUS | Evidenced current registration architecture. **Not** future authorization. |
| 24 | KLRS CANDIDACY | CANDIDATE COMPULSORY CLAIM. Not final authorization. |
| 25 | HUMAN BILL A DISPOSITION | **BLANK** |
| 26 | POST-BILL-A AUTHORITY STATUS | **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-233, 234 |
| 28 | GOV-DATA LOCATORS | SRC-BILL-A-260 |
| 29 | SOURCE DATE / VERSION | 8-143 / 8-145 2025 K.S.A. HTML/PDF retrieved 2026-09-02; ACFR FY2024 |
| 30 | VERIFICATION STATUS | TRACED (architecture). Every vehicle class not enumerated as a separate row. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-001; CF-D05-003; UNK-D05-001 |
| 32 | NOTES / TRACEABILITY | Do not collapse with Domain 01/02/04 vehicle claims. EV registration remittance using fuel-tax percentages is **MIXED**, not a second Domain 01 tax. Dealer licensing is related, not this row. |

### KRU-D05-002 — Motor-vehicle certificate of title fees

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-002 / 05 |
| 3 | AUTHORITATIVE NAME | Certificate of title fees (K.S.A. 8-135(c)(4)) |
| 4 | COMMON / ALTERNATE NAME | Title fee; vehicle title |
| 5–6 | LEVEL / ENTITY | State / Division of Vehicles; county treasurer collection mechanism |
| 7–8 | TYPE / COMPULSORY | Title / ownership-document charge / YES as condition of titled ownership transfer/original issue |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 8-135. Distinct from KRU-D05-001 registration and from Domain 04 sales/use on the vehicle. |
| 10 | PAYMENT / REVENUE TRIGGER | Original title; assignment / new title; listed ancillary title services |
| 11 | LEGALLY OBLIGATED PARTY | Applicant for title / transferee as specified in 8-135. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Unlawful operation / fraudulent-and-void sale architecture in 8-135. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory payment for governmental evidence of vehicle ownership / transfer. |
| 14 | RATE / CALCULATION | Original title **$10** in addition to registration; additional **$10** on assignment/new title; other listed $1.50 / $2.50 / $3 / $6.50 amounts are **mechanisms of the same title architecture**, not extra counted claims. |
| 15 | STATED PURPOSE | Certificate of title issuance |
| 16–17 | DESTINATION / FUND | Remitted with registration-fee architecture (8-145). **EVIDENCE REQUIRED** for isolated title-only dollars. |
| 18 | ADMINISTRATIVE | County treasurer / division collection. Collection ≠ extra claim. |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED**. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Isolated title-fee statewide total: **EVIDENCE REQUIRED**. Do not double-count ACFR vehicle registrations and permits line. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. Not Kansas law. |
| 22 | AGCL | Default Domain 05. **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Evidenced current title-fee architecture / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27–28 | LOCATORS | SRC-BILL-A-235 / SRC-BILL-A-260 (do not double-count) |
| 29 | SOURCE DATE / VERSION | 8-135 retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED (architecture) |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-001 |
| 32 | NOTES | Recurrence: EVENT-TRIGGERED. Title good for life of vehicle while held by original holder (8-135). |

### KRU-D05-003 — Driver's license / CDL / examination fees

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-003 / 05 |
| 3 | AUTHORITATIVE NAME | Driver's license, instruction permit, CDL, endorsement, and examination fees (K.S.A. 8-240(f); disposition 8-267) |
| 4 | COMMON / ALTERNATE NAME | DL fees; CDL fees |
| 5–6 | LEVEL / ENTITY | State / Division of Vehicles |
| 7–8 | TYPE / COMPULSORY | Driver authorization charge / YES as condition of legal driving (where a license is required) |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 8-240; 8-267 |
| 10 | PAYMENT / REVENUE TRIGGER | Application, examination, issuance, or renewal of a classified license / CDL / endorsement |
| 11 | LEGALLY OBLIGATED PARTY | Applicant / licensee. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | No license issued / driving without a license (chapter 8). Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory payment for legal authority to drive. CDL is the **same architecture**, not a second counted claim. |
| 14 | RATE / CALCULATION | Examples: class C age 21–64 **$18**; CDL **$18**; endorsements **$10** except air brake; exam **$3**; CDL drive test **$15**. Do not inventory every class as a row. |
| 15 | STATED PURPOSE | License issuance; 8-267 splits include safety, motorcycle safety, truck driver training, photo fee, hazmat, division operating, correctional services special revenue |
| 16–17 | DESTINATION / FUND | Per 8-267; **balance to state highway fund** |
| 18 | ADMINISTRATIVE | Photo fee / operating fund allocations are **mechanisms of this claim**, not extra rows. |
| 19 | DEPENDENCIES | SHF remainder **DEPENDENCY VERIFIED** (destination). Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Isolated DL/CDL statewide total: **EVIDENCE REQUIRED**. Do not double-count KRU-D05-001 ACFR line. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. |
| 22 | AGCL | Default Domain 05. **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Evidenced / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-236, 237 |
| 28 | GOV-DATA LOCATORS | EVIDENCE REQUIRED for isolated dollars |
| 29 | SOURCE DATE / VERSION | 8-240 / 8-267 retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED (architecture). License-term length not separately audited. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-003 |
| 32 | NOTES | Recurrence: PERIODIC. Cost-recovery class: **MIXED**. |

### KRU-D05-004 — Professional / occupational licensing (class)

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-004 / 05 |
| 3 | AUTHORITATIVE NAME | Professional and occupational licensing fees remitted to listed agency fee funds, with 10% credit to the state general fund (K.S.A. 75-3170a) |
| 4 | COMMON / ALTERNATE NAME | Board fees; occupational licenses; professional licenses |
| 5–6 | LEVEL / ENTITY | State / listed licensing boards and agencies |
| 7–8 | TYPE / COMPULSORY | Regulatory license / examination / renewal charge / YES as condition of legal practice of the licensed occupation |
| 9 | CURRENT LEGAL AUTHORITY | 75-3170a plus board-specific fee statutes listed therein (representative: 65-2855 healing arts; 74-1108 nursing; 74-1609 pharmacy; 58-3074 real estate; 1-204 accountancy; 74-7009 technical professions). One profession ≠ one row. |
| 10 | PAYMENT / REVENUE TRIGGER | Application, examination, license, or renewal required to practice |
| 11 | LEGALLY OBLIGATED PARTY | Applicant / licensee. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Practice without a license (board-specific). Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory payment for legal authority to practice a regulated profession/occupation. 10% SGF credit is express reimbursement of statewide administrative services — **MIXED**; not automatic cost recovery of the board’s entire charge. |
| 14 | RATE / CALCULATION | Board-specific / KAR. **Not inventoried profession-by-profession.** 75-3170a: 10% of receipts credited to SGF until **$100,000** per listed fee fund per fiscal year; then 100% to the fee fund. |
| 15 | STATED PURPOSE | 75-3170a: reimburse SGF for accounting, auditing, budgeting, legal, payroll, personnel, purchasing, and other state governmental services. Board statutes: regulation of the profession. |
| 16–17 | DESTINATION / FUND | Agency fee funds + **SGF 10% skim** (capped) |
| 18 | ADMINISTRATIVE | 10% SGF credit is an **allocation of this class**, not a second claim. |
| 19 | DEPENDENCIES | SGF reimbursement architecture **DEPENDENCY VERIFIED** as current-state allocation. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Statewide all-boards total: **EVIDENCE REQUIRED**. Do not invent. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. Professional services may separately be Domain 04 enumerated services — **not this row**. |
| 22 | AGCL | 00A QUESTION REQUIRED (renewal terms board-variable); 00G EVIDENCE REQUIRED (fee-fund vs SGF); 00H LEGAL INTERPRETATION REQUIRED (fee vs tax if charge unreasonably exceeds regulatory service — *Executive Aircraft*). **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Evidenced class architecture / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-238, 253 |
| 28 | GOV-DATA LOCATORS | EVIDENCE REQUIRED |
| 29 | SOURCE DATE / VERSION | 75-3170a retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED (class architecture). Exhaustive KAR fee tables **not** performed. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-002; UNK-D05-008 |
| 32 | NOTES | Recurrence: ANNUAL/BIENNIAL **board-variable**. Cost-recovery class: **MIXED**. |

### KRU-D05-005 — Local occupation / business licenses

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-005 / 05 |
| 3 | AUTHORITATIVE NAME | Local occupation tax / business license charges authorized under city home rule (Kan. Const. art. 12, § 5) and local ordinance |
| 4 | COMMON / ALTERNATE NAME | City occupation tax; business license; occupational license |
| 5–6 | LEVEL / ENTITY | local (city / unified government) / imposing municipality |
| 7–8 | TYPE / COMPULSORY | Local privilege-to-operate charge / YES **where imposed** as a condition of operating in the jurisdiction |
| 9 | CURRENT LEGAL AUTHORITY | Kan. Const. art. 12, § 5. K.S.A. 12-1617 family restricts specified agricultural occupation taxes (limitation, not a claim). Distinct from Domain 03 local income-tax **prohibition**. |
| 10 | PAYMENT / REVENUE TRIGGER | Conducting a business/occupation in a jurisdiction that requires the license |
| 11 | LEGALLY OBLIGATED PARTY | Business operator as defined by local ordinance. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Local ordinance remedies. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory local authorization to operate. Whether the charge is a fee, tax, or mixed: **LEGAL INTERPRETATION REQUIRED**. **LOCAL IMPLEMENTATION VARIABLE.** |
| 14 | RATE / CALCULATION | Ordinance-variable. One municipality ≠ one claim. Representative implementation (not statewide universal): Wyandotte County / KCK occupation-tax license (annual). |
| 15 | STATED PURPOSE | Local ordinance / home-rule — **LOCAL IMPLEMENTATION VARIABLE** |
| 16–17 | DESTINATION / FUND | Typically local general or special funds — **EVIDENCE REQUIRED** per jurisdiction |
| 18 | ADMINISTRATIVE | Local collection. Collection ≠ extra claim. |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED** / **LOCAL IMPLEMENTATION VARIABLE**. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Statewide inventory: **EVIDENCE REQUIRED**. Not attempted. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. Not a local FairTax. |
| 22 | AGCL | 00B QUESTION REQUIRED (invoice/license notice varies); 00H POTENTIAL CONFLICT surface (home rule vs closed KLRS; fee-vs-tax; 12-194). **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Enabling + variable local imposition / CANDIDATE COMPULSORY CLAIM **where levied** |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-252 |
| 28 | GOV-DATA LOCATORS | SRC-BILL-A-261 (representative local publication — **not** statewide authority) |
| 29 | SOURCE DATE / VERSION | Retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED (architecture). Every city schedule **not** inventoried. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-006; UNK-D05-010 |
| 32 | NOTES | Do not treat one city’s schedule as statewide universal imposition. |

### KRU-D05-006 — SOS business-entity filing / maintenance

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-006 / 05 |
| 3 | AUTHORITATIVE NAME | Secretary of State business-entity filing fees (K.S.A. 17-7506) and biennial business-entity information report fee (K.S.A. 17-7503(f)) |
| 4 | COMMON / ALTERNATE NAME | Corporate filing fees; annual/biennial report; franchise-like entity maintenance (label not dispositive) |
| 5–6 | LEVEL / ENTITY | State / Secretary of State |
| 7–8 | TYPE / COMPULSORY | Filing / legal-status maintenance charge / YES to obtain or maintain legal entity status as specified |
| 9 | CURRENT LEGAL AUTHORITY | 17-7506; 17-7503(f); failure architecture 17-7509 / 17-7510. Distinct from income/property/sales taxes. |
| 10 | PAYMENT / REVENUE TRIGGER | Formation, amendment, foreign authority, biennial information report, other required filings |
| 11 | LEGALLY OBLIGATED PARTY | Entity / organizer as specified. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Forfeiture / loss of good standing architecture (17-7509 / 17-7510). Exact legal effect **LEGAL EFFECT UNKNOWN** beyond citation. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory governmental filing to obtain or maintain legal entity status. Optional expedited / certified-copy services (17-7506(d)–(e)) are **not** extra compulsory rows unless they become the only practical path — **not evidenced**. |
| 14 | RATE / CALCULATION | Fees by KAR within statutory caps (for-profit articles **≤$250**; nonprofit articles **≤$50**; listed documents **≤$150**; certified copies **≤$50**). Biennial report: **$80 plus** SOS KAR amount (17-7503(f)). |
| 15 | STATED PURPOSE | Filing / public-information report |
| 16–17 | DESTINATION / FUND | SOS fee architecture — exact fund mapping **EVIDENCE REQUIRED** |
| 18 | ADMINISTRATIVE | Optional expedited services distinguished from compulsory filings. |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED**. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Isolated SOS filing totals: **EVIDENCE REQUIRED**. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. |
| 22 | AGCL | Default Domain 05. 00A PROVISIONAL ALIGNMENT + QUESTION REQUIRED (biennial recurrence). **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Evidenced / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-239, 240 |
| 28 | GOV-DATA LOCATORS | EVIDENCE REQUIRED |
| 29 | SOURCE DATE / VERSION | 17-7503 / 17-7506 retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED (architecture). Exhaustive KAR fee table **not** transcribed. |
| 31 | CONFLICT / UNKNOWN IDS | UNK-D05-011 |
| 32 | NOTES | Recurrence: EVENT + BIENNIAL. LLC/other entity chapters may share architecture — **class**, not extra rows. |

### KRU-D05-007 — Local building / development / inspection permits

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-007 / 05 |
| 3 | AUTHORITATIVE NAME | Local building, electrical, plumbing, mechanical, zoning, subdivision, and inspection permit charges |
| 4 | COMMON / ALTERNATE NAME | Building permits; development fees; inspection fees |
| 5–6 | LEVEL / ENTITY | local (city/county) / imposing jurisdiction; state contractor-licensing chapters (e.g. ch. 12 plumbing/electrical) are related |
| 7–8 | TYPE / COMPULSORY | Permit / inspection charge / YES **where imposed** as a condition of lawful construction/land-use |
| 9 | CURRENT LEGAL AUTHORITY | Local codes under home rule / statutory enabling. State contractor licensing is related architecture, not a second counted claim class unless economically distinct. |
| 10 | PAYMENT / REVENUE TRIGGER | Application for building/land-use permission or required inspection |
| 11 | LEGALLY OBLIGATED PARTY | Applicant / owner / contractor as local code specifies. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | No permit; stop-work; local remedies. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory permission to build/develop. Some local “fees” may be taxes or assessments (*Home Builders Ass'n v. Overland Park*; *Heartland v. Mission* TUF = **tax**). **LEGAL INTERPRETATION REQUIRED**. Special assessments **REFERRED TO DOMAIN 06** (not executed). |
| 14 | RATE / CALCULATION | **LOCAL IMPLEMENTATION VARIABLE**. Not inventoried municipality-by-municipality. |
| 15 | STATED PURPOSE | Local code / inspection — **LOCAL IMPLEMENTATION VARIABLE** |
| 16–17 | DESTINATION / FUND | Local — **EVIDENCE REQUIRED** per jurisdiction |
| 18 | ADMINISTRATIVE | Reinspection charges are typically **the same architecture**, not extra rows. |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED**. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Statewide inventory: **EVIDENCE REQUIRED**. Not attempted. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. Construction materials may be Domain 04 — **not this row**. |
| 22 | AGCL | 00H LEGAL INTERPRETATION REQUIRED / POTENTIAL CONFLICT surface (12-194; fee vs tax vs assessment). **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Class architecture / CANDIDATE COMPULSORY CLAIM **where imposed** |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-252, 254 |
| 28 | GOV-DATA LOCATORS | EVIDENCE REQUIRED |
| 29 | SOURCE DATE / VERSION | Retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED (class). Every municipality **not** inventoried. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-005; UNK-D05-010 |
| 32 | NOTES | Recurrence: EVENT / PERMIT-TERM. Cost-recovery class: **EVIDENCE REQUIRED** / **MIXED**. |

### KRU-D05-008 — Environmental / health regulatory permits (class)

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-008 / 05 |
| 3 | AUTHORITATIVE NAME | State environmental and health regulatory permit / license charges (KDHE class; representative ch. 65) |
| 4 | COMMON / ALTERNATE NAME | Air permits; water/waste permits; storage-tank fees |
| 5–6 | LEVEL / ENTITY | State / KDHE (and delegated programs) |
| 7–8 | TYPE / COMPULSORY | Environmental/health regulatory permit charge / YES as condition of the regulated activity |
| 9 | CURRENT LEGAL AUTHORITY | Representative: K.S.A. 65-3008 (air) class; water/waste and storage-tank chapters. Exact KAR fee inventory **not** exhaustive. |
| 10 | PAYMENT / REVENUE TRIGGER | Application, issuance, or renewal of a required environmental/health permit |
| 11 | LEGALLY OBLIGATED PARTY | Permittee / applicant. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Unlawful operation without permit. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory regulatory authorization. Industry-wide assessments may require **Domain 06 referral** if they are assessments rather than permits — **not executed**. |
| 14 | RATE / CALCULATION | KAR / program-specific — **EVIDENCE REQUIRED** for complete schedule |
| 15 | STATED PURPOSE | Program regulation / often cost-of-program — **EVIDENCE REQUIRED** per program |
| 16–17 | DESTINATION / FUND | Program funds — **EVIDENCE REQUIRED** |
| 18 | ADMINISTRATIVE | Application vs annual permit is typically **the same class**, not extra rows. |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED**. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Isolated KDHE fee-fund dollars: **EVIDENCE REQUIRED**. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. |
| 22 | AGCL | Default Domain 05. **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Class architecture / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-258 (class citation; exhaustive KAR not retrieved) |
| 28 | GOV-DATA LOCATORS | EVIDENCE REQUIRED |
| 29 | SOURCE DATE / VERSION | Retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED (class). Every permit form **not** a row. |
| 31 | CONFLICT / UNKNOWN IDS | UNK-D05-012 |
| 32 | NOTES | Recurrence: typically PERMIT-TERM / ANNUAL. Cost-recovery class: **EVIDENCE REQUIRED**. |

### KRU-D05-009 — Food establishment / food-processing licenses

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-009 / 05 |
| 3 | AUTHORITATIVE NAME | Food establishment and food processing plant license fees (K.S.A. 65-688; prohibition 65-689) |
| 4 | COMMON / ALTERNATE NAME | Food license; restaurant license (state food-safety program) |
| 5–6 | LEVEL / ENTITY | State / Kansas Department of Agriculture (secretary) |
| 7–8 | TYPE / COMPULSORY | Food-safety license / YES — unlawful to operate without license (65-689(a)) |
| 9 | CURRENT LEGAL AUTHORITY | 65-688; 65-689 |
| 10 | PAYMENT / REVENUE TRIGGER | Application and annual license for a food establishment or food processing plant |
| 11 | LEGALLY OBLIGATED PARTY | Operator. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Unlawful operation (65-689). Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory regulatory authorization. Statute directs fees “to cover all of the cost of inspection” and requires decrease if excess (65-688(g)). **REGULATORY / COST-RECOVERY CANDIDATE** — not proof every dollar equals marginal cost; **not** RETAIN. |
| 14 | RATE / CALCULATION | Graduated KAR schedule; application **cap $350**; annual license caps by square footage (establishment up to **$750**; processor up to **$400**). |
| 15 | STATED PURPOSE | Cover cost of inspection (65-688) |
| 16–17 | DESTINATION / FUND | Food safety fee fund (65-688(i)) |
| 18 | ADMINISTRATIVE | Secretary shall increase/decrease fees so revenue matches inspection purpose (within caps). |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED**. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Isolated food-safety fee-fund dollars: **EVIDENCE REQUIRED**. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. Food sales may be Domain 04 — **not this row**. |
| 22 | AGCL | 00A PROVISIONAL ALIGNMENT (annual + statutory excess-decrease); 00G PROVISIONAL ALIGNMENT (dedicated fund). **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Evidenced / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-241 |
| 28 | GOV-DATA LOCATORS | EVIDENCE REQUIRED |
| 29 | SOURCE DATE / VERSION | 65-688 / 65-689 retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-004 |
| 32 | NOTES | Recurrence: APPLICATION + ANNUAL. Distinct from local health permits that may overlap — **LOCAL IMPLEMENTATION VARIABLE** residual. |

### KRU-D05-010 — Alcoholic-liquor licensing

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-010 / 05 |
| 3 | AUTHORITATIVE NAME | Alcoholic-liquor license fees (K.S.A. 41-310) |
| 4 | COMMON / ALTERNATE NAME | ABC licenses; liquor licenses; CMB/drinking-establishment licenses (same class) |
| 5–6 | LEVEL / ENTITY | State ABC + city/township occupation tax within statutory caps |
| 7–8 | TYPE / COMPULSORY | Liquor regulatory license / YES as condition of licensed liquor activity |
| 9 | CURRENT LEGAL AUTHORITY | 41-310. Distinct from Domain 01 KRU-D01-007 gallonage, KRU-D01-008 drink tax, KRU-D01-009 enforcement tax. Do not reopen Domain 01. |
| 10 | PAYMENT / REVENUE TRIGGER | Issuance/renewal of a state liquor license; additional local occupation/license tax where levied within caps |
| 11 | LEGALLY OBLIGATED PARTY | Licensee. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | No license / unlawful sale. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory regulatory authorization to manufacture/distribute/sell liquor. Local occupation tax may credit township **general fund** (41-310) — **MIXED**. |
| 14 | RATE / CALCULATION | Biennial statutory schedule (examples: spirits manufacturer **$5,000**; retailer **$500**; microbrewery/farm winery **$500**; distributors **$2,000**). Local occupation tax caps in 41-310(j), (l). |
| 15 | STATED PURPOSE | Liquor regulation / local occupation tax as specified |
| 16–17 | DESTINATION / FUND | ABC / state architecture; township occupation tax may go to township GF |
| 18 | ADMINISTRATIVE | City/township occupation tax is **the same liquor-license class overlay**, not Domain 01. |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED**. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Isolated license-fee dollars vs Domain 01 liquor taxes: **EVIDENCE REQUIRED**. Do not double-count gallonage. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. Liquor retail sales may be Domain 04 — **not this row**. |
| 22 | AGCL | Default Domain 05. **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Evidenced / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-242 |
| 28 | GOV-DATA LOCATORS | EVIDENCE REQUIRED |
| 29 | SOURCE DATE / VERSION | 41-310 retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED (architecture). Every license subtype **not** a row. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-007; UNK-D05-002 |
| 32 | NOTES | Recurrence: BIENNIAL (state). Tobacco dealer licenses identified, not counted (UNK-D05-002). Gaming licensing identified, not counted (UNK-D05-004). |

### KRU-D05-011 — Kansas 911 fees

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-011 / 05 |
| 3 | AUTHORITATIVE NAME | 911 fee of $0.90 per month per subscriber account (K.S.A. 12-5369) and prepaid wireless 911 fee of 2.06% per retail transaction (K.S.A. 12-5371) |
| 4 | COMMON / ALTERNATE NAME | 911 surcharge; prepaid 911; PSAP fee |
| 5–6 | LEVEL / ENTITY | State 911 coordinating / PSAP architecture; sellers collect prepaid; providers remit monthly; KDOR collection of prepaid is a **mechanism** |
| 7–8 | TYPE / COMPULSORY | Compulsory per-subscriber / per-prepaid-transaction charge / YES |
| 9 | CURRENT LEGAL AUTHORITY | 12-5369; 12-5370; 12-5371; uses 12-5375. **Not** Domain 04 sales tax. Domain 04 referred this charge; evidence places it in Domain 05 **with fee-vs-tax unresolved**. |
| 10 | PAYMENT / REVENUE TRIGGER | Monthly subscriber account capable of contacting a PSAP; or prepaid wireless retail transaction (not on prepaid for the monthly fee) |
| 11 | LEGALLY OBLIGATED PARTY | Subscriber / consumer; collected by provider or seller. Collection ≠ extra claim. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Provider/seller remittance duties. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Dedicated 911/PSAP financing. Monthly fee may be **lowered** if moneys exceed PSAP operating costs (12-5369(b)) → **REGULATORY / COST-RECOVERY CANDIDATE**. Prepaid **percentage of retail transaction** is **MIXED**. Whether fee, surcharge, or tax: **LEGAL INTERPRETATION REQUIRED**. |
| 14 | RATE / CALCULATION | **$0.90**/month per subscriber account; prepaid **2.06%** per retail transaction (adjusted if 12-5369 reduced: new fee/50). Seller collects; not in sales-tax base if separately stated (as provided). |
| 15 | STATED PURPOSE | Operate PSAPs / 911 (12-5369(b); 12-5375) |
| 16–17 | DESTINATION / FUND | State 911 funds / PSAP distributions (12-5374/5375) — dedicated uses |
| 18 | ADMINISTRATIVE | Two collection mechanisms, **one claim class**. KDOR remittance path ≠ Domain 04 row. |
| 19 | DEPENDENCIES | PSAP operations **DEPENDENCY VERIFIED** as statutory purpose. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Isolated 911 statewide total: **EVIDENCE REQUIRED**. Do not add to Domain 04 RST. |
| 21 | H.R. 25 | Outside consumption-tax event as a class; prepaid 911 may **stack at collection** on a retail prepaid-wireless sale alongside Domain 04 — **collection timing**, not a FairTax design. Not Kansas law. |
| 22 | AGCL | 00B QUESTION REQUIRED (often billed on telecom invoice); 00H LEGAL INTERPRETATION REQUIRED. **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Evidenced / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-243, 244 |
| 28 | GOV-DATA LOCATORS | EVIDENCE REQUIRED |
| 29 | SOURCE DATE / VERSION | 12-5369 / 12-5371; 12-5371 history through L. 2024, ch. 53; July 1, 2025 |
| 30 | VERIFICATION STATUS | TRACED (architecture) |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-008 |
| 32 | NOTES | Recurrence: MONTHLY or PER TRANSACTION. Do not automatically classify “surcharge” as Domain 05 from the word alone — evidence of compulsory 911 architecture controls. |

### KRU-D05-012 — Municipal franchise / telecom access-line or gross-receipts fees

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-012 / 05 |
| 3 | AUTHORITATIVE NAME | City franchise / telecommunications access-line fee or gross-receipts charge (K.S.A. 12-2001) |
| 4 | COMMON / ALTERNATE NAME | Franchise fee; ROW fee; access-line fee |
| 5–6 | LEVEL / ENTITY | local (city) / imposing city; providers collect access-line fee |
| 7–8 | TYPE / COMPULSORY | Franchise consideration / ROW / telecom charge / YES **where granted/imposed** |
| 9 | CURRENT LEGAL AUTHORITY | 12-2001. Word “franchise” is **not** dispositive. |
| 10 | PAYMENT / REVENUE TRIGGER | Franchise grant / provision of local exchange telecommunications service as specified |
| 11 | LEGALLY OBLIGATED PARTY | Provider / subscriber as ordinance specifies (access-line collected from customer). Collection ≠ extra claim. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Franchise/ordinance remedies. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Possible functions: franchise consideration; right-of-way compensation; regulatory fee; tax. **LEGAL INTERPRETATION REQUIRED.** **LOCAL IMPLEMENTATION VARIABLE.** |
| 14 | RATE / CALCULATION | Telecom LEC: access-line fee max **$2.75/month** (from 2012) **or** up to **5% of gross receipts**. Must be competitively neutral / nondiscriminatory. Other utility franchises: **EVIDENCE REQUIRED** as subclass. |
| 15 | STATED PURPOSE | Franchise / ROW / city ordinance |
| 16–17 | DESTINATION / FUND | City treasury — **LOCAL IMPLEMENTATION VARIABLE** |
| 18 | ADMINISTRATIVE | Provider collection is a **mechanism**. |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED**. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Statewide city franchise inventory: **EVIDENCE REQUIRED**. Not attempted. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. Not a local FairTax. |
| 22 | AGCL | 00B QUESTION REQUIRED (often on utility bill); 00H LEGAL INTERPRETATION REQUIRED (*Executive Aircraft*). **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Enabling + variable local imposition / CANDIDATE COMPULSORY CLAIM **where imposed** |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-245, 253 |
| 28 | GOV-DATA LOCATORS | EVIDENCE REQUIRED |
| 29 | SOURCE DATE / VERSION | 12-2001 retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED (enabling). Every city franchise **not** inventoried. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-009 |
| 32 | NOTES | Recurrence: PERIODIC (monthly/annual as ordinance). Cost-recovery class: **LEGAL INTERPRETATION REQUIRED** / **MIXED**. |

### KRU-D05-013 — District-court docket / filing fees

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-013 / 05 |
| 3 | AUTHORITATIVE NAME | Docket fee (K.S.A. 60-2001); disposition (K.S.A. 20-362) |
| 4 | COMMON / ALTERNATE NAME | Court filing fee; docket fee |
| 5–6 | LEVEL / ENTITY | State judicial branch + county (portions) |
| 7–8 | TYPE / COMPULSORY | Access-to-process charge / YES except poverty affidavit |
| 9 | CURRENT LEGAL AUTHORITY | 60-2001; 20-362. Distinct from Domain 07 fines/penalties. Criminal docket (28-172a) is **related architecture**, not a second counted row. |
| 10 | PAYMENT / REVENUE TRIGGER | Filing / docketing a case |
| 11 | LEGALLY OBLIGATED PARTY | Filer (poverty-affidavit exception). Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Case not filed/docketed (60-2001(a)). Late/penalty add-ons **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory payment to access a governmental legal process — **not** a voluntary souvenir copy. Mixed destinations (county GF, law library, PATF, e-filing fund, **SGF remainder**) → **MIXED**. |
| 14 | RATE / CALCULATION | Docket fee **$173**. Additional Supreme Court charge **≤$22** through **June 30, 2025** for non-judicial personnel — **currentness after 2025-06-30: UNK-D05-007**. |
| 15 | STATED PURPOSE | Docketing; additional charge for non-judicial personnel (time-limited overlay) |
| 16–17 | DESTINATION / FUND | 20-362: $10 county GF; library fees to county law library; $2/$1 prosecuting-attorneys training; first **$1,500,000** remainder (FY2022 onward) to electronic filing and management fund; balance **SGF** |
| 18 | ADMINISTRATIVE | Multiple statutory allocations of **one** docket architecture — not multiple claims. |
| 19 | DEPENDENCIES | E-filing fund / SGF remainder **DEPENDENCY VERIFIED** as destination. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Isolated docket-fee statewide total: **EVIDENCE REQUIRED**. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. |
| 22 | AGCL | 00D QUESTION REQUIRED (poverty affidavit is a partial exit, not a general exit). **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Evidenced / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-246, 247 |
| 28 | GOV-DATA LOCATORS | EVIDENCE REQUIRED |
| 29 | SOURCE DATE / VERSION | 60-2001 / 20-362 retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED (architecture). $22 overlay currentness **UNK-D05-007**. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-010; UNK-D05-007 |
| 32 | NOTES | Recurrence: PER CASE. Cost-recovery class: **MIXED**. |

### KRU-D05-014 — Register-of-deeds recording fees

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-014 / 05 |
| 3 | AUTHORITATIVE NAME | Register of deeds fees (K.S.A. 28-115) |
| 4 | COMMON / ALTERNATE NAME | Recording fees; ROD fees |
| 5–6 | LEVEL / ENTITY | local (county) / register of deeds; specified state heritage-trust remittance |
| 7–8 | TYPE / COMPULSORY | Recording / public-notice charge / YES to record instruments as specified |
| 9 | CURRENT LEGAL AUTHORITY | 28-115; technology split 28-115a class. UCC amounts in UCC — **not** an extra Domain 05 row unless economically distinct. |
| 10 | PAYMENT / REVENUE TRIGGER | Recording an instrument |
| 11 | LEGALLY OBLIGATED PARTY | Person presenting the instrument. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Instrument not recorded. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory payment to use the public recording system for legal notice. Remainder to **county general fund** (28-115(h)) plus technology/heritage dedications → **MIXED**. |
| 14 | RATE / CALCULATION | On/after 2018-01-01: **$17** first page + **$13** each additional; plus **$3**/page technology split; plus **$1**/page heritage trust (cap **$30,000**/year to state then county GF). Mortgage cap **$125** for qualifying principal-residence mortgages ≤$75,000. |
| 15 | STATED PURPOSE | Recording; technology funds; heritage trust |
| 16–17 | DESTINATION / FUND | County GF remainder; ROD/clerk/treasurer technology; heritage trust (capped) |
| 18 | ADMINISTRATIVE | Technology/heritage add-ons are **allocations of this architecture**, not extra claims. |
| 19 | DEPENDENCIES | Heritage trust remittance **DEPENDENCY VERIFIED** as statutory allocation. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Statewide recording-fee total: **EVIDENCE REQUIRED**. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. |
| 22 | AGCL | 00G MIXED destination (county GF vs dedicated). **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Evidenced / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-248 |
| 28 | GOV-DATA LOCATORS | EVIDENCE REQUIRED |
| 29 | SOURCE DATE / VERSION | 28-115 retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-010 |
| 32 | NOTES | Recurrence: PER TRANSACTION. Optional extra copies of records may be voluntary — distinguished from compulsory recording of an instrument that must be recorded for legal effect. |

### KRU-D05-015 — Hunting / fishing / wildlife licenses

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-015 / 05 |
| 3 | AUTHORITATIVE NAME | Wildlife license and permit fees fixed by the secretary within statutory maxima (K.S.A. 32-988); service charge (K.S.A. 32-989) |
| 4 | COMMON / ALTERNATE NAME | Hunting license; fishing license; combination license |
| 5–6 | LEVEL / ENTITY | State / Kansas Department of Wildlife and Parks; county clerks as vendors |
| 7–8 | TYPE / COMPULSORY | Take-authorization / resource-access charge / YES as condition of legal hunting/fishing where a license is required |
| 9 | CURRENT LEGAL AUTHORITY | 32-988; 32-989. Destination citations in 32-989(b): 32-990, 32-991, 32-993. Parks fee fund (32-991) is **allied** park receipts — do **not** dump hunting licenses there without 32-990/993. Full 32-990/993 text: **UNK-D05-013**. |
| 10 | PAYMENT / REVENUE TRIGGER | Issuance of a hunting, fishing, combination, or related wildlife license/permit |
| 11 | LEGALLY OBLIGATED PARTY | Licensee. County-clerk $1 service charge retained to county GF (32-989). Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Unlawful take. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | **MIXED** — regulatory authorization to take wildlife **and** user/resource-access payment. Do not assume one label. Park enterprise product/service charges **REFERRED TO DOMAIN 08** (not executed). |
| 14 | RATE / CALCULATION | Secretary by KAR within maxima (example: resident combination hunting and fishing **maximum $50**; lifetime combination **maximum $1,000**). Service charge **≤$1.00** with listed exceptions. |
| 15 | STATED PURPOSE | Wildlife licenses/permits; service charge for issuance |
| 16–17 | DESTINATION / FUND | Per 32-989(b) citing 32-990 / 32-991 / 32-993; county-clerk retainage to county GF. Isolated wildlife-fee-fund dollars: **EVIDENCE REQUIRED**. |
| 18 | ADMINISTRATIVE | $1 service charge is a **mechanism of this class**, not a second counted claim. |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED**. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Isolated hunting/fishing collections: **EVIDENCE REQUIRED**. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. |
| 22 | AGCL | Default Domain 05. **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Evidenced maxima / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-249 |
| 28 | GOV-DATA LOCATORS | EVIDENCE REQUIRED |
| 29 | SOURCE DATE / VERSION | 32-988 / 32-989 retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED (maxima / service charge). KAR fee table and 32-990/993 text **PARTIAL**. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-011; UNK-D05-013 |
| 32 | NOTES | Recurrence: ANNUAL / LICENSE-TERM / LIFETIME option. Cost-recovery class: **MIXED** / **EVIDENCE REQUIRED**. |

### KRU-D05-016 — Insurance licensing / certificate-of-authority fees

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-016 / 05 |
| 3 | AUTHORITATIVE NAME | Insurance company/society licensing and filing **fees** in the K.S.A. 40-252 schedule (not the premium tax) |
| 4 | COMMON / ALTERNATE NAME | Insurance department fees; certificate of authority fee; annual statement filing fee |
| 5–6 | LEVEL / ENTITY | State / Kansas Insurance Department |
| 7–8 | TYPE / COMPULSORY | Regulatory licensing/filing fee / YES as condition of authority to transact insurance as specified |
| 9 | CURRENT LEGAL AUTHORITY | 40-252 **fee items only**. The **premium tax** (2% TY2025 / 1.98% TY2026+ on Kansas-risk premiums) is a **tax** — **REFERRED** (not Domain 01–04; Domain 03 already excluded it). Do not duplicate ACFR “Insurance premiums taxes.” |
| 10 | PAYMENT / REVENUE TRIGGER | Admission, certificate of authority, annual statement filing, agent appointment, other listed **fees** |
| 11 | LEGALLY OBLIGATED PARTY | Insurer / society as specified. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | No authority / filing not accepted. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory regulatory authorization/filing. Distinct from premium **tax**. |
| 14 | RATE / CALCULATION | Examples from 40-252 fee schedule: filing annual statement **$100**; certificate of authority **$10**; admission examination of charter **$500**; agent appointment **$2**. Do not treat the 2%/1.98% premium tax as this row’s amount. |
| 15 | STATED PURPOSE | Insurance regulation / filings |
| 16–17 | DESTINATION / FUND | Insurance department fee architecture — **EVIDENCE REQUIRED** for isolated fee vs tax split |
| 18 | ADMINISTRATIVE | Do not collapse premium tax into this fee row. |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED**. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Isolated **fee** (not premium tax) dollars: **EVIDENCE REQUIRED**. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. Insurance premiums are a separate tax architecture — not this row. |
| 22 | AGCL | Default Domain 05. **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Evidenced fees / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-250 |
| 28 | GOV-DATA LOCATORS | EVIDENCE REQUIRED (do not use premium-tax ACFR line) |
| 29 | SOURCE DATE / VERSION | 40-252 retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED (fee vs tax split). Exhaustive 40-252 fee list not required for class. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-012 |
| 32 | NOTES | Recurrence: ANNUAL + admission. Cost-recovery class: **EVIDENCE REQUIRED** / **MIXED**. |

### KRU-D05-017 — Oversize / overweight special permits

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-017 / 05 |
| 3 | AUTHORITATIVE NAME | Special permits for oversize/overweight / special vehicle combinations (K.S.A. 8-1911) |
| 4 | COMMON / ALTERNATE NAME | Oversize permit; overweight permit; superload permit |
| 5–6 | LEVEL / ENTITY | State (local authorities may issue on local highways) |
| 7–8 | TYPE / COMPULSORY | Transportation permit / YES as condition of lawful oversize/overweight movement |
| 9 | CURRENT LEGAL AUTHORITY | 8-1911. Distinct from KRU-D05-001 registration and from KRU-D01-003 motor-fuel trip permits. |
| 10 | PAYMENT / REVENUE TRIGGER | Issuance of a special permit |
| 11 | LEGALLY OBLIGATED PARTY | Permit applicant / operator. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Movement without required permit. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory authorization for nonstandard highway use. Proceeds to **state highway fund** → **MIXED**. |
| 14 | RATE / CALCULATION | On/after 2020-01-01: single-trip **$40**; large structure/superload **$200**; annual **$200**; special vehicle combination **$2,000**/year plus **$50**/power unit. No fees for political-subdivision vehicles. |
| 15 | STATED PURPOSE | Special movement authorization |
| 16–17 | DESTINATION / FUND | State highway fund (8-1911(f)) |
| 18 | ADMINISTRATIVE | Local-highway permits by local authorities are **the same class**, LOCAL IMPLEMENTATION VARIABLE as to who issues. |
| 19 | DEPENDENCIES | SHF **DEPENDENCY VERIFIED** (destination). Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | May be inside ACFR “vehicle registrations and permits” — **do not double-count** with KRU-D05-001. Isolated oversize dollars: **EVIDENCE REQUIRED**. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. |
| 22 | AGCL | 00E EVIDENCE REQUIRED (SHF). **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Evidenced / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-251 |
| 28 | GOV-DATA LOCATORS | SRC-BILL-A-260 (do not double-count) |
| 29 | SOURCE DATE / VERSION | 8-1911 retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED |
| 31 | CONFLICT / UNKNOWN IDS | UNK-D05-003 |
| 32 | NOTES | Recurrence: PER TRIP or ANNUAL. KCC motor-carrier authority identified, not counted (UNK-D05-003). |

### KRU-D05-018 — Financial-institution regulatory / examination fees

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D05-018 / 05 |
| 3 | AUTHORITATIVE NAME | Bank/OSBC regulatory, charter, and examination fees (class; K.S.A. 9-1703 listed in 75-3170a) |
| 4 | COMMON / ALTERNATE NAME | Bank examination fees; OSBC fees |
| 5–6 | LEVEL / ENTITY | State / Office of the State Bank Commissioner (and related financial regulators) |
| 7–8 | TYPE / COMPULSORY | Financial-institution regulatory charge / YES as condition of charter/examination as specified |
| 9 | CURRENT LEGAL AUTHORITY | 9-1703 (listed in 75-3170a). **Distinct from** Domain 03 privilege tax (79-1107 / 79-1108). Do not duplicate. |
| 10 | PAYMENT / REVENUE TRIGGER | Examination, charter, or other OSBC regulatory fee event |
| 11 | LEGALLY OBLIGATED PARTY | Supervised institution. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Supervisory remedies. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Compulsory regulatory/supervisory payment. 10% SGF credit where 75-3170a applies → **MIXED**. |
| 14 | RATE / CALCULATION | Exact current schedule: **EVIDENCE REQUIRED**. Architecture TRACED as a class. |
| 15 | STATED PURPOSE | Bank/financial regulation; 75-3170a SGF reimbursement where applicable |
| 16–17 | DESTINATION / FUND | Fee fund + 10% SGF where listed |
| 18 | ADMINISTRATIVE | 10% SGF is allocation, not a second claim. |
| 19 | DEPENDENCIES | **EVIDENCE REQUIRED**. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Isolated OSBC fee dollars (not privilege tax): **EVIDENCE REQUIRED**. |
| 21 | H.R. 25 | Outside consumption-tax event as a class. |
| 22 | AGCL | Same 75-3170a surface as KRU-D05-004. **Never SATISFIED.** |
| 23–24 | CURRENT-STATE / KLRS | Class architecture / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-238, 256 |
| 28 | GOV-DATA LOCATORS | EVIDENCE REQUIRED |
| 29 | SOURCE DATE / VERSION | 75-3170a / 9-1703 listing retrieved 2026-09-02 |
| 30 | VERIFICATION STATUS | TRACED (architecture). Amounts **PARTIAL**. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D05-002; UNK-D05-014 |
| 32 | NOTES | Recurrence: **EVIDENCE REQUIRED**. Credit unions / other financial charters: same **class** unless evidence shows a materially different architecture. |

---

Libertas sine lapsu — Liberty without drift.
