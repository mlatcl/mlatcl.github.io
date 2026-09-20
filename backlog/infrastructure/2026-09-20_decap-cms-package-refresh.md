---
id: "2026-09-20_decap-cms-package-refresh"
title: "Refresh admin shell from Netlify CMS v2 to Decap CMS"
status: "Ready"
priority: "High"
created: "2026-09-20"
last_updated: "2026-09-20"
category: "infrastructure"
related_cips: ["0001"]
owner: ""
dependencies: ["2026-09-20_cms-auth-via-netlify"]
tags:
- backlog
- cms
- decap
---

# Task: Refresh admin shell from Netlify CMS v2 to Decap CMS

## Description

CIP-0001 Phase 1: replace the deprecated `netlify-cms@^2` CDN script and Netlify
Identity widget in `admin/index.html` with Decap CMS 3, and update
`admin/README.md` to match the working Netlify login path.

## Acceptance Criteria

- [ ] `admin/index.html` loads Decap CMS 3 (pinned known-good version)
- [ ] Netlify Identity widget removed unless still required for the chosen auth
- [ ] `local_backend` smoke test works for maintainers
- [ ] `admin/README.md` describes Decap CMS and https://mlatcl.netlify.app/admin/

## Implementation Notes

Keep `backend.name: github` with `repo: mlatcl/mlatcl.github.io`. Editors must
continue to open admin on the Netlify host for OAuth.

## Related

- CIP: 0001

## Progress Updates

### 2026-09-20

Task created from CIP-0001 Phase 1. Auth path already confirmed.
