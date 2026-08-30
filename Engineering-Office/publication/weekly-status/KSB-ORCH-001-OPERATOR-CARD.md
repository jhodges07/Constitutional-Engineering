# ChatGPT / Phone Operator Card — KSB Status (CWC-CE-099)

**Document ID:** KSB-ORCH-001-OPERATOR-CARD  
**Governing Procedure:** KSB-ORCH-001 **v1.5.1** — STD-011 **v1.9.0** / ECR-014 / **CWC-CE-099**  
**Human-facing sequence:** `Prepare KSB Status` → `Next` → `Next`  

---

## Hard rules

1. **Prepare KSB Status** → STATUS only. No PR. No image. No render Issue.  
2. **First Next** → press release in **ONE SINGLE-COPY BOX**. No render Issue.  
3. **Second Next** → controlled PNG **INLINE**. At most one render request.  
4. ZIP / artifact = engineering evidence only.  
5. Controlled image = clean master (via **renderer_id**) + dynamic center panel. **Never** image_gen.  
6. Preserve certified maturity (currently 19/19/4).  

---

## Identity contract (CRITICAL — CWC-CE-099 / KSB-RENDER-003)

```text
Issue field baseline_id  = BL-WEEKLY-STATUS-BASELINE-v1.0
  → HISTORICAL visual baseline identity (gate-enforced)
  → NOT the clean master

Clean master identity    = BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE
  → Active pristine RENDER SOURCE
  → Selected by renderer_id → repository renderer config
  → NEVER place this string in baseline_id

Issue field renderer_id  = ksb_renderer@2.0.0-CWC-CE-097-CANDIDATE
```

Issue #6 failed because `baseline_id` was set to the clean-master ID.

---

## Current certified snapshot

```text
STATUS DATE: 2026-08-30
BILL A/B/C: 19% / 19% / 4%
baseline_id (Issue): BL-WEEKLY-STATUS-BASELINE-v1.0
CLEAN MASTER (render source): BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE
RENDERER: ksb_renderer@2.0.0-CWC-CE-097-CANDIDATE
CANONICAL SHA (current): 87e48e631edbc21cc64d96cc2095a0b2703d63d0
```
