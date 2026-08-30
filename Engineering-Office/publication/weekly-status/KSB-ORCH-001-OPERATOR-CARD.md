# ChatGPT / Phone Operator Card — KSB Status (CWC-CE-094)

**Document ID:** KSB-ORCH-001-OPERATOR-CARD  
**Governing Procedure:** KSB-ORCH-001 **v1.3.0** — STD-011 **v1.7.0** / ECR-011 / ECR-012  
**Human-facing sequence:** `Prepare KSB Status` → `Next` → `Next`  

---

## Hard rules

1. **Prepare KSB Status** → STATUS only in the reply. No PR. No image. No render Issue.  
2. **First Next** → complete press release in **ONE SINGLE-COPY BOX** (publishable text only inside the box). No render Issue.  
3. **Second Next** → controlled image path; at most one render request; on success display **PNG INLINE** in the reply.  
4. ZIP / Actions artifact / RESULT.json = **engineering evidence**, not the ordinary Human image product.  
5. Do not ask the Human to open a ZIP merely to see the weekly image.  
6. Controlled image = baseline + clean plates + current variables + deterministic renderer + anti-drift. **Never** image_gen.  
7. If image still running: `KSB IMAGE: IN PROGRESS` — reuse same request (no duplicate).  
8. Preserve certified maturity across steps (currently 19/19/4).  
9. After all three products: HUMAN REVIEW REQUIRED. Publication NOT PERFORMED.  
10. After PACKAGE COMPLETE, Next does not start a new cycle.

---

## Intended interaction

```text
Human: Prepare KSB Status
ChatGPT: <STATUS>

Human: Next
ChatGPT: [ONE COPYABLE BOX — full press release]

Human: Next
ChatGPT: [CONTROLLED PNG DISPLAYED INLINE]
```

---

## Current certified snapshot

```text
STATUS DATE: 2026-08-30
BILL A/B/C: 19% / 19% / 4%
BASELINE: BL-WEEKLY-STATUS-BASELINE-v1.0 (17F574D4…)
RENDERER: ksb_renderer@1.1.0-CWC-CE-094
```
