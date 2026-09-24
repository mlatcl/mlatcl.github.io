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
  - joery-de-vries
  - neil-d-lawrence
projects:
  - information-topography
student_learn: >-
  You will learn about open-ended and multi-agent reinforcement learning:
  occupancy measures and their polytopes, the linear-programming formulation
  of RL, and concavity arguments for deterministic optima. You will learn
  about Nash equilibria and best-response dynamics in games and opponent
  modelling.
published: 2026-09-24
title: Homeostatic Regulators in Multi-Agent Environments
overview: >-
  Conant and Ashby's good regulator theorem concerns a regulator that holds
  an outcome steady against a disturbance. Its success criterion is the
  entropy of the outcome, which is different from the classical notion of
  reward in reinforcement learning: it is a concave objective over the
  occupancy polytope, so an optimal single regulator is deterministic. This
  project asks what happens when the disturbance is another regulator.
  Several agents share an environment and each minimises the entropy of its
  own outcome under its own reference measure. From any agent's viewpoint the
  other agents are structured, adaptive disturbances. Refinements of the
  theorem, notably Wentworth's, say the regulator must carry a posterior over
  its disturbance, thus the notion of "model" that Conant and Ashby's theorem
  implies is a posterior over the other agents' policies. We will try to
  answer whether this posterior is necessary, and whether the joint problem
  is Nash. The working hypothesis is that competing regulators partition the
  state space into per-agent stable niches, which remains to be verified
  experimentally.
project_objective: >-
  (1) Formalise the n-regulator game on product occupancy polytopes and
  define the augmented state (environment state plus posterior) to capture
  the problem again as an MDP. Determine whether a pure stationary
  equilibrium exists in a shared-resource task. (2) Build a tabular
  shared-resource gridworld, compute equilibria by best-response iteration,
  and test the niche hypothesis. (3) Learn with independent regulators using
  a majorisation-minimisation method, with and without the opponent posterior
  in the state, and evaluate what a minimal complexity model of an opponent
  requires. (4) Evaluate scaling behavior to many agents (in an open-ended
  setting). Deliverables: environment, short theory note, equilibrium and
  learning comparison, thesis chapter.
project_bigger_picture: >-
  Multi-agent collaboration is important in the agentic world. A regulator
  that is minimal in the sense of its behavioral complexity (i.e., minimizes
  entropy of its outcome) is also predictable to the agents around it. Agents
  that behave predictably need less communication or escalation. This
  project is a fundamental step towards building our understanding of this
  framework.
year: 2026
---
