# KSB Issue-bridge active dependency lock

**Document ID:** KSB-ISSUE-BRIDGE-DEPS-001  
**Authority:** ECR-009 / CWC-CE-088  
**Classification:** AUTHORITATIVE CONFIGURATION (active)  
**Date:** 2026-08-30  

| Package | Pin | Notes |
|---|---|---|
| Python (render host) | 3.12.10 | `actions/setup-python` |
| Pillow | 12.3.0 | |
| opencv-python | **5.0.0.93** | Only OpenCV 5.x distribution on PyPI as of Test #1 remediation; `==5.0.0` does **not** exist. Hosted workflow installs `opencv-python` (not headless). Local Windows may already provide `cv2` via `opencv-python-headless==5.0.0.93` (same distribution version; module string may report `5.0.0`). |
| numpy | 2.5.2 | |

**Historical evidence (do not erase):** Test #1 (`KSB-RENDER-2026-08-30-001`, Actions run `33333667791`, SHA `9e7f5b40…`) failed because the workflow requested `opencv-python==5.0.0` and pip reported no matching distribution.
