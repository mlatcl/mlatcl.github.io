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
projects:
  - information-topography
student_learn: >-
  You will learn information geometry (Fisher metric as a Riemannian structure on
  probability manifolds), constrained maximum-entropy dynamics, and the GENERIC /
  steepest-entropy-ascent (SEA) frameworks for non-equilibrium systems. You will
  gain experience implementing nontrivial dynamical systems in Python, designing
  pre-registered intervention experiments, and evaluating geometric predictions
  against null models.
published: 2026-09-20
title: Fisher Conductance as a Predictive Information Topography
overview: >-
  Information theory characterises what can be transmitted through a channel, but
  does not explain how communication structure arises. The inaccessible game
  (Lawrence, 2025) derives a dynamical system from information-theoretic axioms in
  which the Fisher information matrix acts as a state-dependent conductance tensor —
  an *information topography*. 
  
  Existing demonstrations from the inaccessible game are largely descriptive:
  GENERIC-like structure appears, bottlenecks can be visualised. This project asks
  the sharper question required for a generative theory: does the conductance
  geometry *predict* where bottlenecks form and how the topography reorganises
  under controlled interventions?

  The project builds on the open-source companion library
  [tig-code](https://github.com/lawrennd/tig-code) and on the classical equivalence
  between steepest entropy ascent and GENERIC dissipation (Montefusco, Consonni and
  Beretta, 2015). Success means pre-registered predictions from the Fisher
  geometry that outperform naive baselines.
project_objective: >-
  (1) Reproduce the Curie–Weiss and harmonic-oscillator GENERIC analyses from
  tig-code, verifying the symmetric/antisymmetric decomposition $M = S + A$.
  (2) Design three to four interventions (constraint hardness, coupling strength,
  external forcing, resolution $\varepsilon$) with predictions, written *before*
  running dynamics, for bottleneck location, reorganisation timing, and
  $\|A\|/\|S\|$ regime. Predictions must be derived from local conductance /
  eigenvectors of $G(\theta)$. (3) Evaluate hit rate against null models (random
  metric, Euclidean gradient ascent under the same constraints). (4) Write a short
  theory note arguing when Fisher conductance is necessary versus any SEA metric
  (Beretta's generic-metric formulation). Deliverables: reproducible experiment
  suite, prediction log, and a thesis chapter suitable for conversion to a workshop
  paper.
project_bigger_picture: >-
  This project contributes to the mathematical foundations of *information
  topography*: communication structure as an endogenous outcome
  of constrained information dynamics. It connects directly to the IEI module
  (Fisher geometry, $I+H=C$, MaxEnt) and to talks on the inaccessible game and
  information topography. A successful project strengthens the claim that
  topography is predictive, not merely metaphorical.
year: 2026
---
