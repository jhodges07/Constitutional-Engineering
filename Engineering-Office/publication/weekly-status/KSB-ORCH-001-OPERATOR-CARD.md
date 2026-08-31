# ChatGPT / Phone Operator Card — KSB Status (CWC-CE-108)

**Document ID:** KSB-ORCH-001-OPERATOR-CARD  
**Governing Procedure:** KSB-ORCH-001 **v1.5.2** — STD-011 **v1.9.0** / ECR-014 / ECR-015 / **CWC-CE-099** / **CWC-CE-102** / **CWC-CE-107–108**  
**Human-facing sequence:** `Prepare KSB Status` → `Next` → `Next`  

---

## Hard rules

1. **Prepare KSB Status** → STATUS only. No PR. No image. No render Issue.  
2. **First Next** → press release in **ONE SINGLE-COPY BOX**. No render Issue.  
3. **Second Next** → controlled PNG **INLINE**. At most one render request.  
4. ZIP / artifact = engineering evidence only.  
5. Controlled image = clean master (via **renderer_id**) + dynamic center panel. **Never** image_gen.  
6. Preserve certified maturity (currently 19/19/4).  
7. **Fence-safe Issue bodies (CWC-CE-102 / KSB-RENDER-004):** never put ```ksb-render-request fences in PowerShell `python -c` / double-quoted strings. Write JSON → `write_ksb_issue_body.py` → `gh … --body-file`. Pre-submit parse PASS required. Post-create body readback required. Issue #7 evidence: single-backtick corruption.  

---

## Identity contract (CRITICAL — CWC-CE-099 / KSB-RENDER-003)

```text
Issue field baseline_id  = BL-WEEKLY-STATUS-BASELINE-v1.0
  → HISTORICAL visual baseline identity (gate-enforced)
  → NOT the clean master

Clean master identity    = BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.1-CWC-CE-107-CANDIDATE
  → Active pristine RENDER SOURCE (CWC-CE-107 / ECR-015)
  → Selected by renderer_id → repository renderer config
  → NEVER place this string in baseline_id

Historical clean master  = BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE
  → IMMUTABLE evidence only (do not overwrite)

Issue field renderer_id  = ksb_renderer@2.1.0-CWC-CE-107-CANDIDATE
```

Issue #6 failed because `baseline_id` was set to the clean-master ID.

---

## Current certified snapshot

```text
STATUS DATE: 2026-08-30
BILL A/B/C: 19% / 19% / 4%
baseline_id (Issue): BL-WEEKLY-STATUS-BASELINE-v1.0
CLEAN MASTER (render source): BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.1-CWC-CE-107-CANDIDATE
RENDERER: ksb_renderer@2.1.0-CWC-CE-107-CANDIDATE
HUMAN-ACCEPTED CANDIDATE SHA: 5FEECAA3267D07A996968DC4116A0C8AFB8E7181D187302B06401886960D80CC
CANONICAL SHA: origin/main HEAD after CWC-CE-108 (ALLOWED_KSB_CANONICAL_SHAS)
```

---

## Fence-safe render Issue (CRITICAL — CWC-CE-102 / KSB-RENDER-004)

```text
1. Write request.json (UTF-8) — NO markdown fences in PowerShell-interpolated strings
2. python …/write_ksb_issue_body.py --request request.json --out body.md --allowed-sha <SHA>
   → PRE_SUBMISSION: PASS ; OPENING_BACKTICK_COUNT=3
3. gh issue create -R jhodges07/Constitutional-Engineering --title "…" --body-file body.md
4. gh issue view <N> --json body → re-parse locally → STOP if fence missing
```

Do not reopen Issue #7. Do not weaken the gate parser.
