# Human Provisioning — Isolated Windows Runner (Exact Steps)

**Document ID:** KSB-ISSUE-BRIDGE-HUMAN-PROVISIONING-001  
**Status:** HUMAN ACTION REQUIRED  
**Date:** 2026-08-30  
**Discovery:** No repository Actions runners (`total_count=0`). No Hyper-V VMs visible to CE-Engineer. Daily-driver workstation **must not** be registered.

```text
ISOLATED WINDOWS RUNNER: HUMAN PROVISIONING REQUIRED FOR SELF-HOSTED FALLBACK PATH
CURRENT CWC-CE-088 POC PATH: GITHUB-HOSTED windows-2022 (ECR-009 0.3.1)
SELF-HOSTED VM: NOT REQUIRED FOR CURRENT POC / FALLBACK ONLY
HUMAN DAILY-DRIVER WORKSTATION: PROHIBITED
```

**Status note (2026-08-30):** For the NON-PRODUCTION KSB bridge POC, Human directed GitHub-hosted Windows acceleration. This document remains the **self-hosted fallback / future** procedure. Do not delete.
---

## A. Create isolated Windows environment

1. Create a **dedicated** Windows 10/11 or Server 2019+ x64 VM (Hyper-V, VMware, VirtualBox, or equivalent).  
2. Do **not** use the Human daily-driver Windows profile as the runner.  
3. Minimum: 2 vCPU, 4 GB RAM (8 GB preferred), 40 GB free disk.  
4. Do **not** map personal document drives or browser profiles into the VM.  
5. Do **not** open inbound public firewall ports for the runner.  
6. Create a dedicated local Windows user (e.g. `ksb-runner`) with least privilege; avoid using your personal admin login for ongoing runner service.

**Paid cloud VMs:** not authorized by this CWC — require separate Human approval.

---

## B. Install dependencies (inside the VM only)

1. Install **Git for Windows**.  
2. Install **Python 3.12.10** x64 (matches current local certification stack that produced fixture SHA `758AFA76…`; record exact version).  
   - Note: GitHub-hosted **gate** job uses Python 3.11; Windows **render** job uses the VM Python.  
3. Create a venv and install (pin exactly; re-certify after install):

```text
pip install Pillow==12.3.0 opencv-python==5.0.0 numpy==2.5.2
```

4. Confirm font file exists (do **not** copy fonts into Git):

```text
C:\Windows\Fonts\arialbd.ttf
```

5. Clone is **not** required permanently; Actions runner will checkout. Optional smoke clone of `jhodges07/Constitutional-Engineering` for offline verification only.

---

## C. Register repository-scoped GitHub Actions runner

1. On GitHub: `jhodges07/Constitutional-Engineering` → Settings → Actions → Runners → New self-hosted runner → Windows x64.  
2. Follow GitHub’s download/config commands **inside the VM**.  
3. When prompted for labels, ensure:

```text
self-hosted
Windows
ksb-render-windows
```

4. Suggested runner name: `KSB-RENDER-WIN-01`  
5. Scope: **This repository** only (not org-wide).  
6. Registration token: obtain from GitHub UI at registration time; **never** paste into chat, Issues, or the repo.  
7. Install as a Windows service under the dedicated `ksb-runner` account where practical.  
8. Confirm runner shows **Idle/Online** in repo Settings → Actions → Runners.

---

## D. Configure Actions Variables (no secrets required for allowlists)

Repo → Settings → Secrets and variables → Actions → **Variables**:

| Name | Value |
|---|---|
| `AUTHORIZED_KSB_RENDER_ACTORS` | `jhodges07` |
| `ALLOWED_KSB_CANONICAL_SHAS` | *(leave empty until after Git integration — then set to BRIDGE_INTEGRATION_SHA)* |

Do not put these values in public Issue bodies.

Optional labels: `ksb-render:succeeded`, `ksb-render:rejected-auth`, `ksb-render:failed`.

---

## E. After Git integration (CE-GitManager)

1. Note `BRIDGE_INTEGRATION_SHA` from the CWC-088 push.  
2. Set `ALLOWED_KSB_CANONICAL_SHAS` to that SHA (lowercase 40-hex).  
3. Stop — do **not** create the POC Issue until Human authorizes the real-run proof.

---

## F. Stop conditions

- Do not register runner on daily-driver.  
- Do not commit tokens.  
- Do not create `[KSB-RENDER]` Issue in this provisioning step.  
- Do not publish.

---

## G. Return to CE-Engineer

When VM exists, deps installed, runner online, and Variables set (SHA after Git):

Continue CWC-CE-088 with **CE-Engineer** for isolated determinism/anti-drift certification on the VM, then **CE-GitManager** if Git not yet done (preferred order: provision runner can occur before or after Git, but `ALLOWED_KSB_CANONICAL_SHAS` and real-run require Git first for workflow presence).

**Recommended practical order:**

1. Human provisions VM + deps (this doc A–B)  
2. Human authorizes **CE-GitManager** Git package  
3. Human sets Variables (D + E)  
4. Human registers runner (C) against repo with workflow present  
5. CE-Engineer isolated certification + real-run proof (separate CWC)  
