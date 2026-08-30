# WSMAT-001 — KSB Status Maturity Measurement

**Document ID:** WSMAT-001  
**Title:** KSB Status Maturity Measurement  
**Classification:** Engineering Specification (Weekly-Status Maturity Algorithm)  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001  
**Governing Standards:** STD-001; STD-011 Part B; STD-014; WF-001  
**Governing ECR:** ECR-005 — KSB Status Maturity Measurement Control  
**Governing Work Card:** CWC-CE-085  
**Status:** Active  
**Version:** 1.0.0  
**Effective Date:** 2026-08-30  
**Preparing Agent:** CE-Engineer  
**Activation Authority:** ECR-005 Human-accepted / locally implemented under CWC-CE-085  

```text
ACTIVE LOCALLY UNDER ECR-005 / STD-011 v1.3.0
DOES NOT CERTIFY BILL PERCENTAGES BY ITSELF
DOES NOT ACCEPT ANY LOU
GIT CANONICALIZATION PENDING HUMAN GIT GATES
```

**Predecessor proposal (historical):** `PROPOSED-MATURITY-MEASUREMENT-CWC-CE-085.md` (WSMAT-001-PROPOSED 0.1.0-PROPOSED)

---

## 1. Purpose

Define the deterministic algorithm by which Bill A/B/C **CALCULATED MATURITY** is produced for BlueprintLiberty Weekly Public Engineering Status packages.

Human Engineer **CERTIFIED KSB MATURITY** remains required before operative use of `BILL_*_PERCENT` under STD-011.

---

## 2. Normative vs Implementation

| Kind | Content |
|---|---|
| **NORMATIVE** | Stage spine, weights, states, evidence classes, hard gates, rounding, snapshot, roles, identity rules |
| **IMPLEMENTATION DETAIL** | Ledger formatting cosmetics; evaluator tooling; file-layout convenience under weekly-status |

---

## 3. Maturity Question

The percentage answers only:

> How far has this bill legitimately progressed through the controlled legislative engineering process based on verified evidence?

It SHALL NOT represent political popularity, polling, election probability, AI confidence, text volume, file count, calendar elapsed time, or uncontrolled-draft appearance.

---

## 4. Visual VSM Maturity Spine (v1.0)

### 4.1 Public spine

The Human Engineer accepts the 13-stage KSB Value Stream Map as the v1.0 maturity spine.

Canonical stage identifiers and public display labels:

| ID | Public display label (v1.0) |
|---|---|
| KS-S01 | Citizen Problem / Political Idea |
| KS-S02 | Human Engineering Intent |
| KS-S03 | Research & Evidence |
| KS-S04 | Letter of Understanding — LOU |
| KS-S05 | Requirements / SPEC |
| KS-S06 | Constitutional & AGCL Control Evaluation |
| KS-S07 | Legislative Engineering |
| KS-S08 | Engineering & Legal Review |
| KS-S09 | Public Review & Signal |
| KS-S10 | Human Acceptance |
| KS-S11 | Controlled Git Version |
| KS-S12 | Publication |
| KS-S13 | Future Runtime Republic Digital Twin |

### 4.2 Baseline verification note

Accepted visual baseline: `baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png` (immutable SHA-256 `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9`).

Exact glyph-level OCR of baseline stage text was **not** machine-verified in the authorization package drafting session. Public display labels above are the Human-accepted conceptual/v1.0 spine from CWC-CE-085. If Human review finds baseline wording differs, **public display labels SHALL be corrected to match the baseline**; canonical IDs KS-S01…KS-S13 remain stable. The baseline image SHALL NOT be silently edited.

### 4.3 Operational authority

Visual VSM alone does **not** declare a stage complete.

Operational gate completion derives from STD-001 / WF-001 (and applicable artifact lifecycle controls). Stage credit requires controlled evidence per this specification.

Engineering Definition relationship (STD-001 §4.1):

```text
Human Engineering Intent → Research → LOU → HG-D1 → SPEC → HG-D2 → Controlled Execution…
```

---

## 5. Weighting (v1.0)

```text
TOTAL_STAGE_UNITS = 13.0
full stage credit  = 1.0 stage unit
```

Equal weighting: each stage has identical maximum weight.

---

## 6. Rounding

```text
raw_maturity = 100 × credited_stage_units / 13
public_percent = round_half_up(raw_maturity)
```

**round_half_up:** fractional part ≥ 0.5 rounds away from zero toward the next integer; otherwise toward zero.  
Example: 7.5 → 8; 26.5 → 27; 26.49 → 26.

Do **not** use language-default banker rounding if it differs from half-up.

Clamp final display to integer range **0…100** inclusive. Algorithm design SHALL NOT produce values outside that range under valid inputs; out-of-range is a defect.

No false-precision decimals on the public image.

---

## 7. General Stage-State Model (v1.0)

Enumerated credits only:

| State | Code | Stage units |
|---|---|---|
| NOT_STARTED | NS | 0.00 |
| IN_DEVELOPMENT | ID | 0.50 |
| READY_FOR_REVIEW | RR | 0.75 |
| COMPLETE / ACCEPTED | CA | 1.00 |

Rules:

1. Only one state applies per stage per bill per evidence snapshot.  
2. READY_FOR_REVIEW ≠ HUMAN-ACCEPTED.  
3. Partial credit does **not** satisfy a Human Gate, authorize the next stage, imply acceptance, or unlock downstream maturity.  
4. Subjective intermediate values (e.g., 0.33) are **forbidden** in v1.0.

Stages with Human-gate completion semantics use CA only when the applicable Human acceptance event is recorded.

---

## 8. Evidence Classification

| Class | Meaning | May earn credit? |
|---|---|---|
| CONTROLLED | Tracked/accepted Engineering Office artifact or explicitly Human-accepted controlled record | Yes, if criteria met |
| RECOGNIZED_DRAFT | Engineering Definition draft under STD-001 process with document identity (may be local pending Git) | Yes for draft states only |
| INFORMATIVE | Research packs, AI synthesis, packages | Supports S03 per criteria; not gate acceptance |
| PUBLIC_PIN | STD-011 public FIXED title pin | Limited; see S01 |
| UNVERIFIED / UNKNOWN | Missing or non-reconstructible | **No credit** |
| CONVERSATION_ONLY | Chat memory / discussion without artifact | **No credit** |

Silence ≠ acceptance. AI SHALL NOT invent missing evidence.

---

## 9. Stage Evidence Criteria (v1.0)

### 9.1 KS-S01 — Citizen Problem / Political Idea

| State | Evidence |
|---|---|
| NS | No controlled statement of the citizen problem / political idea for this Bill identity |
| ID | Controlled or recognized draft problem statement exists but incomplete / unstable |
| RR | Explicit readiness-for-Human-review of the problem statement recorded in controlled artifact |
| CA | Human Engineer has accepted a problem/idea statement for this Bill **or** a Human-accepted public Bill title pin exists that uniquely identifies the legislative object for weekly status **and** a controlled problem statement is present in a recognized Engineering Definition draft for that same Bill identity |

**Note:** Public title pin alone without any Engineering Definition problem statement → maximum **ID (0.50)** for S01, not CA.

### 9.2 KS-S02 — Human Engineering Intent

| State | Evidence |
|---|---|
| NS | No HE intent recorded for this Bill |
| ID | Intent appears in recognized Engineering Definition draft (e.g., LOU draft sections) but incomplete |
| RR | Explicit readiness for Human review of intent recorded |
| CA | Human Engineer acceptance of intent for this Bill recorded (may be via HG-D1 on an LOU that states intent, or other explicit HE acceptance record). Public title pin alone ≠ CA |

### 9.3 KS-S03 — Research & Evidence

| State | Evidence |
|---|---|
| NS | No research record / evidence annex / recognized research package for this Bill |
| ID | Informative research artifacts exist with identifiable provenance (STD-001 §4.5 fields as available) |
| RR | Research package explicitly marked ready for Human review |
| CA | Human Engineer accepts that research sufficiency for LOU advancement is met **or** accepted LOU (HG-D1) incorporates a research annex satisfying STD-001 §4.5 minimum fields |

Research remains informative; CA for S03 does **not** create engineering requirements authority.

### 9.4 KS-S04 — Letter of Understanding (LOU)

| State | Evidence |
|---|---|
| NS | No recognized LOU draft for this Bill legislative object |
| ID | Recognized LOU draft exists; Acceptance Status ≠ ACCEPTED; HG-D1 not passed |
| RR | Controlled artifact explicitly declares LOU ready for Human HG-D1 review |
| CA | Valid Human Engineer HG-D1 acceptance recorded for that LOU |

`IN_DEVELOPMENT ≠ HG-D1 PASSED`. `READY_FOR_REVIEW ≠ HG-D1 PASSED`. Silence ≠ HG-D1.

### 9.5 KS-S05 — Requirements / SPEC

| State | Evidence |
|---|---|
| NS | No SPEC/requirements draft for this Bill |
| ID | Recognized SPEC/requirements draft exists |
| RR | Explicit ready-for-HG-D2 review |
| CA | HG-D2 acceptance recorded |

**Hard gate:** If HG-D1 unsatisfied for this Bill → S05 credited units = **0.00** regardless of drafts.

### 9.6 KS-S06 — Constitutional & AGCL Control Evaluation

| State | Evidence |
|---|---|
| NS / ID / RR / CA | Controlled evaluation artifacts for this Bill against constitutional/AGCL constraints |

**Hard gate:** Requires HG-D1; otherwise 0.00.

### 9.7 KS-S07 — Legislative Engineering

| State | Evidence |
|---|---|
| NS / ID / RR / CA | Controlled legislative drafting artifacts for this Bill under Legislative Manager / STD-008 authority as applicable |

**Hard gate:** Requires HG-D1 and HG-D2 (unless HE expressly waives Definition for that work under STD-001 — waiver must be explicit in authorizing CWC). Without gates → 0.00.

### 9.8 KS-S08 — Engineering & Legal Review

Controlled review records for this Bill.  
**Hard gate:** Requires S07 CA predecessor authority chain (HG-D1/HG-D2 as applicable). Else 0.00.

### 9.9 KS-S09 — Public Review & Signal

Controlled public-review release authorization for this Bill (not weekly-status packaging alone).  
**Hard gate:** Requires applicable prior engineering gates. Else 0.00.

### 9.10 KS-S10 — Human Acceptance

Maps primarily to WF-001 **HG-3** (Human Acceptance of the governed work product for that Bill cycle), not HG-D1/HG-D2.  
CA only on recorded HG-3 (or explicit HE acceptance record for that artifact).  
**Hard gate:** Prior mandatory gates for that work must be satisfied. Else 0.00.

### 9.11 KS-S11 — Controlled Git Version

Maps to WF-001 **HG-4 / HG-5** evidence: approved commit/push of the governing Bill artifacts.  
CA requires reconstructible SHA for the accepted Bill artifact set.  
**Hard gate:** HG-3 (or applicable acceptance) required before Git maturity credit. Else 0.00.

### 9.12 KS-S12 — Publication

Maps to WF-001 **HG-6** publication authorization for the Bill legislative/public package.  
Weekly KSB Status publication alone does **not** complete S12 for the Bill.  
**Hard gate:** Prior gates required. Else 0.00.

### 9.13 KS-S13 — Future Runtime Republic Digital Twin

| State | Evidence |
|---|---|
| NS | Default until controlled Digital Twin integration requirements for this Bill exist |
| ID / RR | Controlled candidate/runtime integration specs exist |
| CA | Human-accepted controlled integration of this Bill into authorized Digital Twin / runtime observability scope |

**Hard gate:** Requires Publication CA (S12) unless a later Active CONTROL expressly authorizes parallel credit. Else 0.00.

---

## 10. Hard-Gate Ceiling Rules

### 10.1 General rule

A mandatory unsatisfied Human Gate prevents maturity credit for any stage whose authority depends on that gate.

Downstream drafts may be recorded in the ledger as:

```text
DOWNSTREAM WORK EXISTS — MATURITY CREDIT BLOCKED
```

without affecting the percentage.

### 10.2 Gate inventory (maturity-relevant)

| Gate | Blocks maturity for |
|---|---|
| **HG-D1** (LOU Acceptance) | KS-S05…KS-S13 (and any stage defined to require accepted LOU) |
| **HG-D2** (Requirements Acceptance) | KS-S07…KS-S13 when Engineering Definition applies (unless explicit HE waiver) |
| **HG-3** (Human Acceptance) | KS-S11…KS-S13 for that work product |
| **HG-4 / HG-5** (Git) | KS-S11 CA; publication readiness dependent on shared history when required |
| **HG-6** (Publication) | KS-S12 CA |
| **HG-8** (Baseline) | Only when maturity claim depends on declaring/amending an Engineering Baseline |

Distinct Human decisions SHALL NOT be collapsed into one maturity event.

### 10.3 Current preserved fact (as of ECR-005 drafting)

Bill A / Bill B / Bill C — **LOU NOT PASSED** (HG-D1 unsatisfied).  
Therefore KS-S05…KS-S13 = **0.00** until controlled HG-D1 exists for each Bill.

---

## 11. Evidence Snapshot

Every calculation SHALL record at minimum:

| Field | Requirement |
|---|---|
| `status_calendar_date` | YYYY-MM-DD for the KSB cycle under evaluation |
| `repository` | Constitutional-Engineering (and other verified repos if used) |
| `branch` | e.g., main |
| `commit_sha` | Evaluated HEAD (local and/or origin as stated) |
| `bill_id` | A / B / C |
| `bill_public_title` | STD-011 §26 pin |
| `stage_states` | KS-S01…KS-S13 state codes |
| `credited_stage_units` | Sum |
| `raw_maturity` | Unrounded |
| `calculated_percent` | After half-up |
| `blocking_gate` | First unsatisfied mandatory gate, if any |
| `blocked_downstream_notes` | Optional ledger notes |
| `evidence_refs` | Paths / versions / acceptance states / SHAs |
| `evaluator` | AI system identity |
| `calculation_control` | WSMAT-001 version |

---

## 12. Calculated vs Certified

```text
EVIDENCE SNAPSHOT
        ↓
WSMAT-001 ALGORITHM
        ↓
CALCULATED MATURITY
        ↓
MATURITY LEDGER
        ↓
HUMAN ENGINEER ACCEPT / MODIFY / REJECT
        ↓
CERTIFIED KSB MATURITY
```

| Term | Meaning |
|---|---|
| **CALCULATED MATURITY** | Deterministic algorithm output for a snapshot |
| **CERTIFIED KSB MATURITY** | Calculated value explicitly accepted by Human Engineer for a specific KSB cycle (or Human-modified value with retained calculated value) |

If Human MODIFIES:

- retain `calculated_percent`;  
- record `certified_percent`;  
- record Human disposition / reason (minimum: MODIFY + brief reason).

Do not silently overwrite calculated values.  
Silence ≠ certification.  
AI SHALL NOT certify its own calculation.

---

## 13. AI / ChatGPT Authority

**MAY:**

- inspect available controlled/recognized evidence;  
- classify against Active stage criteria;  
- apply hard-gate ceilings;  
- compute units, raw maturity, half-up percent;  
- produce maturity ledger;  
- propose CALCULATED MATURITY.

**SHALL NOT:**

- certify;  
- satisfy Human Gates;  
- invent evidence;  
- treat silence as acceptance;  
- bypass hard gates;  
- publish uncertified maturity;  
- silently alter algorithm or weights.

---

## 14. Human Engineer Authority

Human Engineer may ACCEPT / MODIFY / REJECT calculated maturity and retains authority over control changes, stage model, weighting, gates, public certification, and publication.

Weekly MODIFY of a certified value does **not** amend WSMAT-001. Algorithm changes require ECR/STD controlled change.

---

## 15. Bill Identity Integrity

A Bill identifier SHALL identify the same legislative object across LOU, SPEC, CWC, drafting, maturity ledger, KSB Status, Git evidence, and publication.

Authoritative weekly-status identities: STD-011 §26.

Bill C: framework repository ≠ Bill C legislative LOU/maturity.

**Activation precondition:** LOU-001 Draft Bill A/B labels SHALL match STD-011 §26 public pins.  
**Status (2026-08-30):** Satisfied locally by LOU-001 Draft 0.3 identity reconciliation under CWC-CE-085 (LOU remains NOT ACCEPTED / HG-D1 PENDING).

---

## 16. First Authoritative Recalculation

Provisional values 27/27/8 are **not grandfathered**.

After Active:

1. Recalculate A/B/C from zero under this specification;  
2. Use reconciled identities + current evidence + gate states;  
3. Submit CALCULATED results for Human certification.

---

## 17. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0-PROPOSED | 2026-08-30 | Candidate Active specification drafted under ECR-005 / CWC-CE-085. Not operative. |
| 1.0.0 | 2026-08-30 | Activated locally under Human-accepted ECR-005 / CWC-CE-085 implementation with STD-011 v1.3.0; LOU-001 Draft 0.3 identity reconciled. |
