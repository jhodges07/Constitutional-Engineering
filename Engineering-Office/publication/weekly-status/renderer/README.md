# KSB Status Deterministic Renderer

**Document ID:** README-PUB-WEEKLY-RENDERER-001  
**Classification:** Implementation / Engineering Note (Not Operative CONTROL)  
**Governing Work Card:** CWC-CE-084; CWC-CE-094; CWC-CE-096 (REJECTED); **CWC-CE-097 / CWC-CE-098**  
**Operative Packaging CONTROL:** STD-011 Version 1.9.0 Part B  
**Renderer version:** 2.0.0-CWC-CE-097-CANDIDATE (**HUMAN VISUALLY ACCEPTED — CWC-CE-098**)  

---

## Purpose

Deterministically construct Kansas BlueprintLiberty Status (KSB Status) public
images from an **immutable clean master template** each render by copying the
master, drawing the controlled center-panel content, and writing a new PNG.

```text
CLEAN MASTER (1536 × 1024, blank center panel)
        ↓
IN-MEMORY COPY (master never overwritten)
        ↓
DYNAMIC CENTER PANEL (bills / bars / percents)
        ↓
NEW PNG
```
        ↓
CURRENT CONTROLLED VARIABLES ONLY
        ↓
DETERMINISTIC RENDERER
        ↓
NEW PNG
        ↓
ANTI-DRIFT vs FIXED LAYER
```

**PROHIBITED as ordinary canvas:** previous weekly output PNG; populated
`BL-WEEKLY-STATUS-BASELINE-v1.0`; plate-over / erase / cover / inpaint of
historical weekly ink.

Generative image models are **not** authorized for weekly production.

---

## Baseline vs fixed layer

| Field | Value |
|---|---|
| Baseline ID | `BL-WEEKLY-STATUS-BASELINE-v1.0` |
| Baseline role | Historical Human-accepted visual reference (NOT ordinary canvas) |
| Path | `../baseline/BL-WEEKLY-STATUS-BASELINE-v1.0.png` |
| SHA-256 | `17F574D4AE505F028054FD4DD97874AA199859D08C2842D380317EDDCC4035B9` |
| Dimensions | 1536 × 912 |
| Fixed layer ID | `FIXED-LAYER-v1.0-CWC-CE-096` |
| Fixed layer path | `assets/FIXED-LAYER-v1.0-CWC-CE-096.png` |
| Fixed layer SHA-256 | `A445685853095203F4D30941AED33320EF1629E643BA0DA6D8FCF95860787E05` |

The renderer **SHALL NOT** modify the accepted baseline file.  
Every render creates a **new blank canvas**, pastes the controlled fixed layer, and draws only current variables (never opens last week’s PNG or the populated baseline as canvas).

---

## Four-variable contract

JSON / mapping input (implementation contract):

```json
{
  "status_date": "YYYY-MM-DD",
  "bill_a_percent": 0,
  "bill_b_percent": 0,
  "bill_c_percent": 0
}
```

| Key | Meaning |
|---|---|
| `status_date` | Calendar date of the KSB Status (not ISO week-year) |
| `bill_a_percent` | Human-approved integer 0–100 |
| `bill_b_percent` | Human-approved integer 0–100 |
| `bill_c_percent` | Human-approved integer 0–100 |

No fifth ordinary weekly variable is permitted.

### STATUS_DATE

Compact public form: `yyyy.mm.ww`

- `yyyy` / `mm` = calendar year/month of `status_date`
- `ww` = ISO-8601 week-of-year (`01`–`53`) via `date.isocalendar()`
- Display on image: `Date: {yyyy.mm.ww}` (prefix is FIXED copy re-stamped with the compact value)
- No `(Week NN of YYYY)`, legends, or ISO explanations

### Percentages

Human-supplied / Human-approved only.  
Renderer validates → formats `{n}%` → renders text + progress-bar fill.  
Missing / non-integer / out-of-range → **fail closed** (no successful image).

`ENGINEERED` labels beneath percentages are **FIXED** (outside variable text regions).

---

## Variable regions

Authoritative geometry: `regions.json`

Authorized change areas (with 2px antialias pad in the validator):

- `STATUS_DATE.region`
- `BILL_*_PERCENT.text_region`
- `BILL_*_PERCENT.bar`

---

## Rendering mechanism

1. Verify baseline SHA-256.  
2. Copy baseline pixels.  
3. Clear each text region by deterministic OpenCV Telea inpaint (runtime; **no stored clean plates**).  
4. Restore each bar track to measured track color; redraw fill width = `percent/100 * track_width`.  
5. Draw date and percentage text with **Arial Bold** (`arialbd.ttf`) at measured sizes/colors.  
6. Save PNG with fixed compress parameters for byte determinism.  
7. Re-verify baseline SHA-256 unchanged.

Typography note: baseline font is unidentified bold sans-serif; Arial Bold is the documented deterministic substitute (size-matched). Not treated as material redesign.

---

## Anti-drift

`ksb_renderer.antidrift.validate_anti_drift(baseline, rendered, authorized_rects)`

PASS only if:

- dimensions = 1536 × 912  
- unauthorized changed pixels = 0  

---

## Tests (NON-PRODUCTION)

```text
python Engineering-Office/publication/weekly-status/renderer/tests/run_tests.py
```

Outputs land in `tests/_non_production_output/` (non-production only).

---

## Output naming

Controlled weekly production filename contract (unchanged):

```text
YYYY-MM-DD-BlueprintLiberty-Weekly-Status.png
```

This CWC does not generate production packages.

---

## Failure behavior

| Condition | Behavior |
|---|---|
| Invalid / missing input | `InputValidationError`; no success image |
| Baseline SHA mismatch | hard stop |
| Anti-drift unauthorized pixels | FAIL |
| Fixed-pixel mutation (test) | validator rejects |

---

## Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0-CWC-CE-084 | 2026-08-30 | Initial deterministic renderer + anti-drift + NON-PRODUCTION tests. |
| 1.1.0-CWC-CE-094 | 2026-08-30 | ECR-012: solid variable plate fill replaces ordinary Telea inpaint; fresh composition; baseline file unchanged. |
| 2.0.0-CWC-CE-096-CANDIDATE | 2026-08-30 | ECR-013: blank canvas + fixed layer; populated baseline not canvas; Human visual acceptance required before activation. |
