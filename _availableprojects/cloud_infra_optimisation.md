---
month: 06
layout: project-to-supervise
title: Multi-objective optimisation of cloud infrastructure
status: Available
categories:
  - mphil
  - prtiii
overview: Machine learning (ML) and optimisation techniques are increasingly used
  to help solve decision-making problems that would be difficult 
  or time-consuming to address manually. One such problem is the configuration of
  cloud infrastructure, where many deployment parameters can affect several
  competing objectives at the same time. This project investigates the use of
  multi-objective optimisation to automatically explore different cloud infrastructure
  configurations defined through Infrastructure-as-Code templates. Our aim will be to build
  a fully automated system that identifies a range of Pareto-optimal configurations
  that represent different trade-offs between the objectives being considered.
  Such a system can help reduce the time and cost required to create efficient cloud deployments
  while providing a better understanding of the available configuration choices.
supervisors:
  - andrei-paleyes
  - neil-d-lawrence
published: 2026-06-05
student_learn: You will learn about multi-objective optimisation. You will learn how to
  define and create cloud resources using Infrastructure-as-Code approach.
  You will gain experience working with Amazon Web Services (AWS), and potentially other cloud providers.
  You will learn about Bayesian optimization and how to apply it to practical tasks.
project_objective: The goal of the project is to implement a procedure of
  building a 2D Pareto front between two chosen metrics for a chosen compute workload
  deployed to the cloud. We suggest using BoTorch for multi-objective optimization
  but other tools can also be considered. Once the implementation is in place,
  experiments on different service parameters and output metrics will be carried out.
  The final step of the project is to analyse the discovered trade-offs.
project_bigger_picture: >-
  This project is part of a wider research programme Interfaces. One of the goals of this programme
  is to build methods for interpretable automated decision loops in software systems.
  You will have a chance to interact with the wider team and a successful project will form part of the
  portfolio of Interfaces demonstrations. We will also encourage publication of the
  project's result.

  This idea continues the line of work done by our research team of applying multi-objective Bayesian optimisation to study trade-offs involved in building ML models: [2D utility/privacy](https://arxiv.org/abs/1905.10862), [3D utility/privacy/fairness](https://arxiv.org/abs/2311.15691), [2D utility/energy] (https://arxiv.org/abs/2601.08991).
year: 2026
---

