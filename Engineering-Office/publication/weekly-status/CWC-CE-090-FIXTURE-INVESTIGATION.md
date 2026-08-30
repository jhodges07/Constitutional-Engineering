# CWC-CE-090 — Hosted Fixture Investigation

**Document ID:** CWC-CE-090-FIXTURE-INVESTIGATION  
**Preparing Agent:** CE-Engineer  
**Date:** 2026-08-30  
**Authority:** ECR-010 0.1.1-AMENDED / CWC-CE-090  

```text
HISTORICAL FIXTURE REPLACEMENT: NOT AUTHORIZED
BASELINE UNCHANGED
CLASSIFICATION: C — INVALID COMPARISON (DIFFERENT INPUT SEMANTICS)
```

---

## 1. SHA inventory

| Artifact | Full SHA-256 |
|---|---|
| Hosted Test #2 PNG (run `33334671439` / RESULT.json + re-hash) | `10BE46068452820CB557604377D88D7C5B2F952C71BABBF2892E5C9FE2F5D83F` |
| Prior local 2026-08-30 controlled PNG (recorded) | `10BE46068452820CB557604377D88D7C5B2F952C71BABBF2892E5C9FE2F5D83F` |
| Historical renderer certification fixture | `758AFA76D1CA087CECD7C62A982FAEF36A7009C673A5B1ED894343893CB26B3A` |
| Baseline `BL-WEEKLY-STATUS-BASELINE-v1.0` | `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9` |

**BYTE IDENTITY (hosted Test #2 ↔ prior local 2026-08-30):** **PASS** (full SHA identical).

---

## 2. What `758AFA76…` represents

Source: CWC-CE-084 renderer NON-PRODUCTION suite (`renderer/tests/run_tests.py` fixture **A**).

| Field | Value |
|---|---|
| Semantics | **Fixed known-input renderer certification / determinism fixture** (NOT a weekly-output fixture for certified maturity 19/19/4) |
| Input file | `renderer/tests/fixtures/A_placeholder_equivalent.json` |
| `status_date` | `2026-08-30` |
| `bill_a_percent` | **25** |
| `bill_b_percent` | **35** |
| `bill_c_percent` | **10** |
| Baseline | `BL-WEEKLY-STATUS-BASELINE-v1.0` |
| Renderer | `ksb_renderer@1.0.0-CWC-CE-084` |
| Role in tests | Double-render SHA identity + anti-drift for placeholder-equivalent values |
| Invariant across different payloads? | **NO** — different VARIABLE inputs produce different PNG hashes by design |

---

## 3. What Test #2 used

| Field | Value |
|---|---|
| `status_date` | `2026-08-30` |
| `bill_a_percent` | **19** |
| `bill_b_percent` | **19** |
| `bill_c_percent` | **4** |
| Baseline / renderer | same controlled identities |

**Same date, different Bill percentages ⇒ comparing Test #2 output to `758AFA76…` is semantically invalid.**

Determinism requirement that applies:

```text
SAME INPUT → SAME OUTPUT
```

Not:

```text
DIFFERENT INPUT → SAME OUTPUT
```

---

## 4. Hosted vs local (same input)

Test #2 hosted output and the prior local 2026-08-30 PNG (19/19/4) are **byte-identical**.

```text
HOSTED-LOCAL SAME-INPUT DETERMINISM: PASS
```

---

## 5. Hosted internal determinism

`issue-bridge/scripts/run_render.py` performs a **single** render + anti-drift check. It does **not** double-render and compare hashes inside the hosted job.

```text
HOSTED INTERNAL DETERMINISM: NOT EXECUTED
(local suite still proves same-input double-render for fixture A)
```

RESULT.json `renderer_test_result=PASS` means render + anti-drift succeeded, not historical-fixture equality.

---

## 6. Classification

**C. INVALID COMPARISON — FIXTURE REPRESENTS DIFFERENT INPUT/SEMANTICS**

| Question | Answer |
|---|---|
| Fixture control defect? | **NO** — misuse was interpretive (post-hoc CWC-CE-089 comparison), not a workflow hard-fail against `758AFA76…` |
| Fixture control change required? | **NO** under this CWC |
| Fixture control change made? | **NO** |
| New / replaced fixture? | **NO** |

Workflow does not currently gate on `758AFA76…`. No control correction required to “force” Test #2 to match that hash.
