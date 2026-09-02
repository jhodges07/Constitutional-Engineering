# WD-BILL-A-031 — Domain 02 Master Register Execution Instance

**Document ID:** WD-BILL-A-031  
**Title:** Kansas Government Revenue Universe / KLRS Master Register — Domain 02 Execution Instance  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-130 (initial execution); CWC-CE-131 (evidence closure / reconciliation)  
**Schema authority:** WD-BILL-A-019 (this file does **not** replace the schema lock)  
**Governing LOU candidate:** LOU-004 Draft 1.1 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / DOMAIN 02 ROWS POPULATED FROM EVIDENCE — CLOSURE APPLIED — REGISTER **NOT** STATEWIDE COMPLETE — NOT ACCEPTED  
**Version:** 0.2.0  
**Effective Date:** 2026-09-02  
**Retrieval date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-031-Domain-02-Master-Register-Execution.md  

```text
EXECUTION INSTANCE OF WD-BILL-A-019 SCHEMA
DOMAIN 02 ONLY
HUMAN DISPOSITION = BLANK ON EVERY ROW
BLANK ≠ RETAIN
CURRENT EXISTENCE ≠ POST-BILL-A AUTHORITY
KLRS CANDIDACY ≠ FINAL AUTHORIZATION
STATEWIDE UNIVERSE NOT CERTIFIED
NOT A SPEC / NOT HG-D1 / NOT HG-D2
NO PROPERTY-TAX ELIMINATION DESIGN
```

Narrative audit: WD-BILL-A-030. Sources: WD-BILL-A-032. Completeness: WD-BILL-A-033. Conflicts: WD-BILL-A-034. Constitutional / school-finance / dependency: WD-BILL-A-035. Closure: WD-BILL-A-037.

Domain 01 rows remain in WD-BILL-A-022 and are **not** rewritten here.

Common field values unless a row overrides:

- Field 2 EVIDENCE DOMAIN = 02
- Field 25 HUMAN BILL A DISPOSITION = **BLANK**
- Field 26 POST-BILL-A AUTHORITY STATUS = **NOT DETERMINED**
- Field 29 SOURCE DATE / VERSION = 2025 Kansas Statutes PDFs / constitutional text as retrieved 2026-09-02; KLRD Tax Facts 2024 Supplement (updated Jan 2025); PVD Table IV 2023–2025
- Retrieval date = 2026-09-02

Property-subject, valuation basis, mill architecture, and class differences that the CWC listed as discovery questions are recorded in fields 10, 13, 14, and 32. They are **not** added as extra schema columns.

---

## 1. Index of Domain 02 rows

| Master Record ID | Authoritative name | Compulsory | Verification | Disposition |
|---|---|---|---|---|
| KRU-D02-001 | Classified ad valorem taxation of taxable real and tangible personal property | YES | TRACED (architecture) | BLANK |
| KRU-D02-002 | Statewide 20-mill unified-school-district levy (K.S.A. 72-5142) | YES | TRACED | BLANK |
| KRU-D02-003 | School local-option-budget / supplemental general ad valorem levy | YES (where adopted) | TRACED (authority); rate VARIABLE | BLANK |
| KRU-D02-004 | School capital-outlay levy | YES (where authorized) | TRACED (authority); mill generally ≤8 unless higher path | BLANK |
| KRU-D02-005 | Bond-and-interest / debt-service property levy | YES where bonds outstanding | TRACED (10-113 duty); rates VARIABLE | BLANK |
| KRU-D02-006 | County ad valorem levies | YES | TRACED (79-1801 architecture); LOCAL IMPLEMENTATION VARIABLE | BLANK |
| KRU-D02-007 | City ad valorem levies | YES | TRACED (79-1801 architecture); LOCAL IMPLEMENTATION VARIABLE | BLANK |
| KRU-D02-008 | Township ad valorem levies | YES | TRACED (79-1801 architecture); LOCAL IMPLEMENTATION VARIABLE | BLANK |
| KRU-D02-009 | Other taxing-subdivision ad valorem levies | YES where levied | TRACED as a class; not every entity enumerated | BLANK |
| KRU-D02-010 | State 1-mill educational-building levy (tax year 2025) | YES for year 2025 | TRACED for TY 2025; TY 2026 mill **NOT CURRENT** (L. 2025, ch. 71) | BLANK |
| KRU-D02-011 | State 0.5-mill state-institutions-building levy (tax year 2025) | YES for year 2025 | TRACED for TY 2025; TY 2026 mill **NOT CURRENT** (L. 2025, ch. 71) | BLANK |
| KRU-D02-012 | Motor-vehicle tax in lieu of general personal-property tax | YES | TRACED | BLANK |
| KRU-D02-013 | Recreational-vehicle tax in lieu of other property tax | YES | TRACED | BLANK |
| KRU-D02-014 | Public-utility state-appraised property (ad valorem pathway) | YES | TRACED (79-5a01 / 79-5a04 / 79-1439) | BLANK |
| KRU-D02-015 | Mineral-leasehold personal-property ad valorem | YES | TRACED (Art. 11 §1 / 79-1439); distinct from KRU-D01-010 | BLANK |
| KRU-D02-016 | 16M/20M personal-property tax (GVW >12,000 and <20,001 lb) | YES | TRACED (79-5105a) | BLANK |

Counted Domain 02 verified **claim-category** records: **16**.  
This is **not** a count of every local mill levy. Count follows evidence, not the prior 15.

---

## 2. Thirty-two-field records

### KRU-D02-001 — Classified general ad valorem property tax

| # | Field | Value |
|---|---|---|
| 1 | MASTER RECORD ID | KRU-D02-001 |
| 2 | EVIDENCE DOMAIN | 02 |
| 3 | AUTHORITATIVE NAME | Uniform and equal basis of valuation and rate of taxation of all property subject to taxation; classification into Class 1 real property and Class 2 tangible personal property (Kan. Const. art. 11, § 1); assessment percentages K.S.A. 79-1439 |
| 4 | COMMON / ALTERNATE NAME | General property tax; ad valorem tax; mill levy; tangible property tax |
| 5 | GOVERNMENT LEVEL | state and local (stacked mills on one roll) |
| 6 | GOVERNMENT ENTITY / ENTITY CLASS | Taxing subdivisions certifying under K.S.A. 79-1801; county clerk / county treasurer administer the roll and collection |
| 7 | RECEIPT OR CLAIM TYPE | Classified ad valorem tax on taxable tangible property |
| 8 | COMPULSORY STATUS | YES |
| 9 | CURRENT LEGAL AUTHORITY | Kan. Const. art. 11, § 1; art. 11, § 12 (ag use value); K.S.A. 79-1439; 79-503a; 79-1476; 79-1801; 79-2004; 79-201 (exemptions, non-exhaustive) |
| 10 | PAYMENT / REVENUE TRIGGER | Taxable real or tangible personal property is classified, valued, assessed, and placed on the tax roll for the tax year. The legal trigger is **property subject to taxation remaining on the assessment architecture**, not a retail consumption event. |
| 11 | LEGALLY OBLIGATED PARTY | Owner / person charged on the tax roll (real-property payment schedule 79-2004) |
| 12 | CONSEQUENCE OF NONPAYMENT | Unpaid real-property tax: interest under 79-2004 (79-2968 rate + 5 percentage points); foreclosure path referenced in 79-2004. Interest **REFERRED TO DOMAIN 07** as a collection incident (WD-BILL-A-034). |
| 13 | ECONOMIC FUNCTION | Compulsory claim on taxable tangible property **existence / ownership / situs / classified assessed value**. Distinct valuation regimes: FMV (79-503a) vs agricultural use/productivity (art. 11 §12; 79-1476). Do not collapse classes. |
| 14 | RATE / CALCULATION / AMOUNT METHOD | Appraised value × subclass assessment % (79-1439) × mill rate of each overlapping taxing subdivision (1 mill = $1 per $1,000 assessed). Combined mill **VARIABLE BY JURISDICTION**. PVD Table IV 2025 statewide average county levy **127.035** mills. |
| 15 | STATED PURPOSE | Constitutional: uniform/equal valuation and rate as to class; local/state mill purposes stated in each levy statute/budget |
| 16 | REVENUE DESTINATION | Each certifying taxing subdivision (79-1801; distribution 12-1678a). Statewide school 20-mill share remitted per 72-5142. State building mills per 76-6b01 / 76-6b04 when levied. |
| 17 | FUND / POOL TYPE | Mixed: general funds, dedicated mill funds, school funds — determined by each levy |
| 18 | ADMINISTRATIVE / OVERHEAD TREATMENT | County collection architecture; `[TO BE VERIFIED]` for any collection fee split |
| 19 | DEBT / BOND / CONTRACT / FEDERAL-MATCH / OTHER DEPENDENCIES | K.S.A. 10-113: **DEPENDENCY VERIFIED** as a statewide duty to levy for bonds/interest falling due. Impairment if this claim disappeared: **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | KLRD Tax Facts 2024 Supplement Table 1 FY2024 combined General Property **$6,422,236 thousand** (taxes **levied** for collection). Table 5 local tangible property **$6,349,390 thousand**. Levy ≠ collections. |
| 21 | H.R. 25 KANSAS-MIRROR RELATIONSHIP | STRUCTURALLY OUTSIDE H.R. 25 CONSUMPTION EVENT; POTENTIAL CONFLICT WITH BILL A HUMAN INTENT (ownership/existence ≠ intended taxable event). H.R. 25 is not Kansas law. |
| 22 | AGCL 00A–00J CLASSIFICATION | 00A QUESTION REQUIRED; 00C POTENTIAL CONFLICT (pooling / property-rights surface); 00E POTENTIAL CONFLICT (10-113); 00H POTENTIAL CONFLICT surface (Art. 11). **Never SATISFIED.** |
| 23 | CURRENT-STATE STATUS | Evidenced current Kansas classified ad valorem architecture. **Not** future authorization. |
| 24 | KLRS CANDIDACY | CANDIDATE COMPULSORY CLAIM. Not final authorization. |
| 25 | HUMAN BILL A DISPOSITION | **BLANK** |
| 26 | POST-BILL-A AUTHORITY STATUS | **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-075–082, 088, 093 |
| 28 | GOV-DATA LOCATORS | SRC-BILL-A-100–104 |
| 29 | SOURCE DATE / VERSION | 2025 K.S.A. PDFs; Art. 11 §1 as retrieved 2026-09-02; Tax Facts updated Jan 2025; PVD Table IV 2023–2025 |
| 30 | VERIFICATION STATUS | TRACED (architecture). Individual local mill rates not enumerated. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D02-001; CF-D02-002; UNK-D02-001 through UNK-D02-008 |
| 32 | NOTES / TRACEABILITY | Subclass assessment %: residential 11.5%; ag land 30% of **use** value; vacant lots 12%; specified 501(c) 12%; public-utility real 33% (railroad at commercial average); commercial/industrial 25%; other real 30%. Personal: mobile homes 11.5%; mineral leaseholds 30% (stripper 25%); public-utility PP 33%; tax-roll motor vehicles 30%; CIME 25% of depreciated RCN with 20% floor; other TPP 30%. Special assessments **not** Domain 02 (12-6a01 → Domain 06). |

### KRU-D02-002 — Statewide 20-mill school-district levy

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D02-002 / 02 |
| 3 | AUTHORITATIVE NAME | Each USD shall levy a tax at the mill rate provided for school years 2025-2026 and 2026-2027 of 20 mills (K.S.A. 72-5142(a)) |
| 4 | COMMON / ALTERNATE NAME | Statewide 20-mill school levy; general fund mill |
| 5–6 | LEVEL / ENTITY | State finance architecture levied by each USD |
| 7–8 | TYPE / COMPULSORY | School ad valorem levy / YES |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 72-5142 (history through L. 2025, ch. 128, § 1; May 8); residential exemption K.S.A. 79-201x (TY 2024+: $75,000 of appraised valuation from **this levy only**; L. 2024, ch. 1, § 9 Special Session) |
| 10 | PAYMENT / REVENUE TRIGGER | USD levy on taxable tangible property (except 79-201x residential exemption from this levy) |
| 11 | LEGALLY OBLIGATED PARTY | Property owner on the roll |
| 12 | CONSEQUENCE OF NONPAYMENT | Same collection path as KRU-D02-001 |
| 13 | ECONOMIC FUNCTION | School-finance property claim remitted to the **state school district finance fund** |
| 14 | RATE / CALCULATION | **20 mills** school years 2025-2026 and 2026-2027. Residential $75,000 appraised-value exemption from this levy (79-201x). |
| 15 | STATED PURPOSE | 72-5142(e) cites Kan. Const. art. 6 (suitable provision for educational finance) |
| 16–17 | DESTINATION / FUND | County treasurer remits to state treasurer except specified pre-1997 12-1774 redevelopment-bond share; credited to **state school district finance fund** (72-5142(c)) |
| 18 | ADMINISTRATIVE | County collection; state remittance |
| 19 | DEPENDENCIES | School-finance / Art. 6 §6(b): **DEPENDENCY VERIFIED** as a current finance mechanism. Whether Art. 6 requires **this mill**: **LEGAL INTERPRETATION REQUIRED**. Not a Gannon holding. |
| 20 | RECEIPT DATA | Included in KLRD Table 5 “Schools” local tangible property FY2024 $2,769,407 thousand (USDs + community colleges + municipal universities — **alias**; not USD-only). Statewide 20-mill dollars not separately isolated in that exhibit. |
| 21 | H.R. 25 | STRUCTURALLY OUTSIDE H.R. 25 CONSUMPTION EVENT; POTENTIAL CONFLICT WITH BILL A HUMAN INTENT |
| 22 | AGCL | 00C / 00H POTENTIAL CONFLICT surface; 00A QUESTION REQUIRED. Never SATISFIED. |
| 23–24 | CURRENT-STATE / KLRS | Current 20-mill mechanism evidenced / CANDIDATE COMPULSORY CLAIM |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27–28 | LOCATORS | SRC-BILL-A-083, 084, 075, 087 |
| 29 | SOURCE DATE | 72-5142 2025 PDF (L. 2025, ch. 128); 79-201x 2025 PDF |
| 30 | VERIFICATION | TRACED |
| 31 | CONFLICTS | CF-D02-001 (PVD exemption-list $75,000 vs a stale $20,000 line); UNK-D02-003 |
| 32 | NOTES | SB 532 mill-reduction is **introduced / not current law**. Do not treat 20 mills as a Human RETAIN. |

### KRU-D02-003 — School LOB / supplemental general levy

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D02-003 / 02 |
| 3 | AUTHORITATIVE NAME | Ad valorem tax levy for the local option budget; proceeds to the supplemental general fund (K.S.A. 72-5147) |
| 4 | COMMON / ALTERNATE NAME | LOB levy; supplemental general fund mill |
| 5–8 | LEVEL / TYPE / COMPULSORY | USD / school ad valorem / YES where adopted |
| 9 | AUTHORITY | K.S.A. 72-5147 |
| 10–11 | TRIGGER / OBLIGOR | Adopted LOB ad valorem on taxable property / owner on roll |
| 12 | NONPAYMENT | Same as KRU-D02-001 |
| 13–14 | FUNCTION / RATE | Local school operating supplement / **VARIABLE BY DISTRICT** |
| 15–17 | PURPOSE / DESTINATION | Supplemental general fund (except 12-1774 redevelopment share) |
| 18–20 | ADMIN / DEBT / RECEIPTS | County collection / POTENTIAL overlap with other USD levies / not isolated in Tax Facts Table 5 |
| 21–26 | H.R. 25 / AGCL / STATUS / KLRS / DISPOSITION / POST | Same pattern as KRU-D02-002: OUTSIDE consumption event; BLANK; NOT DETERMINED |
| 27–30 | LOCATORS / VERIFY | SRC-BILL-A-085 / TRACED (authority); mill VARIABLE |
| 31–32 | CONFLICTS / NOTES | UNK-D02-003 statewide LOB dollar total not isolated. Do not redesign school finance. |

### KRU-D02-004 — School capital-outlay levy

| # | Field | Value |
|---|---|---|
| 1–4 | ID / NAME | KRU-D02-004 / School capital outlay levy (K.S.A. 72-53,113) |
| 5–8 | LEVEL / TYPE / COMPULSORY | USD / capital ad valorem / YES where authorized |
| 9 | AUTHORITY | K.S.A. 72-53,113 (history through L. 2018, ch. 57, § 14; July 1) |
| 10–14 | TRIGGER / RATE | Board capital-outlay levy on taxable property / statutorily prescribed mill rate generally **not exceeding 8 mills** unless protest/election path for a higher rate |
| 15–17 | PURPOSE / FUND | Capital outlay fund |
| 19 | DEPENDENCIES | Capital facilities; **POTENTIAL DEPENDENCY** with related debt; not every district audited |
| 20 | RECEIPTS | Not isolated in Tax Facts Table 5 |
| 21–26 | H.R. 25 / DISPOSITION | OUTSIDE consumption event / **BLANK** / **NOT DETERMINED** |
| 27–30 | LOCATORS | SRC-BILL-A-086 / TRACED (authority) |
| 31–32 | NOTES | Do not enumerate every USD capital mill. |

### KRU-D02-005 — Bond-and-interest / debt-service property levy

| # | Field | Value |
|---|---|---|
| 1–4 | ID / NAME | KRU-D02-005 / Duty to levy annually a sum sufficient to pay interest and bonds falling due (K.S.A. 10-113) |
| 5–8 | LEVEL / TYPE / COMPULSORY | County / city / USD / other issuers of property-tax-backed bonds / YES where bonds outstanding |
| 9 | AUTHORITY | K.S.A. 10-113; underlying bond-authorization statutes `[CITATION/TEXT NEEDED]` per issuer class |
| 10–14 | TRIGGER / RATE | Outstanding bonds/interest falling due / mill sufficient for that year’s debt service — **VARIABLE** |
| 15–17 | PURPOSE / DESTINATION | Bond and interest funds of the issuer |
| 19 | DEPENDENCIES | **DEPENDENCY VERIFIED** as statewide statutory levy duty. Failure is a misdemeanor ($100). Sampled indenture: **not retrieved** (not an EXAMPLE DOCUMENT). Impairment: **LEGAL EFFECT UNKNOWN**. |
| 20 | RECEIPTS | `[REVENUE EFFECT UNKNOWN]` statewide bond-levy total not isolated |
| 21–26 | H.R. 25 / DISPOSITION | OUTSIDE consumption event; 00E POTENTIAL CONFLICT / EVIDENCE REQUIRED; **BLANK** |
| 27–30 | LOCATORS | SRC-BILL-A-089 / TRACED (10-113) |
| 31–32 | NOTES | Do not conclude what Bill A must do about outstanding bonds. |

### KRU-D02-006 — County ad valorem levies

| # | Field | Value |
|---|---|---|
| 1–4 | ID / NAME | KRU-D02-006 / County tangible-property levies certified under K.S.A. 79-1801 |
| 5–8 | LEVEL / TYPE / COMPULSORY | county / ad valorem / YES |
| 9 | AUTHORITY | 79-1801 (architecture); individual county levy statutes not exhaustively fetched |
| 10–14 | TRIGGER / RATE | County budget + October 1 certification / **VARIABLE BY COUNTY** |
| 16–17 | DESTINATION | County funds as budgeted |
| 19 | DEPENDENCIES | County GO debt: **POTENTIAL DEPENDENCY** via 10-113 |
| 20 | RECEIPTS | KLRD Tax Facts Table 5 FY2024 Counties **$1,787,504 thousand** (tangible property levied) |
| 21–26 | H.R. 25 / DISPOSITION | OUTSIDE consumption event / **BLANK** |
| 27–30 | LOCATORS | SRC-BILL-A-088, 100, 104 / TRACED as a class |
| 31–32 | NOTES | AUTHORITY VERIFIED; LOCAL IMPLEMENTATION VARIABLE. Not every county mill listed. |

### KRU-D02-007 — City ad valorem levies

Same architecture as KRU-D02-006 at **city** level. FY2024 cities tangible property **$1,203,901 thousand** (Tax Facts Table 5). Disposition **BLANK**.

### KRU-D02-008 — Township ad valorem levies

Same architecture at **township** level. FY2024 townships **$103,201 thousand**. Disposition **BLANK**.

### KRU-D02-009 — Other taxing-subdivision ad valorem levies

| # | Field | Value |
|---|---|---|
| 1–4 | ID / NAME | KRU-D02-009 / Other taxing subdivisions certifying under 79-1801 (community college, fire, library, recreation, cemetery, watershed, extension, and similar **where levied**) |
| 5–8 | LEVEL / COMPULSORY | local special-purpose / YES where levied |
| 9 | AUTHORITY | 79-1801 as class architecture; organic levy statutes `[CITATION/TEXT NEEDED]` per type |
| 10–14 | TRIGGER / RATE | Entity levy on taxable property in the district / **VARIABLE** |
| 20 | RECEIPTS | Tax Facts Table 5 special districts FY2024 **$485,377 thousand**. Community colleges sit inside Tax Facts **Schools** exhibit (alias — CF-D02-003). |
| 21–26 | H.R. 25 / DISPOSITION | OUTSIDE consumption event / **BLANK** |
| 27–32 | NOTES | Structural completeness objective: **types** of government that can compel property-based payment — not every bill. AUTHORITY VERIFIED as a class; LOCAL IMPLEMENTATION VARIABLE. |

### KRU-D02-010 — State educational-building mill (tax year 2025)

| # | Field | Value |
|---|---|---|
| 1–4 | ID / NAME | KRU-D02-010 / State tax of 1 mill upon all tangible property subject to ad valorem taxation **in the year 2025** (K.S.A. 76-6b01) |
| 5–8 | LEVEL / COMPULSORY | state / YES for year 2025 |
| 9 | AUTHORITY | K.S.A. 76-6b01 (L. 2025, ch. 71, § 1; July 1); destination 76-6b02 |
| 10–14 | TRIGGER / RATE | Statewide mill on taxable tangible property / **1 mill in year 2025** |
| 15–17 | PURPOSE / FUND | Kansas educational building fund — construction/repair at Board of Regents institutions; 76-6b02 also authorizes use for revenue-bond debt service (not a pledge of state faith/credit) |
| 19 | DEPENDENCIES | 76-6b02: **POTENTIAL DEPENDENCY** on EBF for specified revenue bonds. 76-6b02(c): beginning July 1, 2026, **SGF transfer** ($56,000,000 then formula) — that transfer is **not** itself a Domain 02 mill. |
| 20 | RECEIPTS | Tax Facts Table 3 FY2024 Educational Bldg. **$48,564 thousand** (prior-year mill architecture; do not treat as 2026 mill proof) |
| 21–26 | H.R. 25 / DISPOSITION | OUTSIDE consumption event / **BLANK** |
| 23 | CURRENT-STATE STATUS | **CURRENT** as a tax-year **2025** mill. **NOT CURRENT** as a tax-year **2026** mill. L. 2025, ch. 71 / SB 35 discontinued the statewide mill beginning TY 2026. July 1, 2026 SGF transfer **REFERRED TO DOMAIN 09**. Row **preserved**; not deleted. Status change is **not** a Human DISAPPEAR. |
| 27–30 | LOCATORS | SRC-BILL-A-090, 091, 100, 121, 122 / TRACED for **year 2025**; TY 2026 mill **NOT CURRENT** |
| 31–32 | CONFLICTS | CF-D02-004 **RESOLVED — CURRENT LAW VERIFIED**. Do not carry the 2025 mill into 2026. |

### KRU-D02-011 — State institutions-building mill (tax year 2025)

| # | Field | Value |
|---|---|---|
| 1–4 | ID / NAME | KRU-D02-011 / State tax of 0.5 mill **in the year 2025** (K.S.A. 76-6b04) |
| 5–8 | LEVEL / COMPULSORY | state / YES for year 2025 |
| 9 | AUTHORITY | K.S.A. 76-6b04 (L. 2025, ch. 71, § 3; July 1) |
| 10–14 | TRIGGER / RATE | Statewide mill / **0.5 mill in year 2025** |
| 15–17 | PURPOSE / FUND | State institutions building fund (institutions caring for specified persons/children; vocational rehabilitation) |
| 20 | RECEIPTS | Tax Facts Table 3 FY2024 Institutional Bldg. **$24,282 thousand** |
| 21–26 | DISPOSITION | **BLANK** / **NOT DETERMINED** |
| 23 | CURRENT-STATE STATUS | **CURRENT** as a tax-year **2025** mill. **NOT CURRENT** as a tax-year **2026** mill. L. 2025, ch. 71 / SB 35 discontinued the statewide mill beginning TY 2026. July 1, 2026 SGF transfer (76-6b05(e) $25,000,000 then +2% of $25,000,000) **REFERRED TO DOMAIN 09**. Row **preserved**; not deleted. Status change is **not** a Human DISAPPEAR. |
| 27–32 | VERIFY | SRC-BILL-A-092, 121, 122 / TRACED for year 2025; TY 2026 mill **NOT CURRENT** (CF-D02-004 **RESOLVED — CURRENT LAW VERIFIED**) |

### KRU-D02-012 — Motor-vehicle tax (in lieu)

| # | Field | Value |
|---|---|---|
| 1 | MASTER RECORD ID | KRU-D02-012 |
| 2 | EVIDENCE DOMAIN | 02 |
| 3 | AUTHORITATIVE NAME | Tax levied upon every motor vehicle defined in K.S.A. 79-5101 in lieu of general personal-property / other ad valorem taxes (K.S.A. 79-5105 / 79-5101 architecture) |
| 4 | COMMON / ALTERNATE NAME | Motor vehicle tax; personal-property tax on vehicles |
| 5–6 | LEVEL / ENTITY | Local tax-levy unit + state share of receipts (79-5109) |
| 7–8 | TYPE / COMPULSORY | In-lieu property-based vehicle tax / YES |
| 9 | AUTHORITY | K.S.A. 79-5101; 79-5105; 79-5109 |
| 10 | TRIGGER | Tax due at registration; situs in the tax-levy unit. Still a **property** claim (class/age/value × county average rate), not a FairTax consumption event. Distinct from Domain 01 fuel excise and KRU-D01-011 rental excise. |
| 11 | OBLIGOR | Vehicle owner / registrant |
| 12 | NONPAYMENT | Payment is a condition of registration (79-5105 architecture) |
| 13 | ECONOMIC FUNCTION | In-lieu of general personal-property tax on defined motor vehicles |
| 14 | RATE / CALCULATION | Class midpoint; 15%/year reduction; **20%** taxable value (calendar years after 1999) × **county average tax rate computed without school-district general property taxes**; minima $24/$12 (or $12/$6 for 1980 or earlier) (79-5105) |
| 15–17 | PURPOSE / DESTINATION | Allocated to tax-levy unit; distributed among state and taxing subdivisions (79-5109 / 79-5111). State share: 2/3 Educational Building Fund / 1/3 State Institutions Building Fund (2004 SGF split was time-limited). |
| 18 | ADMIN | County treasurer at registration |
| 19 | DEPENDENCIES | Distribution into EBF/SIBF: **POTENTIAL DEPENDENCY** |
| 20 | RECEIPTS | KLRD Table 1 FY2024 Various Vehicle **$477,762 thousand** is **aggregated** (motor vehicle + RV + 16M/20M + rental excise + local CMV fees). Do not disaggregate. |
| 21 | H.R. 25 | STRUCTURALLY OUTSIDE H.R. 25 CONSUMPTION EVENT; POTENTIAL CONFLICT WITH BILL A HUMAN INTENT |
| 22 | AGCL | 00C POTENTIAL CONFLICT surface. Never SATISFIED. |
| 23–26 | STATUS / KLRS / DISPOSITION / POST | Current in-lieu tax / CANDIDATE COMPULSORY CLAIM / **BLANK** / **NOT DETERMINED** |
| 27–30 | LOCATORS | SRC-BILL-A-094–096 / TRACED |
| 31–32 | NOTES | 79-5101 excludes GVW >12,000 lb from this **act** (registration-time collection). The 12,001–20,000 lb band is **KRU-D02-016** (79-5105a): same computation, arrears payment. CMV fee 8-143m **REFERRED TO DOMAIN 05**. |

### KRU-D02-013 — Recreational-vehicle tax (in lieu)

| # | Field | Value |
|---|---|---|
| 1–4 | ID / NAME | KRU-D02-013 / RV tax under K.S.A. 79-5118 to 79-5125; not subject to other property/ad valorem taxes (79-5119) |
| 5–8 | LEVEL / COMPULSORY | local (county treasurer at registration) / YES |
| 9 | AUTHORITY | 79-5118; 79-5119; 79-5120; Kan. Const. art. 11, § 1 (legislature may classify/tax RVs as a class or exempt and tax in lieu) |
| 10–14 | TRIGGER / RATE | Annual registration-year tax: (1) $70 + $.90/cwt model ≤5 years; (2) $50 + $.70/cwt 6–10 years; (3) $30 + $.50/cwt 11+ years; 1981 or earlier = $30 (79-5120) |
| 16 | DESTINATION | `[TO BE VERIFIED]` full distribution statute beyond 79-5119 due-date/exemption text |
| 20 | RECEIPTS | Inside aggregated Various Vehicle line |
| 21–26 | H.R. 25 / DISPOSITION | OUTSIDE consumption event / **BLANK** |
| 27–30 | LOCATORS | SRC-BILL-A-097, 098 / TRACED (imposition); destination PARTIAL |
| 31–32 | NOTES | Constitution permits class or in-lieu. Not a consumption tax. |

### KRU-D02-014 — Public-utility state-appraised property

| # | Field | Value |
|---|---|---|
| 1–4 | ID / NAME | KRU-D02-014 / Director of property valuation annually determines FMV of public-utility real and personal property (K.S.A. 79-5a04); “public utility” defined 79-5a01 |
| 5–8 | LEVEL / COMPULSORY | state appraisal / local+state mills / YES |
| 9 | AUTHORITY | 79-5a01; 79-5a04; assessment 79-1439 (generally 33%; railroad at commercial average) |
| 10–14 | TRIGGER / RATE | Public-utility property as of January 1 unit value allocated to Kansas / same mill stack as KRU-D02-001 on assessed value |
| 13 | ECONOMIC FUNCTION | Distinct **valuation authority** (PVD unit appraisal), not a separate mill tax. Do not double-count mills with KRU-D02-001. |
| 20 | RECEIPTS | Included in general property totals; not isolated in Tax Facts Table 5 |
| 21–26 | DISPOSITION | **BLANK** |
| 27–30 | LOCATORS | SRC-BILL-A-081, 099 / TRACED as valuation pathway |
| 31–32 | NOTES | This is a subclass/appraisal pathway of the general ad valorem tax. |

### KRU-D02-015 — Mineral-leasehold personal-property ad valorem

| # | Field | Value |
|---|---|---|
| 1–4 | ID / NAME | KRU-D02-015 / Mineral leasehold interests assessed as tangible personal property (Art. 11 §1 Class 2 subclass 2; 79-1439(b)(2)) |
| 5–8 | LEVEL / COMPULSORY | local mills on assessed mineral leaseholds / YES |
| 9 | AUTHORITY | Kan. Const. art. 11, § 1; K.S.A. 79-1439(b)(2) — 30% (oil/gas wells with prior-year production ≤5 barrels oil / 100 mcf gas / day assessed at 25%) |
| 10–14 | TRIGGER / RATE | Taxable mineral leasehold on the personal-property roll / assessed % × local mills |
| 13 | ECONOMIC FUNCTION | **Property-tax** on the leasehold. Distinct from Domain 01 mineral **severance** tax (KRU-D01-010 / 79-4217). Do not double-count. |
| 20 | RECEIPTS | Inside general property; not isolated |
| 21–26 | DISPOSITION | **BLANK** |
| 27–32 | LOCATORS | SRC-BILL-A-075, 081 / TRACED. Do not alter Domain 01 findings. |

### KRU-D02-016 — 16M/20M personal-property tax (GVW 12,001–20,000 lb)

| # | Field | Value |
|---|---|---|
| 1 | MASTER RECORD ID | KRU-D02-016 |
| 2 | EVIDENCE DOMAIN | 02 |
| 3 | AUTHORITATIVE NAME | For tax year 1998 and each year thereafter, personal property tax on motor vehicles with GVW more than 12,000 pounds but less than 20,001 pounds shall be computed in accordance with K.S.A. 79-5101 et seq. but paid at the time required by K.S.A. 79-2004a (K.S.A. 79-5105a) |
| 4 | COMMON / ALTERNATE NAME | 16M/20M; 12K–20K GVW personal-property tax; tagged-vehicle arrears tax |
| 5–6 | LEVEL / ENTITY | County personal-property roll / county treasurer (79-2004a installment dates) |
| 7–8 | TYPE / COMPULSORY | Personal-property tax computed under the motor-vehicle tax formula / YES |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 79-5105a (L. 1997, ch. 187, § 5; L. 1998, ch. 140, § 3; Jan. 1, 1999). Payment timing: 79-2004a. Computation: 79-5101 et seq. |
| 10 | TRIGGER | Taxable motor vehicle in the 12,001–20,000 lb GVW band on the personal-property architecture; **not** registration-time collection. Official PVD 2026 Personal Property Summary: formula-driven value; **20%** assessment; taxes paid in arrears. |
| 11 | OBLIGOR | Owner / person charged on the personal-property roll |
| 12 | NONPAYMENT | Personal-property installment / interest architecture under 79-2004a (interest **REFERRED TO DOMAIN 07** as a collection incident) |
| 13 | ECONOMIC FUNCTION | Distinct compulsory property claim: 79-5101(c) excludes >12,000 lb from the motor-vehicle tax **act**; 79-5105a re-applies the 79-5101 computation to this weight band with arrears payment. Distinct from KRU-D02-012 (registration-time MV tax) and from tax-roll vehicles ≥24,000 lb / non-highway FMV **30%** (79-1439 / 79-306d). Not the 8-143m CMV fee (Domain 05). |
| 14 | RATE / CALCULATION | Computed under 79-5101 et seq. (class/age formula; 20% taxable value after 1999 × county average rate without school-district general taxes, as applicable to that computation). Paid Dec. 20 / May 10 under 79-2004a. |
| 15–17 | PURPOSE / DESTINATION | Personal-property tax to the county / taxing subdivisions under the personal-property collection architecture; not isolated in Tax Facts (inside **Various Vehicle** aggregate — CF-D02-005) |
| 18 | ADMIN | County appraiser / county treasurer; PVD 2026 Personal Property Summary |
| 19 | DEPENDENCIES | `[TO BE VERIFIED]` beyond ordinary personal-property collection |
| 20 | RECEIPTS | Inside aggregated KLRD Various Vehicle; **no official isolated statewide dollar** retrieved |
| 21 | H.R. 25 | STRUCTURALLY OUTSIDE H.R. 25 CONSUMPTION EVENT; POTENTIAL CONFLICT WITH BILL A HUMAN INTENT |
| 22 | AGCL | 00C POTENTIAL CONFLICT surface. Never SATISFIED. |
| 23–26 | STATUS / KLRS / DISPOSITION / POST | CURRENT / CANDIDATE COMPULSORY CLAIM / **BLANK** / **NOT DETERMINED** |
| 27–30 | LOCATORS | SRC-BILL-A-094, 095, 115, 116, 126 / TRACED |
| 31–32 | NOTES | CWC-CE-130 listed 16M/20M as UNK-D02-005 with no verified row. CWC-CE-131 fetched 79-5105a and added this row. County appraiser guides assisted discovery only. Disposition **BLANK**. |

---

## 3. Referrals (not Domain 02 counted rows)

| Item | Classification | Authority |
|---|---|---|
| Municipal improvement-district special assessments | **REFERRED TO DOMAIN 06** | K.S.A. 12-6a01 et seq. — benefit/improvement district, not general ownership/value |
| Real-property tax interest | **REFERRED TO DOMAIN 07** | K.S.A. 79-2004 (interest to county general fund except city special-assessment interest agreement) |
| Commercial vehicle fee | **REFERRED TO DOMAIN 05** | K.S.A. 8-143m — fee in lieu of CMV ad valorem; Kansas-based amounts distributed like motor-vehicle tax |
| Chapter 8 registration fees | **REFERRED TO DOMAIN 05** | Distinct from 79-5105 motor-vehicle tax |
| Vehicle rental excise | Already KRU-D01-011 | Do not add to Domain 02 |
| Mineral severance | Already KRU-D01-010 | Distinct from KRU-D02-015 |
| Watercraft property tax | **Not a current claim** on and after Jan. 1, 2026 | K.S.A. 79-5501(e) (L. 2025, ch. 123, § 12) |
| Local-option intangibles tax (gross earnings from money/notes/evidence of debt) | **REFERRED TO DOMAIN 03** | K.S.A. 12-1,101. Not classified ad valorem on tangible property (Art. 11 carves those instruments out). Domain 03 **not executed**. |
| Aircraft | **NOT A DISTINCT CLAIM** | Exemptions 79-201k / 79-220. Residual non-exempt aircraft remain inside KRU-D02-001. |
| 76-6b02(c) / 76-6b05(e) SGF transfers | **REFERRED TO DOMAIN 09** | Financing/transfer beginning July 1, 2026; not a TY 2026 Domain 02 mill. Domain 09 **not executed**. |

---

## 4. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-09-02 | CWC-CE-130 Domain 02 execution instance. 15 claim-category rows. Dispositions BLANK. Schema authority remains WD-BILL-A-019. |
| 0.2.0 | 2026-09-02 | CWC-CE-131 closure: added KRU-D02-016; KRU-D02-010/011 TY 2026 mill NOT CURRENT. Count **16**. Dispositions BLANK. |
