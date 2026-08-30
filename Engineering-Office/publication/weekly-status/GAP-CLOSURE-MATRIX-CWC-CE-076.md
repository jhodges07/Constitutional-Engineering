# CWC-CE-076 — Weekly Status Gap-Closure Matrix and Control Architecture

**Document ID:** WSGAP-001  
**Title:** Weekly Status Gap-Closure Matrix and Control Architecture Decision  
**Classification:** Informational Engineering Definition — Control Design  
**Governing Work Card:** CWC-CE-076; CWC-CE-077 (Human acceptance / Git gate)  
**Status:** Human-Accepted Informational Design Record / Not Operative CONTROL  
**Human Acceptance:** ACCEPTED 2026-08-30 under CWC-CE-077 (Decision 3) — Option D accepted; remains informational  
**Version:** 0.1.1  
**Effective Date:** 2026-08-30  
**Related ECR:** ECR-004 (Approved — HUMAN ACCEPTED / APPROVED FOR CONTROL IMPLEMENTATION; NOT YET IMPLEMENTED)

```text
HUMAN-ACCEPTED DESIGN RECORD
OPTION D ACCEPTED
NOT OPERATIVE CONTROL
```

---

## 1. Recommended Control Architecture (OPTION D)

**Permanent path (Option A):** Extend **STD-011** through **ECR-004** so weekly-status packages share the public-documentation CONTROL surface with LOU packages, while remaining a distinct package class.

**First phone POC bridge (Option C, temporary):** After HE accepts ECR-004 (or records an explicit named waiver), supplies the baseline mockup, pins Bill C public title, and commits informational architecture to GitHub, a **later separate CWC** may authorize one phone POC under Human percentage/narrative/Git/publication gates.

**Option B (dedicated STD)** deferred unless STD-011 becomes overloaded.

**Rationale:** artifact-force separation (WSPC-001 stays informative; STD-011 becomes operative packaging); maintainability (one public-doc standard); HE supremacy; clear Git/publication boundaries; anti-drift enforceable against baseline; phone operation remains HE-triggered; automation stays future/gated.

**Simple command preservation:**

```text
"Prepare this week's BlueprintLiberty status."
```

maps to HE trigger → evidence → AI proposal → HE approval → mechanical representation → HE Git gates → HE publication — and does **not** collapse those layers.

---

## 2. Gap-Closure Matrix

| Gap ID | Description | Current state | POC blocker? | Production blocker? | Required disposition | Responsible authority | Proposed CWC/action | Closure evidence required |
|---|---|---|---|---|---|---|---|---|
| GAP-WS-001 | STD-011 does not govern weekly-status | True (STD-011 §2 LOU-only) | **YES** (unless HE records explicit temporary waiver) | **YES** | Approve ECR-004; implement STD-011 extension | Human Engineer + CE-Engineer under later CWC | HE accept ECR-004 → implementation CWC | STD-011 Active text includes weekly-status package class |
| GAP-WS-002 | No ECR/CONTROL activates weekly-status | True (ECR-004 only Proposed) | **YES** (same as 001) | **YES** | Approve ECR-004 (or dedicated STD path) | Human Engineer | HE disposition on ECR-004 | ECR Status ≠ Proposed; Verified implementation recorded |
| GAP-WS-003 | Approved visual baseline absent | `baseline/` empty | **YES — HARD** | **YES — HARD** | HE supplies approved mockup; controlled ingest | Human Engineer | Baseline ingest CWC (or section of next CWC) | File in `baseline/` + acceptance record + checksum |
| GAP-WS-004 | Deterministic renderer not authorized/implemented | Not implemented | **YES for image half** (design OK; impl later) | **YES** until implemented | Define min renderer now; implement in later CWC | Human Engineer | Renderer implementation CWC after baseline exists | Template renders only VARIABLE fields; anti-drift PASS |
| GAP-WS-005 | Bill C identity not controlled | **Title-pin portion CLOSED (CWC-CE-077):** FIXED public title `Kansas NBEF Act (Node-Based Educational Framework)` Human-accepted. Engineering-truth LOU/SPEC still future. | Title pin **NO** longer POC blocker | Durable engineering-truth object still open | HE pin public FIXED title (done); later LOU/SPEC for engineering truth | Human Engineer | CWC-CE-077 title pin; later NBEF LOU if needed | Written HE acceptance of FIXED Bill C title string recorded; **not** legislative enactment |
| GAP-WS-006 | Architecture not on origin/main | Closed by CWC-CE-077 Git package when push succeeds | **CLOSED** after successful push | Soft | Commit CWC-CE-075/076 informational package | Human Engineer Git gate | CWC-CE-077 | `git ls-tree origin/main` lists README + WSPC-001 + WSGAP-001 + ECR-004 |
| GAP-WS-007 | No automated % CONTROL | None; WSPC requires HE % | **NO** — MAY REMAIN HUMAN-GATED DURING POC | Deferred maturity for automation | Keep HE-supplied/approved percentages | Human Engineer | Deferred; optional future CONTROL | N/A for POC |
| GAP-WS-008 | STD-002 Reserved | Reserved; WF-001 gates Active | **NO** — MAY REMAIN HUMAN-GATED DURING POC | Deferred | Retain WF-001 HG-4/HG-5; do not invent STD-002 | Human Engineer | Deferred STD-002 activation | N/A for POC |

### Classification summary

| Classification | Gaps |
|---|---|
| MUST CLOSE BEFORE PHONE POC | GAP-WS-001/002 (or named HE waiver), GAP-WS-003, GAP-WS-005 (title pin), GAP-WS-006, GAP-WS-004 **implementation** (minimum renderer) |
| MAY REMAIN HUMAN-GATED DURING PHONE POC | GAP-WS-007, GAP-WS-008 |
| DEFERRED PRODUCTION MATURITY ITEM | Automated %, STD-002 activation, dedicated weekly STD (Option B), recurring schedule, autonomous publication |
| SUPERSEDED / NOT ACTUALLY REQUIRED | None identified |

---

## 3. Percentage Authority Decision

**POC:** HE-SUPPLIED / HE-APPROVED percentages only.  
**Automated calculation:** DEFERRED PRODUCTION MATURITY ITEM.  
Do **not** create an operative maturity formula under CWC-CE-076.

---

## 4. Git Operations Authority Decision

**POC:** WF-001 Human Git gates (HG-4 commit / HG-5 push) are **sufficient**.  
**STD-002:** remains Reserved; do **not** activate for the demonstration.

---

## 5. Bill C Identity Requirement

**PUBLIC WEEKLY-STATUS TITLE PIN (CWC-CE-077 Decision 5 — ACCEPTED):**

```text
Kansas NBEF Act (Node-Based Educational Framework)
```

This string is the **FIXED public-status title** for BlueprintLiberty Weekly Public Engineering Status report/image architecture.

**Explicit distinction:**

| Kind | Status |
|---|---|
| PUBLIC WEEKLY-STATUS TITLE PIN | **ACCEPTED** 2026-08-30 under CWC-CE-077 |
| LEGISLATIVE ENGINEERING ACCEPTANCE | **NOT** conferred |
| Legislative enactment / statutory drafting | **NOT** authorized |
| Future NBEF LOU/SPEC | **NOT** replaced; remains separately authorized |

**NBEF:** Node-Based Educational Framework  

1. **POC FIXED-label requirement:** **CLOSED** by this Human-accepted title pin.  
2. **Required for engineering truth (not POC packaging):** a later controlled Engineering Definition object (candidate LOU / SPEC / Legislative-Manager project artifact) for NBEF — **separately authorized**.  
3. **Not authorized by CWC-CE-077:** legislative acceptance, statutory drafting, or treating the public title pin as enacted law.

---

## 6. Visual Baseline Acceptance Model (GAP-WS-003)

**Hard prerequisite** for controlled image POC. **Do not fabricate a substitute.**

### 6.1 Expected ingest path

```text
Engineering-Office/publication/weekly-status/baseline/
```

### 6.2 Expected filename (proposed)

```text
BL-WEEKLY-STATUS-BASELINE-v1.0.png
```

(or HE-directed extension: `.svg` / `.pdf` master + derived PNG)

Companion acceptance record (proposed):

```text
baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.acceptance.md
```

### 6.3 Acceptance record minimum fields

| Field | Requirement |
|---|---|
| Baseline ID | e.g. `BL-WS-BASELINE-001` |
| Version | e.g. `1.0.0` |
| Source/provenance | Human Engineer supplied; date; originating file name |
| Acceptance state | HE ACCEPTED / REJECTED / SUPERSEDED |
| SHA-256 | Required for the binary baseline file |
| FIXED element list | Titles, layout, colors, Bill A/B/C title strings, BlueprintLiberty.com spelling, etc. |
| VARIABLE slots | `STATUS_DATE`, `BILL_A_PERCENT`, `BILL_B_PERCENT`, `BILL_C_PERCENT` positions |
| Replacement procedure | New version via HE-authorized CWC; old baseline archived; no silent overwrite |

### 6.4 Current status

**AWAITING HUMAN-SUPPLIED APPROVED MOCKUP**

---

## 7. Deterministic Renderer Requirement (GAP-WS-004)

### 7.1 Minimum for first phone POC

Controlled template that injects **only**:

- `{{STATUS_DATE}}`  
- `{{BILL_A_PERCENT}}`  
- `{{BILL_B_PERCENT}}`  
- `{{BILL_C_PERCENT}}`  

Preferred order:

1. **SVG template** derived from accepted baseline geometry; or  
2. **HTML/CSS template → PNG** using HE-authorized local toolchain;  

Generative-image text for controlled fields is **not** the control target.

### 7.2 Anti-drift

Renderer SHALL NOT redesign FIXED elements. Validation compares FIXED regions/hash policy to baseline acceptance record.

### 7.3 Where to implement

| Location | Disposition |
|---|---|
| This repository (`Engineering-Office/publication/weekly-status/` or `tools/`) | Preferred for template + verification scripts once authorized |
| Separate tooling repo | Optional if toolchain becomes large |
| CWC-CE-076 | **Design only — no production tooling implementation** |

Implementation requires a **later CWC** after baseline ingest.

---

## 8. Phone-POC Minimum Authority Set

Before the first phone test CWC may be authorized, close or expressly waive:

1. GAP-WS-006 — architecture + WSPC-001 on GitHub  
2. GAP-WS-001/002 — ECR-004 Approved (+ implement or named waiver)  
3. GAP-WS-003 — accepted baseline in `baseline/`  
4. GAP-WS-005 — FIXED Bill C title pin  
5. GAP-WS-004 — minimum deterministic render path implemented and verified once  

May remain Human-gated: GAP-WS-007, GAP-WS-008.

### Intended phone path (not authorized by this CWC)

HE (phone) → ChatGPT reads GitHub evidence → candidate status → HE approves %/narrative → controlled package → bounded GitHub write → Cursor verifies → HE retains publication authority.

---

## 9. POC vs Production Boundary

| | Phone POC Authority | Recurring Production Authority |
|---|---|---|
| Trigger | Single HE-authorized CWC | Standing CONTROL + weekly HE trigger |
| Packages | One (or expressly counted) test package | Ongoing historical series |
| Automation | None / manual interchange | Future CONTROL only |
| Publication | HE only | HE only unless CONTROL changes |
| Success effect | Proves path | Does **not** auto-enable production |

A successful phone POC **SHALL NOT** automatically authorize recurring weekly production, scheduled automation, or autonomous publication.

---

## 10. Distance to First Phone POC

```text
NOW
 → HE Git gate: commit CWC-CE-075 informational artifacts (+ optional CWC-CE-076 design artifacts)
 → HE accept ECR-004 (or named waiver)
 → HE supply + accept visual baseline
 → HE pin Bill C FIXED title
 → Later CWC: implement STD-011 weekly rules (if not waived) + minimum renderer
 → Later CWC: FIRST PHONE POC (new number; not this CWC)
```

**Not ready to execute phone POC under CWC-CE-076.**

---

## 11. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-08-30 | Initial gap-closure matrix and Option D architecture under CWC-CE-076. Not operative. |
| 0.1.1 | 2026-08-30 | CWC-CE-077: Human acceptance of Option D; Bill C PUBLIC WEEKLY-STATUS TITLE PIN; GAP-WS-005 title-pin / GAP-WS-006 closure recording. Remains Not Operative CONTROL. |
