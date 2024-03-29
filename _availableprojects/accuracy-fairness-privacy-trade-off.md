---
month: 0
layout: project-to-supervise
title: Automatic Discovery of Trade-off Between Accuracy, Privacy and Fairness
  for ML models
status: Completed
categories:
  - mphil
  - prtiii
overview: When machine learning models are deployed to solve real world
  problems, they are often trained on sensitive data, e.g. healthcare or
  financial records. Practitioners need to ensure fairness and privacy of the
  resulting model. Often privacy and fairness guarantees may only be achieved
  through sacrificing accuracy (as classically measured). Usually both privacy
  and fairness are set as fixed constraints, and the exact effect of such
  constraints on accuracy is unclear. This project proposes to develop a
  procedure of automatic discovery of the trade-off between these three metrics.
supervisors:
  - andrei-paleyes
  - neil-d-lawrence
published: 2021-06-30
student_learn: You will learn about multi-objective optimisation. You will learn
  about differential privacy and fairness metrics for ML models. You will learn
  about Bayesian optimization and learn how to apply it to practical tasks. You
  will gain experience of building models using the PyTorch library.
project_objective: The goal of the project is to implement a procedure of
  building a 3D Pareto front between accuracy, differential privacy and fairness
  (for some given fairness metric) for a selection of ML models and datasets. We
  suggest using BoTorch for multi-objective optimization and Opacus for training
  with differential privacy, but other tools can also be considered. Once the
  implementation is in place, the next step is to analyze the trade-offs and
  consider their implications for practical use cases.
project_bigger_picture: >-
  This project is part of a wider project called AutoAI. The aim is to build
  explainable and maintainable machine learning systems. You will have a chance
  to interact with the wider team and a successful project will form part of the
  portfolio of AutoAI demonstrations. We will also encourage publication of the
  project's result.

  Automatic trade-off between accuracy and privacy is studied in [this paper](https://arxiv.org/abs/1905.10862), and this project is a direct continuation of that work. Three-way trade-offs between accuracy, fairness and privacy were also [considered before](https://arxiv.org/abs/2102.05975), but not in a fully automated fashion.
year: 2021
---
