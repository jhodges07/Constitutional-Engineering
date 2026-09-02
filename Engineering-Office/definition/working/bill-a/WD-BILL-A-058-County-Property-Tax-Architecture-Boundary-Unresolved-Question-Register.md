# WD-BILL-A-058 — County Property-Tax Architecture Boundary / Unresolved Question Register

**Document ID:** WD-BILL-A-058  
**Title:** County Property-Tax All-In / All-Out Architecture Boundary and Unresolved Question Register  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-139  
**Governing LOU candidate:** LOU-004 Draft 1.6 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / CANDIDATE — NOT ACCEPTED  
**Version:** 1.0.0  
**Effective Date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-058-County-Property-Tax-Architecture-Boundary-Unresolved-Question-Register.md  
**Source ID:** SRC-BILL-A-231  
**Human-intent companion:** WD-BILL-A-057 (SRC-BILL-A-230)

```text
ARCHITECTURE BOUNDARY + UNRESOLVED QUESTIONS
NOT DECISIONS
NOT REQUIREMENTS
NOT A SPEC
NOT LEGISLATION
NOT HUMAN ACCEPTANCE
Q-BILL-A-006 NOT ISSUED
```

This register preserves the CWC-CE-139 architecture boundary and the questions that remain open after Human intent was recorded. It does **not** answer those questions. Companion intent: WD-BILL-A-057.

---

# 1. Architecture boundary (locked as candidate recording)

## 1.1 What county choice applies to

```text
COUNTY CHOICE APPLIES TO PROPERTY-TAX TRANSITION.
```

ALL-IN / ALL-OUT = candidate **property-tax transition boundary**.  
ALL-IN / ALL-OUT ≠ general Bill A opt-in / opt-out.

## 1.2 What county choice does not apply to

```text
COUNTY CHOICE DOES NOT APPLY TO API ACCESS.
COUNTY CHOICE DOES NOT APPLY TO TAXPAYER SUPREMACY.
COUNTY CHOICE DOES NOT APPLY TO RUNTIME REPUBLIC ARCHITECTURE.
```

ALL-OUT ≠ escape from statewide taxpayer controls.

## 1.3 Statewide / non-optional (Human Engineering Intent)

| Component | County-optional? | Status |
|---|---|---|
| API / data access | **NO** | HUMAN INTENT — statewide; no API SPEC |
| Taxpayer Supremacy | **NO** | HUMAN INTENT — statewide; legal implementation OPEN |
| Runtime Republic architecture | **NO** | HUMAN INTENT — statewide architectural objective; not enacted software |
| Transparency / node accountability / collection-and-expenditure visibility | **NO** as candidate association where Q-BILL-A-001 already supports it | CROSS-REFERENCED existing intent; exact contents remain under Definition |
| Property-tax transition | **YES** (county ALL-IN / ALL-OUT) | HUMAN INTENT — candidate mechanism |
| Independent county consumption-tax system | **NO** | County PT election is not authority to create a separate FairTax |

Do not invent additional mandatory statewide components.

## 1.4 Candidate principles (not accepted requirements)

| ID | Principle | Scope |
|---|---|---|
| CP-PT-001 | ALL-IN = complete entry into the defined property-tax transition package | Property-tax transition package only |
| CP-PT-002 | ALL-OUT = non-entry into that package at the applicable decision point | Property-tax transition package only |
| CP-PT-003 | No cherry-picking of legacy PT architecture plus selected replacement benefits | ALL-IN counties |
| CP-PT-004 | County PT transition should be authorized by county voters | Mechanism OPEN |
| CP-PT-005 | Intended ALL-IN end state = zero property-tax authority | Dependencies must be engineered, not used as automatic retention |
| CP-PT-006 | DEPENDENCY ≠ RETAIN | Obligations cannot be ignored |
| CP-PT-007 | A phaseout must not be defeated merely by rising property values or assessed valuations | Mechanism OPEN |
| CP-PT-008 | 5 years = HUMAN CANDIDATE; 7 years = HUMAN CANDIDATE; final duration = HUMAN DECISION REQUIRED | Do not select |
| CP-PT-009 | County variation may produce comparative Kansas evidence (not causation) | Measurement concept only |

---

# 2. Classification vocabulary

| Class | Meaning |
|---|---|
| HUMAN DECISION REQUIRED | The Human Engineer must decide; Cursor shall not infer |
| ENGINEERING REQUIRED | Later controlled engineering; not this CWC |
| LEGAL RESEARCH REQUIRED | Primary-legal evidence not yet sufficient |
| LEGAL INTERPRETATION REQUIRED | Text located; legal effect on the contemplated architecture not established |
| FISCAL RESEARCH REQUIRED | Quantity / incidence / equalization research not authorized here |
| NOT YET DETERMINED | Recorded as open; do not treat silence as a decision |
| CONTROLLED EVIDENCE (CONTEXT ONLY) | Existing Domain 02 / LOU artifacts frame the question; not a disposition |

---

# 3. Unresolved question register

These IDs are **not** Q-BILL-A-006. They are deferred Definition questions. Do not manufacture a Human questionnaire item merely because a number is available.

### UQ-PT-001 — Phaseout duration

| Field | Value |
|---|---|
| Question | 5-year or 7-year property-tax phaseout for an ALL-IN county? |
| Status | **HUMAN DECISION REQUIRED** |
| Recording | 5 YEARS: HUMAN CANDIDATE. 7 YEARS: HUMAN CANDIDATE. FINAL DURATION: HUMAN DECISION REQUIRED. |
| LOU-001 five-year statewide mandate | **NOT TRANSFERRED** into LOU-004 as selected duration (LOU-004 §2.8) |
| This CWC | Does not select |

### UQ-PT-002 — Phaseout baseline (what declines)

| Field | Value |
|---|---|
| Question | What engineered measure declines during the transition: mill rate; property-tax revenue authority; levy dollars; controlled base-year levy; or another measure? |
| Status | **HUMAN DECISION REQUIRED** + **ENGINEERING REQUIRED** |
| Constraint | A phaseout must not be defeated merely by rising property values or assessed valuations |
| This CWC | Does not select mathematics; does not calculate a schedule |

### UQ-PT-003 — ALL-IN reversibility

| Field | Value |
|---|---|
| Question | Can an ALL-IN county later return to property taxation? If yes: when, how often, under what voter threshold? Does ALL-IN become irreversible after activation? Does zero property tax become a permanent exit point? |
| Status | **HUMAN DECISION REQUIRED** |
| This CWC | Does not decide |

### UQ-PT-004 — ALL-OUT later entry

| Field | Value |
|---|---|
| Question | Can an ALL-OUT county later elect ALL-IN? If yes: when, how often, under what voter threshold, after what waiting period? |
| Status | **HUMAN DECISION REQUIRED** |
| This CWC | Does not decide |

### UQ-PT-005 — ALL-OUT permanence / reconsideration

| Field | Value |
|---|---|
| Question | Does ALL-OUT mean later reconsideration, another election, a waiting period, a terminal statewide deadline, or permanent legacy property taxation? |
| Status | **NOT YET DETERMINED** / **HUMAN DECISION REQUIRED** |
| Forbidden inference | ALL-OUT ≠ permanent property-tax authority; ALL-OUT ≠ escape from statewide Bill A controls |

### UQ-PT-006 — Terminal statewide deadline

| Field | Value |
|---|---|
| Question | Does Bill A/B ultimately establish a statewide terminal date after which property taxation ends even for counties that previously remained ALL-OUT? |
| Possible states | NO TERMINAL DEADLINE · TERMINAL DEADLINE · **HUMAN DECISION REQUIRED** |
| Status | **HUMAN DECISION REQUIRED** |
| This CWC | Does not choose |

### UQ-PT-007 — Voter-authorization mechanism

| Field | Value |
|---|---|
| Candidate principle | County property-tax transition should be authorized by county voters |
| Open mechanism | Election; referendum; petition; county resolution plus election; constitutional authority; statutory authority; other |
| Status | **HUMAN DECISION REQUIRED** + **LEGAL RESEARCH REQUIRED** |
| This CWC | Does not draft election statutes |

### UQ-PT-008 — City / in-county jurisdiction binding

| Field | Value |
|---|---|
| Question | Does a county ALL-IN election bind all property-taxing jurisdictions geographically within that county (including cities) for purposes of the property-tax transition? |
| Domain 02 context | KRU-D02-006 (county) and KRU-D02-007 (city) are separate claim-category classes |
| Status | **HUMAN DECISION REQUIRED** |
| This CWC | Does not invent a candidate answer |

### UQ-PT-009 — Special-district / township / community-college binding

| Field | Value |
|---|---|
| Question | How does the county transition boundary interact with townships, fire districts, library districts, community colleges, other taxing subdivisions, and special districts? |
| Domain 02 context | KRU-D02-008; KRU-D02-009; UNK-D02-010 (types evidenced; every enabling section not fetched) |
| Status | **HUMAN DECISION REQUIRED** + **ENGINEERING REQUIRED** + **LEGAL RESEARCH REQUIRED** |
| This CWC | Does not invent the answer |

### UQ-PT-010 — Cross-county school district / mixed ALL-IN–ALL-OUT geography

| Field | Value |
|---|---|
| Issue | A school district may cross or otherwise interact with county boundaries |
| Framing evidence | KRU-D02-002 statewide 20-mill remitted to the state school district finance fund; KRU-D02-003/004/005 local USD mills; Art. 6 §6(b) DEPENDENCY VERIFIED as legislative duty (WD-BILL-A-035) |
| Open questions | Mixed-county property in one USD; obligation allocation; indirect burden shift onto the remaining county; equalization vs county choice |
| Status | **ENGINEERING REQUIRED** + **LEGAL RESEARCH REQUIRED** + **LEGAL INTERPRETATION REQUIRED** + **FISCAL RESEARCH REQUIRED** |
| Geographic USD-span inventory | **LEGAL RESEARCH REQUIRED** — not executed as a statewide inventory in Domain 02 |
| This CWC | Frames only; does not solve; does not reopen Domain 02 |

### UQ-PT-011 — Statewide 20-mill USD levy vs county choice

| Field | Value |
|---|---|
| Issue | KRU-D02-002 is a statewide USD mill remitted to a state fund. County ALL-IN / ALL-OUT is a county property-tax transition choice. |
| Status | **ENGINEERING REQUIRED** + **LEGAL RESEARCH REQUIRED** |
| Forbidden inference | Do not treat the 20-mill as RETAIN or DISAPPEAR |

### UQ-PT-012 — Which Domain 02 claims are inside the ALL-IN package

| Field | Value |
|---|---|
| Issue | ALL-IN may ultimately affect multiple Domain 02 claims (general ad valorem, USD mills, city/county/township/special-district mills, state building mills, in-lieu motor-vehicle/RV, utility, mineral, 16M/20M) |
| Status | **ENGINEERING DEFINITION REQUIRED** |
| This CWC | Does not mark RETAIN / TRANSFORM / DISAPPEAR |

### UQ-PT-013 — Existing debt / pledged revenue / impairment

| Field | Value |
|---|---|
| Principles | EXISTING DEBT DEPENDENCY ≠ PERMANENT PROPERTY-TAX RETENTION. EXISTING OBLIGATIONS CANNOT BE IGNORED. |
| Later engineering (not now) | Debt inventory; pledged-revenue analysis; maturity schedules; refinancing; replacement pledge; sinking funds; transition reserves; legal impairment analysis |
| Domain 02 context | KRU-D02-005; 10-113 DEPENDENCY VERIFIED; UNK-D02-008 LEGAL EFFECT UNKNOWN |
| Status | **ENGINEERING REQUIRED** + **LEGAL RESEARCH REQUIRED** / **LEGAL INTERPRETATION REQUIRED** |
| This CWC | Does not design mechanisms |

### UQ-PT-014 — Replacement revenue / distribution

| Field | Value |
|---|---|
| Issue | Replacement / distribution architecture for ALL-IN counties; relationship of statewide consumption taxation to county property-tax replacement distribution |
| Status | **NOT YET ENGINEERED** |
| Forbidden this CWC | FairTax rate calculation; replacement-revenue calculation; future state/local distribution formula; independent county consumption-tax systems |

### UQ-PT-015 — Bill A / Bill B allocation

| Field | Value |
|---|---|
| Candidate | Bill A = statewide tax-system architecture + API + Taxpayer Supremacy + Runtime Republic + county PT transition authority/interface. Bill B = PT elimination mechanics + ALL-IN/ALL-OUT implementation + 5/7-year phaseout + PT end state |
| LOU-001 | Different candidate split (Bill B = five-year mandate; Bill A = comprehensive replacement **plus** same five-year destination) — NOT ACCEPTED into LOU-004; NOT TRANSFERRED |
| Status | **HUMAN DECISION REQUIRED** |
| This CWC | Candidate only; no final allocation; Bill B artifacts unmodified |

### UQ-PT-016 — Constitutional / legal permissibility of county ALL-IN / ALL-OUT

| Field | Value |
|---|---|
| Topics | Uniformity/classification; school finance; local taxing authority; home rule; county authority; special districts; bond obligations; equal protection/uniform operation; state/local revenue authority |
| Status | **LEGAL RESEARCH REQUIRED** / **LEGAL INTERPRETATION REQUIRED** |
| This CWC | No legality conclusion; no constitutional amendment |

### UQ-PT-017 — Property-tax transition package contents

| Field | Value |
|---|---|
| Issue | No-cherry-picking requires a defined package. Exact contents are not closed by this CWC. |
| Status | **ENGINEERING DEFINITION REQUIRED** |
| Constraint | Package definition SHALL NOT be used to convert ALL-OUT into a general Bill A opt-out |

### UQ-PT-018 — Comparative-signal implementation

| Field | Value |
|---|---|
| Candidate | ALL-IN vs ALL-OUT results: taxpayer cost; government performance; economic signals; property/housing signals; revenue stability; accountability signals |
| Status | **ENGINEERING REQUIRED** (later); measurement concept only |
| Forbidden | Causation claims; econometric-study design under this CWC |

### UQ-PT-019 — Sinking-fund / phaseout coupling

| Field | Value |
|---|---|
| Candidate relationship | Property-tax phaseout ↔ sinking-fund discipline (WD-BILL-A-007 §8) |
| Status | **ENGINEERING REQUIRED** |
| Forbidden this CWC | Funding-amount calculations; specific fund designs |

### UQ-PT-020 — Exact statewide mandatory architecture contents

| Field | Value |
|---|---|
| Locked now | API, Taxpayer Supremacy, and Runtime Republic are statewide / non-county-optional Human intent |
| Remainder | Exact contents of other statewide controls remain subject to controlled Definition |
| Status | **ENGINEERING DEFINITION REQUIRED** |
| Constraint | Do not invent additional mandatory components in this cycle |

---

# 4. Domain / gate / certification firewall (unchanged)

| Item | Status |
|---|---|
| Domain 01 | 14 verified records; SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS; dispositions **BLANK** |
| Domain 02 | 16 verified records; SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS; dispositions **BLANK** — **not reopened** |
| Domain 03 | 5 verified records; SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS; dispositions **BLANK** |
| Domain 04 | 5 verified records; SUBSTANTIALLY COMPLETE WITH EXPLICIT GAPS; dispositions **BLANK** |
| Arithmetic total | 40 verified claim-category records. **40 ≠ retained taxes. 40 ≠ future Bill A claims.** |
| Revenue Universe | **NOT CERTIFIED** |
| KLRS | **NOT CERTIFIED** |
| Domain 05 | **NOT EXECUTED** |
| HG-D1 | **NOT PASSED** |
| SPEC | **NONE** |
| HG-D2 | **NOT PASSED** |
| Bill A maturity | **19% UNCHANGED** |
| LOU-004 | **DRAFT / CANDIDATE / NOT HUMAN-ACCEPTED** |

---

# 5. AGCL mapping note

AGCL classifications for this cycle live in WD-BILL-A-004. Permitted classes only:

**PROVISIONAL ALIGNMENT · QUESTION REQUIRED · EVIDENCE REQUIRED · POTENTIAL CONFLICT · NOT APPLICABLE**

No AGCL control may be marked **SATISFIED**.

---

Libertas sine lapsu — Liberty without drift.
