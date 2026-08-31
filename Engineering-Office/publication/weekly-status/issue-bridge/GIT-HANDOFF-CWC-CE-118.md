# GIT HANDOFF — CWC-CE-118

**From:** CE-Engineer  
**To:** CE-GitManager  
**Status:** Local Outcome A — awaiting Human-authorized canonicalize CWC — COMMIT/PUSH by CE-Engineer: NONE

## Purpose

Canonicalize the bounded KSB three-step **controlled image delivery** defect correction so final `Next` resolves the exact package PNG instead of allowing presentation-layer image-search substitution.

## Do not modify

- Frozen public package content bound to HG-6 / `dedce82d5b9bcaa97e9775aae449680bc9b0edb8` (status text, press release bytes, package PNG bytes, manifest content freeze)
- Maturity 19 / 19 / 4
- HG-6 PASSED record
- Publication destination / execution (still Human-required; NOT YET PERFORMED)

## Authorized paths only

1. `Engineering-Office/publication/weekly-status/orchestration/ksb_package_state.py`
2. `Engineering-Office/publication/weekly-status/orchestration/tests/test_three_step.py`
3. `Engineering-Office/publication/weekly-status/orchestration/tests/test_ce118_controlled_image_delivery.py`
4. `Engineering-Office/publication/weekly-status/KSB-ORCH-001-OPERATOR-CARD.md`
5. `Engineering-Office/publication/weekly-status/KSB-ORCH-001-Phone-Command-Orchestration.md`
6. `Engineering-Office/publication/weekly-status/CWC-CE-118-VALIDATION.md`
7. `Engineering-Office/publication/weekly-status/issue-bridge/GIT-HANDOFF-CWC-CE-118.md` (this file)

Do **not** stage unrelated Human dirty/untracked paths.

## Suggested commit subject

```text
CWC-CE-118: deliver exact KSB package PNG on final Next; forbid image-search fallback
```

## Starting SHA (verify before commit)

`fa4da4b55cf2041f3dd1fb7ca2a0a8e1cd6487b4`

If `origin/main` advanced unexpectedly: STOP; do not reset/rebase/merge/stash Human work.

## Local validation already run

```text
python orchestration/tests/test_three_step.py → PASS
python orchestration/tests/test_ce118_controlled_image_delivery.py → PASS
GENERIC IMAGE SEARCH SUBSTITUTE: REJECTED / IMPOSSIBLE UNDER CONTROLLED PATH
fixture SHA: 5FEECAA3267D07A996968DC4116A0C8AFB8E7181D187302B06401886960D80CC
dims: 1536×912
```

## After push — Human acceptance

```text
Prepare KSB Status → STATUS
Next → PRESS RELEASE
Next → EXACT CONTROLLED KSB IMAGE (not Capitol image search)
```

## STOP

CE-Engineer boundary: no commit, no push under CWC-CE-118.
