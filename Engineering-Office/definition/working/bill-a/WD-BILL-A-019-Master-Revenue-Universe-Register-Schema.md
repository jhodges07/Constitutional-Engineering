# WD-BILL-A-019 — Master Kansas Government Revenue Universe / KLRS Register Schema

**Document ID:** WD-BILL-A-019  
**Title:** Master Kansas Government Revenue Universe / Kansas Legal Revenue Scope Register Schema and Evidence Domains  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-125 (locks candidate schema; does **not** populate findings)  
**Governing Human Intent:** WD-BILL-A-018 / Q-BILL-A-005 Option (a); WD-BILL-A-015 / Q-BILL-A-004; WD-BILL-A-012 / Q-BILL-A-003  
**Governing LOU candidate:** LOU-004 Draft 0.9 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / CANDIDATE SCHEMA LOCKED — DOMAIN 01 EXECUTION IN WD-BILL-A-022 — STATEWIDE REGISTER **NOT** COMPLETE — NOT ACCEPTED  
**Version:** 0.3.0  
**Effective Date:** 2026-09-02  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-019-Master-Revenue-Universe-Register-Schema.md  
**Source ID:** SRC-BILL-A-022  

```text
CANDIDATE MASTER REGISTER SCHEMA
SCHEMA AUTHORITY REMAINS THIS FILE
DOMAIN 01 EXECUTION INSTANCE = WD-BILL-A-022
STATEWIDE REGISTER NOT COMPLETE
BLANK DISPOSITION ≠ RETAIN
KLRS CANDIDACY ≠ FINAL AUTHORIZATION
MOTOR FUEL IS NOT RETAINED
NOT A SPEC
NOT HG-D1 / HG-D2
```

Parent architecture: WD-BILL-A-016. Completeness / execution control: WD-BILL-A-020.

This file **locks** the candidate one-master-register schema and candidate evidence-domain list for later Human-authorized execution. It does **not** invent claims in order to fill rows.

---

## 1. One master register

There is **one** master register for:

- Kansas Government Revenue Universe rows (all material discovered receipts / claims); and
- Kansas Legal Revenue Scope candidacy / later closed-set analysis (compulsory-demand subset only, Q-BILL-A-005 Option (a)).

Architecture: **C with B as mandatory first step** (CWC-CE-124 recommendation; this CWC is that first step). Controlled evidence domains write into this register. Do not create competing inventories.

---

## 2. Minimum schema (candidate; locked for later execution)

| # | Field | Rule |
|---|---|---|
| 1 | MASTER RECORD ID | Stable ID assigned only when a claim/receipt is **discovered by evidence**. Do not invent IDs to complete the schema. |
| 2 | EVIDENCE DOMAIN | Domain 01–12 (or later Human-authorized domain). See §3. |
| 3 | AUTHORITATIVE NAME | Verbatim from PRIMARY-LEGAL / GOV-DATA |
| 4 | COMMON / ALTERNATE NAME | Aliases; used for duplicate normalization |
| 5 | GOVERNMENT LEVEL | state / local / intergovernmental / other **evidenced** class |
| 6 | GOVERNMENT ENTITY / ENTITY CLASS | Who imposes / receives — discover, do not invent the entity universe |
| 7 | RECEIPT OR CLAIM TYPE | Working type from sources; not a final legal taxonomy |
| 8 | COMPULSORY STATUS | YES / NO / UNCERTAIN / EVIDENCE REQUIRED |
| 9 | CURRENT LEGAL AUTHORITY | Citation or `[CITATION/TEXT NEEDED]` / `[LEGAL EFFECT UNKNOWN]` |
| 10 | PAYMENT / REVENUE TRIGGER | Event or condition |
| 11 | LEGALLY OBLIGATED PARTY, IF ANY | Who must pay, if a demand exists |
| 12 | CONSEQUENCE OF NONPAYMENT, IF APPLICABLE | Evidence or `[TO BE VERIFIED]` |
| 13 | ECONOMIC FUNCTION | What the claim/receipt economically attaches to |
| 14 | RATE / CALCULATION / AMOUNT METHOD | **Do not invent rates** |
| 15 | STATED PURPOSE | Legally or publicly stated |
| 16 | REVENUE DESTINATION | Where money goes |
| 17 | FUND / POOL TYPE | General, dedicated, restricted, special, local, trust, enterprise, or other **evidenced** class |
| 18 | ADMINISTRATIVE / OVERHEAD TREATMENT | Deductions / transfers if evidenced |
| 19 | DEBT / BOND / CONTRACT / FEDERAL-MATCH / OTHER DEPENDENCIES | `[LEGAL EFFECT UNKNOWN]` until cited |
| 20 | OFFICIAL COLLECTION / RECEIPT DATA | `[REVENUE EFFECT UNKNOWN]` until retrieved |
| 21 | H.R. 25 KANSAS-MIRROR RELATIONSHIP | WD-BILL-A-009; SRC-BILL-A-015 is federal model only |
| 22 | AGCL 00A–00J CLASSIFICATION | Never SATISFIED by audit alone |
| 23 | CURRENT-STATE STATUS | Evidenced current existence/authority — **not** future authorization |
| 24 | KLRS CANDIDACY | CANDIDATE COMPULSORY CLAIM / OTHER RECEIPT / CLASSIFICATION UNRESOLVED. **Not final authorization.** Option (a): only compulsory claims are KLRS candidates. |
| 25 | HUMAN BILL A DISPOSITION | Default **BLANK**. Values if later Human-set: RETAIN / TRANSFORM / DISAPPEAR / HUMAN DECISION REQUIRED / EVIDENCE INSUFFICIENT. **BLANK ≠ RETAIN.** |
| 26 | POST-BILL-A AUTHORITY STATUS | **NOT DETERMINED** until later Human-controlled engineering |
| 27 | PRIMARY-LEGAL LOCATORS | Constitution / statute / session law / regulation / case / ordinance as located |
| 28 | GOV-DATA LOCATORS | Official fiscal / publication locators |
| 29 | SOURCE DATE / VERSION | As of date of the source used |
| 30 | VERIFICATION STATUS | NOT STARTED / PARTIAL / TRACED / CONFLICT / BLOCKED |
| 31 | CONFLICT / UNKNOWN IDS | CF- / UNK- cross-references |
| 32 | NOTES / TRACEABILITY | Non-authoritative notes; no silent findings |

**Excise / excise-type rows (Domain 01)** SHALL also complete WD-BILL-A-012 §2 questions 1–14.

Do not populate unsupported findings merely to complete the schema.

---

## 3. Candidate evidence domains (organization only)

These labels organize later execution. They are **not** proof that each class exists and are **not** exhaustive.

| Domain | Title | Notes |
|---|---|---|
| 01 | EXCISE / EXCISE-TYPE CLAIMS | **First recommended execution domain.** WD-BILL-A-012 controlling; WD-BILL-A-013 subordinate requirement. Must answer beyond-motor-fuel question from evidence. Privilege/severance/gallonage/pack that **function as excise-type** land here first. |
| 02 | PROPERTY-BASED CLAIMS | Discover; do not invent. Bill B relationship remains Domain G unasked — do not merge Bill B into Bill A. |
| 03 | INCOME / EARNINGS / PRIVILEGE-BASED CLAIMS | Privilege already treated as excise-type in Domain 01 is not double-invented; remainder discovered here. |
| 04 | SALES / USE / CONSUMPTION CLAIMS | H.R. 25 mirror relationship required; stacking tests for surviving excises remain Q-003. |
| 05 | FEES / LICENSES / PERMITS / REGULATORY CLAIMS | Compulsory vs other: field 8. Label is not the test (anti-evasion). |
| 06 | ASSESSMENTS / SPECIAL ASSESSMENTS / LOCAL CLAIMS | Local entity universe discovered, not invented. |
| 07 | FINES / PENALTIES / FORFEITURES / COURT-RELATED RECEIPTS | Not automatically KLRS. Compulsory-demand analysis required; default Option (a) keeps non-demand receipts outside closed set unless Human later adds. |
| 08 | ENTERPRISE / USER / SERVICE RECEIPTS | Mixed compulsory/voluntary likely; UNCERTAIN permitted. |
| 09 | INTERGOVERNMENTAL / FEDERAL / GRANT RECEIPTS | Other-receipt class unless Human later expressly adds to KLRS. |
| 10 | BORROWING / BONDS / FINANCING PROCEEDS | Receipt ≠ demand authority. Debt dependencies still traced (field 19). |
| 11 | INVESTMENT / ASSET / DONATION / OTHER NON-COMPULSORY RECEIPTS | Outside closed demand-authority set unless Human later expressly determines otherwise. |
| 12 | UNCLASSIFIED / DISCOVERED REVENUE PATHWAYS | Catch-all so a pathway cannot vanish because it fits no prior domain. |

Recommended change from a flatter CWC-CE-124 domain list: keep **twelve** domains rather than collapsing 07–11 into one “other receipts” bucket, because Option (a) requires tracing other receipts **without** treating them as demand authority. Collapsing would hide classification work.

---

## 4. Domain 01 priority

Recommend Domain 01 as the **first** Human-authorized execution domain after this foundation.

Reason: the original practical question remains unanswered and must not be answered from AI memory:

**DO KANSANS CURRENTLY PAY EXCISE TAXES OR MATERIALLY EQUIVALENT EXCISE-TYPE CLAIMS BEYOND MOTOR-FUEL / GASOLINE TAXATION?**

**CWC-CE-127:** Domain 01 execution instance WD-BILL-A-022 answers the beyond-motor-fuel question in WD-BILL-A-023 as YES — VERIFIED. That answer is **not** a RETAIN. This schema file remains the authority for fields 1–32. Do not treat WD-BILL-A-022 as a competing schema.  
**CWC-CE-128:** Domain 01 rows updated from closure evidence; count remains 14; gaming referred. Schema authority unchanged.

Motor fuel remains the example of the uniform surviving-excise standard and is **not RETAINED**.

---

## 5. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-09-02 | CWC-CE-125: locked candidate 32-field master schema and Domains 01–12. Register empty. Audit not executed. |
| 0.2.0 | 2026-09-02 | CWC-CE-127: schema authority preserved. Domain 01 rows live in WD-BILL-A-022. Statewide register not complete. |
| 0.3.0 | 2026-09-02 | CWC-CE-128: schema authority preserved. Domain 01 closure in WD-BILL-A-028. Statewide register not complete. |
