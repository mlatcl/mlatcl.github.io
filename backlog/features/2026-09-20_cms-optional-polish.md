---
id: "2026-09-20_cms-optional-polish"
title: "Optional Decap polish: editorial workflow and previews"
status: "Proposed"
priority: "Low"
created: "2026-09-20"
last_updated: "2026-09-20"
category: "features"
related_cips: ["0001"]
owner: ""
dependencies: ["2026-09-20_decap-cms-package-refresh", "2026-09-20_cms-schema-infotop-fields"]
tags:
- backlog
- cms
- polish
---

# Task: Optional Decap polish: editorial workflow and previews

## Description

CIP-0001 Phase 4 (deferred): editorial workflow if branch protection blocks
direct CMS commits to `main`; optional custom previews for
`project-to-supervise` and `project-single`; media-folder guidance.

## Acceptance Criteria

- [ ] Decision recorded on `publish_mode: editorial_workflow` vs direct-to-main
- [ ] If enabled, CMS create/update opens a reviewable PR or editorial entry
- [ ] Optional: basic preview config for available projects and group projects
- [ ] Document any branch-protection implications for editors

## Implementation Notes

Do not start until Phases 1–3 are Closed unless branch protection forces it
earlier.

## Related

- CIP: 0001

## Progress Updates

### 2026-09-20

Task created as deferred polish from CIP-0001 Phase 4.
