# WD-BILL-A-013 — Kansas Excise / Excise-Type Audit Requirement

**Document ID:** WD-BILL-A-013  
**Title:** Kansas Excise and Materially Equivalent Excise-Type Claim — Audit Requirement and Evidence Plan  
**Classification:** Non-Normative Engineering Definition Working Artifact  
**Authority:** Constitutional Engineering Office  
**Governing Work Card:** CWC-CE-123 (defines requirement; does **not** execute the audit); CWC-CE-124 (reconciles this file as **subordinate** to Kansas Legal Revenue Scope — does **not** rewrite Q-BILL-A-003)  
**Governing Human Intent:** WD-BILL-A-012 / Q-BILL-A-003; parent architecture WD-BILL-A-016 / Q-BILL-A-004  
**Governing LOU candidate:** LOU-004 Draft 0.6 — NOT ACCEPTED — HG-D1 NOT PASSED  
**Assigned Agent:** CE — Bill A Definition Engineer  
**Status:** WORKING / REQUIREMENT DEFINED — AUDIT **NOT PERFORMED** — SUBORDINATE TO WD-BILL-A-016 — NOT ACCEPTED  
**Version:** 0.2.0  
**Effective Date:** 2026-09-01  
**Storage Path:** Engineering-Office/definition/working/bill-a/WD-BILL-A-013-Kansas-Excise-Audit-Requirement.md  
**Source ID:** SRC-BILL-A-018  

```text
AUDIT REQUIREMENT / EVIDENCE PLAN
AUDIT NOT EXECUTED UNDER CWC-CE-123 OR CWC-CE-124
SUBORDINATE DOMAIN OF KANSAS LEGAL REVENUE SCOPE (WD-BILL-A-016)
MOTOR FUEL IS NOT RETAINED
NO KANSAS INVENTORY INVENTED
NO RATES / COLLECTIONS / FUND DESTINATIONS INVENTED
AI SYNTHESIS IS NOT KANSAS-LAW EVIDENCE
NO RETAIN / TRANSFORM / DISAPPEAR DISPOSITIONS
NOT A SPEC
NOT HG-D1 / HG-D2
RECOMMENDED NEXT CONTROLLED WORK — NOT SELF-AUTHORIZED
```

---

## 1. Why this artifact exists

Q-BILL-A-003 Human Intent requires a complete evidenced audit of all existing Kansas excise taxes and materially equivalent excise-type revenue claims **before** final disposition under Bill A.

Executing that statewide audit would materially broaden CWC-CE-123 (Definition recording of Human Intent). This file **defines** the excise-domain audit. It does **not** perform it.

**CWC-CE-124 reconciliation (not erasure):** This requirement remains valid. It is now the **EXCISE subordinate domain** of the Kansas Legal Revenue Scope architecture (WD-BILL-A-016). The narrow Q-BILL-A-004 (a)–(g) scope gate is **historically retained and SUPERSEDED** as the complete Q-004 question by WD-BILL-A-015. Privilege, severance, unlabeled gallonage/pack/unit/volume, license/permit-on-commodity, and local-option classes remain on the **excise-type search surface** inside this domain and on the broader KLRS search surface. They are **not** findings and **not** RETAIN decisions.

**Required unanswered evidence question (do not answer from AI memory):** Do Kansans currently pay excise taxes or materially equivalent excise-type claims **beyond motor-fuel / gasoline taxation**?

**Recommended next controlled work:** not a standalone full-state excise execution card. See WD-BILL-A-016 §8 (methodology CWC first, then Domain EXCISE execution into the master KLRS register). Exact CWC number: **not assigned here**.

---

## 2. Scope (working; Human scope-gate remaining)

### 2.1 In-scope (intent)

- All existing Kansas **state** taxes and charges denominated or functioning as **excise** or **excise-type** (including gallonage, pack, privilege-on-commodity/activity, severance, and materially similar unit or activity levies), as discovered from PRIMARY-LEGAL / GOV-DATA — **not** from memory or AI synthesis.  
- For each discovered claim: the fourteen questions in WD-BILL-A-012 §2.  
- H.R. 25 Kansas-mirror stack/overlap test (WD-BILL-A-009; SRC-BILL-A-015).  
- AGCL 00A–00J classification per claim (not satisfaction).  

### 2.2 Out of scope until Human or later CWC expands

- Performing the audit in this CWC.  
- Inventing a list of Kansas excises.  
- RETAIN / TRANSFORM / DISAPPEAR decisions.  
- Statutory drafting; SPEC; HG-D1/HG-D2; publication; commit; push.  
- Fiscal replacement-revenue totals.  
- **Historical (Draft 0.5 / v0.1.0):** local-option excises, license/permit charges, and fee classes that are not clearly excise-type were recorded as scope UNDETERMINED pending narrow Q-BILL-A-004. **CWC-CE-124:** those classes are now on the **KLRS / excise-type search surface** (WD-BILL-A-015 §4). Search-surface inclusion is **not** a finding they exist and **not** a RETAIN. Non-excise fees remain primarily Domain STATE FEE / LOCAL in WD-BILL-A-016 unless evidence shows they function as excise-type.

### 2.3 “Materially equivalent” (historical gate SUPERSEDED as complete Q-004; still live inside this domain)

**Historical:** The Human used “materially equivalent excise-type claims” without enumerating Kansas classes; a bounded Q-BILL-A-004 (a)–(g) was asked (WD-BILL-A-002 v0.5.0).

**CWC-CE-124:** That narrow question is **SUPERSEDED** as the complete Q-004 answer by WD-BILL-A-015. The audit SHALL still specifically evidence whether Kansans pay excise or materially equivalent excise-type claims **beyond motor-fuel / gasoline**. The Domain EXCISE CWC SHALL NOT invent that set from AI memory. Discovery uses PRIMARY-LEGAL / GOV-DATA and the search surface in WD-BILL-A-015 §4.

---

## 3. Evidence plan (source classes, not findings)

Default authority: **NON-AUTHORITATIVE** until verified into the audit register. Classification does not confer engineering authority.

| Plan ID | Need | Required class | Candidate source types (locators to retrieve in audit CWC — **not verified here**) |
|---|---|---|---|
| EV-KS-REV-001 | Complete state revenue-claim inventory (context) | PRIMARY-LEGAL + GOV-DATA | Kansas Statutes Annotated (taxation and related titles — **exact sections [TO BE VERIFIED]**); Kansas Constitution finance/tax/dedication provisions (**exact articles [CITATION/TEXT NEEDED]**); session laws |
| EV-KS-REV-002 | Excise-tax inventory | PRIMARY-LEGAL + GOV-DATA | Same; plus KDOR and KLRD tax-structure publications (**titles/editions [TO BE VERIFIED]**) |
| EV-KS-REV-003 | Materially equivalent claims (privilege, severance, gallonage/pack levies, etc.) | PRIMARY-LEGAL + GOV-DATA | Discovered by search, not by pre-asserted list |
| EV-KS-REV-004 | Stated purpose and statutory disposition | PRIMARY-LEGAL | Enacting/amending statutes; dedicating language |
| EV-KS-REV-005 | Dedicated / special / general fund routing | PRIMARY-LEGAL + GOV-DATA | Statute; State of Kansas ACFR fund statements; agency finance reports |
| EV-KS-REV-006 | Administrative charges or transfers against pools | PRIMARY-LEGAL + GOV-DATA | Statute; appropriation acts; fund transfer language; ACFR notes |
| EV-KS-REV-007 | Constitutional/statutory authority | PRIMARY-LEGAL | Kansas Constitution; KSA; controlling case law **if located** — do not invent holdings |
| EV-KS-REV-008 | H.R. 25 stack/duplicate test | PRIMARY-LEGAL (federal model SRC-BILL-A-015) + Kansas PRIMARY-LEGAL | WD-BILL-A-009 crosswalk |
| EV-KS-REV-009 | Rates / calculation methods | PRIMARY-LEGAL + GOV-DATA | Current statute/admin rule; official rate publications — **do not invent rates** |
| EV-KS-REV-010 | Debt / bond / contract / federal-match dependencies | PRIMARY-LEGAL + GOV-DATA | Bond official statements; indentures; federal grant conditions **if located**; `[LEGAL EFFECT UNKNOWN]` until cited |
| EV-KS-REV-011 | Collections / amounts | GOV-DATA | KDOR statistics; Consensus Revenue Estimate; ACFR — **[REVENUE EFFECT UNKNOWN]** until retrieved |
| EV-KS-REV-012 | AGCL fit | CONTROL-DOC (AGCL 00A–00J) + audit findings | WD-BILL-A-004 method; no control marked satisfied by audit alone |

**Forbidden as Kansas-law or fiscal evidence:** AI-SYNTHESIS (including SRC-BILL-A-010 Grok scout).

**Pin already on file (federal model only):** SRC-BILL-A-015 — H.R. 25 IH PDF. Does **not** substitute for Kansas PRIMARY-LEGAL.

---

## 4. Per-claim audit register (minimum fields)

When the audit CWC executes, each claim row SHALL include at least:

| Field | Rule |
|---|---|
| Claim ID | Stable Bill A audit ID |
| Claim name (as in source) | Verbatim from PRIMARY-LEGAL / GOV-DATA |
| Source locators | Statute/constitution/publication + date |
| Answers to questions 1–14 | Citation or `[TO BE VERIFIED]` / `[CITATION/TEXT NEEDED]` / `[LEGAL EFFECT UNKNOWN]` / `[REVENUE EFFECT UNKNOWN]` |
| H.R. 25 overlap/stack | Crosswalk ID + status |
| AGCL 00A–00J | PROVISIONAL ALIGNMENT / QUESTION REQUIRED / EVIDENCE REQUIRED / POTENTIAL CONFLICT — **never SATISFIED by audit alone** |
| Human disposition | **blank** until Human decision — default blank ≠ RETAIN |

---

## 5. Acceptance criteria (for the future audit CWC)

PASS of the **audit work card** (not this CWC) would require:

1. Inventory method documented; no pre-invented claim list.  
2. Every in-scope discovered claim has 14-question coverage with PRIMARY-LEGAL / GOV-DATA locators or explicit unknown notation.  
3. AI synthesis not used as Kansas law, rate, collection, purpose, destination, or obligation evidence.  
4. H.R. 25 stack/overlap tested or marked BLOCKED/VERIFY.  
5. AGCL classified without self-certification of satisfaction.  
6. No RETAIN/TRANSFORM/DISAPPEAR invented.  
7. No HG-D1, SPEC, HG-D2, legislative draft, publication, maturity change, commit, or push unless a later CWC separately authorizes Git.  
8. Unrelated working-tree files not staged.

This CWC-CE-123 recording does **not** pass those criteria because the audit is **not executed**.

---

## 6. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-09-01 | Defined audit requirement and evidence plan after Q-BILL-A-003 Human Intent. Audit not performed. |
| 0.2.0 | 2026-09-02 | CWC-CE-124: reconciled as subordinate Domain EXCISE of WD-BILL-A-016. Narrow Q-004 marked superseded historically. Beyond-motor-fuel question preserved. Audit still not performed. Motor fuel not RETAINED. |
