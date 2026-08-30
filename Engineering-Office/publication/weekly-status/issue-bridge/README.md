# KSB Issue-bridge — Local Implementation README

**Document ID:** KSB-ISSUE-BRIDGE-IMPL-001  
**ECR-009:** v0.3.0 HUMAN ACCEPTED  
**Status:** Implemented locally — remote execution Human-gated  

## Layout

| Path | Role |
|---|---|
| `ksb_issue_bridge/` | Gate + RESULT library |
| `scripts/run_gate.py` | Actions gate CLI |
| `scripts/run_render.py` | Actions render helper (existing renderer only) |
| `tests/test_gate.py` | Local security/schema tests |
| `ISOLATED-WINDOWS-RUNNER-SPEC.md` | Runner provisioning |
| `HUMAN-ADMIN-GATE.md` | Exact Human gates |
| `../../../.github/workflows/ksb-render-bridge.yml` | Workflow (local; not deployed until Git gate) |

## Local gate tests

```powershell
cd Engineering-Office\publication\weekly-status\issue-bridge
python tests\test_gate.py
```

## Env vars (Actions Variables)

- `AUTHORIZED_KSB_RENDER_ACTORS`
- `ALLOWED_KSB_CANONICAL_SHAS`
