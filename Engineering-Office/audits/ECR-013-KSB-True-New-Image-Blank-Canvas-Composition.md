# ECR-013 — KSB True New-Image Deterministic Blank-Canvas Composition

**Document ID:** ECR-013  
**Title:** True New Image Each Render / Blank Canvas / Fixed Layer / Design Specification Control  
**Classification:** Engineering Change Request  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001  
**Governing Standards:** STD-011 Part B; KSB-ORCH-001  
**Governing Work Card:** **CWC-CE-096**  
**Predecessor:** ECR-012; CWC-CE-094; CWC-CE-095  
**Status:** **HUMAN ACCEPTED for local candidate implementation** (source: CWC-CE-096 Human Engineer requirement “new image each time”); **OPERATIONAL ACTIVATION BLOCKED** pending Human visual acceptance of candidate PNG  
**Version:** **1.0.0**  
**Effective Date:** 2026-08-30 (local candidate under CWC-CE-096; Git / live activation pending)  
**Primary Category:** PUB  
**Secondary Categories:** STD, ADM  
**Requestor:** Human Engineer  
**Preparing Agent:** CE-Engineer  

```text
HUMAN REQUIREMENT (CWC-CE-096):
NEW IMAGE EACH TIME = NEW BLANK CANVAS + CONTROLLED SPEC/ASSETS/TEXT + CURRENT VARIABLES

PROHIBITED AS ORDINARY CANVAS:
- previous weekly KSB PNG
- populated BL-WEEKLY-STATUS-BASELINE-v1.0
- plate-over / erase / cover / inpaint of historical weekly ink

CANDIDATE RENDERER: ksb_renderer@2.0.0-CWC-CE-096-CANDIDATE
OPERATIONAL ACCEPTANCE: REQUIRED (Human visual gate) BEFORE ACTIVATION / GIT
NO MATURITY / PUBLICATION / LIVE RENDER UNDER THIS CWC
```

---

## 1. Defect

| ID | Title | Classification |
|---|---|---|
| **KSB-RENDER-002** | Operational human acceptance failure — plate-over-populated-baseline retained visible historical weekly content (e.g. Bill C “10%” with current “4%”) | OPERATIONAL HUMAN ACCEPTANCE FAILURE |

**Evidence preserved:** KSB-RENDER-2026-08-30-004 / Issue #5 / run 33336840366 / SHA `ad370c32116973a7f063214cd08f1601bd435c93` / renderer `ksb_renderer@1.1.0-CWC-CE-094` / workflow SUCCESS / Human REJECTED.

CWC-CE-094 / ECR-012 plate-fill improved composition but did **not** satisfy “new image each time” as blank-canvas construction.

---

## 2. Authorized changes

1. Ordinary render equation:

```text
NEW PNG = F(
  BLANK 1536×912 CANVAS,
  CONTROLLED DESIGN SPECIFICATION (regions.json),
  CONTROLLED FIXED LAYER / FIXED ASSETS,
  CONTROLLED FIXED TEXT (embedded in fixed layer until separately extracted),
  CURRENT status_date / bill_a / bill_b / bill_c
)
```

2. Controlled fixed-layer asset `FIXED-LAYER-v1.0-CWC-CE-096` (hashed) with **zero weekly variable ink**.  
3. Anti-drift reference for ordinary renders = **fixed layer** (not populated baseline as canvas).  
4. Baseline `BL-WEEKLY-STATUS-BASELINE-v1.0` retained as **historical Human-accepted visual reference** (integrity verified; **not** ordinary canvas).  
5. Candidate renderer identity `ksb_renderer@2.0.0-CWC-CE-096-CANDIDATE`.  
6. Regression: three-state contamination, fresh-process equivalence, source-lineage, historical-value absence.  
7. STD-011 / KSB-ORCH amendments for blank-canvas composition.

---

## 3. Non-goals

No generative image · no maturity change · no live Issue / workflow dispatch · no push/publication under CWC-CE-096 · no silent change to stale breadcrumb “Live 2026.10.05 Report (Files)” · no rewrite of CWC-CE-094/095 historical records.

---

## 4. Implementation package (local)

| Item | Identity |
|---|---|
| Renderer | `2.0.0-CWC-CE-096-CANDIDATE` |
| Fixed layer | `renderer/assets/FIXED-LAYER-v1.0-CWC-CE-096.png` |
| Fixed layer SHA-256 | `A445685853095203F4D30941AED33320EF1629E643BA0DA6D8FCF95860787E05` |
| Design spec | `renderer/regions.json` |
| Asset manifest | `renderer/assets/fixed_assets_manifest.json` |
| STD-011 | → 1.8.0 |
| KSB-ORCH-001 | → 1.4.0 |

---

## 5. Activation gate

Local technical PASS ≠ operational acceptance.

**NEXT:** Human Engineer visual inspection of candidate PNG labeled **CANDIDATE — NOT YET OPERATIONALLY ACCEPTED**.

Only after Human ACCEPT: CE-GitManager canonicalization + renderer allowlist / SHA updates.
