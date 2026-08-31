# CWC-CE-118 — Validation Report (Outcome A)

**Work Card:** CWC-CE-118 — KSB THREE-STEP PHONE WORKFLOW — CONTROLLED IMAGE DELIVERY DEFECT CORRECTION  
**Agent:** CE-Engineer  
**Date:** 2026-08-30  
**Outcome:** **A** — KSB CONTROLLED IMAGE DELIVERY DEFECT CORRECTED; **HUMAN-CONCURRED** (CWC-CE-119)  

---

## Human-facing summary

```text
CWC-CE-118
KSB THREE-STEP PHONE WORKFLOW — CONTROLLED IMAGE DELIVERY DEFECT
CORRECTION

OUTCOME: A
AGENT: CE-Engineer

STARTING CANONICAL SHA: fa4da4b55cf2041f3dd1fb7ca2a0a8e1cd6487b4
HEAD == origin/main: YES (at start)

DEFECT: FINAL "NEXT" RETURNED GENERIC IMAGE SEARCH INSTEAD OF CONTROLLED KSB IMAGE
DEFECT BOUNDARY: orchestration/presentation — final Next preferred new-render intent and did not bind exact package PNG; ChatGPT fell back to web image search
ROOT CAUSE: ksb_package_state._image_path always set create_render_request=True when no prior request; FORBIDDEN substitutes omitted image_search; operator/ORCH lacked hard search firewall for existing package PNG
CORRECTION: prefer verify+deliver images/{status_date}-BlueprintLiberty-Weekly-Status.png; forbid image_search/web/stock/Capitol substitutes; fail visibly if missing/SHA/dims fail

NEW FEATURES: NO
ARCHITECTURE EXPANSION: NO
RENDERER CHANGED: NO
NEW IMAGE: NO
IMAGE SEARCH FALLBACK: PROHIBITED
IMAGE GENERATION FALLBACK: PROHIBITED
NEW RENDER: NO
NEW REQUEST: NO
NEW ISSUE: NO
HOSTED RUN: NO

CONTROLLED IMAGE PATH:
Engineering-Office/publication/weekly-status/images/
2026-08-30-BlueprintLiberty-Weekly-Status.png
CONTROLLED IMAGE SHA:
5FEECAA3267D07A996968DC4116A0C8AFB8E7181D187302B06401886960D80CC — PASS
IMAGE DIMENSIONS: 1536 × 912 — PASS

THREE-STEP CONTRACT: PRESERVED
KSB MATURITY: 19 / 19 / 4 — UNCHANGED
FROZEN PACKAGE: dedce82d5b9bcaa97e9775aae449680bc9b0edb8 — UNCHANGED
HG-6: PASSED — UNCHANGED
PUBLICATION: NOT YET PERFORMED

TESTS: PASS
HUMAN ACCEPTANCE TEST: READY (ChatGPT display after canonicalize — Cursor cannot observe ChatGPT UI)

REPOSITORY CHANGE: YES
VALIDATION: Engineering-Office/publication/weekly-status/CWC-CE-118-VALIDATION.md
GIT HANDOFF: Engineering-Office/publication/weekly-status/issue-bridge/GIT-HANDOFF-CWC-CE-118.md
HUMAN-CONCURRED: YES ("I concur." / CWC-CE-119)
CHATGPT HUMAN ACCEPTANCE TEST: REQUIRED (after CWC-CE-119 push)
UNRELATED HUMAN WORK: PRESERVED

NEXT AGENT: Human Engineer / ChatGPT
NEXT ACTION: After CWC-CE-119 push — run three-step Human acceptance test in ChatGPT (Prepare → STATUS; Next → PRESS RELEASE; Next → EXACT CONTROLLED KSB IMAGE). No substitute if blocked.

STOP.
```

---

## A–BF validation matrix

| ID | Item | Result |
|---|---|---|
| A | Outcome | **A** |
| B | Agent | CE-Engineer |
| C | Repository | jhodges07/Constitutional-Engineering (`X:\GitHub\Constitutional-Engineering`) |
| D | Branch | `main` |
| E | Starting HEAD | `fa4da4b55cf2041f3dd1fb7ca2a0a8e1cd6487b4` |
| F | Starting origin/main | `fa4da4b55cf2041f3dd1fb7ca2a0a8e1cd6487b4` |
| G | HEAD == origin/main | YES |
| H | Working-tree before | Dirty (unrelated Human paths present) |
| I | Unrelated Human work before | Present — preserved |
| J | Existing three-step contract | Prepare→STATUS; Next→PRESS RELEASE; Next→CONTROLLED IMAGE |
| K | Observed defect | Final Next → generic Kansas Capitol / image-search results |
| L | Defect boundary | Orchestration/presentation delivery of exact package PNG |
| M | Root cause | No prefer-existing-package-image path; image_search not forbidden; ChatGPT unbound to artifact |
| N | Minimum correction | Prefer verified package PNG; forbid search/gen substitutes; controlled failure |
| O | New features added | NO |
| P | Architecture expansion | NO |
| Q | Renderer changed | NO |
| R | New image created | NO |
| S | Image search allowed | NO (PROHIBITED) |
| T | Image generation allowed | NO (PROHIBITED) |
| U | New local render | NO |
| V | New hosted render | NO |
| W | New request | NO |
| X | New Issue | NO |
| Y | New hosted run | NO |
| Z | Controlled image path | `…/images/2026-08-30-BlueprintLiberty-Weekly-Status.png` |
| AA | Expected image SHA | `5FEECAA3…860D80CC` |
| AB | Observed image SHA | `5FEECAA3…860D80CC` — PASS |
| AC | Expected dimensions | 1536 × 912 |
| AD | Observed dimensions | 1536 × 912 — PASS |
| AE | Exact artifact resolution | PASS (orchestrator + CE-118 tests) |
| AF | Missing-artifact behavior | `DELIVERY BLOCKED` / identity fail — no substitute |
| AG | STATUS behavior | PRESERVED |
| AH | PRESS RELEASE behavior | PRESERVED (541-word package text untouched) |
| AI | Three-step contract after | PRESERVED |
| AJ | Bill A maturity | 19% |
| AK | Bill B maturity | 19% |
| AL | Bill C maturity | 4% |
| AM | Maturity changed | NO |
| AN | Frozen package SHA | `dedce82d5b9bcaa97e9775aae449680bc9b0edb8` |
| AO | Frozen package modified | NO |
| AP | HG-6 | PASSED (bound to `dedce82…`) — UNCHANGED |
| AQ | Publication destination | HUMAN DECISION REQUIRED |
| AR | Publication state | NOT YET PERFORMED |
| AS | Bills/LOUs changed | NO |
| AT | Tests | PASS (`test_three_step.py`, `test_ce118_controlled_image_delivery.py`) |
| AU | Human acceptance test | READY (post-canonicalize ChatGPT: Prepare → Next → Next → exact PNG) |
| AV | Repository change required | YES |
| AW | Validation path | `…/CWC-CE-118-VALIDATION.md` |
| AX | Git handoff path | `…/issue-bridge/GIT-HANDOFF-CWC-CE-118.md` |
| AY | Changed/new authorized paths | See handoff |
| AZ | Commit | NONE |
| BA | Push | NONE |
| BB | Working-tree after | CE-118 paths dirty + unrelated Human work preserved |
| BC | Unrelated Human work after | PRESERVED |
| BD | Next agent | CE-GitManager |
| BE | Next action | Canonicalize only CE-118 correction + evidence |
| BF | STOP confirmation | STOP |

---

## Cursor vs ChatGPT boundary

Cursor verified orchestration resolves and verifies the exact controlled artifact (path/SHA/dims) and rejects image-search substitutes. Cursor did **not** observe the ChatGPT conversation UI. After CE-GitManager canonicalize, Human verifies:

1. Prepare KSB Status → STATUS  
2. Next → press release (~500 words; package text)  
3. Next → **exact** controlled KSB PNG (not Capitol web search)

---

## STOP

CE-Engineer SHALL NOT commit or push under this CWC.
