# GIT HANDOFF — CWC-CE-099

**From:** CE-Engineer  
**To:** Human Engineer → CE-GitManager (after Human authorize)  
**Status:** Local Outcome A — **no push under this CWC**  

## Changed paths (scoped)

- `issue-bridge/ksb_issue_bridge/constants.py` — identity contract comments  
- `issue-bridge/ksb_issue_bridge/gate.py` — explicit mismatch messages (expected vs got)  
- `issue-bridge/tests/test_gate.py` — reject clean-master-as-baseline_id  
- `issue-bridge/tests/test_ce099_baseline_id_contract.py` — new  
- `KSB-ORCH-001-Phone-Command-Orchestration.md` → 1.5.1  
- `KSB-ORCH-001-OPERATOR-CARD.md` — Issue field contract  
- `KSB-RENDER-003-Baseline-ID-Contract-Mismatch.md`  
- `CWC-CE-099-VALIDATION.md`  
- this handoff  

## Do not

- Reuse Issue #6  
- Change renderer / clean master / maturity / date / breadcrumb  
- Create hosted test under CE-099  

## After Human ACCEPT of this reconciliation

1. CE-GitManager commit scoped paths  
2. Confirm `ALLOWED_KSB_CANONICAL_SHAS` includes post-commit SHA if required  
3. Separate CWC for one new hosted test with **corrected** `baseline_id`
