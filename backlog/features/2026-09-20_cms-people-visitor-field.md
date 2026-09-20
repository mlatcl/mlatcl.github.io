---
id: "2026-09-20_cms-people-visitor-field"
title: "Add visitor boolean to Decap CMS people collection"
status: "Completed"
priority: "Medium"
created: "2026-09-20"
last_updated: "2026-09-20"
category: "features"
related_cips: ["0001"]
owner: ""
dependencies: []
tags:
- backlog
- cms
- people
- visitor
---

# Task: Add visitor boolean to Decap CMS people collection

## Description

Person pages use a `visitor` frontmatter flag (for example Andrei Paleyes and
Diana Robinson as Visiting Researcher). The Decap CMS people collection in
`admin/config.yml` exposes `student` and `alumni` booleans but not `visitor`.
Editors saving a person through the CMS can drop or fail to set visitor status.

## Acceptance Criteria

- [x] `admin/config.yml` people collection includes a `visitor` boolean field
- [x] Field hint explains when to use it (visiting researchers / students)
- [x] Editing an existing visitor via CMS preserves `visitor: true` on save
- [x] Diana Robinson and Andrei Paleyes remain correctly flagged after a CMS
      round-trip smoke test

## Implementation Notes

Place the field near `student` and `alumni` in the people collection. Match
existing boolean widget style. No theme change required unless listing logic
should treat visitors specially beyond position title.

## Related

- CIP: 0001
- Files: `admin/config.yml`, `_people/diana-robinson.md`, `_people/andrei-paleyes.md`

## Progress Updates

### 2026-09-20

Task created after updating Diana Robinson to Visiting Researcher and noticing
the CMS schema gap.

### 2026-09-20

Implemented and verified in repo (Decap shell, schema, docs).
