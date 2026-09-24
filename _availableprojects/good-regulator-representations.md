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
  You will learn about state abstraction and irrelevance criteria, convex and
  occupancy objectives in reinforcement learning, successor features and value
  equivalence, belief states under partial observability, and self-predictive
  and inverse-dynamics losses for latent world models. You will learn how to
  implement and evaluate modern deep RL algorithms.
published: 2026-09-24
title: What Does a Good Regulator Need to Know?
overview: >-
  Conant and Ashby's (1970) good regulator theorem says a successful regulator
  must be a model of its system. Which model depends on what the regulator
  observes: Wentworth's (2021) "gooder regulator" for instance requires the
  belief state. Since a good regulator objective minimises the entropy of a
  regulated outcome this adds a secondary dependence during learning due to
  concavity of the optimization problem. Similar to convex RL, it can be
  solved by a sequence of linear rewards built from the occupancy of the
  outcome features. Although the agent converges to a single deterministic
  policy, during learning its representation must support every reward in the
  sequence. Therefore, reusing what it learned under earlier rewards while
  staying focused on what the objective makes relevant is crucial. For
  instance, the successor features of the outcome suffice for this. Despite
  much work on state abstraction, self-predictive representations and
  sensorimotor world models, it is unclear what a good regulator needs to
  represent while it learns. This project investigates what acting and
  learning require for good regulators in the language of state abstractions
  of Li, Walsh and Littman (2006) and of Ni et al. (2024), and what
  combination of latent world-model loss delivers all aspects.
project_objective: >-
  (1) Review state abstractions and representation-learning methods, and
  categorize each by what makes it relevant to a good-regulator: what does
  acting require and what does learning require? (2) Find or build a simple
  reinforcement learning environment with carefully placed distractors to
  verify our categorisation. For example: an action that the outcome ignores,
  a disturbance confounded with the action's effect on dynamics, random
  uncontrollable noise on the outcomes, the noisy TV problem that injects
  noise into observations, or another task if needed. (3) Train latent world
  models on our categorization. For example, use self-prediction, inverse
  dynamics, or an outcome head, and ablate these losses together to test the
  overall categorisation. Which distractor is invariant to each latent model?
  Which latent model is sufficient for acting and which lets the regulator
  learn the same policy. (4) Evaluate baselines such as bisimulation and
  reconstruction-based world models, and where relevant, combine with
  exploration methods such as curiosity which are known to entrench agents on
  the noisy TV. Deliverables: the regulator-relevant taxonomy, the task and
  loss comparison, and thesis chapter suitable for a paper.
project_bigger_picture: >-
  Learning a good regulator is practically relevant for many tasks, but it
  also requires the regulator to be maximally simple in the occupancy of its
  outcome. This makes the regulator predictable. As autonomous agents are
  increasingly embodied in the modern world, robust learning algorithms will
  become more important. This project builds improved understanding to work
  towards that.
year: 2026
---
