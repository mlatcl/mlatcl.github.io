---
month: 09
layout: project-to-supervise
status: Available
categories:
  - prtiii
  - mphil
prerequisites: >-
  [L172 Information, Energy and Intelligence (IEI)](https://mlatcl.github.io/iei/), or equivalent preparation in information theory, maximum entropy, and information geometry.
supervisors:
  - neil-d-lawrence
  - christian-cabrera
projects:
  - information-topography
  - interfaces
student_learn: >-
  You will learn the Good Regulator Theorem and its modern strengthenings
  (information-bottlenecked "Gooder" regulators; embodied / observer-attributed
  variants), entropy estimators for policies and outcomes, and experimental design
  for agent evaluation under distribution shift. You will connect cybernetic
  viability conditions to measurable properties of LLM-based agents.
published: 2026-09-20
title: Testing Good Regulator Notions in Agentic Loops
overview: >-
  Conant and Ashby's Good Regulator Theorem is often quoted as "every good
  regulator must be a model of the system," but the bare result mainly yields
  determinism $H(A\mid S)=0$ among minimal entropy-minimising policies, this is a weak
  sense of "model." Recent work strengthens or reframes the claim: Wentworth's
  Gooder Regulator (information bottleneck forcing an internal posterior), Virgo
  et al. (2025) on observer-attributed belief updating for embodied agents, and
  algorithmic / internal-model principles from control theory. Parallel work on
  action-sufficient representations argues that a regulator need only preserve
  distinctions that matter for action consequences.

  Agentic AI systems have generated excitement, alongside them the term "world models," is used usually without saying
  what definition is meant. This project builds a controllable agentic loop and
  tests which operational definition of "has a model" predicts out-of-distribution
  failure — and when a checkpoint looks like judgement but is only a frozen
  attenuator (agentic debt).
project_objective: >-
  (1) Formalise three operational definitions of "has a model": bare Conant–Ashby
  determinism; information-bottlenecked internal summary (Gooder); observer-attributed
  belief updating (Virgo et al.). (2) Build a controllable environment (e.g. grid
  world, structured negotiation, or tool-use sandbox) where regulation quality
  $H(Z)$ and each model notion can be estimated. (3) Train or prompt agents under
  capacity limits; evaluate which definition predicts OOD failure under distribution
  shift and "frozen attenuator" conditions. (4) Map failures onto the judgement
  layer: when does a human- or model-facing checkpoint absorb uncertainty without
  retaining escalatable distinctions? Deliverables: environment + estimators,
  comparative evaluation, and thesis chapter.
project_bigger_picture: >-
  The judgement layer is a junction where authority is exercised
  over information flow. Agentic debt is the accrued cost when that layer is
  automated without preserved escalation. This project gives those concepts
  experimental teeth in engineered systems while remaining grounded in IEI
  material on the entropic Good Regulator.
year: 2026
---
