---
month: 09
year: 2024
layout: project-to-supervise
title: Efficient batching for multi-objective Bayesian optimisation
status: Available
categories:
  - mphil
  - prtiii
overview: Bayesian optimisation (BO) is a popular technique for optimising expensive black-box processes in machine learning, life sciences and industry. BO can be succesfully used in single and multi-objective settings. While BO is naturally an iterative procedure, in certain situations it is possible to perform multiple evaluations of the objective process, a technique known as batching. This project proposes to develop efficient method for batching of multi-objective BO. It will jointly supervised with [Henry Moss](https://henrymoss.github.io/).
supervisors:
  - andrei-paleyes
  - carl-henrik-ek
published: 2024-09-25
project_objective: The goal of the project is to implement a multi-objective version of "local penalisation", well known batching method for single-objective BO (https://proceedings.mlr.press/v51/gonzalez16a.html). Concretely, it entails coming up with a way to estimate/learn Lipschitz constant of a multi-objective function, analogous with how it was done in the original paper for a single-objective case. The proposed idea should be implemented in code and evaluated on benchmark optimisation problems. For implementation we suggest using BoTorch, but other tools can also be considered. The final step of the project is to analyse the efficiency of the implemented method. We will also encourage publication of the project's result.
student_learn: You will learn about multi-objective Bayesian optimisation. You will gain experience of building models using the PyTorch or other frameworks.
project_bigger_picture: The student will be a part of an eco-system with PhD students and research fellows specialising in different areas of machine learning. They will get a chance to refine their project ideas in collaboration with other researchers who specialise in a broad array of research involving Gaussian processes, re-inforcement learning, software engineering, climate science and AI for science.
---
