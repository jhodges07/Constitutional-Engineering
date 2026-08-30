# CWC-CE-076 — Weekly Status Gap-Closure Matrix and Control Architecture

**Document ID:** WSGAP-001  
**Title:** Weekly Status Gap-Closure Matrix and Control Architecture Decision  
**Classification:** Informational Engineering Definition — Control Design  
**Governing Work Card:** CWC-CE-076; CWC-CE-077 (Human acceptance / Git gate)  
**Status:** Human-Accepted Informational Design Record / Not Operative CONTROL  
**Human Acceptance:** ACCEPTED 2026-08-30 under CWC-CE-077 (Decision 3) — Option D accepted; remains informational  
**Version:** 0.2.5  
**Effective Date:** 2026-08-30  
**Related ECR:** ECR-004 (Implemented under CWC-CE-078 — STD-011 Part B Active for packaging rules; package generation / phone POC / publication remain separately gated; CWC-CE-081 → STD-011 v1.2.0 date-format / public-image content; CWC-CE-082 → STD-011 v1.2.1 ISO-8601 `ww`)

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
| GAP-WS-001 | STD-011 does not govern weekly-status | **CLOSED (CWC-CE-078):** STD-011 v1.1.0 Part B Active | **NO** | **NO** (packaging CONTROL present) | Implement STD-011 Part B | Human Engineer + CE-Engineer | CWC-CE-078 | STD-011 Active text includes weekly-status package class |
| GAP-WS-002 | No ECR/CONTROL activates weekly-status | **CLOSED (CWC-CE-078):** ECR-004 Implemented; STD-011 Part B operative for packaging rules | **NO** | Soft (Verified-Closed may remain pending) | Approve + implement ECR-004 | Human Engineer | CWC-CE-077 accept; CWC-CE-078 implement | ECR Implemented; STD-011 Part B present |
| GAP-WS-003 | Approved visual baseline absent | **CLOSED (CWC-CE-083):** Human-accepted `BL-WEEKLY-STATUS-BASELINE-v1.0` SHA-256 `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9` | **NO** | Soft (Git remote integration may remain pending Human Git gate) | HE accept exact artifact (done) | Human Engineer | CWC-CE-083 | File in `baseline/` + acceptance record + checksum + HE acceptance |
| GAP-WS-004 | Deterministic renderer not authorized/implemented | Packaging CONTROL exists; renderer not implemented | **YES for image half** | **YES** until implemented | Implement deterministic renderer after baseline | Human Engineer | Renderer CWC after baseline | Template renders only VARIABLE + controlled config; anti-drift PASS |
| GAP-WS-005 | Bill C identity not controlled | **Title-pin portion CLOSED (CWC-CE-077):** FIXED public title `Kansas NBEF Act (Node-Based Educational Framework)` Human-accepted. Engineering-truth LOU/SPEC still future. | Title pin **NO** longer POC blocker | Durable engineering-truth object still open | HE pin public FIXED title (done); later LOU/SPEC for engineering truth | Human Engineer | CWC-CE-077 title pin; later NBEF LOU if needed | Written HE acceptance of FIXED Bill C title string recorded; **not** legislative enactment |
| GAP-WS-006 | Architecture not on origin/main | **CLOSED (CWC-CE-077)** | **CLOSED** | Soft | Commit informational architecture | Human Engineer Git gate | CWC-CE-077 | `git ls-tree origin/main` lists README + WSPC-001 + WSGAP-001 + ECR-004 |
| GAP-WS-007 | No automated % CONTROL | None; STD-011 / WSPC require HE % | **NO** — MAY REMAIN HUMAN-GATED DURING POC | Deferred maturity for automation | Keep HE-supplied/approved percentages | Human Engineer | Deferred; optional future CONTROL | N/A for POC |
| GAP-WS-008 | STD-002 Reserved | Reserved; WF-001 gates Active | **NO** — MAY REMAIN HUMAN-GATED DURING POC | Deferred | Retain WF-001 HG-4/HG-5; do not invent STD-002 | Human Engineer | Deferred STD-002 activation | N/A for POC |
| GAP-WS-009 | PUBLIC URL CONTROL | **CLOSED (CWC-CE-078):** STD-011 §28 PUBLIC URL REQUIREMENT; `PUBLIC_URL_01` = BlueprintLiberty.com | **NO** | **NO** for initial pin | Integrate PUBLIC URL REQUIREMENT into STD-011 | Human Engineer + CE-Engineer | CWC-CE-078 | STD-011 §28 Active; initial pin recorded |

### Classification summary

| Classification | Gaps |
|---|---|
| MUST CLOSE BEFORE PHONE POC | GAP-WS-004 (renderer implementation) |
| CLOSED (packaging / URL / title / GitHub architecture / baseline) | GAP-WS-001, GAP-WS-002, GAP-WS-003, GAP-WS-005 (title pin), GAP-WS-006, GAP-WS-009 |
| MAY REMAIN HUMAN-GATED DURING PHONE POC | GAP-WS-007, GAP-WS-008 |
| DEFERRED PRODUCTION MATURITY ITEM | Automated %, STD-002 activation, dedicated weekly STD (Option B), recurring schedule, autonomous publication, NBEF engineering-truth LOU/SPEC |
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

**HUMAN-ACCEPTED BASELINE — GAP-WS-003 CLOSED**

Accepted path:

```text
Engineering-Office/publication/weekly-status/baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png
```

Accepted SHA-256:

```text
17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9
```

Companion record:

```text
baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.acceptance.md
```

Human Engineer accepted the exact artifact as `BL-WEEKLY-STATUS-BASELINE-v1.0` on 2026-08-30 under CWC-CE-083.  
Git stage/commit/push of the accepted baseline package remains a separate Human Git gate unless expressly authorized.  
**GAP-WS-004 remains OPEN** (deterministic renderer not implemented).

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
NOW (after CWC-CE-083 Human baseline acceptance)
 → HE Git gate for accepted baseline + acceptance/control records (if not yet on origin/main)
 → Later CWC: deterministic renderer (GAP-WS-004) — recommended CWC-CE-084
 → Later CWC: FIRST PHONE POC
```

**Not ready to execute phone POC.** Packaging CONTROL, PUBLIC URL REQUIREMENT, and Human-accepted visual baseline are present; **GAP-WS-004 (renderer)** remains the hard prerequisite.

---

## 11. Version History

| Version | Date | Summary |
|---|---|---|
| 0.1.0 | 2026-08-30 | Initial gap-closure matrix and Option D architecture under CWC-CE-076. Not operative. |
| 0.1.1 | 2026-08-30 | CWC-CE-077: Human acceptance of Option D; Bill C PUBLIC WEEKLY-STATUS TITLE PIN; GAP-WS-005 title-pin / GAP-WS-006 closure recording. Remains Not Operative CONTROL. |
| 0.2.0 | 2026-08-30 | CWC-CE-078: GAP-WS-001/002/009 CLOSED via STD-011 v1.1.0 Part B + PUBLIC URL REQUIREMENT; remaining POC blockers = baseline + renderer. |
| 0.2.1 | 2026-08-30 | CWC-CE-081: Related ECR header residual retained as Implemented; note STD-011 v1.2.0 date-format / public-image exclusions; GAP-WS-003/004 remain OPEN; ww algorithm Human-decision open. |
| 0.2.2 | 2026-08-30 | CWC-CE-082: ISO-8601 `ww` Human authorization recorded; ww algorithm blocker removed; GAP-WS-003/004 remain OPEN; remains Not Operative CONTROL. |
| 0.2.3 | 2026-08-30 | CWC-CE-083: candidate baseline prepared (dev-strip crop); acceptance pending; GAP-WS-003 remains OPEN; GAP-WS-004 remains OPEN. |
| 0.2.4 | 2026-08-30 | CWC-CE-083 Cont. #2: header parenthetical removed; candidate SHA `17F574D4…`; GAP-WS-003 remains OPEN. |
| 0.2.5 | 2026-08-30 | CWC-CE-083: Human acceptance of SHA `17F574D4…` as `BL-WEEKLY-STATUS-BASELINE-v1.0`; **GAP-WS-003 CLOSED**; GAP-WS-004 remains OPEN. |
