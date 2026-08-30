# Human Administrative Gate — KSB Issue-bridge Remote Enablement

**Document ID:** KSB-ISSUE-BRIDGE-HUMAN-ADMIN-GATE-001  
**Authority:** ECR-009 v0.3.0 HUMAN ACCEPTED  
**Status:** STOP — HUMAN ACTION REQUIRED  
**Date:** 2026-08-30  

Local implementation is complete. Remote bridge POC cannot proceed until the following Human gates are satisfied **in order**.

---

## Gate 1 — Isolated Windows runner provisioning

1. Create dedicated Windows VM (not daily-driver).  
2. Install Git, Python 3.11, Pillow, OpenCV, NumPy.  
3. Confirm `C:\Windows\Fonts\arialbd.ttf` exists.  
4. Install GitHub Actions self-hosted runner with labels: `self-hosted`, `Windows`, `ksb-render-windows`.  
5. Do **not** paste registration tokens into chat/repo files.

See `ISOLATED-WINDOWS-RUNNER-SPEC.md`.

---

## Gate 2 — GitHub Actions repository Variables

In `jhodges07/Constitutional-Engineering` → Settings → Secrets and variables → Actions → **Variables**:

| Variable | Example value | Purpose |
|---|---|---|
| `AUTHORIZED_KSB_RENDER_ACTORS` | `jhodges07` | Comma-separated GitHub logins allowed to open render Issues |
| `ALLOWED_KSB_CANONICAL_SHAS` | `4aeaf60b330ad41b5750ce523ad850a75325aa78` | Comma-separated SHAs permitted for checkout/render |

Do **not** put these values in public Issue bodies.

Optional: create labels `ksb-render:succeeded`, `ksb-render:rejected-auth`, `ksb-render:failed` (workflow tolerates missing labels).

---

## Gate 3 — Git deployment of workflow + bridge package

Commit/push (Human Git gates HG-4/HG-5) must include at least:

- `.github/workflows/ksb-render-bridge.yml`
- `Engineering-Office/publication/weekly-status/issue-bridge/**`
- ECR-009 acceptance record + related CWC-088 package as Human directs

**This CWC does not stage/commit/push.**

```text
GIT INTEGRATION REQUIRED FOR REMOTE BRIDGE POC
```

---

## Gate 4 — Non-production real-run proof (after 1–3)

ChatGPT opens controlled `[KSB-RENDER]` Issue → gate PASS → isolated render → artifact → ChatGPT download/reconcile → no publication.

Final `Prepare KSB Status` phone POC remains separately gated.
