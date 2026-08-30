# Git Handoff Manifest — CWC-CE-088 KSB Issue-Bridge

**Document ID:** KSB-ISSUE-BRIDGE-GIT-HANDOFF-001  
**Preparing Agent:** CE-Engineer  
**Intended Next Agent:** CE-GitManager  
**Date:** 2026-08-30  
**Predecessor HEAD (pre-integration):** `4aeaf60b330ad41b5750ce523ad850a75325aa78`  

```text
GIT: NOT ADVANCED
STAGING: NOT PERFORMED
SECRETS IN PACKAGE: NONE
```

---

## 1. Purpose

Exact controlled file set for Human-authorized Git integration enabling the remote Issue-trigger bridge POC. Unrelated Human work is **excluded**.

---

## 2. SHA bootstrap order (mandatory)

```text
1. Local CWC-088 package complete (current state)
2. Human authorizes Git (HG-4 / HG-5)
3. CE-GitManager commits + pushes approved package
4. Record resulting origin/main SHA = BRIDGE_INTEGRATION_SHA
5. Human sets Actions Variable ALLOWED_KSB_CANONICAL_SHAS = BRIDGE_INTEGRATION_SHA
   (and later package-prep SHAs as needed)
6. Human sets AUTHORIZED_KSB_RENDER_ACTORS = jhodges07
7. Isolated runner registered + online (labels: self-hosted, Windows, ksb-render-windows)
8. Non-production [KSB-RENDER] Issue / real-run proof (separate authority)
```

Do **not** set `ALLOWED_KSB_CANONICAL_SHAS` to the pre-integration predecessor alone if the bridge workflow/scripts are only present after step 3.

Gate job checks out the workflow tree from the commit that contains the workflow (default branch tip after integration). Render job checks out `canonical_sha` from the Issue payload, which must be on the allowlist — typically `BRIDGE_INTEGRATION_SHA` for the first POC.

---

## 3. Include (controlled package)

| Path | Status | Reason | Secrets? |
|---|---|---|---|
| `.github/workflows/ksb-render-bridge.yml` | created (local) | Issue-trigger workflow | No |
| `Engineering-Office/publication/weekly-status/issue-bridge/**` | created (local) | Gate/RESULT/scripts/specs/tests | No |
| `Engineering-Office/audits/ECR-009-KSB-Phone-Render-Execution-Bridge-Control.md` | created (local) | v0.3.0 HUMAN ACCEPTED | No |
| `Engineering-Office/audits/ECR-008-KSB-Single-Command-Sunday-Package-Control.md` | created (local) | Sunday package ECR | No |
| `Engineering-Office/standards/STD-011-Public-Documentation.md` | modified (local 1.5.0) | §36.9 package contract | No |
| `Engineering-Office/publication/weekly-status/KSB-ORCH-001-Phone-Command-Orchestration.md` | modified (local v1.1.0) | Orchestration | No |
| `Engineering-Office/publication/weekly-status/KSB-ORCH-001-OPERATOR-CARD.md` | modified | Operator aid | No |
| `Engineering-Office/publication/weekly-status/press-releases/**` | created (local) | Press-release path/template | No |
| `Engineering-Office/publication/weekly-status/KSB-ORCH-001-TEST-SCENARIOS-CWC-CE-088.md` | created | Tests | No |
| `Engineering-Office/publication/weekly-status/KSB-RENDER-BRIDGE-001-Capability-Architecture.md` | created | Discovery | No |
| `Engineering-Office/publication/weekly-status/KSB-TRIGGER-RETURN-001-Capability-Proof.md` | created | Capability proof | No |
| `Engineering-Office/publication/weekly-status/KSB-ISSUE-BRIDGE-001-Architecture.md` | created | Issue-trigger architecture | No |
| `Engineering-Office/publication/weekly-status/CWC-CE-088-VALIDATION.md` | created | Validation | No |
| `Engineering-Office/publication/weekly-status/CWC-CE-088-RENDER-BRIDGE-VALIDATION.md` | created | Validation | No |
| `Engineering-Office/publication/weekly-status/CWC-CE-088-TRIGGER-RETURN-VALIDATION.md` | created | Validation | No |
| `Engineering-Office/publication/weekly-status/CWC-CE-088-ISSUE-BRIDGE-VALIDATION.md` | created | Validation | No |
| `Engineering-Office/publication/weekly-status/CWC-CE-088-ISSUE-BRIDGE-IMPL-VALIDATION.md` | created | Validation | No |
| `Engineering-Office/publication/weekly-status/CWC-CE-088-RUNNER-READINESS-VALIDATION.md` | created (this CWC) | Runner readiness | No |
| `Engineering-Office/publication/weekly-status/issue-bridge/GIT-HANDOFF-MANIFEST.md` | this file | CE-GitManager handoff | No |
| `Engineering-Office/publication/weekly-status/issue-bridge/FUTURE-REMOTE-POC-FIXTURE.md` | created | Future POC template | No |

CE-GitManager SHALL confirm final path list against `git status` at handoff time and **exclude** unrelated dirty/untracked Human work (CERs, packages/, definition/working/, LOU generation logs, workspace file, etc.).

---

## 4. Exclude (examples — not exhaustive)

- `Engineering-Office/packages/**`
- `Engineering-Office/definition/working/**`
- Unrelated `CER-*` / LOU generation logs
- `Constitutional-Engineering.code-workspace`
- Any PAT, runner token, password, or Actions secret value
- Font binaries (`arialbd.ttf` etc.)

---

## 5. Post-commit Human Actions Variables

| Variable | When | Value |
|---|---|---|
| `AUTHORIZED_KSB_RENDER_ACTORS` | After Git (or before POC) | `jhodges07` |
| `ALLOWED_KSB_CANONICAL_SHAS` | **After** Git push | Exact `BRIDGE_INTEGRATION_SHA` (40-char lowercase hex) |

Mechanism: repository **Actions Variables** (not secrets; not Issue body).

---

## 6. CE-GitManager checklist

- [ ] Human authorizes commit/push  
- [ ] Stage only §3 paths (reconciled)  
- [ ] Commit message per repo style (CWC-CE-088 Issue-bridge)  
- [ ] Push to `origin/main`  
- [ ] Report `BRIDGE_INTEGRATION_SHA` to Human  
- [ ] Do **not** register runner or create POC Issue unless separately authorized  
