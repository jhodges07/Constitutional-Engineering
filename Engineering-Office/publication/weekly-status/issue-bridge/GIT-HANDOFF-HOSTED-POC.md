# Git Handoff — CWC-CE-088 GitHub-Hosted Windows POC

**Document ID:** KSB-ISSUE-BRIDGE-HOSTED-POC-GIT-HANDOFF-001  
**Preparing Agent:** CE-Engineer  
**Intended Next Agent:** CE-GitManager  
**Date:** 2026-08-30  
**Parent SHA (expected):** `20fc998e1b94585acd998b62c21e45085a6c083b`  

```text
GIT HANDOFF: READY
STAGING/COMMIT/PUSH: CE-GitManager ONLY
SECRETS: NONE
```

---

## 1. Exact include paths (stage only these)

| Path | Change |
|---|---|
| `.github/workflows/ksb-render-bridge.yml` | `runs-on: windows-2022` + Python/deps/font/runtime evidence |
| `Engineering-Office/audits/ECR-009-KSB-Phone-Render-Execution-Bridge-Control.md` | v0.3.1 hosted-Windows POC authority |
| `Engineering-Office/publication/weekly-status/issue-bridge/HUMAN-PROVISIONING-STEPS.md` | Mark self-hosted as fallback |
| `Engineering-Office/publication/weekly-status/issue-bridge/GIT-HANDOFF-HOSTED-POC.md` | This file |
| `Engineering-Office/publication/weekly-status/CWC-CE-088-HOSTED-POC-VALIDATION.md` | Validation (if present) |

Exclude all unrelated Human dirty/untracked work.

---

## 2. Recommended commit message

```text
CWC-CE-088: authorize GitHub-hosted Windows for KSB bridge POC

Replace self-hosted ksb-render-windows dependency for the
non-production Issue-trigger render path with windows-2022 while
preserving gate authorization and four-variable controls.
```

---

## 3. Post-push Human / CE-Engineer Actions

1. Record `HOSTED_POC_INTEGRATION_SHA` = full 40-char `origin/main`.  
2. Update Actions Variable `ALLOWED_KSB_CANONICAL_SHAS` to that SHA (exact).  
3. Keep `AUTHORIZED_KSB_RENDER_ACTORS=jhodges07`.  
4. **ChatGPT/phone** creates `[KSB-RENDER]` Issue — Cursor does **not**.  

---

## 4. CE-GitManager checklist

- [ ] Verify parent = `20fc998…` (or current origin/main if already advanced only by authorized work)  
- [ ] Stage explicit paths only  
- [ ] Secret scan / validation per GitManager CWC  
- [ ] Commit + non-force push  
- [ ] Return `HOSTED_POC_INTEGRATION_SHA`  
- [ ] Do not create test Issue  
