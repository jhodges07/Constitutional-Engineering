# GIT HANDOFF — CWC-CE-107

**From:** CE-Engineer  
**To:** Human Engineer → CE-GitManager (**only after Human visual ACCEPT**)  
**Status:** Human visual ACCEPT recorded — **CWC-CE-108 canonicalization authorized**  

## Scope

Public-image cleanup: dynamic date, stable breadcrumb, remove engineering metadata strip.

## Changed / added paths (scoped)

### Templates
- `templates/BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.1-CWC-CE-107-CANDIDATE.png` (**new**; do not overwrite v1.0)
- `templates/BL-WEEKLY-STATUS-CLEAN-TEMPLATE-v1.0-CANDIDATE.png` — **UNCHANGED** (immutable evidence)

### Renderer
- `renderer/regions.json`
- `renderer/ksb_renderer/render.py`
- `renderer/ksb_renderer/antidrift.py`
- `renderer/scripts/build_ce107_clean_master.py`
- `renderer/tests/test_ce107_public_cleanup.py`
- `renderer/tests/run_tests.py`
- `renderer/tests/test_ce097_clean_template.py`
- `renderer/tests/_non_production_output/CANDIDATE-CWC-CE-107-PUBLIC-CLEANUP-19-19-4.png` (optional evidence)

### Bridge constants / tests
- `issue-bridge/ksb_issue_bridge/constants.py`
- `issue-bridge/tests/test_gate.py`
- `issue-bridge/tests/test_ce099_baseline_id_contract.py`
- `issue-bridge/tests/test_ce102_fence_safe.py`

### Controls / evidence
- `audits/ECR-015-KSB-Public-Image-Cleanup-PROPOSED.md`
- `publication/weekly-status/CWC-CE-107-VALIDATION.md`
- `publication/weekly-status/issue-bridge/GIT-HANDOFF-CWC-CE-107.md` (this file)

## Do NOT include

- Unrelated Human dirty/untracked work  
- `__pycache__/`  
- Probe crops / CE-104 artifact trees unless requested  

## Version disposition

| Control | Disposition |
|---|---|
| STD-011 | **1.9.0 UNCHANGED** |
| KSB-ORCH | **1.5.2 UNCHANGED** until after Human ACCEPT (then operator-card identity update) |
| ECR-015 | **HUMAN-ACCEPTED** — activated under CWC-CE-108 |
| baseline_id | UNCHANGED |
| Hosted gate/fence | UNCHANGED (schema/parser) |
| RENDERER_ID | `ksb_renderer@2.1.0-CWC-CE-107-CANDIDATE` (accepted) |
| Clean master | successor v1.1-CWC-CE-107-CANDIDATE; v1.0 preserved |
| KSB-ORCH operator card | identity update only (version **1.5.2** unchanged) |

## Candidate identities

| Field | Value |
|---|---|
| Clean master SHA | `29E243233AB0872FFF2323ACC882FC477F71865CE072C4416EEFBDEC8F8576E0` |
| Candidate PNG SHA | `5FEECAA3267D07A996968DC4116A0C8AFB8E7181D187302B06401886960D80CC` |
| Dims | 1536 × 912 |

## After Human ACCEPT

1. CE-GitManager commit scoped paths only.  
2. Activate ECR-015 upon Human acceptance record.  
3. Update KSB-ORCH operator card identities if required.  
4. Separate CWC: decide whether one hosted acceptance render with new `renderer_id` is required before HG-6 publication.
