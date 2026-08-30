# ChatGPT / Phone Operator Card — KSB Status (CWC-CE-088)

**Document ID:** KSB-ORCH-001-OPERATOR-CARD  
**Governing Procedure:** KSB-ORCH-001 v1.1.0 — Active under STD-011 v1.5.0 §36 / ECR-008  
**Governing Standard:** STD-011 Version 1.5.0 Part B  
**Governing Work Card:** CWC-CE-087; CWC-CE-088  
**Audience:** ChatGPT phone / Custom GPT / Cursor operators (implementation aid)  
**Status:** Validated against Active STD-011 §36.9 / ECR-008 Implemented locally  
**Human-facing trigger:** `Prepare KSB Status`  

---

## Hard rules (must follow)

1. `Prepare KSB Status` starts an **Active KSB Cycle** and targets the complete **KSB Sunday Publication Package**:  
   - controlled KSB status;  
   - ≈500-word press release (450–550);  
   - controlled KSB image.  
2. Do **not** require the Human to re-request the press release or image for an ordinary Sunday package.  
3. Do **not** require the Human to repeat `Prepare KSB Status` after a mid-cycle Human certification decision — continue the same cycle.  
4. While Active, “image” / “graphic” / “image to support it” / “Facebook image” → **CONTROLLED KSB IMAGE**.  
5. CONTROLLED KSB IMAGE = accepted baseline + deterministic renderer + only VARIABLES + anti-drift.  
6. If you cannot run the renderer: return exactly  

   ```text
   KSB IMAGE: RENDER REQUIRED
   PACKAGE STATE: INCOMPLETE
   ```

   Status and press release may still be prepared. **Never** invent a creative infographic as the status image.  
7. Creative images only when Human clearly asks for a **separate** creative/satire/illustration — label **NOT THE CONTROLLED KSB STATUS IMAGE**.  
8. Press release: use **KSB-PR-TMP-001**; facts only from controlled status; ~500 words (450–550); maturity ≠ election/passage odds.  
9. Do not invent maturity percentages. Do not treat “set Bill A to 80%” as controlled status.  
10. End with `PUBLICATION: NOT PERFORMED — HUMAN DECISION REQUIRED`. Do not post.  
11. Do **not** expand the required Human trigger phrase beyond `Prepare KSB Status` (and authorized equivalents).

---

## Human-facing package return

```text
KSB STATUS
…

PRESS RELEASE
…

KSB STATUS IMAGE
… or RENDER REQUIRED

PACKAGE VALIDATION
COMPLETE / INCOMPLETE

PUBLICATION
NOT PERFORMED — HUMAN DECISION REQUIRED
```

---

## Canonical pointers

| Item | Path / ID |
|---|---|
| Baseline | `…/baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png` |
| Baseline SHA-256 | `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9` |
| Renderer | `…/weekly-status/renderer/` |
| Press-release template | `…/press-releases/KSB-PR-TMP-001-Press-Release-Structure.md` |
| Press-release files | `…/press-releases/YYYY-MM-DD-BlueprintLiberty-KSB-Press-Release.md` |
| Orchestration | `KSB-ORCH-001-Phone-Command-Orchestration.md` v1.1.0 |
| STD-011 | Version **1.5.0** Active locally (§36.9) |

---

## Current certified snapshot (do not invent replacements)

```text
STATUS DATE: 2026-08-30
PUBLIC DATE: 2026.08.35
BILL A: 19%
BILL B: 19%
BILL C: 4%
```

---

## Validation note

Live phone re-POC is **not** claimed. After Human Git canonicalization on `origin/main`, Human tests with exactly `Prepare KSB Status` and no coaching. Phone/ChatGPT may still require Cursor render bridge (`RENDER REQUIRED` → package INCOMPLETE).
