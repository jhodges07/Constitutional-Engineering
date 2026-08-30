# Fence-safe hosted KSB render Issue procedure (CWC-CE-102)

**Defect:** KSB-RENDER-004  
**Scope:** Issue body construction only. Does not change baseline_id, clean master, renderer, or maturity.

---

## Forbidden

- Embedding triple-backtick fences in PowerShell `python -c "…"` or double-quoted PowerShell strings.
- `gh issue create --body "…```ksb-render-request…"` with shell-interpolated fences.
- Ad hoc backtick escape sequences as the primary construction method.
- Reusing Issue #7 / run 33339896335.
- Putting clean-master identity in `baseline_id`.

---

## Required envelope fields (CWC-CE-100)

```json
{
  "request_schema_version": "1.0.0",
  "publication_request_type": "KSB_WEEKLY_STATUS",
  "request_id": "<NEW UNIQUE PRODUCTION REQUEST ID>",
  "canonical_sha": "<CURRENT AUTHORIZED CANONICAL SHA>",
  "baseline_id": "BL-WEEKLY-STATUS-BASELINE-v1.0",
  "renderer_id": "ksb_renderer@2.0.0-CWC-CE-097-CANDIDATE",
  "render_payload": {
    "status_date": "2026-08-30",
    "bill_a_percent": 19,
    "bill_b_percent": 19,
    "bill_c_percent": 4
  }
}
```

---

## Machine-usable steps (future hosted CWC only)

Paths relative to repository root `Constitutional-Engineering`.

### 1. Write request JSON (UTF-8)

Write the envelope to a temp/work file, e.g. `request.json`, using Python/`Set-Content -Encoding utf8` **without** any markdown fence characters in the shell command that builds JSON.

### 2. Build fenced Issue body (Python only)

```text
python Engineering-Office/publication/weekly-status/issue-bridge/scripts/write_ksb_issue_body.py ^
  --request request.json ^
  --out issue-body.md ^
  --allowed-sha <CANONICAL_SHA>
```

Required script output includes:

- `PRE_SUBMISSION: PASS`
- `OPENING_FENCE_REPR='```ksb-render-request'`
- `OPENING_BACKTICK_COUNT=3`

### 3. Mandatory pre-submission validation

The script (with `--allowed-sha`) already runs canonical `extract_request_json` + `validate_envelope`.

Additional manual check (recommended):

```text
python -c "import sys; from pathlib import Path; sys.path.insert(0, r'Engineering-Office/publication/weekly-status/issue-bridge'); from ksb_issue_bridge.issue_body import pre_submit_validate; print(pre_submit_validate(Path('issue-body.md').read_text(encoding='utf-8'), allowed_shas=['<CANONICAL_SHA>'])['request_id'])"
```

Note: Prefer invoking a small `.py` file or the writer script rather than putting backticks in PowerShell-interpolated strings.

Required:

```text
PRE-SUBMISSION FENCE = PASS
PRE-SUBMISSION JSON = PASS
PRE-SUBMISSION CONTRACT = PASS
```

If any fail: STOP. Do not create an Issue.

### 4. Safe GitHub CLI invocation (body-file only)

Exact argv pattern (do not interpolate body contents):

```text
gh issue create -R jhodges07/Constitutional-Engineering --title "[KSB-RENDER] <DATE> <REQUEST_ID>" --body-file issue-body.md
```

### 5. Post-creation readback (mandatory)

```text
gh issue view <N> -R jhodges07/Constitutional-Engineering --json number,body,title -q .
```

Verify:

1. Body contains exact opening line ```ksb-render-request (three backticks).  
2. Body contains exact closing ```.  
3. `request_id` matches the intended NEW production ID.  
4. Canonical `extract_request_json` / `pre_submit_validate` ACCEPT on the read-back body.

If body differs from intended fences: STOP. Do not create another Issue under the same one-attempt authorization.

### 6. Only then rely on workflow

Workflow execution is meaningful only after steps 3–5 pass.

---

## Body file lifecycle

- Temporary; not source of truth.  
- No secrets.  
- UTF-8.  
- May live under `issue-bridge/tests/_non_production_output/` for local proof only.  
- Production CWC should use a controlled work path and discard after readback.
