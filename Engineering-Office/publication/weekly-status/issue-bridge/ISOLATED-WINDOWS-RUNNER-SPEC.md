# Isolated Windows Runner Specification — KSB Issue-bridge

**Document ID:** KSB-ISSUE-BRIDGE-RUNNER-SPEC-001  
**Authority:** ECR-009 v0.3.0 HUMAN ACCEPTED  
**Status:** SPECIFICATION ONLY — NOT PROVISIONED  
**Date:** 2026-08-30  

```text
HUMAN DAILY-DRIVER WORKSTATION: PROHIBITED AS KSB ISSUE-TRIGGER RUNNER
ISOLATED WINDOWS RUNNER: REQUIRED
```

---

## 1. Purpose

Provide a dedicated Windows execution environment for the `render` job of
`.github/workflows/ksb-render-bridge.yml` so public Issue events cannot cause
arbitrary code execution on the Human Engineer’s daily-driver workstation.

---

## 2. Isolation requirement

| Requirement | Value |
|---|---|
| Form factor | Dedicated Windows VM (Hyper-V / VMware / equivalent) or equivalent isolated physical host |
| Daily-driver reuse | **FORBIDDEN** |
| Interactive Human sessions | Minimize; prefer runner-only login |
| Shared personal secrets | Do not store personal browser profiles, password managers, or unrelated tokens on this host |

---

## 3. Hardware (minimum)

| Resource | Minimum |
|---|---|
| CPU | 2 vCPU |
| RAM | 4 GB (8 GB preferred) |
| Storage | 40 GB free |
| Network | Outbound HTTPS to GitHub Actions endpoints only as required by runner |

---

## 4. Software

| Component | Requirement |
|---|---|
| Windows | Windows 10/11 or Windows Server 2019+ **x64** with desktop experience (font stack) |
| Git | Current Git for Windows |
| Python | **3.11.x** (match local renderer validation) |
| Pillow | Version matching local Engineering workspace install used for CWC-CE-084 tests |
| OpenCV (`opencv-python`) | Same as local renderer tests |
| NumPy | Same as local renderer tests |
| GitHub Actions runner | Latest stable self-hosted runner for Windows x64 |
| Font | `C:\Windows\Fonts\arialbd.ttf` (Arial Bold) present; verify file exists before registration |

Exact pip freeze SHOULD be recorded at first successful real-run proof.

---

## 5. Runner labels (mandatory)

Register with labels:

```text
self-hosted
Windows
ksb-render-windows
```

Workflow targets: `[self-hosted, Windows, ksb-render-windows]`  
Never target bare `self-hosted` alone.

---

## 6. Network

Outbound only as required by GitHub Actions runner documentation (github.com, actions blobs, etc.).  
No inbound public ports required for Issue-trigger design.  
Do not expose RDP to the public Internet without separate Human security decision.

---

## 7. Credentials / secrets

| Item | Rule |
|---|---|
| Runner registration token | Create via GitHub UI/API at registration time; **never commit** |
| `GITHUB_TOKEN` | Provided by Actions per job; least privilege from workflow permissions |
| Repo variables | `AUTHORIZED_KSB_RENDER_ACTORS`, `ALLOWED_KSB_CANONICAL_SHAS` — repository Variables (not Issue body) |
| Workspace cleanup | Enable runner work folder cleanup after jobs |

---

## 8. Lifecycle / patching

- Apply Windows updates on a controlled cadence.  
- After font or Python changes, re-run renderer suite + determinism check before returning to service.  
- Decommission: remove runner from GitHub Org/Repo settings; wipe VM.

---

## 9. Logging

Retain Actions logs via GitHub. Avoid copying secrets into Issue comments. RESULT.json must not contain secrets.

---

## 10. Current environment discovery

As of CWC-CE-088 runner-readiness continuation (2026-08-30):

| Check | Result |
|---|---|
| GitHub Actions runners on repo | **`total_count: 0`** |
| Hyper-V `Get-VM` | **Unavailable / no VMs visible to CE-Engineer** |
| Actions Variables configured | **`0`** |
| Daily-driver as runner | **PROHIBITED** |

```text
ISOLATED WINDOWS RUNNER ENVIRONMENT: NOT AVAILABLE
ISOLATED WINDOWS RUNNER: HUMAN PROVISIONING REQUIRED
```

Exact Human steps: `HUMAN-PROVISIONING-STEPS.md`

### Dependency lock (from local re-certification evidence — install on VM, then re-prove)

| Package | Version observed on Engineering certification host |
|---|---|
| Python | 3.12.10 (Windows render target candidate) |
| Pillow | 12.3.0 |
| OpenCV (`cv2`) | 5.0.0 |
| NumPy | 2.5.2 |

Historical deterministic fixture SHA (fixture A, local suite):  
`758AFA76D1CA087CECD7C62A982FAEF36A7009C673A5B1ED894343893CB26B3A`

Isolated VM must reproduce byte identity after install; do not claim PASS until VM runs prove it.

Gate job (ubuntu) uses Actions `setup-python` **3.11** — independent of Windows render Python.