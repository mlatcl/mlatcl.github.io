---
id: "2026-09-20_cms-schema-infotop-fields"
title: "Align CMS available-project schema with InfoTop frontmatter"
status: "Ready"
priority: "High"
created: "2026-09-20"
last_updated: "2026-09-20"
category: "features"
related_cips: ["0001"]
owner: ""
dependencies: ["2026-09-20_decap-cms-package-refresh"]
tags:
- backlog
- cms
- availableprojects
- infotop
---

# Task: Align CMS available-project schema with InfoTop frontmatter

## Description

CIP-0001 Phase 2: update the `availableprojects` collection so CMS edits do not
drop InfoTop-era fields, especially `prerequisites`, and so category values
match Liquid filters in `available-projects.html`.

## Acceptance Criteria

- [ ] `prerequisites` field added to `availableprojects` in `admin/config.yml`
- [ ] Category options aligned with content/templates (`prtii`, `prtiii`,
      `mphil` / `MPhil`, `PhD`) without breaking listings
- [ ] Related `projects` relation resolves `information-topography`,
      `ai-adoption`, and `interfaces`
- [ ] Spot-check: open an Available InfoTop brief in CMS and save without
      losing undeclared fields (or add any other fields that would otherwise
      be dropped)
- [ ] People/projects smoke-edits for InfoTop group pages round-trip cleanly

## Implementation Notes

Also consider adding the people `visitor` field in the same PR if
`2026-09-20_cms-people-visitor-field` is still open — related schema hygiene.

## Related

- CIP: 0001
- Task: 2026-09-20_cms-people-visitor-field

## Progress Updates

### 2026-09-20

Task created from CIP-0001 Phase 2.
