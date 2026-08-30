# CWC-CE-096 — Validation Report

**Work Card:** CWC-CE-096 — KSB TRUE NEW-IMAGE DETERMINISTIC COMPOSITION  
**Agent:** CE-Engineer  
**Date:** 2026-08-30  
**Outcome:** **A**

---

## Human-facing summary

```text
CWC-CE-096
KSB TRUE NEW-IMAGE DETERMINISTIC COMPOSITION

OUTCOME: A
HUMAN REQUIREMENT: NEW IMAGE EACH TIME
NEW BLANK CANVAS: PASS
PREVIOUS WEEKLY PNG USED AS CANVAS: NO
POPULATED BASELINE USED AS CANVAS: NO
OLD WEEKLY IMAGE MODIFIED: NO
HISTORICAL VALUES REQUIRE ERASURE: NO
CONTROLLED DESIGN SPECIFICATION: PASS (regions.json)
CONTROLLED FIXED ASSETS: PASS (FIXED-LAYER-v1.0-CWC-CE-096)
CURRENT VALUES DRAWN FRESH: PASS
THREE-STATE CONTAMINATION: 0
RENDER-HISTORY EFFECT: 0
DETERMINISM: PASS
VISUAL CONTROL: PASS (anti-drift vs fixed layer)
PRESS RELEASE CONTRACT: PRESERVED
INLINE IMAGE CONTRACT: PRESERVED
BASELINE: PRESERVED AS HISTORICAL VISUAL AUTHORITY
CURRENT (historical operational) RENDERER: ksb_renderer@1.1.0-CWC-CE-094
CANDIDATE RENDERER: ksb_renderer@2.0.0-CWC-CE-096-CANDIDATE
KSB MATURITY: 19 / 19 / 4 — UNCHANGED
CANDIDATE IMAGE: produced (see paths below) — NOT OPERATIONALLY ACCEPTED
HUMAN VISUAL ACCEPTANCE: REQUIRED
LIVE RENDER ISSUE: NOT CREATED
WORKFLOW DISPATCH: NOT PERFORMED
GIT PUSH: NOT PERFORMED
PUBLICATION: NOT PERFORMED
NEXT AGENT: Human Engineer
NEXT ACTION: Visually accept or reject candidate PNG before Git canonicalization
STOP.
```

---

## Required validation matrix

| Field | Result |
|---|---|
| A Outcome | **A** |
| B Agent | CE-Engineer |
| C Repository | jhodges07/Constitutional-Engineering (`X:\GitHub\Constitutional-Engineering`) |
| D Branch | main |
| E Starting HEAD | `ad370c32116973a7f063214cd08f1601bd435c93` |
| F Starting origin/main | `ad370c32116973a7f063214cd08f1601bd435c93` |
| G Expected predecessor SHA | `ad370c32116973a7f063214cd08f1601bd435c93` |
| H HEAD == origin/main | PASS (at start; local uncommitted CWC-CE-096 work; no push) |
| I Working-tree state | Unrelated Human dirty/untracked work present — preserved |
| J Unrelated Human work preserved | YES |
| K Operational rejection evidence recorded | YES |
| L Defect identity | **KSB-RENDER-002** |
| M Issue #5 preserved | YES |
| N Run 33336840366 preserved | YES |
| O Workflow success preserved | YES (execution SUCCESS ≠ product acceptance) |
| P Human image acceptance | REJECTED (Issue #5 product) |
| Q Current (historical) renderer | `ksb_renderer@1.1.0-CWC-CE-094` |
| R Candidate renderer | `ksb_renderer@2.0.0-CWC-CE-096-CANDIDATE` |
| S New blank canvas created? | YES (`Image.new`) |
| T Canvas dimensions | 1536 × 912 |
| U Previous output used as canvas? | NO |
| V Previous output bytes read? | 0 (as canvas) |
| W Populated baseline used as canvas? | NO (integrity hash only) |
| X Historical fixture used as canvas? | NO |
| Y Old values erased? | NOT NECESSARY |
| Z Old values covered? | NOT NECESSARY |
| AA Old values inpainted? | NOT NECESSARY |
| AB Design specification path | `renderer/regions.json` |
| AC Fixed asset manifest | `renderer/assets/fixed_assets_manifest.json` |
| AD Fixed-text source | Embedded in fixed layer (stale breadcrumb recorded; not silently changed) |
| AE Weekly variable contract | status_date, bill_a/b/c_percent only |
| AF Bill A | 19% |
| AG Bill B | 19% |
| AH Bill C | 4% |
| AI Three-state values | A 25/35/10; B 19/19/4; C 73/2/91 |
| AJ Three-state contamination | **0** |
| AK Fresh-process equivalence | PASS |
| AL Render-history effect | **0** |
| AM Historical-value absence | PASS |
| AN Source-lineage | PASS (no baseline Image.open as canvas) |
| AO Fixed-asset validation | PASS |
| AP Design-specification validation | PASS |
| AQ Determinism | PASS |
| AR Visual-control validation | PASS (anti-drift vs fixed layer) |
| AS Anti-drift/successor | PASS |
| AT Package continuity | PASS |
| AU No duplicate render | PASS |
| AV Press-release contract | PRESERVED |
| AW Inline-image contract | PRESERVED |
| AX Baseline ID | BL-WEEKLY-STATUS-BASELINE-v1.0 |
| AY Baseline SHA | 17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9 |
| AZ Baseline historical role | Human-accepted visual reference — NOT ordinary canvas |
| BA Baseline used as canvas? | NO |
| BB Stale breadcrumb finding | YES — recorded |
| BC "Live 2026.10.05 Report" | **STALE_BASELINE_STATIC_CONTENT** — incorrect future/static date; do not silently change; propose separate CWC |
| BD ECR required? | YES |
| BE ECR identity/version | ECR-013 1.0.0 |
| BF ECR Human acceptance required for activation? | YES (visual gate); local candidate implementation authorized by CWC-CE-096 |
| BG Controls affected | ECR-013; STD-011→1.8.0; KSB-ORCH→1.4.0; renderer; regions; fixed assets; tests; constants (candidate) |
| BH Local implementation performed? | YES |
| BI Candidate PNG path | `Engineering-Office/publication/weekly-status/renderer/tests/_non_production_output/CANDIDATE-CWC-CE-096-NOT-OPERATIONALLY-ACCEPTED-19-19-4.png` |
| BJ Candidate PNG SHA | `9DE5ECC8530182C45A69DCC394A3FF567443374D5BCE18D9AF4AAD6399E8618E` |
| BK Candidate labeled not operationally accepted? | YES |
| BL Human visual acceptance required? | YES |
| BM Live render Issue created? | NO |
| BN Workflow dispatched? | NO |
| BO New hosted test created? | NO |
| BP Git commit? | NO |
| BQ Git push? | NO |
| BR Publication? | NO |
| BS KSB maturity | 19 / 19 / 4 |
| BT Maturity unchanged | YES |
| BU Bill/LOU state unchanged | YES |
| BV Next agent | **Human Engineer** |
| BW Next logical action | Visually ACCEPT or REJECT candidate PNG; if ACCEPT → CE-GitManager for canonicalization |
| BX Final STOP | STOP |

---

## Local test counts

| Suite | Result |
|---|---|
| `renderer/tests/run_tests.py` | **20/20 PASS** |
| `renderer/tests/test_ce094_composition.py` (successor-compatible) | **14/14 PASS** |
| `renderer/tests/test_ce096_blank_canvas.py` | **PASS** (blank canvas, lineage, three-state, fresh-process, historical absence, antidrift, candidate PNG) |
| `orchestration/tests/test_three_step.py` | **32/32 PASS** (continuity, no-duplicate, single-copy PR, inline PNG) |
| `issue-bridge/tests/test_gate.py` | **19/19 PASS** |

---

## Architecture implemented

```text
Image.new(1536×912)
+ FIXED-LAYER-v1.0-CWC-CE-096 (SHA A4456858…)
+ current variables only
→ PNG
```

Fixed layer SHA-256: `A445685853095203F4D30941AED33320EF1629E643BA0DA6D8FCF95860787E05`

---

## STOP

No live Issue · no workflow_dispatch · no push · no publication.  
Human visual acceptance required before operational activation.
