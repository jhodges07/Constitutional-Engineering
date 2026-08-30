# KSB-ORCH-001 — KSB Phone-Command Orchestration Procedure

**Document ID:** KSB-ORCH-001  
**Title:** KSB Phone-Command Orchestration / Baseline Continuity / Follow-Up Context  
**Classification:** Engineering Procedure (Weekly Status Orchestration)  
**Authority:** Constitutional Engineering Office  
**Governing Standard:** STD-011 Part B Version 1.5.1 (operative packaging CONTROL — §36 / §36.9 / §36.10)  
**Governing ECR:** ECR-007 (Implemented); ECR-008 (Human-accepted / Implemented locally)  
**Governing Work Card:** CWC-CE-087; CWC-CE-088  
**Related Failure:** KSB-POC-FAIL-001; KSB-POC-FAIL-002  
**Related Template:** KSB-PR-TMP-001  
**Status:** Active  
**Version:** 1.1.1  
**Effective Date:** 2026-08-30  
**Preparing Agent:** CE-Engineer  
**Activation:** Human-accepted ECR-008 / CWC-CE-088 Bounded Continuation — STD-011 §36.9; CWC-CE-088 defect remediation — §36.10  

```text
ACTIVE UNDER STD-011 v1.5.1 §36 / §36.10 / ECR-008
KSB SUNDAY PUBLICATION PACKAGE CONTRACT ACTIVE
HUMAN ACCEPTANCE REQUIRES COMPLETE PACKAGE
PRESERVES CWC-CE-087 FOLLOW-UP / CREATIVE / RENDER REQUIRED RULES
DOES NOT CHANGE CERTIFIED MATURITY
DOES NOT PUBLISH
DOES NOT REPLACE THE DETERMINISTIC RENDERER
GIT CANONICALIZATION PENDING HUMAN GIT GATE
```

---

## 1. Purpose

Make phone-first ChatGPT (and Cursor) orchestration of Kansas BlueprintLiberty Status (KSB Status) **deterministic** so that:

1. `Prepare KSB Status` establishes a controlled cycle **and** targets the complete **KSB Sunday Publication Package**;  
2. ordinary Sunday run prepares controlled status + ≈500-word press release + controlled KSB image without a second Human request;  
3. reasonable follow-ups retain cycle/artifact identity;  
4. “image” defaults to the **CONTROLLED KSB IMAGE**;  
5. creative artwork cannot silently replace the controlled status image;  
6. renderer unavailability yields an explicit controlled failure state and **INCOMPLETE** package, not a generative substitute.

---

## 2. Authority relationship

| Layer | Role |
|---|---|
| STD-011 Part B §25 | Operative image model: baseline + variables; generative text rendering **not** authoritative |
| WSMAT-001 / CERT records | Maturity calculation / Human certification |
| CWC-CE-084 renderer | Deterministic production mechanism |
| **This procedure** | Phone/command/follow-up orchestration semantics |
| WSPC-001 | Informational production-contract background (non-operative) |

This procedure does **not** alter the four ordinary weekly VARIABLES.

---

## 3. Command contract — `Prepare KSB Status`

Human trigger phrases (equivalent):

```text
Prepare KSB Status
Prepare this week's BlueprintLiberty status
Prepare BlueprintLiberty weekly status
```

(Exact wording may vary; intent governs.)

### 3.1 Required internal sequence (Human need not recite)

1. Identify canonical repository / evidence (`Constitutional-Engineering`).  
2. Determine controlled status calendar date.  
3. Retrieve Active maturity authority (WSMAT-001 / STD-011).  
4. Inspect controlled Bill evidence.  
5. Calculate candidate maturity under Active authority.  
6. Identify required Human certification.  
7. Preserve prior certified values until replacement is certified.  
8. Obtain Human certification where required (**context persists** — Human need not restate `Prepare KSB Status`).  
9. Prepare controlled status manifest.  
10. Prepare Markdown status/report (**Deliverable A**).  
11. Prepare approximately 500-word press release from controlled status (**Deliverable B**; KSB-PR-TMP-001; tolerance 450–550 words).  
12. Invoke deterministic KSB renderer (or declare RENDER REQUIRED) (**Deliverable C**).  
13. Use accepted baseline only.  
14. Insert only authorized VARIABLE values.  
15. Perform anti-drift validation.  
16. Determine package state **COMPLETE** or **INCOMPLETE**.  
17. Return Human-reviewable **KSB Sunday Publication Package**.  
18. **Preserve active cycle / artifact identity for follow-ups.**  
19. Stop at required Human Git/publication gates — **PUBLICATION NOT PERFORMED**.

### 3.2 Active cycle creation

On successful Step-1 entry, the assistant SHALL create / retain an **Active KSB Cycle Context** containing at minimum:

| Field | Example |
|---|---|
| `cycle_id` | `KSB-CYCLE-2026-08-30` |
| `status_date` | `2026-08-30` |
| `public_status_date` | `2026.08.35` |
| `bill_a_percent` | certified integer |
| `bill_b_percent` | certified integer |
| `bill_c_percent` | certified integer |
| `baseline_id` | `BL-WEEKLY-STATUS-BASELINE-v1.0` |
| `baseline_sha256` | accepted SHA |
| `renderer_id` | `ksb_renderer` / CWC-CE-084 |
| `package_paths` | manifest / report / press-release / image (or RENDER REQUIRED) |
| `package_state` | COMPLETE / INCOMPLETE |
| `certification_state` | as recorded |
| `cycle_state` | ACTIVE |

### 3.3 One-command semantics

“One command” means the Human does **not** ordinarily need to separately request the press release or image.

It does **NOT** mean bypassing required Human certification, Git, or publication gates.

If certification is required mid-cycle:

```text
HUMAN CERTIFICATION REQUIRED
```

After the Human decides, the **same** Active cycle continues toward all three deliverables without requiring the Human to repeat `Prepare KSB Status`.

---

## 4. Active-cycle context rule (no magic-phrase dependency)

While `cycle_state = ACTIVE`, follow-up Human instructions about the status, report, image, graphic, social-media post, press release, weekly update, Facebook post, publication material, or supporting media **SHALL operate within this cycle**.

The Human SHALL NOT be required to re-say `Prepare KSB Status` for each follow-up.

### 4.1 Cycle ends when

A. workflow completed and Human closes the cycle; **or**  
B. Human explicitly changes subject/workflow; **or**  
C. a conflicting controlled workflow is invoked; **or**  
D. Human explicitly requests a different artifact class (e.g., separate creative artwork); **or**  
E. a new `Prepare KSB Status` starts a **new** cycle (prior cycle preserved historically).

---

## 5. Controlled KSB image vs creative artwork

### 5.1 CONTROLLED KSB IMAGE

Uses accepted baseline; deterministic renderer; only authorized VARIABLE regions; anti-drift; preserves controlled identity.

### 5.2 CREATIVE SUPPORTING ARTWORK

Independently generated visual material. Not the KSB Status image. No KSB engineering authority. Allowed only when Human intent **clearly** requests separate creative artwork.

### 5.3 Ambiguous “image” resolution (DEFAULT)

When an Active KSB Cycle exists and Human requests any of:

```text
the image
status image
weekly image
image to support it
graphic
Facebook image
social-media image
post image
```

or reasonably equivalent wording:

**DEFAULT = CONTROLLED KSB IMAGE.**

Do **not** invoke generic creative image generation as the default.

### 5.4 Explicit creative exception

Creative generation may proceed only when Human clearly distinguishes, e.g.:

```text
a separate image
a new creative image
political satire
an illustration
a different design
make another graphic
```

Creative output SHALL be labeled **NOT THE CONTROLLED KSB STATUS IMAGE** and SHALL NOT overwrite cycle package image identity.

---

## 6. Renderer routing and failure-safe behavior

### 6.1 Authorized production path

```text
ACCEPTED BASELINE
 → DETERMINISTIC RENDERER (CWC-CE-084)
 → AUTHORIZED VARIABLES ONLY
 → ANTI-DRIFT PASS
 → PACKAGE IMAGE
```

Path:

```text
Engineering-Office/publication/weekly-status/renderer/
```

Baseline:

```text
Engineering-Office/publication/weekly-status/baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png
```

### 6.2 Renderer unavailable (phone / ChatGPT limitation)

If the execution environment cannot run the deterministic renderer:

```text
KSB IMAGE: RENDER REQUIRED
```

Then identify the controlled bridge (Cursor / local CE-Engineer / authorized GitHub interchange) to complete render.

**SHALL NOT** substitute a generative/creative image and present it as the KSB status image.

A visible controlled failure is preferable to an uncontrolled substitute.

---

## 7. KSB Sunday Publication Package

**Controlled identity:** `KSB Sunday Publication Package`  
(ordinary weekly Human-reviewable set within the Weekly Public Engineering Status package class)

### 7.1 Mandatory deliverables

| ID | Deliverable | Path convention |
|---|---|---|
| A | Controlled KSB Status (manifest + Markdown report) | `manifests/` + `reports/YYYY-MM-DD-BlueprintLiberty-Weekly-Status.md` |
| B | Press release (~500 words; 450–550 tolerance) | `press-releases/YYYY-MM-DD-BlueprintLiberty-KSB-Press-Release.md` |
| C | Controlled KSB Status Image | `images/YYYY-MM-DD-BlueprintLiberty-Weekly-Status.png` |

### 7.2 COMPLETE

`PACKAGE STATE: COMPLETE` only if all are true:

1. controlled status available;  
2. required Human certification satisfied for the cycle;  
3. press release generated from controlled facts within 450–550 words (KSB-PR-TMP-001);  
4. controlled KSB image successfully rendered;  
5. anti-drift validation PASS;  
6. required package validation PASS.

### 7.3 INCOMPLETE

If any mandatory component is unavailable:

```text
PACKAGE STATE: INCOMPLETE
UNRESOLVED: <exact component>
```

Examples: `KSB IMAGE: RENDER REQUIRED` → package INCOMPLETE (status and press release may still be prepared).  

Generative/creative substitution SHALL **NOT** convert INCOMPLETE → COMPLETE.

### 7.3.1 Human acceptance vs infrastructure (CWC-CE-088 / KSB-POC-FAIL-002)

`Prepare KSB Status` **Human acceptance** PASS requires the complete Human-reviewable package returned through the ChatGPT interaction (status + press release + controlled image).  

Bridge/runtime partial success (Issue created, gate PASS, runner started, Python installed, diagnostics returned) SHALL **NOT** be reported as Human command PASS.  

A runtime diagnostic SHALL **NOT** substitute for the requested package. When acceptance testing specifically requires the complete package, a diagnostic/INCOMPLETE result is still acceptance **FAIL**, even when failure reporting itself is correctly formed.

Authorized incomplete/failure reporting remains:

```text
PACKAGE STATE: INCOMPLETE
UNRESOLVED: <exact component>
```

including `KSB IMAGE: RENDER REQUIRED` when the controlled image cannot be produced. Equivalent package-generation failure wording may be used when already authorized; do not redefine failure reporting as package success.

### 7.4 Human-facing return structure

```text
KSB STATUS
[controlled status]

PRESS RELEASE
[approximately 500 words]

KSB STATUS IMAGE
[controlled image path/link — or RENDER REQUIRED]

PACKAGE VALIDATION
[COMPLETE / INCOMPLETE + material result]

PUBLICATION
NOT PERFORMED — HUMAN DECISION REQUIRED
```

### 7.5 Manifest traceability

Weekly manifests SHOULD identify all three package artifacts (status report, press release, image) plus validation/package state for audit.

---

## 8. Press release (ordinary deliverable + follow-up)

### 8.1 Ordinary production

Under `Prepare KSB Status`, the press release is a **mandatory ordinary deliverable** (not optional follow-up).

Structure: **KSB-PR-TMP-001**.  
Facts: only from controlled KSB status / certified values / disclosed evidence.  
Length: approximately 500 words (450–550).

### 8.2 Evidence firewall

```text
CONTROLLED REPOSITORY EVIDENCE → CONTROLLED STATUS → PRESS RELEASE
```

Press release ≠ engineering truth. SHALL NOT alter maturity, Bill identity, certification, HG-D1, HG-PR, control status, research acceptance, or Git state.

Inconsistent derived claims SHALL be rejected/corrected.

### 8.3 Editorial follow-up

After package preparation, requests such as “Shorten the press release,” “Give me the Facebook text,” “Change the headline” may refine derived prose. Editorial follow-up SHALL NOT silently modify engineering truth.

---

## 9. Social-media follow-up

Ordinary social package for an Active cycle SHOULD contain:

1. Controlled KSB status image (or RENDER REQUIRED state);  
2. Human-approved supporting text / press release;  
3. Controlled public URL (`BlueprintLiberty.com`);  
4. Appropriate status date.

Social publication itself (HG-6) does not alter engineering evidence. This procedure does not authorize posting.

---

## 10. Percentage / maturity firewall

AI SHALL NOT treat conversational requests like `Change Bill A to 80%` as operative VARIABLE changes.

Absent required maturity evidence path + Human CERTIFIED KSB MATURITY for that cycle:

```text
REJECT / UNABLE — not controlled status
```

Preserve certified historical snapshot unless a new authorized certification replaces it.

---

## 11. Source-of-truth firewall

```text
CONTROLLED REPOSITORY EVIDENCE
 → STATUS MEASUREMENT
 → HUMAN CERTIFICATION
 → STATUS MANIFEST
 → REPORT / PRESS RELEASE / IMAGE GENERATION
 → VALIDATION
 → HUMAN ACCEPTANCE
 → PUBLICATION
```

Never reverse. Public graphics, creative artwork, and press releases are not engineering truth.

---

## 12. Baseline immutability reminder

Ordinary weekly cycle SHALL NOT creatively regenerate layout, headings, VSM, repository foundation, Bill presentation, Why This Matters, footer, Capitol imagery, flags, typography, fixed labels, fixed explanatory text, controlled URLs, or branding.

Only authorized VARIABLE regions may change. Press-release text is **not** an image-renderer variable.

---

## 13. Phone-first requirement

The Human should be able to say `Prepare KSB Status` without opening Cursor, finding the baseline, manually editing PNG, calculating percentages by hand, or requesting a second “create press release / image” command for the ordinary Sunday package.

Technical ceremony remains behind this orchestration. Human certification and publication gates remain.

---

## 14. Operator return states (minimum)

| State | Meaning |
|---|---|
| `KSB CYCLE: ACTIVE` | Context retained |
| `PACKAGE STATE: COMPLETE` | All three deliverables validated |
| `PACKAGE STATE: INCOMPLETE` | Mandatory component unresolved (name it) |
| `KSB IMAGE: READY` | Controlled image available in package |
| `KSB IMAGE: RENDER REQUIRED` | Controlled render pending; no creative substitute; package INCOMPLETE |
| `KSB IMAGE: ANTI-DRIFT FAIL` | Stop; do not publish; package INCOMPLETE |
| `HUMAN CERTIFICATION REQUIRED` | Gate; cycle context persists |
| `PUBLICATION: NOT PERFORMED` | Human HG-6 still required |
| `CREATIVE ARTWORK: SEPARATE` | Explicit creative request; not status image |

---

## 15. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-30 | Initial Active-local procedure under CWC-CE-087 correcting KSB-POC-FAIL-001. |
| 1.0.0 | 2026-08-30 | Confirmed Active under STD-011 §36 after Human acceptance / local implementation of ECR-007 (CWC-CE-087 Bounded Continuation). |
| 1.1.0 | 2026-08-30 | CWC-CE-088: single-command KSB Sunday Publication Package (status + ≈500-word press release + controlled image); COMPLETE/INCOMPLETE; certification continuity; ECR-008 Proposed for STD-011 binding. |
| 1.1.0 | 2026-08-30 | Confirmed Active under STD-011 v1.5.0 §36.9 after Human acceptance / local implementation of ECR-008 (CWC-CE-088 Bounded Continuation). |
| 1.1.1 | 2026-08-30 | CWC-CE-088 defect remediation: Human acceptance vs infrastructure (§7.3.1); complete package required for command PASS; records KSB-POC-FAIL-002; aligns to STD-011 v1.5.1 §36.10. |
