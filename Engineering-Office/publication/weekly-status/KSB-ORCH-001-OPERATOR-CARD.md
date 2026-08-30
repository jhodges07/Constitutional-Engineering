# ChatGPT / Phone Operator Card — KSB Status (CWC-CE-092)

**Document ID:** KSB-ORCH-001-OPERATOR-CARD  
**Governing Procedure:** KSB-ORCH-001 **v1.2.0** — Active under STD-011 **v1.6.0** §36 / §36.11 / ECR-011  
**Governing Standard:** STD-011 Version 1.6.0 Part B  
**Governing Work Card:** CWC-CE-087; CWC-CE-088; **CWC-CE-092**  
**Audience:** ChatGPT phone / Custom GPT / Cursor operators (implementation aid)  
**Status:** Active under ECR-011 Human-accepted three-step contract  
**Human-facing sequence:** `Prepare KSB Status` → `Next` → `Next`  

---

## Hard rules (must follow)

1. **Step 1 — `Prepare KSB Status`:** return controlled **KSB STATUS** only, then **stop**.  
   - Do **not** auto-return press release or image.  
   - Do **not** create a GitHub render Issue at Step 1.  
2. **Step 2 — `Next`** (status complete; PR not yet returned): return ≈500-word press release (450–550; KSB-PR-TMP-001) from the **same** package values. Stop. Do **not** create a render Issue.  
3. **Step 3 — `Next`** (PR complete; image not returned): enter **CONTROLLED IMAGE** path only.  
4. At most **one** render request/Issue per active package. If image IN PROGRESS, `Next` reuses that request — **no duplicates**.  
5. While Active, “image” / “graphic” / “Facebook image” → **CONTROLLED KSB IMAGE**.  
6. CONTROLLED KSB IMAGE = accepted baseline + deterministic renderer + only VARIABLES + anti-drift. **Never** `image_gen` as status image.  
7. If render unavailable / running: `KSB IMAGE: IN PROGRESS` or `KSB IMAGE: RENDER REQUIRED` / `BLOCKED` as applicable — package may still have STATUS + PRESS RELEASE.  
8. Creative images only when Human clearly asks for a **separate** creative artifact — label **NOT THE CONTROLLED KSB STATUS IMAGE**.  
9. Do not invent maturity percentages. Preserve certified values across steps.  
10. After all three products: `PACKAGE COMPLETE — HUMAN REVIEW REQUIRED`. `PUBLICATION: NOT PERFORMED`.  
11. After PACKAGE COMPLETE, `Next` does **not** start a new weekly cycle — require new `Prepare KSB Status`.  
12. Do not ask the Human to open GitHub, find run IDs, or download artifacts for ordinary success.

---

## Human-facing sequence

```text
Human: Prepare KSB Status
System: <controlled KSB status>

Human: Next
System: <approximately 500-word KSB press release>

Human: Next
System: <controlled KSB image | IN PROGRESS | BLOCKED>
```

---

## Canonical pointers

| Item | Path / ID |
|---|---|
| Baseline | `…/baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png` |
| Baseline SHA-256 | `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9` |
| Renderer | `…/weekly-status/renderer/` |
| Orchestration state machine | `…/orchestration/ksb_package_state.py` |
| Press-release template | `…/press-releases/KSB-PR-TMP-001-Press-Release-Structure.md` |
| Orchestration | `KSB-ORCH-001` **v1.2.0** |
| STD-011 | Version **1.6.0** (§36.11) |

---

## Current certified snapshot (do not invent replacements)

```text
STATUS DATE: 2026-08-30
PUBLIC DATE: 2026.08.35
BILL A: 19%
BILL B: 19%
BILL C: 4%
BASELINE: BL-WEEKLY-STATUS-BASELINE-v1.0
```
