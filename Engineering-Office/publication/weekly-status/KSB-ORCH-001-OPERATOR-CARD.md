# ChatGPT / Phone Operator Card — KSB Status (CWC-CE-087)

**Document ID:** KSB-ORCH-001-OPERATOR-CARD  
**Governing Procedure:** KSB-ORCH-001 v1.0.0 — Active under STD-011 §36 / ECR-007  
**Governing Standard:** STD-011 Version 1.4.0 Part B  
**Governing Work Card:** CWC-CE-087  
**Audience:** ChatGPT phone / Custom GPT / Cursor operators (implementation aid)  
**Status:** Validated against Active authority — subordinate to STD-011 §36 and KSB-ORCH-001  
**Human-facing trigger (unchanged):** `Prepare KSB Status`  

---

## Hard rules (must follow)

1. `Prepare KSB Status` starts an **Active KSB Cycle**. Keep it until closed or replaced.  
2. Do **not** require the Human to repeat `Prepare KSB Status` for ordinary follow-ups.  
3. While Active, “image” / “graphic” / “image to support it” / “Facebook image” → **CONTROLLED KSB IMAGE**.  
4. CONTROLLED KSB IMAGE = accepted baseline + deterministic renderer + only VARIABLES + anti-drift.  
5. If you cannot run the renderer: return exactly  

   ```text
   KSB IMAGE: RENDER REQUIRED
   ```

   Then name the Cursor / local render bridge. **Never** invent a creative infographic as the status image.  
6. Creative images only when Human clearly asks for a **separate** creative/satire/illustration — label them **NOT THE CONTROLLED KSB STATUS IMAGE**.  
7. Press releases may use new prose but must not change certified percentages, Bill titles, or status date.  
8. Do not invent maturity percentages. Do not treat “set Bill A to 80%” as controlled status.  
9. Do not publish, commit, or push unless Human explicitly authorizes those gates.  
10. Do **not** expand the required Human command beyond `Prepare KSB Status` (and authorized equivalents).

---

## Canonical pointers

| Item | Path / ID |
|---|---|
| Baseline | `Engineering-Office/publication/weekly-status/baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png` |
| Baseline SHA-256 | `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9` |
| Renderer | `Engineering-Office/publication/weekly-status/renderer/` |
| Orchestration | `KSB-ORCH-001-Phone-Command-Orchestration.md` |
| STD-011 §36 | Active in `STD-011-Public-Documentation.md` v1.4.0 |
| Failure lesson | `KSB-POC-FAIL-001-Creative-Image-Substitution.md` |

---

## Current certified snapshot (do not invent replacements)

```text
STATUS DATE: 2026-08-30
PUBLIC DATE: 2026.08.35
BILL A: 19%
BILL B: 19%
BILL C: 4%
```

(Replace only after a new authorized certification cycle.)

---

## Validation note (CWC-CE-087 Bounded Continuation)

Operator Card validated against Human-accepted ECR-007 / STD-011 §36 / Active KSB-ORCH-001.  
Live phone re-POC is **not** claimed by this card and awaits canonical Git integration.
