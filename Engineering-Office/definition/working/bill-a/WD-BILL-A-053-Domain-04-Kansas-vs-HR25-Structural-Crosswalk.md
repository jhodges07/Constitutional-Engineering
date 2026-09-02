# WD-BILL-A-053 — Domain 04 Kansas vs H.R. 25 Structural Crosswalk

**Document ID:** WD-BILL-A-053  
**Title:** Domain 04 Kansas Current Sales / Use Architecture vs H.R. 25 FairTax Structural Crosswalk  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-136; CWC-CE-137 (closure)  
**H.R. 25 pin:** SRC-BILL-A-015 (federal model); WD-BILL-A-009  
**Governing Human Intent (crosswalk only):** WD-BILL-A-008 / Q-BILL-A-002  
**Governing LOU candidate:** LOU-004 Draft 1.5 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / COMPARISON ONLY — NOT A DISPOSITION — NOT KANSAS LAW  
**Version:** 0.2.0  
**Effective Date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-053-Domain-04-Kansas-vs-HR25-Structural-Crosswalk.md  

```text
CURRENT KANSAS SALES / USE TAX ≠ H.R. 25 FAIRTAX
H.R. 25 = FEDERAL ECONOMIC MODEL, NOT KANSAS LAW
SIMILARITY ≠ EQUIVALENCE
STRUCTURAL MATCH ≠ RETAIN
MATERIAL STRUCTURAL DIFFERENCE ≠ DISAPPEAR
NO FUTURE BILL A DESIGN
NO KANSAS FAIRTAX RATE
SEPARATE SUBSTANTIVE ECONOMIC STANDARD FROM FEDERAL IMPLEMENTATION MACHINERY
```

Human intent to **mirror the exact H.R. 25 substantive economic standard**, adapted only where Kansas jurisdiction requires, is a **crosswalk**, not a current-law finding and not a RETAIN of Kansas RST.

---

## 1. Classification vocabulary (this CWC)

| Class | Meaning |
|---|---|
| STRUCTURAL MATCH | Current Kansas feature and H.R. 25 substantive economic standard align in function |
| PARTIAL STRUCTURAL MATCH | Some overlap; not equivalence |
| MATERIAL STRUCTURAL DIFFERENCE | Evidenced architectures differ in a way that would matter if Bill A later mirrors H.R. 25 |
| FEDERAL-SPECIFIC | H.R. 25 federal administrative machinery — do not silently treat as Kansas law |
| KANSAS-SPECIFIC | Kansas current-law feature without H.R. 25 analogue, or Kansas-only overlay |
| EVIDENCE REQUIRED | Comparison blocked without additional authoritative text |
| NOT APPLICABLE | Feature does not exist on one side in a comparable form |

---

## 2. High-priority business-purpose crosswalk

H.R. 25 (XW-HR25-004 / proposed IRC §102): business-purpose and investment-purpose purchases are **not taxed as final consumption**.

| Feature | Current Kansas | H.R. 25 (controlled project evidence) | Class |
|---|---|---|---|
| General business-purpose exemption | **Not located.** Category exemptions only (79-3606(m)/(n)/(kk) and others) | General business-purpose / investment-purpose exclusion from final consumption | **MATERIAL STRUCTURAL DIFFERENCE** |
| Resale | 79-3602(jj) sale other than for resale; ST-28A | Intermediate sales not taxed as final consumption | **PARTIAL STRUCTURAL MATCH** — resale ≠ full business-purpose |
| Production / ingredients | 79-3606(m) ingredient/component | Intermediate production inputs | **PARTIAL STRUCTURAL MATCH** |
| Manufacturing machinery | 79-3606(kk) integrated production machinery/equipment | Business-purpose capital | **PARTIAL STRUCTURAL MATCH** — bounded industrial definition; not all business equipment |
| Business services | Only if enumerated in 79-3603; most professional services **not listed** | Taxable services as final consumption; business-purpose services not final consumption | **MATERIAL STRUCTURAL DIFFERENCE** (both directions: Kansas narrower on services, broader on taxing unlisted business purchases of TPP) |
| Business consumables | Taxable unless (n) consumed-in-production or other listed exemption | Business-purpose not final consumption | **MATERIAL STRUCTURAL DIFFERENCE** |
| Utilities | Residential/ag state 0% on specified delivered fuels; commercial generally taxable unless exempted | Business vs household consumption under H.R. 25 standard | **MATERIAL STRUCTURAL DIFFERENCE** / **KANSAS-SPECIFIC** rate patchwork |
| Construction inputs | Contractor materials generally taxed (79-3603(l)); PEC for listed public/nonprofit projects | Business-purpose construction inputs vs household | **MATERIAL STRUCTURAL DIFFERENCE** |
| Mixed use | No general percentage statute located | H.R. 25 mixed-use standard (Human intent = exact H.R. 25) | **MATERIAL STRUCTURAL DIFFERENCE** / **NO GENERAL EQUIVALENT LOCATED** |
| Business-to-personal conversion | 79-3703(e); PEC misuse; inventory personal use examples | H.R. 25 conversion standard | **PARTIAL STRUCTURAL MATCH** (category-specific only) |
| Investment purpose | No general investment-purpose consumption exemption located | Investment-purpose purchases not final consumption | **MATERIAL STRUCTURAL DIFFERENCE** / **EVIDENCE REQUIRED** if a narrow Kansas analogue exists outside 79-3606 |

**Do not convert these findings into future Bill A requirements** beyond already-recorded Human intent.

---

## 3. High-priority used-property crosswalk

H.R. 25 (XW-HR25-001 / proposed IRC §2(14)): taxable “property” **excludes used property**.

| Feature | Current Kansas | H.R. 25 | Class |
|---|---|---|---|
| New property sold at retail | Taxable (79-3603(a)) unless exempted | Taxable as new final consumption (federal model) | **PARTIAL STRUCTURAL MATCH** |
| Used property generally | **No general used-goods exemption** | Used property excluded from “property” | **MATERIAL STRUCTURAL DIFFERENCE** |
| Private casual / isolated sale | Generally **exempt** (79-3606(l); 79-3602(q)) | Used / not new final consumption | **PARTIAL STRUCTURAL MATCH** (casual TPP) |
| Dealer / retailer sale of used property | Generally **taxable** | Used property excluded | **MATERIAL STRUCTURAL DIFFERENCE** |
| Trade-in | Sales-price rules in 79-3602 / KS-1510 (bounded) | Federal used-property / trade-in machinery | **EVIDENCE REQUIRED** for exact H.R. 25 trade-in text vs Kansas sales-price; do not invent |
| Motor vehicle | Isolated/occasional **taxable** (79-3603(o)); dealer sales taxable | Used vs new under H.R. 25 | **MATERIAL STRUCTURAL DIFFERENCE** (Kansas taxes isolated vehicles) |
| Used manufactured/mobile homes | 79-3606(bb) exempts other than original retail sale | Used property | **PARTIAL STRUCTURAL MATCH** (narrow class) |

**Do not assume USED = EXEMPT or USED = TAXABLE** as a single Kansas rule.

---

## 4. High-priority services crosswalk

| Question | Current Kansas evidence | H.R. 25 | Class |
|---|---|---|---|
| Starting rule | **ONLY ENUMERATED / SPECIFIC SERVICES** in 79-3603 | Broad final-consumption **taxable services** (with defined exclusions) | **MATERIAL STRUCTURAL DIFFERENCE** |
| Major gap if Bill A later mirrors H.R. 25 | Many consumer services **not** in 79-3603; Kansas **does** tax listed services (lodging, repair, telecom, meals, etc.) | Would tax a broader household-service set; would exclude business-purpose services | Comparison only — **no gap-closing design** |
| Use tax on services | KDOR: **labor services not subject to use tax** | Federal consumption of services | **KANSAS-SPECIFIC** sales/use split |

---

## 5. Mixed-use / conversion crosswalk

| Item | Class | Evidence |
|---|---|---|
| General H.R. 25 mixed-use equivalent in Kansas | **NOT LOCATED** as a general statute | UNK-D04-003 **PARTIALLY RESOLVED — NO GENERAL EQUIVALENT LOCATED** |
| Use-tax subsequent-use rule | **PARTIAL STRUCTURAL MATCH** | 79-3703(e) |
| Category-specific mechanisms | **PARTIAL STRUCTURAL MATCH** | PEC misuse; inventory withdrawal (KS-1510) |
| Architecture class | **CATEGORY-SPECIFIC MECHANISMS ONLY** | WD-BILL-A-055 |
| Future design | **NOT AUTHORIZED** | — |

---

## 6. Other structural similarities / differences

| Feature | Class | Notes |
|---|---|---|
| Retail consumption event exists | **PARTIAL STRUCTURAL MATCH** | Kansas RST is a consumption-type tax; it is **not** H.R. 25 |
| Destination combined rate | **PARTIAL STRUCTURAL MATCH** / **KANSAS-SPECIFIC** local overlays | Important for later distribution engineering; **no formula designed** |
| Food | **MATERIAL STRUCTURAL DIFFERENCE** | Kansas state food rate 0%; local remains. H.R. 25 taxes new final consumption including food (federal model). **Do not design** Kansas food treatment. |
| Prebate / family consumption allowance | **FEDERAL-SPECIFIC** / **NOT APPLICABLE** to current Kansas RST | Do not calculate a prebate |
| Retailer compensation | **FEDERAL-SPECIFIC** | Kansas retailer is a collector of RST; not H.R. 25 compensation design |
| SSUTA / Streamlined registration | **KANSAS-SPECIFIC** administration | Not H.R. 25 federal machinery |
| Marketplace facilitator / remote seller | **KANSAS-SPECIFIC** collection | Not extra claims; not silently imported federal Wayfair machinery as H.R. 25 |
| State/local split; CID/TDD/STAR | **KANSAS-SPECIFIC** | H.R. 25 is a federal bill |
| Compensating use tax | **KANSAS-SPECIFIC** legal form | Complementary to RST |
| 18% of rate to SHF | **KANSAS-SPECIFIC** destination | Not an H.R. 25 feature |
| Enumerated vs inclusive service base | **MATERIAL STRUCTURAL DIFFERENCE** | §4 |
| Used retailer goods | **MATERIAL STRUCTURAL DIFFERENCE** | §3 |

---

## 7. Federal machinery firewall

Do **not** treat as Kansas law or as automatic Bill A machinery:

- federal IRS administration;
- federal “United States” geographic definitions;
- federal employer classifications;
- §801 financial-intermediation rules (XW-HR25-001);
- federal export definitions;
- federal prebate delivery;
- federal criminal provisions.

**SUBSTANTIVE ECONOMIC STANDARD** (final consumption of new property/services; business-purpose; used property) remains the Human-intent mirror target. **FEDERAL-SPECIFIC IMPLEMENTATION MACHINERY** remains federal.

---

## 8. Disposition firewall

Every comparison class above is **evidence analysis**.

- STRUCTURAL MATCH ≠ RETAIN.  
- MATERIAL STRUCTURAL DIFFERENCE ≠ DISAPPEAR.  
- Field 25 remains **BLANK**.  
- Field 26 remains **NOT DETERMINED**.
