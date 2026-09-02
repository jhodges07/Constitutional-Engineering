# WD-BILL-A-022 — Domain 01 Master Register Execution Instance

**Document ID:** WD-BILL-A-022  
**Title:** Kansas Government Revenue Universe / KLRS Master Register — Domain 01 Execution Instance  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-127; CWC-CE-128 (destination/gaming/fiscal/TGT/dependency closure; dispositions remain **BLANK**)  
**Schema authority:** WD-BILL-A-019 (this file does **not** replace the schema lock)  
**Governing LOU candidate:** LOU-004 Draft 0.9 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / DOMAIN 01 ROWS POPULATED FROM EVIDENCE — CWC-CE-128 CLOSURE APPLIED WHERE EVIDENCED — REGISTER **NOT** STATEWIDE COMPLETE — NOT ACCEPTED  
**Version:** 0.2.0  
**Effective Date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-022-Domain-01-Master-Register-Execution.md  
**Source ID:** SRC-BILL-A-024  

```text
EXECUTION INSTANCE OF WD-BILL-A-019 SCHEMA
DOMAIN 01 ONLY
HUMAN DISPOSITION = BLANK ON EVERY ROW
BLANK ≠ RETAIN
MOTOR FUEL IS NOT RETAINED
KLRS CANDIDACY ≠ FINAL AUTHORIZATION
STATEWIDE UNIVERSE NOT CERTIFIED
NOT A SPEC / NOT HG-D1 / NOT HG-D2
```

Narrative audit: WD-BILL-A-023. Closure: WD-BILL-A-028. Sources: WD-BILL-A-024. Completeness: WD-BILL-A-025. Conflicts: WD-BILL-A-026.

Common field values unless a row overrides:

- Field 2 EVIDENCE DOMAIN = 01
- Field 25 HUMAN BILL A DISPOSITION = **BLANK**
- Field 26 POST-BILL-A AUTHORITY STATUS = **NOT DETERMINED**
- Field 29 SOURCE DATE / VERSION = 2025/2026 Kansas Statutes as retrieved 2026-09-02; KDOR AR FY2025 (officials listed January 2026)
- Retrieval date = 2026-09-02

---

## 1. Index of Domain 01 rows

| Master Record ID | Authoritative name | Compulsory | Verification | Disposition |
|---|---|---|---|---|
| KRU-D01-001 | Tax imposed on use, sale or delivery of motor-vehicle fuels or special fuels | YES | TRACED | BLANK |
| KRU-D01-002 | LP-gas motor fuel tax | YES | PARTIAL (79-3492 quoted from official 2026 HTML; full PDF not separately saved) | BLANK |
| KRU-D01-003 | 24-hour or 72-hour motor fuel permits | YES | TRACED | BLANK |
| KRU-D01-004 | Tax on cigarettes imposed | YES | TRACED | BLANK |
| KRU-D01-005 | Tax on privilege of selling tobacco products | YES | TRACED | BLANK |
| KRU-D01-006 | Tax on electronic cigarettes imposed | YES | TRACED | BLANK |
| KRU-D01-007 | Gallonage tax on alcoholic liquor, cereal malt beverage or malt products | YES | TRACED | BLANK |
| KRU-D01-008 | Liquor drink tax | YES | TRACED | BLANK |
| KRU-D01-009 | Liquor enforcement tax | YES | TRACED | BLANK |
| KRU-D01-010 | Mineral severance tax | YES | TRACED (imposition + 79-4227 / 79-4219 destination/credit) | BLANK |
| KRU-D01-011 | Excise tax upon rental or lease of certain motor vehicles | YES | TRACED; CONFLICT on fund name | BLANK |
| KRU-D01-012 | Tax on new tire sales | YES | TRACED | BLANK |
| KRU-D01-013 | Transient guest tax | YES (where levied) | TRACED (authority); KDOR-administered implementation PARTIAL; non-KDOR home-rule INCOMPLETE | BLANK |
| KRU-D01-014 | Bingo taxation | YES | TRACED (imposition + 75-5182 destination; (e) CURRENT VERSION TO BE VERIFIED) | BLANK |

---

## 2. Thirty-two-field records

### KRU-D01-001 — Motor-vehicle fuels and special fuels tax

| # | Field | Value |
|---|---|---|
| 1 | MASTER RECORD ID | KRU-D01-001 |
| 2 | EVIDENCE DOMAIN | 01 |
| 3 | AUTHORITATIVE NAME | Tax imposed on use, sale or delivery of motor-vehicle fuels or special fuels (K.S.A. 79-3408 catchline) |
| 4 | COMMON / ALTERNATE NAME | Motor fuel tax; gasoline tax; special fuels / diesel tax; E85; gasohol (AR25 rate table) |
| 5 | GOVERNMENT LEVEL | state |
| 6 | GOVERNMENT ENTITY / ENTITY CLASS | State of Kansas; administered by Kansas Department of Revenue |
| 7 | RECEIPT OR CLAIM TYPE | Excise / volume tax on motor-vehicle fuels and special fuels |
| 8 | COMPULSORY STATUS | YES |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 79-3408; rates K.S.A. 79-34,141. History on 79-34,141 through L. 2014, ch. 81, § 11; July 1. |
| 10 | PAYMENT / REVENUE TRIGGER | Use, sale, or delivery of motor-vehicle fuels or special fuels in this state (79-3408(a)); computed on fuels received by each distributor, manufacturer, or importer (79-3408(b)) |
| 11 | LEGALLY OBLIGATED PARTY | Incidence imposed on the distributor of the first receipt, including distributors, manufacturers, and importers that import into Kansas (79-3408(b)) |
| 12 | CONSEQUENCE OF NONPAYMENT | `[TO BE VERIFIED]` — motor-fuel enforcement article not fully fetched this CWC |
| 13 | ECONOMIC FUNCTION | Volume levy on highway motor fuels (gasoline/gasohol/E85/special fuels). Distinct from LP-gas user tax (KRU-D01-002) and trip permits (KRU-D01-003). **Do not collapse.** |
| 14 | RATE / CALCULATION / AMOUNT METHOD | 79-34,141: not less than (1) motor-vehicle fuels other than E85 $.24/gal; (2) special fuels $.26/gal; (4) E85 $.17/gal; (5) CNG $.24/gal; (6) LNG $.26/gal. 2.5% ordinary-loss allowance (79-3408(b)). Exemptions include export, U.S., aviation fuel, dyed special fuel for nonhighway use, specified kerosene (79-3408(c)). |
| 15 | STATED PURPOSE | 79-3408 imposition text does not recast a purpose clause. KDOR AR25: “Motor fuel taxes are levied to defray in whole, or in part, the cost of public highways.” |
| 16 | REVENUE DESTINATION | **CWC-CE-128 PRIMARY-LEGAL:** K.S.A. 79-34,142 credits amounts from 79-3408, 79-3408c, 79-3491a, 79-3492, and 79-34,118: **State Highway Fund 66.37% / Special City and County Highway Fund 33.63%**. K.S.A. 79-3425: first credit motor-vehicle fuel tax refund fund, then remainder per 79-34,142; still **cross-cites expired 79-34,161** (CF-D01-008). K.S.A. 79-3425c: $625,000 quarterly from SCCHF to county equalization and adjustment fund; 57% remaining SCCHF to counties / 43% to cities. AR25 FY2025 actual (GOV-DATA, not a substitute for the statutory split): SHF $307,074,537; SCCHF $155,596,152; Alcohol Producers’ Incentive Fund $0; Refund Fund $3,600,865. **CF-D01-004 RESOLVED — DIFFERENT TIME PERIODS** (incentive expired 7/1/2018 per 79-34,164). |
| 17 | FUND / POOL TYPE | Dedicated highway funds (evidenced). Alcohol-producers incentive expired FY2018; AR25 statutory table is stale. |
| 18 | ADMINISTRATIVE / OVERHEAD TREATMENT | 2.5% distributor physical-loss allowance (not a stated KDOR skim). Other admin `%` `[TO BE VERIFIED]`. KAR 92-14 not fetched. |
| 19 | DEBT / BOND / CONTRACT / FEDERAL-MATCH / OTHER DEPENDENCIES | **DEPENDENCY VERIFIED (statewide statutory rule, not a sampled indenture):** K.S.A. 68-2320 — KDOT highway revenue bonds payable solely from revenues accruing to the state highway fund, transferred to the highway bond debt service fund and pledged to payment; 18% debt-service cap vs projected SHF revenues for additional post-2010 bonds. ACFR FY2025: SHF revenues include motor fuels taxes, sales/use, drivers’ license and vehicle registration. **POTENTIAL DEPENDENCY:** 68-2320(c)(2)(B) subtracts expected federal interest-subsidy payments from debt-service requirements — not a motor-fuel matching-grant finding. Federal dyed-fuel definition 26 U.S.C. § 4082 remains an exemption overlay (79-3408(c)(6)). City SCCHF may pay 79-3425g bonds (79-3425c(c)) — **DEPENDENCY VERIFIED (local)**. Constitutional impairment if this claim disappeared: **LEGAL EFFECT UNKNOWN**. |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | KDOR AR25 FY2025 gross motor-fuel collections $466,271,554 (Regular and E-85 $329,181,761; Special/Diesel $124,523,420; LP Gas $2,010,296; Interstate $10,257,903; Trip permits $298,174). |
| 21 | H.R. 25 KANSAS-MIRROR RELATIONSHIP | Example of intended surviving-excise non-stack (XW-HR25-011). Current KS retail fuel sales also bear sales tax — current stack ≠ post-Bill-A authorization. QUESTION REQUIRED. |
| 22 | AGCL 00A–00J CLASSIFICATION | 00A QUESTION REQUIRED; 00C EVIDENCE REQUIRED; 00E **POTENTIAL CONFLICT / EVIDENCE REQUIRED** (68-2320 SHF pledge); 00G EVIDENCE REQUIRED. Never SATISFIED. |
| 23 | CURRENT-STATE STATUS | CURRENT / OPERATIVE (2026 K.S.A. text; FY2025 collections) |
| 24 | KLRS CANDIDACY | CANDIDATE COMPULSORY CLAIM. **Not final authorization.** |
| 25 | HUMAN BILL A DISPOSITION | **BLANK** |
| 26 | POST-BILL-A AUTHORITY STATUS | NOT DETERMINED |
| 27 | PRIMARY-LEGAL LOCATORS | https://www.kslegislature.gov/b2025_26/laws/079_000_0000_chapter/079_034_0000_article/079_034_0008_section/079_034_0008_k/ ; https://www.kslegislature.gov/b2025_26/laws/079_000_0000_chapter/079_034_0000_article/079_034_0141_section/079_034_0141_k/ ; 79-34,142 / 79-3425 / 79-3425c / 79-34,164 / 68-2320 2025 Revisor PDFs (WD-BILL-A-024 SRC-BILL-A-055 et seq.) |
| 28 | GOV-DATA LOCATORS | https://www.ksrevenue.gov/bustaxtypes.html ; KDOR Annual Report FY2025 https://www.ksrevenue.gov/pdf/ar25complete.pdf (Motor Fuel Tax section; rate table citing 79-34,141) |
| 29 | SOURCE DATE / VERSION | 2026 Kansas Statutes HTML; 2025 K.S.A. as published; AR25 FY2025 |
| 30 | VERIFICATION STATUS | TRACED |
| 31 | CONFLICT / UNKNOWN IDS | CF-D01-004 (closed — expired program); CF-D01-008 (79-3425 still cites 79-34,161); UNK-D01-001 (indenture not sampled; statute/ACFR used); UNK-EX-005 |
| 32 | NOTES / TRACEABILITY | **MOTOR FUEL IS NOT RETAINED.** Example of uniform surviving-excise standard only. Rate lines for gasoline, special fuels, and E85 share 79-3408 imposition; they are recorded as one claim with a rate schedule, not collapsed with LP-gas user tax. |

### KRU-D01-002 — LP-gas / CNG / LNG motor-fuel tax

| # | Field | Value |
|---|---|---|
| 1–2 | ID / DOMAIN | KRU-D01-002 / 01 |
| 3 | AUTHORITATIVE NAME | LP-gas motor fuel tax (K.S.A. 79-3492 catchline as published) |
| 4 | COMMON / ALTERNATE NAME | LP-gas; compressed natural gas; liquefied natural gas motor-fuel tax |
| 5–8 | Level / entity / type / compulsory | state / KDOR / volume motor-fuel tax on LP-gas users/dealers / YES |
| 9 | CURRENT LEGAL AUTHORITY | K.S.A. 79-3492; rates K.S.A. 79-34,141(3),(5),(6) |
| 10 | TRIGGER | Placement of LP-gas into the fuel supply tank of a motor vehicle while the vehicle is within this state (official 2026 HTML quote of 79-3492(a)) |
| 11 | OBLIGATED PARTY | LP-gas user or LP-gas dealer (79-3492(a)) — **distinct from** distributor-of-first-receipt under 79-3408 |
| 12 | NONPAYMENT | `[TO BE VERIFIED]` |
| 13 | ECONOMIC FUNCTION | Alternative-fuel / LP-gas highway use levy |
| 14 | RATE | LP-gas other than CNG/LNG $.23/gal; CNG $.24/GGE; LNG $.26/DGE; conversion 126.67 CF or 5.66 lb CNG = 1 GGE; 6.06 lb LNG = 1 DGE |
| 15–17 | Purpose / destination / fund | Treated with motor-fuel distribution in AR25 (LP Gas Fuel FY2025 $2,010,296). **79-34,142** includes 79-3492 receipts in the 66.37% SHF / 33.63% SCCHF split. Dedicated highway family. |
| 18–19 | Admin / dependencies | `[TO BE VERIFIED]` / `[LEGAL EFFECT UNKNOWN]` |
| 20 | COLLECTIONS | Included in AR25 motor-fuel-by-type LP Gas Fuel $2,010,296 FY2025 |
| 21 | H.R. 25 | Same family as 001 — QUESTION REQUIRED; NOT RETAINED |
| 22 | AGCL | Same pattern as 001. Never SATISFIED. |
| 23–26 | Status / KLRS / disposition / post-Bill-A | CURRENT / CANDIDATE COMPULSORY CLAIM / **BLANK** / NOT DETERMINED |
| 27 | PRIMARY-LEGAL | https://www.kslegislature.gov/b2025_26/laws/079_000_0000_chapter/079_034_0000_article/079_034_0092_section/079_034_0092_k/ |
| 28 | GOV-DATA | AR25 motor-fuel-by-type table |
| 29–32 | Date / verification / conflicts / notes | 2026-09-02 / PARTIAL / UNK-D01-002 (full 79-3492 PDF not separately archived) / Distinct legal claim from 79-3408. **NOT RETAINED.** |

### KRU-D01-003 — Motor-fuel trip permits

| # | Field | Value |
|---|---|---|
| 1–8 | | KRU-D01-003 / 01 / 24-hour or 72-hour motor fuel permits / trip permits / state / KDOR / permit in lieu of interstate motor-fuel use tax / YES |
| 9 | AUTHORITY | K.S.A. 79-34,118. History through L. 2006, ch. 119, § 1; July 1. |
| 10–11 | Trigger / party | Application and payment by any interstate motor fuel user; authorizes one commercial motor vehicle for 24 or 72 hours without compliance with other Interstate Motor Fuel Use Act provisions and in lieu of the tax imposed by K.S.A. 79-34,109 |
| 12 | NONPAYMENT | `[TO BE VERIFIED]` |
| 13 | ECONOMIC FUNCTION | Time-limited permit substitute for interstate motor-fuel use tax |
| 14 | RATE | $13 per 24-hour permit; $25 per 72-hour permit. May be purchased in multiples of three. |
| 15–17 | Purpose / destination / fund | In lieu of 79-34,109 interstate tax. **79-34,142** includes 79-34,118 receipts in the 66.37% SHF / 33.63% SCCHF split. AR25 folds trip-permit collections into motor-fuel totals (FY2025 $298,174, including KHP-issued permits). |
| 18 | ADMIN | Secretary may designate agents or contract with private issuing agents (79-34,118) — **private-contract collection pathway evidenced; fee split `[TO BE VERIFIED]`** |
| 19–20 | Deps / collections | Same SHF pledge family as KRU-D01-001 (68-2320 / ACFR) — **DEPENDENCY VERIFIED** at the highway-fund level, not a separate trip-permit indenture. / FY2025 $298,174 |
| 21–26 | | Motor-fuel family; **NOT RETAINED**; BLANK; NOT DETERMINED |
| 27 | PRIMARY-LEGAL | https://www.kslegislature.gov/media/statute/079_000_0000_chapter/079_034_0000_article/079_034_0118_section/079_034_0118_k.pdf |
| 30–32 | | TRACED / — / Distinct from 79-3408 gallons tax. |

### KRU-D01-004 — Cigarette tax

| # | Field | Value |
|---|---|---|
| 1–8 | | KRU-D01-004 / 01 / Tax on cigarettes imposed / cigarette tax / state / KDOR / pack/unit excise / YES |
| 9 | AUTHORITY | K.S.A. 79-3310. On and after July 1, 2015. History through L. 2015, ch. 99, § 29; July 1. |
| 10–11 | Trigger / party | All cigarettes sold, distributed, or given away within Kansas; paid only once by the **wholesale dealer first receiving** the cigarettes |
| 12 | NONPAYMENT | KDOR cigarette page: failure to file may result in denial of stamp purchases; further penalties `[TO BE VERIFIED]` |
| 13 | ECONOMIC FUNCTION | Pack/unit compulsory levy on cigarettes |
| 14 | RATE | $1.29 on each 20 cigarettes or fractional part thereof, or $1.61 on each 25 cigarettes |
| 15–17 | Purpose / destination / fund | Imposition does not state a restricted purpose. **K.S.A. 79-3387(a):** entire amount of **taxes imposed by this act** credited to **SGF**. **79-3387(b):** license fees, 79-3324a forfeitures, and fines → cigarette and tobacco products regulation fund (79-3391), used exclusively for cigarette/tobacco regulation and enforcement. AR25 groups Cigarette & Tobacco Taxes → SGF. KLRD Tax Facts FY2024: Cigarette $90,094 thousand. |
| 18–19 | Admin / deps | `[TO BE VERIFIED]` / NPM/PACT federal overlay `[LEGAL EFFECT UNKNOWN]` |
| 20 | COLLECTIONS | AR25 SGF table: Cigarette/Tobacco Tax FY2025 $96,261,221 (combined cigarette/tobacco line; **not split** in that table) |
| 21 | H.R. 25 | POTENTIAL CONFLICT — retail new-goods overlap / stack unless later surviving-excise non-stack rule |
| 22 | AGCL | 00C POTENTIAL CONFLICT (SGF pooling); 00A QUESTION REQUIRED. Never SATISFIED. |
| 23–26 | | CURRENT / CANDIDATE COMPULSORY CLAIM / **BLANK** / NOT DETERMINED |
| 27 | PRIMARY-LEGAL | https://www.kslegislature.gov/media/statute/079_000_0000_chapter/079_033_0000_article/079_033_0010_section/079_033_0010_k.pdf |
| 28 | GOV-DATA | https://www.ksrevenue.gov/bustaxtypescig.html ; AR25 rate table and SGF collections |
| 30–31 | | TRACED / UNK-D01-004 (cigarette vs tobacco collection split in AR25 combined SGF line); CF-D01-006 (e-cig “this act” coverage PARTIALLY RESOLVED) |

### KRU-D01-005 — Tobacco products tax

| # | Field | Value |
|---|---|---|
| 1–8 | | KRU-D01-005 / 01 / Tax on privilege of selling tobacco products / OTP / other tobacco products tax / state / KDOR / wholesale-price privilege tax / YES |
| 9 | AUTHORITY | K.S.A. 79-3371. History: L. 1972, ch. 375, § 2; July 1. |
| 10–11 | Trigger / party | Privilege of selling or dealing in tobacco products by a distributor, at the time the distributor brings products into the state for sale, manufactures in-state for sale, or ships to Kansas retailers |
| 12 | NONPAYMENT | `[TO BE VERIFIED]` |
| 13–14 | Function / rate | Privilege-on-commodity; **10% of wholesale sales price** |
| 15–17 | | No restricted purpose in 79-3371. Destination: **79-3387(a) taxes of this act → SGF**; fees/fines/forfeitures to regulation fund. AR25 combined cigarette & tobacco → SGF. KLRD FY2024 Tobacco Products $10,509 thousand. General fund for the tax. |
| 18–21 | | `[TO BE VERIFIED]` / `[LEGAL EFFECT UNKNOWN]` / combined FY2025 line with cigarettes / POTENTIAL CONFLICT (FairTax stack) |
| 22–26 | | 00C POTENTIAL CONFLICT / CURRENT / CANDIDATE COMPULSORY CLAIM / **BLANK** / NOT DETERMINED |
| 27 | PRIMARY-LEGAL | https://www.kslegislature.gov/media/statute/079_000_0000_chapter/079_033_0000_article/079_033_0071_section/079_033_0071_k.pdf |
| 30 | | TRACED |

### KRU-D01-006 — Electronic-cigarette / consumable-material tax

| # | Field | Value |
|---|---|---|
| 1–8 | | KRU-D01-006 / 01 / Tax on electronic cigarettes imposed / consumable material tax / e-cigarette tax / state / KDOR / unit (ml) privilege tax / YES |
| 9 | AUTHORITY | K.S.A. 79-3399. On and after July 1, 2017. History through L. 2017, ch. 96, § 25; June 22. |
| 10–11 | Trigger / party | Privilege of selling or dealing in electronic cigarettes by a distributor at $.05/ml of consumable material. For untaxed product in retail-dealer possession, tax at earliest of bringing into state, manufacturing, or selling to consumers. |
| 12–14 | | `[TO BE VERIFIED]` / milliliter levy on e-cigarette consumable material / $.05 per milliliter and proportionate fractional parts |
| 15–17 | | No restricted purpose in 79-3399. Destination: **CF-D01-006 PARTIALLY RESOLVED** — 79-3399 has no remittance clause; 79-3387 was co-amended L. 2017, ch. 96 with 79-3399; KLRD Tax Facts FY2024 reports **Electronic Cigarette $4,294 thousand, 100% SGF**. Do not treat the KLRD line as a statutory sentence that 79-3399 is inside “this act.” Working destination for the tax: SGF. |
| 20 | COLLECTIONS | KLRD Tax Facts FY2024 Electronic Cigarette $4,294 thousand (separate SGF line). AR25 FY2025 SGF cigarette/tobacco line remains combined. |
| 21–26 | | POTENTIAL CONFLICT (FairTax stack) / CURRENT / CANDIDATE COMPULSORY CLAIM / **BLANK** / NOT DETERMINED |
| 27 | PRIMARY-LEGAL | https://www.kslegislature.gov/media/statute/079_000_0000_chapter/079_033_0000_article/079_033_0099_section/079_033_0099_k.pdf |
| 28 | GOV-DATA | KDOR cigarette page Consumable Material Tax; AR25 rate table citing 79-3399 |
| 30–31 | | TRACED / CF-D01-006 (whether e-cig receipts are inside 79-3387 SGF credit) |

### KRU-D01-007 — Liquor gallonage tax

| # | Field | Value |
|---|---|---|
| 1–8 | | KRU-D01-007 / 01 / Tax rate; exemptions; collection and disposition of tax (41-501 catchline) / liquor gallonage tax / state / KDOR ABC / volume gallonage / YES |
| 9 | AUTHORITY | K.S.A. 41-501. History through L. 2022, ch. 71, § 4; January 1, 2023. |
| 10–11 | Trigger / party | Manufacturing, using, selling, storing, or purchasing alcoholic liquor, CMB, or malt products; paid only once by the person who first manufactures, uses, sells, stores, purchases, or receives; manufacturer if produced in Kansas; distributor if imported for wholesale |
| 12 | NONPAYMENT | `[TO BE VERIFIED]` |
| 13–14 | | Volume levy on alcoholic beverages / beer & CMB $.18/gal; wort/liquid malt $.20/gal; malt syrup/extract $.10/lb; wine ≤16% $.30/gal; wine >16% $.75/gal; alcohol & spirits $2.50/gal |
| 15 | PURPOSE | “For the purpose of raising revenue” (41-501(b)(1)) |
| 16–17 | DESTINATION | 1/10 of alcohol-and-spirits collections to Community Alcoholism and Intoxication Programs Fund; **balance to SGF** (41-501(i)). Mixed general + dedicated. |
| 18–19 | | `[TO BE VERIFIED]` / `[LEGAL EFFECT UNKNOWN]` |
| 20 | COLLECTIONS | AR25 ABC aggregate FY2025 $175,037,988 (gallonage + liquor excise + enforcement + fees — **not split** in the TOC summary line) |
| 21 | H.R. 25 | QUESTION REQUIRED (upstream volume vs retail FairTax event) |
| 22–26 | | 00C POTENTIAL CONFLICT (SGF) / CURRENT / CANDIDATE COMPULSORY CLAIM / **BLANK** / NOT DETERMINED |
| 27 | PRIMARY-LEGAL | https://www.kslegislature.gov/b2025_26/laws/041_000_0000_chapter/041_005_0000_article/041_005_0001_section/041_005_0001_k/ |
| 30 | | TRACED |
| 32 | NOTES | 41-501(g): retail sales of alcoholic liquor (and specified microbrewery/farm-winery consumer sales) **not** subject to retailers’ sales tax but **are** subject to enforcement tax. Stacking pattern is statutory. HB 2714 introduced — **not current law**. |

### KRU-D01-008 — Liquor drink tax

| # | Field | Value |
|---|---|---|
| 1–8 | | KRU-D01-008 / 01 / Imposition and rate of tax; paid by consumer and collected by seller / liquor drink tax; liquor excise tax (AR25 label) / state (with local share) / KDOR / gross-receipts excise-type / YES |
| 9 | AUTHORITY | K.S.A. 79-41a02; disposition K.S.A. 79-41a03. 79-41a03 history through L. 2024, ch. 2, § 9 (Special Session); July 1. |
| 10–11 | Trigger / party | Privilege of selling alcoholic liquor: 10% of gross receipts of clubs, caterers, drinking establishments, public venues, temporary permit holders, and sample acquisition costs. **Paid by the consumer**; seller collects and remits. |
| 12 | NONPAYMENT | Collectible in the manner of retailers’ sales tax under K.S.A. 79-3617 (79-41a03(c)) |
| 13–14 | | On-premises alcoholic-liquor consumption / 10% of gross receipts |
| 15 | PURPOSE | Privilege-of-selling imposition; no 100% restricted-purpose clause in 79-41a02 |
| 16–17 | DESTINATION | 25% SGF; 5% Community Alcoholism and Intoxication Programs Fund; balance Local Alcoholic Liquor Fund — subject to refund-fund maintenance; State Fairgrounds temporary-permit special split; **STAR-bond override up to 100% to bond debt service** (79-41a03(d)) |
| 18 | ADMIN | `[TO BE VERIFIED]` as a percentage; SGF 25% is general pooling not labeled “admin” |
| 19 | DEPENDENCIES | **VERIFIED:** STAR bond project district remittance to city/county or KDFA bond debt service funds (79-41a03(d)(2)) |
| 20 | COLLECTIONS | Inside AR25 ABC aggregate; standalone drink-tax total `[REVENUE EFFECT UNKNOWN]` in this extract |
| 21 | H.R. 25 | POTENTIAL CONFLICT — consumer-paid gross receipts on drinks would overlap FairTax-taxable consumption |
| 22–26 | | 00C POTENTIAL CONFLICT; 00E EVIDENCE REQUIRED (STAR bonds) / CURRENT / CANDIDATE COMPULSORY CLAIM / **BLANK** / NOT DETERMINED |
| 27 | PRIMARY-LEGAL | https://www.kslegislature.gov/b2025_26/laws/079_000_0000_chapter/079_041a_0000_article/079_041a_0002_section/079_041a_0002_k/ ; 79-41a03 PDF via Revisor media path |
| 30 | | TRACED |

### KRU-D01-009 — Liquor enforcement tax

| # | Field | Value |
|---|---|---|
| 1–8 | | KRU-D01-009 / 01 / Imposition and rate of tax (79-4101) / liquor enforcement tax / state / KDOR / 8% gross-receipts tax / YES |
| 9 | AUTHORITY | K.S.A. 79-4101. History through L. 2019, ch. 18, § 3; April 1. |
| 10–11 | Trigger / party | Privilege of engaging in specified alcoholic-liquor / CMB sales by retailers, microbreweries, microdistilleries, farm wineries, and distributors to on-premise licensees |
| 12 | NONPAYMENT | `[TO BE VERIFIED]` |
| 13–14 | | Package-store / specified producer-to-consumer and distributor-to-on-premise sales / **8% of gross receipts**; in addition to license fees (79-4101(b)) |
| 15 | PURPOSE | “For the purpose of providing revenue which may be used by the state, counties and cities in the **enforcement** of the provisions of this act” |
| 16–17 | DESTINATION | **K.S.A. 79-4108 (2025 PDF):** default entire remittance of 79-4101 through 79-4105 taxes to **SGF**; remaining former county/city alcoholic liquor control enforcement fund transferred to SGF. Exception (b): State Fairgrounds consumer sales **30% SGF / remainder State Fair capital improvements fund** (K.S.A. 2-223); expires if the fair is outside Hutchinson city limits. Exception (c): **STAR-bond remittance up to 100%** to city/county or KDFA bond debt service (L. 2024, ch. 2, § 8 Special Session). Purpose in 79-4101 (“enforcement”) vs SGF default is a **verified purpose/destination mismatch** — POTENTIAL CONFLICT vs uniform A/B, not silently reconciled. AR25: SGF (cites 79-4108). KLRD FY2024 Liquor Enforcement $83,715 thousand. |
| 18–21 | | `[TO BE VERIFIED]` / **DEPENDENCY VERIFIED:** STAR-bond remittance 79-4108(c) (in addition to drink-tax 79-41a03(d)(2)). / inside ABC aggregate; KLRD FY2024 named line / POTENTIAL CONFLICT (stack; 41-501(g) substitutes this tax for sales tax on certain retail liquor sales) |
| 22–26 | | 00A/00C QUESTION REQUIRED + POTENTIAL CONFLICT; 00E POTENTIAL CONFLICT / EVIDENCE REQUIRED (STAR) / CURRENT / CANDIDATE COMPULSORY CLAIM / **BLANK** / NOT DETERMINED |
| 27 | PRIMARY-LEGAL | https://www.kslegislature.gov/b2025_26/laws/079_000_0000_chapter/079_041_0000_article/079_041_0001_section/079_041_0001_k/ ; 79-4108 2025 Revisor PDF (SRC-BILL-A-056) |
| 30–31 | | TRACED / UNK-D01-005 closed as to 79-4108 text; purpose vs SGF use remains POTENTIAL CONFLICT |
| 32 | NOTES | HB 2630 (introduced) would authorize additional local liquor enforcement tax — **not current law**. |

### KRU-D01-010 — Mineral severance tax

| # | Field | Value |
|---|---|---|
| 1–8 | | KRU-D01-010 / 01 / Mineral severance tax; imposition of tax / mineral tax; oil and gas severance tax / state (with county share) / KDOR / severance **excise** / YES |
| 9 | AUTHORITY | K.S.A. 79-4217. History through L. 2013, ch. 87, § 7; April 25. Rates also referenced with 79-4219 in AR25. |
| 10–11 | Trigger / party | Severance and production of coal, oil, or gas from the earth or water in this state for sale, transport, storage, profit, or commercial use; borne ratably by all persons within “producer” |
| 12 | NONPAYMENT | `[TO BE VERIFIED]` |
| 13–14 | | Resource-extraction excise / 8% of gross value of oil or gas; $1 per ton of coal; extensive exemptions in 79-4217(b). **K.S.A. 79-4219:** property-tax credit **3.67% of gross value** (oil; gas from FY1997 onward) — confirms AR25 “8% with 3.67% property tax credit.” |
| 15 | PURPOSE | Statute labels it an **excise tax**; no additional restricted-purpose clause retrieved in 79-4217/79-4227 beyond the labeled tax and destination splits. |
| 16–17 | DESTINATION | **K.S.A. 79-4227 (current FY2016+ formula):** (1) mineral production tax refund fund (cap $50,000); (2) **7%** of remainder → special county mineral production tax fund (county treasurer **50% county GF / 50% school districts** by assessed mineral value); (3) of remaining moneys for counties with ≥$100,000 oil/gas receipts: **20% mineral production education fund** (Revisor note: cite should be 72-5130, not 72-6462*); **remainder SGF**. AR25 “93% SGF less 12.41% OGVDTF” is the **FY2013–2015** formula in the same section — **stale as current law**. **CF-D01-007 RESOLVED — DIFFERENT ACCOUNTING BASES.** |
| 18–19 | | `[TO BE VERIFIED]` / `[LEGAL EFFECT UNKNOWN]` |
| 20 | COLLECTIONS | AR25 net after credits/exemptions FY2025: Oil $33,589,975; Natural Gas $5,867,594; Total $39,457,569. SGF line Mineral Tax FY2025 $26,493,817. ACFR FY2025 SGF severance actual $26,494 thousand. KLRD FY2024 Oil $38,551 thousand (SGF $25,924 / other $12,627). Difference is credit + refund + 7% county + 20% education — **not** an unexplained loss. |
| 21 | H.R. 25 | EVIDENCE REQUIRED / possibly NOT APPLICABLE to retail-consumption taxable event |
| 22–26 | | 00C POTENTIAL CONFLICT (SGF) / CURRENT / CANDIDATE COMPULSORY CLAIM / **BLANK** / NOT DETERMINED |
| 27 | PRIMARY-LEGAL | https://www.kslegislature.gov/b2025_26/laws/079_000_0000_chapter/079_042_0000_article/079_042_0017_section/079_042_0017_k/ |
| 30–32 | | TRACED / CF-D01-007 closed as different accounting bases; UNK-D01-006 closed as to 79-4219/79-4227 text / HB 2775 introduced exemption — **not current law**. Statute uses the word **excise**. |

### KRU-D01-011 — Vehicle rental excise tax

| # | Field | Value |
|---|---|---|
| 1–8 | | KRU-D01-011 / 01 / Excise tax upon rental or lease of certain motor vehicles / vehicle rental excise tax / state (remitted to counties) / KDOR / short-term rental excise stacked on sales tax / YES |
| 9 | AUTHORITY | K.S.A. 79-5117. History: L. 1991, ch. 286, § 1; L. 2001, ch. 5, § 467; July 1. |
| 10–11 | Trigger / party | Rental or lease not exceeding 28 days of motor vehicles that except for K.S.A. 79-5101 would be subject to motor-vehicle property tax. Administration follows retailers’ sales tax laws (79-5117(b)). Who economically pays vs who remits: `[LEGAL EFFECT UNKNOWN]` |
| 12 | NONPAYMENT | Sales-tax collection machinery applied (79-5117(b)) |
| 13–14 | | Short-term vehicle-rental gross receipts / **3½%** in addition to Kansas retailers’ sales tax |
| 15 | PURPOSE | No separate purpose clause in 79-5117(a) beyond imposing an excise in addition to sales tax |
| 16–17 | DESTINATION | **CF-D01-001 RESOLVED — DIFFERENT ACCOUNTING CONCEPTS:** 79-5117(c) legally credits **SGF** then remits to county treasurers June 30 and November 30 for levy-unit apportionment as 79-5110/79-5111. AR25 operational label: Rental Motor Vehicle Excise Tax Fund then 100% county treasurer. KLRD Table 4 FY2024: Vehicle Rental Excise **$81 thousand, 0 SGF / all other funds** — consistent with SGF as waypoint, not retained general revenue. No current statute creating the AR25 fund name was located. |
| 18–19 | | `[TO BE VERIFIED]` / `[LEGAL EFFECT UNKNOWN]` |
| 20 | COLLECTIONS | KLRD Table 4 FY2024 named line $81 thousand other-funds residual — **MATCHED as a line**, not proof of statewide economic tax volume. |
| 21 | H.R. 25 | POTENTIAL CONFLICT — express current stack with sales tax; rental of property/services mapping EVIDENCE REQUIRED (used vs new) |
| 22–26 | | 00G EVIDENCE REQUIRED (AR25 fund label vs SGF waypoint; conflict closed as accounting concepts) / CURRENT / CANDIDATE COMPULSORY CLAIM / **BLANK** / NOT DETERMINED |
| 27 | PRIMARY-LEGAL | https://www.kslegislature.gov/b2025_26/laws/079_000_0000_chapter/079_051_0000_article/079_051_0017_section/079_051_0017_k/ |
| 30–32 | | TRACED / CF-D01-001 closed as different accounting concepts (fund name still an AR25 label) / HB 2154 introduced would discontinue this excise — **not current law**. |

### KRU-D01-012 — New-tire excise tax

| # | Field | Value |
|---|---|---|
| 1–8 | | KRU-D01-012 / 01 / Tax on new tire sales / tire excise tax / state / KDOR / per-unit new-tire excise stacked on other taxes / YES |
| 9 | AUTHORITY | K.S.A. 65-3424d. History through L. 2001, ch. 167, § 4; July 1. AR25 cites 65-3424 — **CF-D01-002 RESOLVED — SOURCE ERROR IDENTIFIED** (65-3424 is definitions). |
| 10–11 | Trigger / party | Retail sales of new vehicle tires (excluding innertubes), including new tires mounted on a vehicle sold at retail for the first time. **Paid by the purchaser**; collected by the retailer. |
| 12 | NONPAYMENT | Collectible as retailers’ sales tax under K.S.A. 79-3617 (65-3424d(d)) |
| 13–14 | | Unit levy on new highway-vehicle tires / **$.25 per vehicle tire** |
| 15–17 | PURPOSE / DESTINATION / FUND | Remittance “to the credit of the waste tire management fund” (65-3424d(e)). AR25: Tires Excise Tax → Waste Tire Management Fund. Dedicated. |
| 18–19 | | `[TO BE VERIFIED]` whether the waste-tire fund finances KDHE/KDOR overhead / `[LEGAL EFFECT UNKNOWN]` |
| 20 | COLLECTIONS | KLRD FY2024 New Tires $974 thousand, 0 SGF. |
| 21 | H.R. 25 | POTENTIAL CONFLICT — new-goods retail sale; KDOR states tax is in addition to sales tax (Pub. KS-1530 / tire page) |
| 22–26 | | 00C closer to restricted pool than SGF claims but C/D still EVIDENCE REQUIRED / CURRENT / CANDIDATE COMPULSORY CLAIM / **BLANK** / NOT DETERMINED |
| 27 | PRIMARY-LEGAL | https://www.kslegislature.gov/media/statute/065_000_0000_chapter/065_034_0000_article/065_034_0024d_section/065_034_0024d_k.pdf |
| 28 | GOV-DATA | https://www.ksrevenue.gov/bustaxtypestire.html ; Pub. KS-1530 Rev. 7-30-25 |
| 30–31 | | TRACED / CF-D01-002 |

### KRU-D01-013 — Transient guest tax

| # | Field | Value |
|---|---|---|
| 1–8 | | KRU-D01-013 / 01 / Transient guest tax / lodging tax; hotel tax / local with state administration / cities and counties; KDOR collects / local-option gross-receipts lodging tax / YES where levied |
| 9 | AUTHORITY | K.S.A. 12-1693 (population >300,000 county scheme, election); K.S.A. 12-1697 (any city or county, ordinance/resolution); collection/disposition K.S.A. 12-1694. Definitions K.S.A. 12-1692. |
| 10–11 | Trigger / party | Gross receipts from transient guests for sleeping accommodations (≤28 consecutive days). **Paid by the consumer or user**; business collects. |
| 12 | NONPAYMENT | 12-1694(c): collectible as retailers’ sales tax under K.S.A. 79-3617 |
| 13–14 | | Short-term lodging / enabling cap **not to exceed 2%** in 12-1693 and 12-1697. **LOCAL IMPLEMENTATION VERIFIED (KDOR-administered):** official KDOR *Transient Guest Tax Rates and Filers* as of July 1, 2026 — 39 counties, 126 cities including special districts, 165 city+county listed rates. Many listed rates **exceed 2%** (examples: Kansas City 10%; Goddard/Overland Park/Olathe/Mission 9%; Abilene/Lawrence 8%; Shawnee County 7%; Sedgwick County 5%; Osborne County 1%). **CF-D01-003 PARTIALLY RESOLVED.** Non-KDOR-administered home-rule levies: **LOCAL IMPLEMENTATION INVENTORY INCOMPLETE**. |
| 15 | PURPOSE | “In order to provide revenues to promote tourism and conventions.” Local fund: convention and tourism promotion; not more than 20% for tourism promotion (12-1694(e)). |
| 16–17 | DESTINATION | 2% of collections to SGF “to defray the expenses of the department in administration and enforcement”; remainder county and city transient guest tax fund → local treasurers (12-1694(c)). AR25 matches 98% / 2%. |
| 18 | ADMIN | **Express 2% SGF administrative deduction.** Material UNK-EX-005 evidence. |
| 19–20 | | `[LEGAL EFFECT UNKNOWN]` / KLRD FY2024 combined state+local TGT $63,579 thousand; **State Transient Guest $1,287 thousand 100% SGF** (~2% skim, consistent with 12-1694) |
| 21 | H.R. 25 | POTENTIAL CONFLICT — lodging consumption; KDOR Pub. KS-1216: in addition to sales tax |
| 22–26 | | 00H POTENTIAL CONFLICT (home rule); 00D/00A QUESTION REQUIRED / CURRENT enabling authority; local levy not universal / CANDIDATE COMPULSORY CLAIM where levied / **BLANK** / NOT DETERMINED |
| 27 | PRIMARY-LEGAL | 12-1692, 12-1693, 12-1694, 12-1697 official legislature/Revisor locators in WD-BILL-A-024 |
| 28 | GOV-DATA | AR25; KDOR Pub. KS-1216 Rev. 9-11-25; KDOR https://www.ksrevenue.gov/pdf/tgratesfilers.pdf (as of July 1, 2026); https://ksrevenue.gov/prtgreports.html ; Kansas LPA TGT audit page (secondary to statutes; used for home-rule gap, not as the rate list) |
| 30–32 | | PARTIAL (authority TRACED; KDOR-administered implementation VERIFIED; non-KDOR home-rule INCOMPLETE) / CF-D01-003 / Distinguish AUTHORITY VERIFIED from LOCAL IMPLEMENTATION VERIFIED (KDOR list) vs INCOMPLETE (non-KDOR). |

### KRU-D01-014 — Bingo taxes

| # | Field | Value |
|---|---|---|
| 1–8 | | KRU-D01-014 / 01 / Same; taxation (75-5176) / bingo tax; charitable gaming bingo tax / state / KDOR charitable gaming / privilege/gross-receipts and unit gaming taxes / YES |
| 9 | AUTHORITY | K.S.A. 75-5176. History: L. 2015, ch. 62, § 6; July 1. |
| 10–11 | Trigger / party | Licensee: 3% of gross receipts from charges for participation in call bingo using reusable cards and admission fees. Distributor: $0.002 per bingo face; 1% of printed retail sales price of all tickets in each box of instant bingo tickets. |
| 12 | NONPAYMENT | Bond may be required (75-5176(e)); further `[TO BE VERIFIED]` |
| 13–14 | | Charitable-gaming activity taxes / rates as in field 10 |
| 15 | PURPOSE | “For the purpose of providing revenue which may be used by the state and for the privilege of operating or conducting games of bingo” |
| 16–17 | DESTINATION | **K.S.A. 75-5182:** license/registration fees and 75-5176 tax credited to **state charitable gaming regulation fund** (except 75-5183); expended for **administration and enforcement** of the Kansas charitable gaming act; year-end excess transferred to **SGF** (75-5182(d)). Subsection (c) refers to (d) and (e); retrieved PDF showed (d) then History — **(e) CURRENT VERSION TO BE VERIFIED**. AR25: Bingo Enforcement Tax → State Charitable Gaming Regulation Fund. KLRD FY2024 Bingo/Raffle $313 thousand, 0 SGF. Direct UNK-EX-005 evidence (admin from pool + leftover to SGF) — test remains **RESERVED**. |
| 18–20 | | **Express admin/enforcement use of the tax pool** (75-5182) / `[LEGAL EFFECT UNKNOWN]` beyond that statute / KLRD FY2024 Bingo/Raffle $313 thousand |
| 21 | H.R. 25 | EVIDENCE REQUIRED vs XW-HR25-007/013 gaming architecture |
| 22–26 | | 00A QUESTION REQUIRED / CURRENT / CANDIDATE COMPULSORY CLAIM / **BLANK** / NOT DETERMINED |
| 27 | PRIMARY-LEGAL | https://www.kslegislature.gov/media/statute/075_000_0000_chapter/075_051_0000_article/075_051_0076_section/075_051_0076_k.pdf |
| 30 | | TRACED (imposition + destination); 75-5182(e) CURRENT VERSION TO BE VERIFIED |

---

## 3. Fourteen-question and A–J cross-reference

Completed in WD-BILL-A-023 §§S–T for all material Domain 01 claims. Rows above carry the minimum CWC-CE-127 fields.

---

## 4. Investigated / not counted as verified Domain 01 rows

These were on the search surface or KDOR index. They are **not** asserted as verified Domain 01 claims. Human disposition = **BLANK**. No RETAIN.

| Working ID | Item | Disposition of classification | Basis |
|---|---|---|---|
| D01-INV-001 | Drycleaning environmental surcharge / solvent fee | Refer Domain 05 unless later evidence shows excise-type function | KDOR index; AR25 cites 65-34,150 / 65-34,151; environmental surcharge |
| D01-INV-002 | Water protection fee / clean drinking water fee | Refer Domain 05 | KDOR index; AR25 82a-954 / 82a-2101 |
| D01-INV-003 | Environmental assurance fee | Refer Domain 05 | AR25 65-34,117 / 65-34,114 |
| D01-INV-004 | Oil inspection fee | Refer Domain 05 | AR25 55-426 / 55-427 |
| D01-INV-005 | Sand royalty | Refer Domain 11/12 | Royalty per AR25 70a-102; not treated as Domain 01 excise without further legal analysis |
| D01-INV-006 | Drug stamp tax | Refer Domain 07; CLASSIFICATION UNRESOLVED | KDOR index; AR25 79-5202 / 79-5211 |
| D01-INV-007 | Financial-institution privilege tax | Refer Domain 03 | Income/privilege on net income (79-1107/1108); not Domain 01 commodity excise |
| D01-INV-008 | Lottery gaming facility privilege fee / expanded-lottery revenue share / lottery ticket proceeds | **RECLASSIFIED / REFERRED** — not a Domain 01 counted row. History preserved. | **CWC-CE-128:** K.S.A. 74-8734, 74-8711, 74-8768 retrieved. Lottery tickets: NON-COMPULSORY / ENTERPRISE → **REFERRED TO DOMAIN 08**. Casino/lottery-gaming facility state ≥22% + local/problem-gambling shares: GOVERNMENTAL SHARE OF GAMING REVENUE / ENTERPRISE (state-owned operation, contracted manager) → **REFERRED TO DOMAIN 08**. Privilege fee $25M/$5.5M: REGULATORY / PRIVILEGE CLAIM → **REFERRED TO DOMAIN 05**. Bingo (KRU-D01-014) remains Domain 01. See WD-BILL-A-028 §3. |

Prepaid wireless 911 fee (AR25 12-5371) is Domain 05, not Domain 01.

Working referral IDs (not counted in the 14): KRU-REF-08-001 through KRU-REF-08-004 and KRU-REF-05-001 — WD-BILL-A-028 §3.

---

## 5. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-09-02 | CWC-CE-127: 14 Domain 01 rows populated from PRIMARY-LEGAL / GOV-DATA. All dispositions BLANK. Motor fuel not RETAINED. |
| 0.2.0 | 2026-09-02 | CWC-CE-128: destination statutes, TGT KDOR list, 68-2320 pledge, conflict closures, gaming referred. Count remains 14. Dispositions BLANK. |
