# ECR-012 — KSB Human Product Delivery and Fresh Deterministic Image Composition

**Document ID:** ECR-012  
**Title:** Single-Copy Press Release / Inline Controlled Image / Clean Variable Composition  
**Classification:** Engineering Change Request  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001  
**Governing Standards:** STD-011 Part B (§36); KSB-ORCH-001  
**Governing Work Card:** **CWC-CE-094**  
**Predecessor:** ECR-011; ECR-009; CWC-CE-084; CWC-CE-092; CWC-CE-093  
**Status:** **HUMAN ACCEPTED** (source: CWC-CE-094 Human Engineer concurrence)  
**Version:** **1.0.0**  
**Effective Date:** 2026-08-30 (local implementation under CWC-CE-094; Git pending)  
**Primary Category:** PUB  
**Secondary Categories:** STD, ADM  
**Requestor:** Human Engineer  
**Preparing Agent:** CE-Engineer  

```text
HUMAN ACCEPTED — CWC-CE-094
COMMAND 2: ONE SINGLE-COPY PRESS-RELEASE BOX
COMMAND 3: INLINE CONTROLLED PNG (ZIP = engineering artifact only)
FRESH DETERMINISTIC COMPOSITION FROM CLEAN VARIABLE PLATES
NO ORDINARY INPAINT / PIXEL-SURGERY DEPENDENCY
BASELINE v1.0 FILE UNCHANGED (accepted appearance authority preserved)
NO MATURITY / PUBLICATION / LIVE RENDER UNDER THIS CWC
```

---

## 1. Defects

| ID | Title |
|---|---|
| KSB-HUMAN-DELIVERY-001 | Press release not required as one single-copy box |
| KSB-HUMAN-DELIVERY-002 | ZIP/file treated as primary Human image product |
| KSB-RENDER-001 | Historical variable values ghost under current values (baseline baked 25/35/10 + Telea inpaint ordinary path) |

---

## 2. Authorized changes

1. Human-product rules for Commands 2–3 (STD-011 / KSB-ORCH).  
2. Renderer: replace ordinary `_clear_region_inpaint` with **deterministic solid plate fill** of controlled `plate_rgb` / bar `track_rgb`, then draw current variables.  
3. Preserve `BL-WEEKLY-STATUS-BASELINE-v1.0` file/SHA as Human-accepted **visual appearance / anti-drift reference**; composition clears variable plates each render (no new baseline acceptance required for this remediation).  
4. Terminology: **BASELINE** = accepted appearance + anti-drift reference; **variable plates** = clean fill colors for weekly composition (documented in `regions.json`).

---

## 3. Non-goals

No generative image · no baseline silent replacement · no maturity change · no live Test #4 · no publication · no overwrite of historical fixture `758AFA76…`.

---

## 4. Implementation package

STD-011 → 1.7.0 · KSB-ORCH-001 → 1.3.0 · renderer 1.1.0-CWC-CE-094 · regions plate_rgb · orchestration delivery fields · tests.
