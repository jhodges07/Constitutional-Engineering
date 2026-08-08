# WF-002 — Engineering Release Workflow

**Document ID:** WF-002  
**Title:** Engineering Release Workflow  
**Classification:** Engineering Workflow  
**Authority:** Constitutional Engineering Office  
**Governing Architecture:** ARCH-001 — Constitutional Engineering Architecture  
**Governing Policy:** POL-001 — Engineering Office Governance Policy  
**Governing Operating Workflow:** WF-001 — Engineering Office Operating Workflow  
**Related Standards:** STD-001, STD-002 (when Active), STD-014, STD-015  
**Governing Index:** IDX-001 — Engineering Office Master Index  
**Governing CWC-CE:** CWC-CE-032 — Engineering Office Release Baseline 1.0  
**Status:** Draft  
**Version:** 1.0.0  
**Effective Date:** 2026-08-08  

---

## 1. Purpose

This workflow defines the complete Engineering Office release lifecycle from Human Acceptance through Git Commit, Git Tag, Git Push, and Baseline Certification.

It establishes the authoritative process for declaring Engineering Office Release Baseline Version 1.0 and all subsequent Office release baselines.

WF-002 specializes release operations that begin after authorized engineering work has reached Human Acceptance under WF-001.  
It does not replace WF-001.

---

## 2. Scope

### 2.1 In Scope

This workflow applies to:

1. Engineering Office Release Baseline declarations (including Version 1.0)  
2. Single-repository and multi-repository release sets under Office authority  
3. Pre-release audits, Human Acceptance gates, Git commit/tag/push sequencing, and baseline certification  
4. Hotfix releases and rollback procedures for released baselines  
5. Publication posture for released baselines  
6. Coordination among Engineering-Office, specialized managers, and control repositories when included in a release set  

### 2.2 Out of Scope

This workflow does not:

1. Authorize bypass of WF-001 work authorization or Human Engineer gates  
2. Redefine ARCH / POL / STD / IDX content  
3. Replace domain-control ownership of AGCL, NBBF, or CDT  
4. Enact law, publish legislation, or ratify constitutional amendments  
5. Require UNBKE or any specific Git hosting vendor  

### 2.3 Authority Position

```
ARCH-001
    ↓
POL-001
    ↓
WF-001 (engineering work lifecycle)
    ↓
WF-002 (release lifecycle)
    ↓
Git Commit → Git Tag → Git Push → Baseline Certification → Publication (when authorized)
```

WF-002 is subordinate to ARCH-001, POL-001, and WF-001.  
STD-014 governs controlled change authorization when release preparation itself requires controlled change.  
STD-015 governs CER reporting for release audits and release execution records.  
IDX-001 is the catalog authority for required governing documents.

---

## 3. Release Philosophy

1. **Release is a governed event, not a convenience push.**  
2. **Human authority is supreme.** AI may prepare release packages; AI may not approve or self-release.  
3. **Baseline integrity precedes speed.** Incomplete indexes, failed audits, or missing certifications block release.  
4. **Traceability is continuous.** Every release shall link authorizing CWC-CE / CER / acceptance records to commit, tag, and push evidence.  
5. **Multi-repository releases are synchronized declarations.** Partial silent pushes are not a baseline.  
6. **Tags identify baselines; commits do not by themselves certify release.**  
7. **Publication does not equal enactment** of legislative or constitutional content.  
8. **Rollback is an engineering procedure**, not an informal history rewrite, unless explicitly authorized.  
9. **Hotfixes are narrow, audited, and versioned**, not undocumented patches.  
10. **Truthfulness is mandatory.** Unperformed audits shall not be reported as passed.

### 3.1 Absolute Release Prohibition

No Engineering Office release may occur unless all of the following are true:

1. All governing documents required by IDX-001 are present.  
2. Required audits pass.  
3. Required certifications are complete.  
4. All required repositories are synchronized.  
5. Human Engineer approval has been recorded.  
6. The release receives an official baseline version.  

If any condition fails, release shall stop.

---

## 4. Release Prerequisites

Before entering the release sequence, the following prerequisites shall be satisfied:

| Prerequisite | Requirement |
|---|---|
| Git readiness | Every repository in the release set is an initialized git repository with a clear working tree posture |
| Branch posture | Release branch/ref strategy is declared and approved |
| IDX currency | IDX-001 catalogs all governing documents required for the release baseline |
| Work closure | Material CEP/CER work intended for the baseline is Human-Accepted or expressly deferred |
| Ownership clarity | Stewardship for each release-set repository is known under ARCH-003 / POL-001 |
| Interface clarity | Cross-repository release coordination uses defined interfaces under ARCH-004 |
| Clean intent | No unauthorized dirty changes remain undisclosed in the release set |
| Tooling independence | Release does not hard-depend on UNBKE |

### 4.1 Version 1.0 Prerequisite Emphasis

For Engineering Office Release Baseline 1.0, prerequisites additionally include:

1. Architecture, policy, standards, workflows, templates, and index baselines required by IDX-001 are present and coherent  
2. Pre-release audit evidence exists (for example a pre-push/pre-release CER)  
3. Manager certifications required for included managers are complete or expressly excluded from the baseline set  
4. Control repositories included in the release set are push-ready or expressly deferred with Human Engineer acknowledgment  

---

## 5. Required Engineering Artifacts

A release package shall include or reference the following artifacts:

| Artifact | Requirement |
|---|---|
| Release CWC-CE | Authorizes the release attempt and baseline version intent |
| Release scope manifest | Lists repositories, branches/refs, and included document sets |
| IDX-001 conformance statement | Confirms governing documents required by IDX-001 are present |
| Pre-release audit CER | Records audit results under Section 6 |
| Certification status register | Lists required certifications and completion state |
| Human Acceptance record | Explicit approval to proceed past the acceptance gate |
| Commit plan | Intended commit set / message strategy per repository |
| Tag plan | Official baseline version tag(s) |
| Push plan | Remotes, branches, and synchronization order |
| Baseline Certification record | Section 11 certification package |
| Rollback plan | Section 13 procedure reference for this release |
| Exceptions log | Any Human Engineer-approved exceptions with scope/duration |

AI-prepared drafts of these artifacts are permitted.  
Final approval authority remains with the Human Engineer.

---

## 6. Pre-Release Audit Requirements

### 6.1 Audit Mandate

Every Engineering Office release requires a pre-release audit.  
The audit shall be recorded in a CER (or approved equivalent audit record) under STD-015.

### 6.2 Minimum Audit Checks

| # | Check | Required Outcome |
|---|---|---|
| 1 | Duplicate document identifiers | None in release set |
| 2 | Broken references | None material, or expressly accepted residual risks |
| 3 | Empty required files | None for Active/required artifacts |
| 4 | Numbering conflicts | None unresolved |
| 5 | Missing Version History | None for controlled DocID artifacts in scope |
| 6 | Orphaned / unindexed governing docs | None relative to IDX-001 requirements |
| 7 | Untracked files that should be committed | Dispositioned (include / exclude / defer) |
| 8 | Unintended modifications | None undisclosed |
| 9 | Repository status for every release-set repository | Recorded and synchronized per plan |
| 10 | Absolute release conditions (Section 3.1) | All true |

### 6.3 Audit Outcomes

| Outcome | Meaning | Release Effect |
|---|---|---|
| Pass | No material release blockers | May proceed to Human Acceptance Gate |
| Partial | Material issues with recorded dispositions | May proceed only if Human Engineer expressly accepts conditions |
| Fail | Material blockers unresolved | Release halted |

Unperformed checks shall be recorded as `Not performed` and treated as blocking unless Human Engineer expressly waives with recorded reason.

---

## 7. Human Acceptance Gate

### 7.1 Gate Rule

No commit/tag/push release sequence may begin until Human Engineer Acceptance is recorded for the release package.

### 7.2 Required Acceptance Fields

| Field | Requirement |
|---|---|
| Acceptance Decision | Accept / Accept with Conditions / Reject / Defer |
| Baseline Version | Official version to be certified (for example `1.0.0`) |
| Release set acknowledgment | Repositories and refs included |
| Audit outcome acknowledgment | Pass / Partial with conditions |
| Certification acknowledgment | Required certifications complete or expressly excluded |
| Synchronization acknowledgment | Required repositories synchronized |
| Conditions | Required if conditional |
| Effective date | Yes |
| Human Engineer identity / record | Yes |

### 7.3 Gate Rules

1. Silence is not acceptance.  
2. AI may not grant acceptance.  
3. Reject or Defer returns the package to remediation; no release Git actions proceed.  
4. Accept with Conditions shall state whether commit/tag/push may proceed before condition closure.  
5. Acceptance of a release package does not waive POL-001 ethics or invent missing IDX-required documents.

---

## 8. Git Commit Workflow

### 8.1 Commit Preconditions

1. Human Acceptance Gate passed for commit stage  
2. Pre-release audit outcome is Pass or accepted Partial  
3. Working tree contents match the approved release scope manifest  
4. No undisclosed files are staged  

### 8.2 Commit Sequence

```
Verify clean/intended working tree
      ↓
Stage only approved paths
      ↓
Human Engineer confirms staged set
      ↓
Create commit(s) with approved message(s)
      ↓
Record commit hash(es) in release CER / baseline record
```

### 8.3 Commit Rules

1. Commits occur only under Human Engineer authorization.  
2. AI may prepare staging recommendations and commit messages; AI may not commit unless explicitly authorized for that action by the Human Engineer under applicable Git standards/policy.  
3. Destructive Git history operations remain prohibited absent explicit Human Engineer approval.  
4. Each repository in the release set receives its own commit evidence when that repository is included.  
5. Commit messages shall reference the release CWC-CE and baseline version intent when practical.  
6. Until STD-002 is Active, WF-001 Git gates and POL-001 approval rules remain binding.

---

## 9. Git Tag Workflow

### 9.1 Tag Purpose

Git tags identify official Engineering Office release baselines.  
A commit without an approved baseline tag is not a certified release baseline.

### 9.2 Tag Preconditions

1. Required commit(s) exist and are recorded  
2. Human Acceptance authorizes tagging for the declared baseline version  
3. Tag name matches Release Numbering (Section 12)  
4. Tag does not reuse an existing baseline identity for different content  

### 9.3 Tag Sequence

```
Confirm commit hash(es)
      ↓
Create annotated tag for baseline version
      ↓
Record tag name + target commit in baseline certification package
      ↓
Verify tag resolves to intended commit
```

### 9.4 Tag Rules

1. Prefer annotated tags for official baselines.  
2. Tag messages shall identify baseline version, release CWC-CE, and acceptance date when practical.  
3. Moving/deleting release tags requires explicit Human Engineer authorization and shall be treated as an exceptional/rollback-related action.  
4. Multi-repository releases may use coordinated tag names per repository under Section 15.  
5. AI may prepare tag commands; AI may not tag without explicit Human Engineer authorization for that action.

---

## 10. Git Push Workflow

### 10.1 Push Preconditions

1. Commit and tag stages complete for the authorized release set  
2. Human Acceptance authorizes push  
3. Required repositories are synchronized per the push plan  
4. Pre-release audit blockers remain closed or accepted  

### 10.2 Push Sequence

```
Confirm local commit/tag evidence
      ↓
Push branch commit(s) to approved remote(s)
      ↓
Push baseline tag(s) to approved remote(s)
      ↓
Verify remote commit/tag presence
      ↓
Record push evidence in release CER / baseline record
```

### 10.3 Push Rules

1. No Engineering Office release push may occur unless Section 3.1 conditions remain satisfied.  
2. Push of untagged release intent is incomplete for baseline certification.  
3. Force-push to protected main/master baselines is prohibited unless the Human Engineer explicitly authorizes it as an exceptional rollback/recovery action.  
4. AI may prepare push commands; AI may not push without explicit Human Engineer authorization for that action.  
5. Partial pushes across a declared multi-repo release set are not baseline-complete until synchronization is restored or the release set is formally narrowed by Human Engineer amendment.

---

## 11. Baseline Certification

### 11.1 Certification Purpose

Baseline Certification declares that a specific versioned release set is the official Engineering Office Release Baseline.

### 11.2 Required Certification Contents

| Element | Requirement |
|---|---|
| Baseline Version | Official version identifier |
| Release CWC-CE | Authorizing work card |
| Audit CER reference | Pre-release audit evidence |
| Human Acceptance reference | Gate record |
| Repository set | Included repos/refs |
| Commit hashes | Per repository |
| Tag names | Per repository / coordinated set |
| Push evidence | Remotes and verification notes |
| IDX-001 conformance statement | Required governing docs present |
| Certification status register | Required certifications complete |
| Synchronization statement | Required repositories synchronized |
| Enactment/publication disclaimer | Release ≠ legal enactment of domain law |
| Human Engineer certification approval | Explicit |

### 11.3 Certification Outcomes

| Outcome | Meaning |
|---|---|
| Certified | Baseline is official |
| Conditional Certified | Certified subject to recorded conditions |
| Not Certified | Release incomplete; do not treat as Office baseline |
| Revoked | Prior certification withdrawn under rollback/hotfix governance |

### 11.4 Version 1.0 Certification Statement Form

When certifying Engineering Office Release Baseline 1.0, the certification record shall state that Baseline `1.0.0` (or approved equivalent tag form) is certified only if Section 3.1 conditions were satisfied at certification time.

AI may prepare the certification package.  
Human Engineer approval is required to certify.

---

## 12. Release Numbering

### 12.1 Baseline Version Scheme

Engineering Office release baselines use semantic versioning:

```text
MAJOR.MINOR.PATCH
```

| Component | Meaning |
|---|---|
| MAJOR | Incompatible Office baseline / governance-break release |
| MINOR | Compatible baseline expansion |
| PATCH | Compatible correction hotfix baseline |

### 12.2 Tag Naming Convention

Recommended official tag forms:

```text
eo-baseline-vMAJOR.MINOR.PATCH
```

Example for Version 1.0:

```text
eo-baseline-v1.0.0
```

Coordinated repository tags may append a repo suffix when required for clarity:

```text
eo-baseline-v1.0.0+engineering-office
eo-baseline-v1.0.0+legislative-manager
```

### 12.3 Numbering Rules

1. Baseline numbers are never reused for different certified content sets.  
2. Hotfixes increment PATCH unless Human Engineer authorizes a higher bump.  
3. Failed/aborted release attempts do not consume a certified baseline number unless a tag was published and must be revoked under Section 13.  
4. Document-level semantic versions remain independent of baseline numbers but should be reconcilable through the release manifest.

---

## 13. Rollback Procedure

### 13.1 Rollback Purpose

Rollback restores the Engineering Office to a last-known certified baseline when a release is defective, incomplete, or erroneously certified.

### 13.2 Rollback Triggers

1. Critical defect discovered post-release  
2. Failed synchronization across declared release-set repositories  
3. Certification issued in error  
4. Human Engineer directive to revoke baseline  

### 13.3 Rollback Sequence

```
Human Engineer authorizes rollback CWC-CE / emergency record
      ↓
Identify last known good certified baseline
      ↓
Announce rollback scope (repos/tags/channels)
      ↓
Restore operational pointer to last good baseline (branch strategy as approved)
      ↓
Revoke or supersede defective baseline certification record
      ↓
Record rollback CER with commit/tag/push evidence
      ↓
Remediate defects under WF-001 before next release attempt
```

### 13.4 Rollback Rules

1. Prefer additive supersession records over silent history rewrite.  
2. Force-push / tag deletion only with explicit Human Engineer approval.  
3. Rollback does not authorize fabrication of audit evidence.  
4. Publication channels shall be updated so defective baselines are not represented as current.  
5. AI may prepare rollback packages; AI may not authorize rollback.

---

## 14. Hotfix Releases

### 14.1 Hotfix Definition

A hotfix release is a narrowly scoped PATCH baseline addressing a critical defect in a certified baseline without opening a broad feature release.

### 14.2 Hotfix Rules

1. Hotfix scope shall be minimal and explicitly listed.  
2. Hotfix still requires:
   - authorizing CWC-CE (or approved emergency authorization later normalized under STD-014/WF-001)
   - targeted pre-release audit checks for affected surfaces
   - Human Acceptance
   - commit / tag / push evidence
   - baseline certification update (PATCH increment)  
3. Hotfix may not silently include unrelated dirty tree changes.  
4. Hotfix does not waive Section 3.1 absolute conditions for the hotfix release set.  
5. Emergency containment follows STD-014 emergency-change rules when applicable, then returns to this workflow for baseline normalization.

---

## 15. Multi-Repository Release Coordination

### 15.1 Synchronization Mandate

All required repositories in a release set shall be synchronized.  
Synchronization means each included repository has the approved commit/tag/push state recorded in the same baseline certification package.

### 15.2 Coordination Sequence

```
Declare release set and lead repository
      ↓
Freeze member versions / commits per repo
      ↓
Run pre-release audit across all included repos
      ↓
Human Acceptance for the set
      ↓
Commit each repo per approved plan
      ↓
Tag each repo with coordinated baseline identity
      ↓
Push in approved order
      ↓
Verify remote synchronization matrix
      ↓
Certify baseline only when matrix is complete
```

### 15.3 Coordination Rules

1. Engineering-Office is typically the lead repository for Office baselines; managers/controls are included only when declared.  
2. Control repositories remain ownership peers; inclusion in a release set does not transfer AGCL/NBBF/CDT ownership.  
3. A repository lacking git readiness cannot be included in a push baseline until initialized or expressly deferred out of the set.  
4. Narrowing the release set after acceptance requires Human Engineer amendment of the release package.  
5. Cross-repo interfaces remain reference-based under ARCH-004; release coordination is not silent cross-writing.

---

## 16. Release Checklist

Before declaring an Engineering Office release ready for Human Engineer final authorization, verify:

| # | Check | Required |
|---|---|---|
| 1 | Release CWC-CE exists and is approved for release intent | Yes |
| 2 | Release scope manifest complete | Yes |
| 3 | All governing documents required by IDX-001 are present | Yes |
| 4 | IDX conformance statement recorded | Yes |
| 5 | Pre-release audit CER completed | Yes |
| 6 | Required audits Pass (or accepted Partial with conditions) | Yes |
| 7 | Required certifications complete (or expressly excluded) | Yes |
| 8 | All required repositories synchronized / sync plan complete | Yes |
| 9 | Human Engineer approval recorded for release gate | Yes |
| 10 | Official baseline version assigned | Yes |
| 11 | Commit plan approved | Yes |
| 12 | Tag plan approved | Yes |
| 13 | Push plan approved | Yes |
| 14 | Rollback plan referenced | Yes |
| 15 | No undisclosed dirty changes in release set | Yes |
| 16 | Absolute Section 3.1 conditions all true | Yes |
| 17 | Baseline certification package prepared | Yes |
| 18 | Publication posture declared (publish / defer) | Yes |

Any failed required check blocks release.

---

## 17. Publication Rules

1. Release baseline certification may occur with or without immediate public publication.  
2. Publication of a certified baseline requires explicit Human Engineer authorization under WF-001 publication gates.  
3. Draft, failed, partial, or uncertified release packages are not published as Office baselines.  
4. Publication channels shall identify baseline version, tag identity, and certification status.  
5. Publication of Engineering Office baselines does not enact legislation, ratify constitutional amendments, or alter AGCL/NBBF/CDT ownership.  
6. Legislative publication packages remain governed by manager-local standards (for example KLS-006) in addition to this workflow when those packages are separately published.  
7. AI may prepare publication manifests; AI may not publish unilaterally.

---

## 18. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0.0 | 2026-08-08 | Initial Engineering Release Workflow defining Human Acceptance through commit, tag, push, baseline certification, numbering, rollback, hotfix, multi-repository coordination, and Release Baseline 1.0 absolute conditions under CWC-CE-032. |
