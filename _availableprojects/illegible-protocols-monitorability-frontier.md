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
student_learn: >-
  You will learn emergent communication in multi-agent systems, monitorability and
  steganography risks for LLM agents, and how to measure protocol illegibility
  quantitatively (mutual information with natural language, human decode accuracy,
  directed information among agents). You will map efficiency–monitorability
  frontiers under bandwidth constraints and test harness interventions.
published: 2026-09-20
title: Illegible Protocols under Bandwidth — The Monitorability Frontier
overview: >-
  Classical emergent-communication work showed agents invent efficient but opaque
  codes under bandwidth limits. LLM multi-agent systems inherit the risk in a new
  form: under token budgets they can drift from English into shorter protocols
  even in fully cooperative settings (e.g. GlossoGen); vision-language referential
  games produce covert signalling; steganography literature studies adversarial
  opacity. Efficiency work (AgentPrune, Agora-style protocols) reduces redundancy
  but rarely measures loss of human monitorability — or whether illegibility is
  merely displaced into tools and memory.

  The question here is can a communication topography predict loss of
  monitorable language, and can harnesses preserve judgement without killing
  performance?
project_objective: >-
  (1) Reproduce a bandwidth-constrained multi-agent setting (referential game or
  GlossoGen-like cooperative scenario) with controllable token / rate limits.
  (2) Define and measure protocol metrics: mutual information with English (or
  human language), human decode accuracy, TE among agents, task reward.
  (3) Sweep bandwidth, optional postmortem / deliberation channels, and model
  strength; fit an efficiency–monitorability frontier. (4) Test harness
  interventions (forced natural language, external monitor, schema constraints)
  and check for channel substitution: illegibility moving into tool args or
  memory rather than disappearing. Deliverables: experimental harness, frontier
  plots, intervention study, thesis chapter.
project_bigger_picture: >-
  Bezos-style service architectures and modern agent scaffolds both assume
  legible interfaces. When AI agents do not share human communication constraints,
  illegible protocols threaten the judgement layer: humans cannot contest what they
  cannot read. This project supplies evidence on that failure mode and informs
  harness design for accountable multi-agent systems (S4 / Interfaces).
year: 2026
---
