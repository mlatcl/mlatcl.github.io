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
  You will study three geometries of changing probability: Fisher–Rao / Crooks
  thermodynamic length, Wasserstein optimal transport, and Schrödinger bridges
  (entropic OT, Sinkhorn). You will fit competing interpolations to logged belief
  trajectories and perform model comparison under interventions on information cost.
published: 2026-09-20
title: Three Geometries of Agency — Crooks, Wasserstein, and Schrödinger Bridges
overview: >-
  The IEI module treats intelligent agency as transport of probability mass and
  distinguishes three geometries that must not be collapsed: (1) Fisher–Rao / Crooks
  thermodynamic length (near-equilibrium, dissipation bounded by $\mathcal{L}^2/\tau$);
  (2) Wasserstein (minimum ground-cost mass transport); (3) Schrödinger bridge
  (maximum-entropy interpolation; discrete MaxEnt coupling via Sinkhorn). Machine
  learning has made Schrödinger bridges practical generative tools (Sinkhorn
  bridges with statistical rates; LightSB-M; SB flow for unpaired translation),
  usually without asking which geometry *explains an agent's belief updates* under
  metabolic or information cost.

  This project treats the three geometries as competing scientific explanations of
  agency, not as interchangeable samplers.
project_objective: >-
  (1) Log belief or latent states of a tractable agent (Bayesian agent, small
  controlled LLM agent, or both) across a multi-step task. (2) Fit Fisher–Rao,
  Wasserstein, and Schrödinger-bridge interpolations between successive belief
  states; score by likelihood / predictive quality and decision-relevance.
  (3) Intervene on cost (temperature, token budget, compute, noise) and test which
  geometry's predictions move correctly. (4) State a comparative, falsifiable
  thesis claim — e.g. under bandwidth stress SB fits; under near-equilibrium
  fine-tuning Fisher–Rao fits — and report where all three fail. Deliverables:
  fitting pipeline, intervention study, and thesis chapter.
project_bigger_picture: >-
  The inaccessible game attempts to give mathematical teath to the notion of information topography. We need more than metaphors for "information flow." Distinguishing geometries clarifies
  what kind of cost shapes communication structure in engineered agents and
  connects IEI's closing lectures to current generative-modelling
  practice (seel Welling et al. on generative AI and stochastic thermodynamics).
year: 2026
---
