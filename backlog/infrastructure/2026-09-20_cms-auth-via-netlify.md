---
id: "2026-09-20_cms-auth-via-netlify"
title: "Confirm Decap GitHub login via Netlify admin URL"
status: "Completed"
priority: "High"
created: "2026-09-20"
last_updated: "2026-09-20"
category: "infrastructure"
related_cips: ["0001"]
owner: ""
dependencies: []
tags:
- backlog
- cms
- auth
- netlify
---

# Task: Confirm Decap GitHub login via Netlify admin URL

## Description

Phase 0 of CIP-0001: diagnose why Login with GitHub failed from GitHub Pages
`/admin/` and confirm the working editorial path.

## Acceptance Criteria

- [x] Root cause documented: Netlify OAuth proxy uses hostname as `site_id`
- [x] Login works via https://mlatcl.netlify.app/admin/
- [x] Decision recorded: keep Netlify as editorial auth host (Option A)

## Implementation Notes

GitHub Pages `mlatcl.github.io/admin/` will keep failing login unless an
external OAuth `base_url` is added later. Do not treat GitHub Pages `/admin/`
as the editor entry point.

## Related

- CIP: 0001

## Progress Updates

### 2026-09-20

Confirmed working via Netlify. Marked Completed.
