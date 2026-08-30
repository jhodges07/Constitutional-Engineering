# GIT HANDOFF — CWC-CE-096 (BLOCKED ON HUMAN VISUAL ACCEPTANCE)

**From:** CE-Engineer  
**To:** Human Engineer (visual gate) → then CE-GitManager  
**Status:** Local Outcome A complete — **DO NOT PUSH** until Human ACCEPT of candidate image  

---

## What changed (local only)

- True blank-canvas compositor (`ksb_renderer@2.0.0-CWC-CE-096-CANDIDATE`)
- Controlled fixed layer asset + manifest
- ECR-013; STD-011 → 1.8.0; KSB-ORCH → 1.4.0
- Three-state / lineage / fresh-process tests
- Candidate PNG for Human review

## Candidate PNG (inspect this)

```text
Engineering-Office/publication/weekly-status/renderer/tests/_non_production_output/CANDIDATE-CWC-CE-096-NOT-OPERATIONALLY-ACCEPTED-19-19-4.png
SHA-256: 9DE5ECC8530182C45A69DCC394A3FF567443374D5BCE18D9AF4AAD6399E8618E
Label: CANDIDATE — NOT YET OPERATIONALLY ACCEPTED
Maturity drawn: 19 / 19 / 4
```

## After Human ACCEPT

1. CE-GitManager: commit scoped CWC-CE-096 paths only (preserve unrelated Human work).  
2. Update `ALLOWED_KSB_CANONICAL_SHAS` to new SHA.  
3. ChatGPT Issues must use `renderer_id=ksb_renderer@2.0.0-CWC-CE-096-CANDIDATE` until a final non-candidate identity is authorized.  
4. Do **not** create live Issues from Cursor.

## After Human REJECT

Return to CE-Engineer with specific visual defects. Do not enlarge masks as primary fix. Do not revert to plate-over-populated-baseline.

## Firewalls preserved

No maturity change · no publication · no live Issue under this CWC · Issue #5 / run 33336840366 historical evidence preserved.

## Stale breadcrumb (separate)

`Live 2026.10.05 Report (Files)` classified **STALE_BASELINE_STATIC_CONTENT** — not silently changed; needs separate Human-authorized CWC if correction desired.
