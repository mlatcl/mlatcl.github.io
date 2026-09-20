---
month: 09
layout: project-to-supervise
status: Available
categories:
  - prtiii
  - mphil
prerequisites: >-
  [L172 Information, Energy and Intelligence (IEI)](https://www.cl.cam.ac.uk/teaching/2627/L172/), or equivalent preparation in information theory, maximum entropy, and information geometry.
supervisors:
  - neil-d-lawrence
  - christian-cabrera
projects:
  - interfaces
  - data-oriented-architectures-for-ai-based-systems
student_learn: >-
  You will learn directed information and transfer entropy (TE), modern neural /
  generative TE estimators, causal message-intervention audits for multi-agent
  LLM systems, and data-oriented instrumentation with DOAgent. You will build
  validated metrics for channel utilisation, saturation, and judgement-junction
  load — not heatmaps that fail under intervention.
published: 2026-09-20
title: Causal Information-Flow Instrumentation for Multi-Agent LLM Systems
overview: >-
  Multi-agent LLM systems are fully instrumentable: every message, tool call, and
  memory write can be logged. Transfer entropy and directed information are the
  natural language for directed flow, with recent estimators (TREET; AGM-TE) and
  early applications to LLM-MAS cascade monitoring. Separately, causal audits of
  latent channels show that end-task performance does not identify whether
  receivers actually use transmitted content (message permute / drop /
  other-example interventions).

  An information topography needs topographic quantities — conductance proxies, saturation,
  judgement-junction load — that survive causal checks. This project builds that
  instrumentation layer on DOAgent-quality traces and refuses to treat a TE
  heatmap as a result.
project_objective: >-
  (1) Instrument a multi-agent system (DOAgent preferred; AutoGen/MetaGPT
  acceptable) with full logs across communication, memory, tool, and execution
  channels. (2) Implement at least two TE/DI estimators; calibrate on synthetic
  graphs with known flow. (3) Run causal message interventions (permute, drop,
  replace with other-example messages); require claimed flows to survive these
  checks. (4) Define and validate saturation and judgement-junction load metrics;
  package a small reusable library with documentation and evaluation. Deliverables:
  library, calibration + intervention study, thesis chapter.
project_bigger_picture: >-
  This is a core target for instrumenting an information topography.  We need deployable tooling so that
  topographic interventions can be evaluated in engineered systems and later in
  partner organisations. The project extends the S4 / DOAgent agenda from
  interpretability of decisions to quantitative information topography, and
  complements existing DOAgent projects on ICU decision support and multi-agent
  interpretability.
year: 2026
---
