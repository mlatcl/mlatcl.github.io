---
month: 09
layout: project-to-supervise
status: Available
categories:
  - prtiii
  - mphil
supervisors:
  - neil-d-lawrence
  - christian-cabrera
projects:
  - information-topography
student_learn: >-
  You will learn information-bottleneck and rate–distortion ideas applied to LLM
  agents, how to evaluate context compression beyond task success, and how to
  design causal attacks that separate next-action preservation from
  consequence-preserving (action-sufficient) representations. You will implement
  diagnostics on modern agent scaffolding (belief summaries, memory compressors).
published: 2026-09-20
title: Action-Sufficiency Audits for LLM Belief Bottlenecks
overview: >-
  **Prerequisite:** students should take [L172 Information, Energy and Intelligence (IEI)](https://www.cl.cam.ac.uk/teaching/2627/L172/), or show equivalent preparation in information theory, maximum entropy, and information geometry.

  Long-horizon LLM agents cannot keep full histories in context. Recent systems
  compress interaction into belief states or summaries: ABBEL maintains
  natural-language belief bottlenecks; CoACT optimises observation compression for
  next-action preservation (NAP); other work uses mutual-information rate between
  raw context and compression as a proxy for compressor quality (ABBEL,
  arXiv:2512.20111; CoACT, arXiv:2607.02911; information-theoretic agentic design,
  arXiv:2512.21720).

  Passing NAP or improving accuracy is not the same as preserving an
  *action-sufficient* representation: a summary $R = f(O)$ such that
  $p(y\mid o, a) = p(y\mid R, a)$ for consequences $y$ of available actions.
  Summaries can preserve the next click while discarding distinctions needed for
  later escalation — a microscopic form of agentic debt. This project builds
  audits that separate those failure modes.
project_objective: >-
  (1) Reproduce one published compressor (ABBEL-style belief bottleneck or
  CoACT-style observation compression) on a fixed agent benchmark. (2) Implement
  action-sufficiency and consequence-equivalence tests, not only next-action match
  or end-task reward. (3) Design distribution-shift attacks: new tools, reordered
  observations, distractors that preserve NAP but break consequence distributions.
  (4) Deliver a diagnostic report showing compressions that pass NAP yet fail
  action-sufficiency, and argue how the lost distinctions would matter at a
  judgement / escalation junction. Deliverables: audit code, attack suite, and
  thesis chapter suitable for a short conference paper.
project_bigger_picture: >-
  The judgement layer is the set of junctions that must preserve
  the ability to contest and escalate. Agent memory compression is where that
  requirement meets engineering practice. This project links IEI information-bottleneck
  material to instrumentation of agentic systems and to the governance
  question: what must not be summarised away?
year: 2026
---
