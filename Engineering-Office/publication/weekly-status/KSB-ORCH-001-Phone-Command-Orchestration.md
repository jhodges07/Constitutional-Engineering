# KSB-ORCH-001 — KSB Phone-Command Orchestration Procedure

**Document ID:** KSB-ORCH-001  
**Title:** KSB Phone-Command Orchestration / Baseline Continuity / Follow-Up Context  
**Classification:** Engineering Procedure (Weekly Status Orchestration)  
**Authority:** Constitutional Engineering Office  
**Governing Standard:** STD-011 Part B Version 1.4.0 (operative packaging CONTROL — §36)  
**Governing ECR:** ECR-007 — KSB Phone-Command Orchestration Control (Human-accepted / Implemented locally)  
**Governing Work Card:** CWC-CE-087  
**Related Failure:** KSB-POC-FAIL-001  
**Status:** Active  
**Version:** 1.0.0  
**Effective Date:** 2026-08-30  
**Preparing Agent:** CE-Engineer  
**Activation:** Human-accepted ECR-007 / CWC-CE-087 Bounded Continuation — STD-011 §36  

```text
ACTIVE UNDER STD-011 §36 / ECR-007
ACTIVE LOCALLY — GIT CANONICALIZATION PENDING HUMAN GIT GATE
DOES NOT CHANGE CERTIFIED MATURITY
DOES NOT PUBLISH
DOES NOT REPLACE THE DETERMINISTIC RENDERER
DOES NOT CLAIM LIVE PHONE RE-POC PASS
```

**Historical note:** Initially Active-locally under CWC-CE-087 pending ECR-007; promoted to operative packaging procedure under STD-011 §36 upon Human acceptance of ECR-007.
---

## 1. Purpose

Make phone-first ChatGPT (and Cursor) orchestration of Kansas BlueprintLiberty Status (KSB Status) **deterministic** so that:

1. `Prepare KSB Status` establishes a controlled cycle;  
2. reasonable follow-ups retain cycle/artifact identity;  
3. “image” defaults to the **CONTROLLED KSB IMAGE**;  
4. creative artwork cannot silently replace the controlled status image;  
5. renderer unavailability yields an explicit controlled failure state, not a generative substitute.

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
8. Obtain Human certification where required.  
9. Prepare controlled status manifest.  
10. Prepare Markdown status/report.  
11. Invoke deterministic KSB renderer (or declare RENDER REQUIRED).  
12. Use accepted baseline only.  
13. Insert only authorized VARIABLE values.  
14. Perform anti-drift validation.  
15. Return Human-reviewable KSB package.  
16. **Preserve active cycle / artifact identity for follow-ups.**  
17. Stop at required Human Git/publication gates.

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
| `package_paths` | manifest / report / image (or RENDER REQUIRED) |
| `certification_state` | as recorded |
| `cycle_state` | ACTIVE |

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

## 7. Press-release follow-up

After Active cycle:

- Press-release **text** MAY be newly drafted.  
- Text SHALL cite/use controlled cycle values (date, Bill identities, certified percentages, certification meaning).  
- Press release **≠** engineering truth and SHALL NOT silently alter percentages, Bill identities, status date, maturity meaning, or certification state.

If paired with “image,” apply §5.3 (controlled KSB image / RENDER REQUIRED).

---

## 8. Social-media follow-up

Ordinary social package for an Active cycle SHOULD contain:

1. Controlled KSB status image (or RENDER REQUIRED state);  
2. Human-approved supporting text / press release;  
3. Controlled public URL (`BlueprintLiberty.com`);  
4. Appropriate status date.

Social publication itself (HG-6) does not alter engineering evidence. This procedure does not authorize posting.

---

## 9. Percentage / maturity firewall

AI SHALL NOT treat conversational requests like `Change Bill A to 80%` as operative VARIABLE changes.

Absent required maturity evidence path + Human CERTIFIED KSB MATURITY for that cycle:

```text
REJECT / UNABLE — not controlled status
```

Preserve certified historical snapshot unless a new authorized certification replaces it.

---

## 10. Source-of-truth firewall

```text
CONTROLLED REPOSITORY EVIDENCE
 → STATUS MEASUREMENT
 → HUMAN CERTIFICATION
 → STATUS MANIFEST
 → REPORT / IMAGE GENERATION
 → VALIDATION
 → HUMAN ACCEPTANCE
 → PUBLICATION
```

Never reverse. Public graphics and creative artwork are not engineering truth.

---

## 11. Baseline immutability reminder

Ordinary weekly cycle SHALL NOT creatively regenerate layout, headings, VSM, repository foundation, Bill presentation, Why This Matters, footer, Capitol imagery, flags, typography, fixed labels, fixed explanatory text, controlled URLs, or branding.

Only authorized VARIABLE regions may change.

---

## 12. Phone-first requirement

The Human should be able to say `Prepare KSB Status` without opening Cursor, finding the baseline, manually editing PNG, or repeating FIXED/VARIABLE theory.

Technical ceremony remains behind this orchestration. Human gates remain.

---

## 13. Operator return states (minimum)

| State | Meaning |
|---|---|
| `KSB CYCLE: ACTIVE` | Context retained |
| `KSB IMAGE: READY` | Controlled image available in package |
| `KSB IMAGE: RENDER REQUIRED` | Controlled render pending; no creative substitute |
| `KSB IMAGE: ANTI-DRIFT FAIL` | Stop; do not publish |
| `CREATIVE ARTWORK: SEPARATE` | Explicit creative request; not status image |

---

## 14. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-30 | Initial Active-local procedure under CWC-CE-087 correcting KSB-POC-FAIL-001. |
| 1.0.0 | 2026-08-30 | Confirmed Active under STD-011 §36 after Human acceptance / local implementation of ECR-007 (CWC-CE-087 Bounded Continuation). |
