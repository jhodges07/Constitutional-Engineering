# GIT HANDOFF — CWC-CE-111

**From:** CE-Engineer  
**To:** CE-GitManager  
**Status:** Human-concurred — **CWC-CE-112 canonicalization authorized**

## Purpose

Canonicalize KSB-ORCH-001 active clean-master / renderer identity synchronization to the Human-accepted and hosted-accepted ECR-015 configuration (v1.1 / 2.1.0).

## Authorized paths only

1. `Engineering-Office/publication/weekly-status/KSB-ORCH-001-Phone-Command-Orchestration.md`
2. `Engineering-Office/publication/weekly-status/CWC-CE-111-VALIDATION.md`
3. `Engineering-Office/publication/weekly-status/issue-bridge/GIT-HANDOFF-CWC-CE-111.md` (this file)

Do **not** include unrelated dirty/untracked Human paths.

## Before → after (active identities)

| Field | Before | After |
|---|---|---|
| Active renderer | `ksb_renderer@2.0.0-CWC-CE-097-CANDIDATE` | `ksb_renderer@2.1.0-CWC-CE-107-CANDIDATE` |
| Active clean master | `BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE` | `BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.1-CWC-CE-107-CANDIDATE` |
| KSB-ORCH version | 1.5.2 | **1.5.2** (unchanged — Option A) |
| STD-011 | 1.9.0 | 1.9.0 (unchanged) |
| baseline_id | `BL-WEEKLY-STATUS-BASELINE-v1.0` | unchanged |
| ECR | — | **no new ECR** |

## Tests (already run by CE-Engineer)

- `issue-bridge/tests/test_ce099_baseline_id_contract.py` → PASS  
- `renderer/tests/test_ce107_public_cleanup.py` → PASS  

## Recommended commit scope / message

Single commit limited to the three authorized paths above.

Suggested subject:

```text
CWC-CE-111: sync KSB-ORCH active identities to v1.1 / 2.1.0
```

## Explicit non-goals

- No renderer / regions / constants code changes  
- No hosted rerender  
- No maturity / publication  
- No ORCH behavior redesign  
- Do not bump KSB-ORCH beyond 1.5.2 under this handoff  

## Starting SHA for this CWC

`87059f38119db8ba129b9a442204028f1e434a12` (CE-110 closure / current origin/main at CE-Engineer start)

## After push (CE-GitManager / Human)

If future hosted Issues must pin the post-commit SHA, update Actions variable `ALLOWED_KSB_CANONICAL_SHAS` only when Human authorizes a new render against that SHA. Documentation-only sync does not itself require a hosted render.
