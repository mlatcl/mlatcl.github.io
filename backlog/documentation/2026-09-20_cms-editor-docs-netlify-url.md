---
id: "2026-09-20_cms-editor-docs-netlify-url"
title: "Update site docs to Decap CMS and Netlify admin URL"
status: "Completed"
priority: "Medium"
created: "2026-09-20"
last_updated: "2026-09-20"
category: "documentation"
related_cips: ["0001"]
owner: ""
dependencies: ["2026-09-20_cms-auth-via-netlify"]
tags:
- backlog
- cms
- documentation
---

# Task: Update site docs to Decap CMS and Netlify admin URL

## Description

CIP-0001 Phase 3 docs slice: root README, `_minijobs/maintain_website.md`, and
`admin/README.md` should say Decap CMS and tell editors to use
https://mlatcl.netlify.app/admin/ (not GitHub Pages `/admin/`).

## Acceptance Criteria

- [x] Root `README.md` names Decap CMS and the Netlify admin URL
- [x] `_minijobs/maintain_website.md` updated likewise
- [x] Explicit note that GitHub Pages `/admin/` cannot complete GitHub login
- [x] Short guidance on proposing an Available student project via CMS
      (status, categories, supervisors, prerequisites, related projects)

## Implementation Notes

Can land after or with the package refresh; does not require schema work to
ship the URL clarification.

## Related

- CIP: 0001

## Progress Updates

### 2026-09-20

Task created from CIP-0001 Phase 3 documentation items.

### 2026-09-20

Implemented and verified in repo (Decap shell, schema, docs).
