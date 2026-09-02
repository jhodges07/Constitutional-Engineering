# WD-BILL-A-049 — Domain 04 Master Register Execution Instance

**Document ID:** WD-BILL-A-049  
**Title:** Kansas Government Revenue Universe / KLRS Master Register — Domain 04 Execution Instance  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-136; CWC-CE-137 (closure)  
**Schema authority:** WD-BILL-A-019 (this file does **not** replace the schema lock)  
**Governing LOU candidate:** LOU-004 Draft 1.5 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / DOMAIN 04 ROWS POPULATED FROM EVIDENCE — CLOSURE APPLIED — REGISTER **NOT** STATEWIDE COMPLETE — NOT ACCEPTED  
**Version:** 0.2.0  
**Effective Date:** 2026-09-02  
**Retrieval date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-049-Domain-04-Master-Register-Execution.md  

```text
EXECUTION INSTANCE OF WD-BILL-A-019 SCHEMA
DOMAIN 04 ONLY
HUMAN DISPOSITION = BLANK ON EVERY ROW
BLANK ≠ RETAIN
STRUCTURAL MATCH ≠ RETAIN
MATERIAL STRUCTURAL DIFFERENCE ≠ DISAPPEAR
CURRENT EXISTENCE ≠ POST-BILL-A AUTHORITY
CURRENT RECEIPTS ≠ REQUIRED REPLACEMENT REVENUE
RETAILER / MARKETPLACE / REMOTE-SELLER COLLECTION ≠ A SECOND TAX
KLRS CANDIDACY ≠ FINAL AUTHORIZATION
STATEWIDE UNIVERSE NOT CERTIFIED
CURRENT KANSAS SALES / USE TAX ≠ H.R. 25 FAIRTAX
NO FAIRTAX RATE CALCULATION
NO FUTURE DISTRIBUTION DESIGN
```

Narrative audit: WD-BILL-A-048. Sources: WD-BILL-A-050. Completeness: WD-BILL-A-051. Conflicts: WD-BILL-A-052. H.R. 25 crosswalk: WD-BILL-A-053.

Domain 01 rows remain in WD-BILL-A-022. Domain 02 rows remain in WD-BILL-A-031. Domain 03 rows remain in WD-BILL-A-040. They are **not** rewritten here.

Common field values unless a row overrides:

- Field 2 EVIDENCE DOMAIN = 04
- Field 25 HUMAN BILL A DISPOSITION = **BLANK**
- Field 26 POST-BILL-A AUTHORITY STATUS = **NOT DETERMINED**
- Retrieval date = 2026-09-02

Remote-seller nexus, marketplace-facilitator remittance, retailer collection, refunds, exemption certificates, and food 0% rate treatment are **MECHANISMS / RATE SCHEDULES** and are **not** extra rows.

---

## 1. Index of Domain 04 rows

| Master Record ID | Authoritative name | Compulsory | Verification | Disposition |
|---|---|---|---|---|
| KRU-D04-001 | Kansas retailers' sales tax (K.S.A. 79-3603) | YES | TRACED (architecture) | BLANK |
| KRU-D04-002 | Kansas compensating use tax (K.S.A. 79-3703) | YES | TRACED (architecture) | BLANK |
| KRU-D04-003 | City and county retailers' sales tax (K.S.A. 12-187 / 12-189) | YES **where locally imposed** | TRACED (enabling + rate architecture); LOCAL IMPLEMENTATION VARIABLE | BLANK |
| KRU-D04-004 | City, county, and municipal-university compensating use tax (K.S.A. 12-198) | YES **where local sales tax is imposed** | TRACED (automatic counterpart) | BLANK |
| KRU-D04-005 | Special-purpose district local sales/use overlays (CID / TDD / STAR class) | YES **where levied** | TRACED (enabling architecture: 12-6a31 / 12-17,145 / 12-17,169); per-district inventory not performed | BLANK |

Counted Domain 04 verified **claim-category** records: **5**.  
Count follows evidence. Human dispositions: **ALL BLANK**.

Food 0% (79-3603d), SHF 18% of rate, redevelopment 2% overlay, remote sellers, marketplace facilitators, and 12-199 vehicle local-rate catch-up are **not** additional counted rows.

---

## 2. Thirty-two-field records

### KRU-D04-001 — State retailers' sales tax

| # | Field | Value |
|---|---|---|
| 1 | MASTER RECORD ID | KRU-D04-001 |
| 2 | EVIDENCE DOMAIN | 04 |
| 3 | AUTHORITATIVE NAME | For the privilege of selling tangible personal property at retail in this state or rendering or furnishing services taxable under the Kansas retailers' sales tax act, there is hereby levied and there shall be collected and paid a tax (K.S.A. 79-3603) |
| 4 | COMMON / ALTERNATE NAME | Kansas retailers' sales tax; state sales tax; RST |
| 5 | GOVERNMENT LEVEL | state |
| 6 | GOVERNMENT ENTITY / ENTITY CLASS | State of Kansas; administered by Kansas Department of Revenue; remitted to State Treasurer |
| 7 | RECEIPT OR CLAIM TYPE | Retailers' sales tax on TPP at retail and enumerated services |
| 8 | COMPULSORY STATUS | YES |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 79-3601 et seq.; 79-3602 (definitions); 79-3603 (imposition/rate/enumerated bases); 79-3603d (food rate); 79-3606 (exemptions); 79-3670 (sourcing). Statutory, not a located constitutional sales-tax mandate. |
| 10 | PAYMENT / REVENUE TRIGGER | Retail sale of TPP or furnishing of a service enumerated in 79-3603(a)–(x), measured by sales price, after exclusions/exemptions |
| 11 | LEGALLY OBLIGATED PARTY | Privilege tax on the **retailer**. Purchaser generally pays as added tax. Economic incidence **NOT ESTABLISHED**. Ultimate economic source (Human intent, crosswalk only): people with money. Retailer remittance ≠ second claim. |
| 12 | CONSEQUENCE OF NONPAYMENT | Kansas retailers' sales tax act remedies (including 79-3615). Penalties/interest **REFERRED TO DOMAIN 07**. Criminal misuse of PEC materials: 79-3606(d)/(e) misdemeanor — **not drafted here**. |
| 13 | ECONOMIC FUNCTION | Compulsory claim on **in-state retail consumption / enumerated services**, not on income, ownership, or a general business-purpose-exempt final-consumption base. Used retailer goods generally included. |
| 14 | RATE / CALCULATION / AMOUNT METHOD | **6.5%** of sales price, except food/food ingredients **0% commencing January 1, 2025** (79-3603d). On/after Jan. 1, 2025, **18% of the tax rate** levied for State Highway Fund. Additional **2%** in designated redevelopment districts (74-8921) until bonds paid / first-series maturity — overlay, not a second counted claim. Combined local rates added under KRU-D04-003/005. |
| 15 | STATED PURPOSE | Statutory privilege of selling TPP at retail or furnishing taxable services |
| 16 | REVENUE DESTINATION | State General Fund (remainder of rate) and State Highway Fund (**18% of the rate** from Jan. 1, 2025). Redevelopment overlay to pledged bond funds where applicable. |
| 17 | FUND / POOL TYPE | SGF (general); SHF (dedicated transportation); special redevelopment where applicable |
| 18 | ADMINISTRATIVE / OVERHEAD TREATMENT | KDOR administration; retailer collection; remote-seller collection when 79-3702(h)(1)(G) nexus met; marketplace facilitator collection under 79-5602/5603 — **mechanisms, not extra claims**. Streamlined Sales Tax registration optional path. |
| 19 | DEBT / BOND / CONTRACT / FEDERAL-MATCH / OTHER DEPENDENCIES | SHF share: **DEPENDENCY VERIFIED** (destination). Redevelopment 2%: **POTENTIAL DEPENDENCY**. Impairment if this claim disappeared: **LEGAL EFFECT UNKNOWN**. Dependency ≠ RETAIN. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Tax Facts 2025 Supplement FY2025 Retail Sales levied **$3,191,983 thousand** (SGF **$2,581,699**; Other Funds **$610,284**). DoA June FY2025 SGF final Retail Sales **$2,581,698,730**. Levy ≠ SGF receipts. Local distributions **not** included. **CURRENT RECEIPTS ≠ REQUIRED REPLACEMENT REVENUE.** |
| 21 | H.R. 25 KANSAS-MIRROR RELATIONSHIP | **PARTIAL STRUCTURAL MATCH** on a retail consumption event; **MATERIAL STRUCTURAL DIFFERENCE** on used property, enumerated-only services, business-input patchwork, food 0% state rate, construction materials, and mixed-use. H.R. 25 is **not Kansas law**. Federal administrative machinery is **FEDERAL-SPECIFIC**. STRUCTURAL MATCH ≠ RETAIN. |
| 22 | AGCL 00A–00J CLASSIFICATION | 00A QUESTION REQUIRED (signals exist; not self-certified); 00C POTENTIAL CONFLICT surface vs intended new-final-consumption event **and** PROVISIONAL ALIGNMENT surface (consumption event exists); 00H QUESTION REQUIRED / PROVISIONAL ALIGNMENT (statutory authority ≠ retention). **Never SATISFIED.** |
| 23 | CURRENT-STATE STATUS | Evidenced current Kansas retailers' sales-tax architecture. **Not** future authorization. **Not** designated as the Bill A replacement tax. |
| 24 | KLRS CANDIDACY | CANDIDATE COMPULSORY CLAIM. Not final authorization. |
| 25 | HUMAN BILL A DISPOSITION | **BLANK** |
| 26 | POST-BILL-A AUTHORITY STATUS | **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-183–188, 191 |
| 28 | GOV-DATA LOCATORS | SRC-BILL-A-200–208 |
| 29 | SOURCE DATE / VERSION | 79-3603 / 79-3603d / 79-3602 / 79-3606 2025 K.S.A. PDFs retrieved 2026-09-02; Tax Facts 2025 Supplement; DoA June FY2025 SGF final |
| 30 | VERIFICATION STATUS | TRACED (architecture). Exhaustive 79-3606 catalog and every taxable service not inventoried. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D04-001; UNK-D04-002; UNK-D04-003 |
| 32 | NOTES / TRACEABILITY | Enumerated services, software, rentals, food 0%, and SHF 18% are **bases/rate/destination of this Act**, not extra rows. Do not add marketplace or remote-seller receipts as a second line. |

### KRU-D04-002 — State compensating use tax

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D04-002 / 04 |
| 3 | AUTHORITATIVE NAME | A tax is hereby levied and there shall be collected from every person in this state a tax or excise for the privilege of using, storing, or consuming within this state any article of tangible personal property (K.S.A. 79-3703) |
| 4 | COMMON / ALTERNATE NAME | Kansas compensating use tax; consumers' compensating use; retailers' compensating use |
| 5–6 | LEVEL / ENTITY | State / State of Kansas; KDOR; State Treasurer |
| 7–8 | TYPE / COMPULSORY | Compensating use tax on TPP used/stored/consumed in Kansas / YES |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 79-3701 et seq.; 79-3702 (definitions, including retailer doing business / $100,000 economic nexus); 79-3703 (imposition). Enforcement/collection of RST provisions apply insofar as practicable (79-3702(b)). |
| 10 | PAYMENT / REVENUE TRIGGER | Use, storage, or consumption of TPP in Kansas where sales tax was not otherwise paid or credited; 79-3703(e) — subsequent Kansas use if the same property/transaction would have been subject to RST if wholly in Kansas |
| 11 | LEGALLY OBLIGATED PARTY | Person using/storing/consuming. Collection may be by in-nexus seller or marketplace facilitator, or purchaser remittance (consumers' use). Collection ≠ second claim. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | Compensating-tax remedies via RST enforcement incorporation. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Complementary consumption claim closing the RST gap on out-of-state / untaxed acquisitions of TPP used in Kansas. **Distinct legal claim** from KRU-D04-001. |
| 14 | RATE / CALCULATION | **6.5%** of consideration paid; food follows 79-3603d (**0%** state from 2025-01-01). **18% of the rate** to SHF from Jan. 1, 2025. Redevelopment 2% overlay as in 79-3703. KDOR: **labor services are not subject to use tax**. |
| 15 | STATED PURPOSE | Privilege of using, storing, or consuming TPP in Kansas |
| 16–17 | DESTINATION / FUND | SGF + SHF share of rate (same architecture as KRU-D04-001) |
| 18 | ADMINISTRATIVE | Retailers' compensating use (seller collection) and consumers' compensating use (purchaser remittance) are **collection variants**, not extra rows. Remote-seller duty under 79-3702(h)(1)(G). |
| 19 | DEPENDENCIES | SHF share **DEPENDENCY VERIFIED**. Impairment **LEGAL EFFECT UNKNOWN**. Do not double-count with KRU-D04-001 receipts. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Tax Facts 2025 Supplement FY2025 Compensating Use levied **$1,088,011 thousand** (SGF **$893,761**; Other Funds **$194,250**). DoA June FY2025 SGF final **$893,761,380**. **CURRENT RECEIPTS ≠ REQUIRED REPLACEMENT REVENUE.** |
| 21 | H.R. 25 KANSAS-MIRROR RELATIONSHIP | **KANSAS-SPECIFIC** complementary use-tax architecture. H.R. 25 taxes a federal final-consumption event, not a state compensating-use overlay. **MATERIAL STRUCTURAL DIFFERENCE** in legal form; complementary **economic** function vs RST is Kansas-specific. Not Kansas law. |
| 22 | AGCL 00A–00J CLASSIFICATION | 00A QUESTION REQUIRED; 00C POTENTIAL CONFLICT / PROVISIONAL ALIGNMENT surfaces as with KRU-D04-001 (consumption vs intended new-final-consumption standard). **Never SATISFIED.** |
| 23 | CURRENT-STATE STATUS | Evidenced current compensating-use architecture. Not future authorization. |
| 24 | KLRS CANDIDACY | CANDIDATE COMPULSORY CLAIM. Not final authorization. |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-189–190, 192 |
| 28 | GOV-DATA LOCATORS | SRC-BILL-A-200–204, 209 |
| 29 | SOURCE DATE / VERSION | 79-3703 / 79-3702 2025 PDFs retrieved 2026-09-02; Tax Facts 2025 Supplement; KDOR compensating-use page |
| 30 | VERIFICATION STATUS | TRACED (architecture). Conversion/mixed-use completeness UNK-D04-003. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D04-001; UNK-D04-003 |
| 32 | NOTES / TRACEABILITY | Do not add retailers' use and consumers' use as two claims. Do not add use-tax dollars to sales-tax dollars for the same transaction. |

### KRU-D04-003 — Local retailers' sales tax

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D04-003 / 04 |
| 3 | AUTHORITATIVE NAME | Countywide and city retailers' sales taxes (K.S.A. 12-187); rates, general and special purposes (K.S.A. 12-189) |
| 4 | COMMON / ALTERNATE NAME | Local sales tax; city/county retailers' sales tax |
| 5–6 | LEVEL / ENTITY | local (city/county) with **state administration** / imposing city or county; KDOR collects; State Treasurer remits |
| 7–8 | TYPE / COMPULSORY | Local-option retailers' sales tax identical in application/exemptions to the state RST act (12-189) / YES **where imposed after required election** |
| 9 | CURRENT LEGAL AUTHORITY | 12-187 (election required); 12-189 (rate caps, KDOR administration, identity with RST act **except 12-189a**); **12-189a** (state-exempt sales that remain locally taxable, including food); 12-191 (situs/sourcing); 12-192 (countywide apportionment). **SB 33: RESOLVED — NOT ENACTED / NOT CURRENT LAW** (CWC-CE-137). |
| 10 | PAYMENT / REVENUE TRIGGER | Same retail transactions subject to Kansas RST, sourced under 79-3670 / 12-191, in a jurisdiction that has imposed the tax |
| 11 | LEGALLY OBLIGATED PARTY | Same retailer/collection architecture as KRU-D04-001. Local government may not collect locally (12-189). Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | State RST enforcement applied insofar as made applicable. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Local consumption-tax claim on the **same RST base**, at locally chosen rates within statutory caps. **State enabling ≠ local imposition.** |
| 14 | RATE / CALCULATION | City: 0.05% increments, **≤2% general + ≤1% special**; special city taxes expire after **10 years**. County: **≤1%** in 0.25% increments **except** numerous county-specific authorizations in 12-189(a)–(pp). **LOCAL IMPLEMENTATION VARIABLE.** Official current rates: KDOR Pub. KS-1700 / locator — not transcribed. Food: **local rates remain** (Notice 24-21). |
| 15 | STATED PURPOSE | General or specified special purposes in the ordinance/resolution/ballot; city special purpose must be specified |
| 16–17 | DESTINATION / FUND | County and city retailers' sales tax fund, then remitted at least quarterly to city/county treasurers (Wilson County capital-improvements exception; redevelopment bond-fund exception). Countywide split per 12-192. |
| 18 | ADMINISTRATIVE | KDOR only. Local tax identical in application/exemptions to RST act except 12-189a. |
| 19 | DEPENDENCIES | **DEPENDENCY VERIFIED** — local governments receive these receipts by statute. Bond pledges: **POTENTIAL DEPENDENCY** where ordinance pledges revenue; impairment **LEGAL EFFECT UNKNOWN**. Dependency ≠ RETAIN. **No future distribution formula designed.** |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | State-collected local tax. **Do not add to SGF.** Tax Facts 2025 Supplement Table 5 Exhibit **Local Sales and Use FY2025 $1,731,014 thousand** (Counties $876,062k; Cities $763,613k; footnote 5 $91,339k). Isolated sales-only vs use-only split: **EVIDENCE REQUIRED**. **CURRENT RECEIPTS ≠ REQUIRED REPLACEMENT REVENUE.** |
| 21 | H.R. 25 KANSAS-MIRROR RELATIONSHIP | **KANSAS-SPECIFIC** local-option overlay on RST. H.R. 25 federal model is not a Kansas local sales-tax statute. Destination sourcing is administratively similar to a destination combined rate but **similarity ≠ equivalence**. |
| 22 | AGCL 00A–00J CLASSIFICATION | 00A QUESTION REQUIRED (election is a local signal; not self-certified); 00H QUESTION REQUIRED (statutory enabling ≠ retention). **Never SATISFIED.** |
| 23 | CURRENT-STATE STATUS | Evidenced enabling + variable local imposition. Not future authorization. |
| 24 | KLRS CANDIDACY | CANDIDATE COMPULSORY CLAIM **where levied**. Not final authorization. |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-193–196; SRC-BILL-A-221 (12-189a) |
| 28 | GOV-DATA LOCATORS | SRC-BILL-A-205–208, 210 |
| 29 | SOURCE DATE / VERSION | 12-187 / 12-189 2025 PDFs retrieved 2026-09-02 (12-189 history through L. 2025, ch. 126, May 8) |
| 30 | VERIFICATION STATUS | TRACED (enabling/rate architecture). Every jurisdiction **not** inventoried. |
| 31 | CONFLICT / UNKNOWN IDS | UNK-D04-001 (resolved not enacted); UNK-D04-004 (combined local Exhibit resolved); CF-D04-002 |
| 32 | NOTES / TRACEABILITY | Do not create a row per city or county. Do not treat food local tax as a separate claim. **12-189a(d)** is why local food tax remains after state 0%. |

### KRU-D04-004 — Local compensating use tax

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D04-004 / 04 |
| 3 | AUTHORITATIVE NAME | A compensating use tax for the privilege of using or storing within a city or county any tangible personal property or any vehicle required to be registered … or any vessel … is hereby imposed by every city, county or municipal university imposing a retailers' sales tax (K.S.A. 12-198) |
| 4 | COMMON / ALTERNATE NAME | Local compensating use tax; local use tax |
| 5–6 | LEVEL / ENTITY | local with state administration / imposing city, county, or municipal university; KDOR collects |
| 7–8 | TYPE / COMPULSORY | Local compensating use tax at the **same rate** as the jurisdiction's retailers' sales tax / YES **automatically where local RST is imposed** |
| 9 | CURRENT LEGAL AUTHORITY | 12-198; 12-199 (in-state registered-vehicle local-rate differential collected by county treasurer at registration — **mechanism**, not extra row); identical in application/exemptions to Kansas compensating tax |
| 10 | PAYMENT / REVENUE TRIGGER | Use/storage of TPP (or specified vehicles/vessels) within a local RST jurisdiction, complementary to local RST, on the state compensating-tax pattern |
| 11 | LEGALLY OBLIGATED PARTY | Same as state use tax / local RST collection architecture. 12-199: purchaser may pay local-rate difference at vehicle registration. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | State compensating-tax enforcement applied insofar as made applicable. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Local complement to KRU-D04-003, matching local RST rate, closing local use/storage gap. Distinct statute; complementary to local RST. |
| 14 | RATE / CALCULATION | **Same rate** as the imposing jurisdiction's retailers' sales tax (12-198). 12-199 vehicle: difference between aggregate destination local RST rates and origin purchase local RST rates. |
| 15 | STATED PURPOSE | Privilege of using or storing TPP/vehicles/vessels in the local jurisdiction |
| 16–17 | DESTINATION / FUND | City and county compensating use tax fund (or municipal university fund); remitted at least quarterly; countywide apportioned as 12-192 |
| 18 | ADMINISTRATIVE | KDOR; 12-199 county treasurer collection at vehicle registration |
| 19 | DEPENDENCIES | Follows KRU-D04-003 imposition. **DEPENDENCY VERIFIED** as automatic local counterpart. Impairment **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Included in local distribution streams; **do not double-count** with KRU-D04-003. Isolated use-tax-only local total: **EVIDENCE REQUIRED** (UNK-D04-004). |
| 21 | H.R. 25 KANSAS-MIRROR RELATIONSHIP | **KANSAS-SPECIFIC** local use-tax counterpart. Not H.R. 25 federal machinery. |
| 22 | AGCL 00A–00J CLASSIFICATION | Same pattern as KRU-D04-003. **Never SATISFIED.** |
| 23 | CURRENT-STATE STATUS | Evidenced automatic local use-tax counterpart. Not future authorization. |
| 24 | KLRS CANDIDACY | CANDIDATE COMPULSORY CLAIM **where local RST is imposed**. Not final authorization. |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-197–198 |
| 28 | GOV-DATA LOCATORS | SRC-BILL-A-205, 209–211 |
| 29 | SOURCE DATE / VERSION | 12-198 2025 PDF retrieved 2026-09-02; 12-199 Revisor/PDF; KS-1526 motor-vehicle booklet |
| 30 | VERIFICATION STATUS | TRACED (automatic counterpart). 12-199 is a mechanism of this claim. |
| 31 | CONFLICT / UNKNOWN IDS | CF-D04-001; UNK-D04-004 |
| 32 | NOTES / TRACEABILITY | Do not treat 12-199 as a fifth claim. Do not double-count state use + local use as two statewide fiscal totals for the same SGF line. |

### KRU-D04-005 — Special-purpose district local sales/use overlays

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D04-005 / 04 |
| 3 | AUTHORITATIVE NAME | Special-purpose district additional retailers' sales taxes: community improvement district sales tax (K.S.A. 12-6a31); transportation development district sales tax (K.S.A. 12-17,145); STAR bond increment pledge of existing state/local sales and use (K.S.A. 12-17,169) — **one class row** |
| 4 | COMMON / ALTERNATE NAME | CID tax; TDD tax; STAR bond district sales tax; special district overlay |
| 5–6 | LEVEL / ENTITY | special district / local with state administration / KDOR collects |
| 7–8 | TYPE / COMPULSORY | Additional local consumption tax on the RST/use base within district boundaries / YES **where levied** |
| 9 | CURRENT LEGAL AUTHORITY | **12-6a31** CID additional RST-base tax ≤2% notwithstanding 12-187–12-197 caps. **12-17,145** TDD additional RST-base tax ≤1%. **12-17,169** STAR increment pledge of **existing** local/state sales and use (not an automatic additional rate). KDOR Pub. KS-1223 / KS-1510: CID/TDD/STAR remain on food. State redevelopment **2%** in 79-3603/79-3703 is a **state rate overlay** under KRU-D04-001/002, not this row. |
| 10 | PAYMENT / REVENUE TRIGGER | Retail/use transactions sourced to the district, on the same RST/use base, where the district tax is in effect |
| 11 | LEGALLY OBLIGATED PARTY | Same retailer/collection architecture. Economic incidence **NOT ESTABLISHED**. |
| 12 | CONSEQUENCE OF NONPAYMENT | State RST/use enforcement as made applicable. Penalties **REFERRED TO DOMAIN 07**. |
| 13 | ECONOMIC FUNCTION | Place-based additional consumption tax for district/project finance — **not** ordinary city/county rate variation |
| 14 | RATE / CALCULATION | CID: 0.10%/0.25% increments **≤2%**. TDD: 0.10%/0.25% increments **≤1%**. STAR: increment of existing RST/use, not a third additional cap in this row. **LOCAL IMPLEMENTATION VARIABLE.** Official combined rates in KS-1700. Not inventoried per district. |
| 15 | STATED PURPOSE | CID/TDD: finance a project in the district (bonds or pay-as-you-go). STAR: special-obligation / increment financing of STAR bond projects |
| 16–17 | DESTINATION / FUND | CID: community improvement district sales tax fund (2% KDOR admin skim capped $200,000/FY). TDD: transportation development district sales tax fund. STAR: pledged increment per 12-17,169. Isolated overlay-only statewide dollars: **EVIDENCE REQUIRED** |
| 18 | ADMINISTRATIVE | KDOR combined-rate collection |
| 19 | DEPENDENCIES | CID/TDD additional tax: **POTENTIAL DEPENDENCY**. STAR increment pledge: **DEPENDENCY VERIFIED** as statutory pledge architecture; project-level **POTENTIAL DEPENDENCY**. Impairment **LEGAL EFFECT UNKNOWN**. Dependency ≠ RETAIN. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | Embedded in combined local rates / Table 5 footnote 5 class. Isolated CID-only / TDD-only / STAR-increment statewide dollars: **EVIDENCE REQUIRED**. Do not add to SGF. |
| 21 | H.R. 25 KANSAS-MIRROR RELATIONSHIP | **KANSAS-SPECIFIC** district overlays. Not H.R. 25 federal machinery. **FEDERAL-SPECIFIC** H.R. 25 administration is not this overlay. |
| 22 | AGCL 00A–00J CLASSIFICATION | 00A / 00H QUESTION REQUIRED (statutory overlay ≠ retention). **Never SATISFIED.** |
| 23 | CURRENT-STATE STATUS | Evidenced as a **class**: CID/TDD additional overlays + STAR increment pledge of existing claims. Not future authorization. |
| 24 | KLRS CANDIDACY | CANDIDATE COMPULSORY CLAIM **where levied**. Not final authorization. |
| 25–26 | DISPOSITION / POST-BILL-A | **BLANK** / **NOT DETERMINED** |
| 27 | PRIMARY-LEGAL LOCATORS | SRC-BILL-A-222 (12-6a31); SRC-BILL-A-223 (12-17,145); SRC-BILL-A-224 (12-17,169) |
| 28 | GOV-DATA LOCATORS | SRC-BILL-A-206–208, 210 |
| 29 | SOURCE DATE / VERSION | 12-6a31 / 12-17,145 / 12-17,169 2025 K.S.A. PDFs retrieved 2026-09-02; KDOR Pub. KS-1223 / KS-1510 |
| 30 | VERIFICATION STATUS | TRACED (enabling architecture). Per-district inventory and isolated overlay dollars not performed. |
| 31 | CONFLICT / UNKNOWN IDS | UNK-D04-005 |
| 32 | NOTES / TRACEABILITY | One class row. Do not fragment ordinary city/county rate differences into this ID. Do not merge with KRU-D04-003. STAR increment is **not** a sixth counted claim. |
