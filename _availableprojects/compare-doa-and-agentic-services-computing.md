---
month: 10
layout: project-to-supervise
theme: data-oriented-architectures-theme
status: Available
categories:
  - prtiii
  - MPhil
supervisors:
  - christian-cabrera
  - neil-d-lawrence
projects:
  - data-oriented-architectures-for-ai-based-systems
  - interfaces
student_learn: >-
  You will learn how multi-agent systems are designed with service styles such
  as microservices or serverless, and how agentic services computing extends
  service-oriented computing to goal-oriented autonomous services. You will
  learn the data dichotomy: services hide data behind interfaces, while
  monitoring and adaptation need that data exposed. You will compare a
  service-style deployment with a DOAgent session on the same game, and use
  entropy and modularity as measures of group behaviour.
published: 2026-10-08
title: Comparing Data-Oriented Architectures and Agentic Services Computing for Building Multi-Agent Systems
overview: >-
  Multi-agent systems are designed and architected using styles like
  microservices or serverless. Recent research proposes extending traditional
  service-oriented computing to agentic services computing. This extension
  transforms reusable functional endpoints into goal-oriented autonomous
  services that can be described, discovered, composed, operated, and governed.
  Services are interfaces that hide data, creating a data dichotomy: machine
  learning systems require data exposure for monitoring and adaptation, while
  services hide it behind interfaces. This dichotomy is one root cause of
  intellectual debt: systems work in practice, but their designers do not
  understand their inner workings. This project compares that service style
  with data-oriented architecture for building multi-agent systems.
  Data-oriented architecture treats data as a first-class citizen and advocates
  decentralised, open deployments. [DOAgent](https://github.com/cabrerac/doagent)
  is a library for building multi-agent systems in which agents coordinate
  through shared data and can be an starting point for the project.
project_objective: >-
  You will compare a service multi-agent system with its Data-Oriented equivalent on information
  flow. The first goal would be to reproduce an existing multi-agent system implementing both versions. Then, you will compare service runs and data-oriented runs by how closely each record policy recovers the metric curve of its own game. Emergent group behaviour is the
  object of the study. Entropy and modularity are measures of that behaviour.
project_bigger_picture: >-
  This project is part of [Data-Oriented Architectures for AI-based
  Systems](/projects/data-oriented-architectures-for-ai-based-systems.html).
  Data-oriented architecture exposes systems' data as a first-class citizen so
  that systems can be monitored, reused, and adapted. The broader goal is to
  address the data dichotomy and mitigate intellectual debt when multi-agent
  systems are built as services. Information topography is the theory this
  comparison heads toward. The work also contributes to the
  [Self-Sustaining Software Systems (S4)](https://arxiv.org/abs/2401.11370)
  agenda, where decisions stay readable after the system has run.
year: 2026
---
