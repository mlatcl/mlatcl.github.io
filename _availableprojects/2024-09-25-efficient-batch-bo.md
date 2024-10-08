---
month: 09
year: 2024
layout: project-to-supervise
title: Design of plant models with Helios and Bayesian optimisation
status: Available
categories:
  - mphil
  - prtiii
overview: Climate change increases the need for crops that can withstand heat and drought. Crop breeding helps develop resilient plants, but evaluating large numbers of plants is challenging. Current methods like high-throughput phenotyping collect images, but extracting detailed plant traits is complex and requires advanced processing. An alternative approach is using procedural 3D plant models, like Helios, which simulate plants based on architectural parameters. However, Helios requires many parameters to generate accurate 3D models, making the model fitting process complex. This project focuses on using Bayesian optimization, a popular machine learning technique for optimising/calibrating expensive black-box processes, to improve the alignment of Helios' 3D plant models with real crop images. By optimizing Helios' parameters based on images from a 2022 UC Davis bean trial, we aim to generate fully annotated 3D crop models, which can be used for breeding selection to enhance climate resilience. In this project we will work closely with [Henry Moss](https://henrymoss.github.io/) and Ioannis Droutsas (Wageningen University).
supervisors:
  - andrei-paleyes
  - carl-henrik-ek
published: 2024-09-25
project_objective: The goal of the project is to implement a Bayesian optimisation (BO) loop to fine-tune a Helios model. Helios is a flexible simulator that creates models of 3D plant objects from a set of architectural parameters (e.g. leaves and stems), each fully accompanied by metadata information such as size, colour and orientation. Helios's flexibility means that a relatively large number of parameters must be calibrated (at least ~60-80) when fitting the simulator to experimental data. We will build custom BO algorithms and Gaussian process surrogate models suitable for such high-dimensional and highly-structured inputs. As, the Helios architectural inputs can be viewed as an ordered list of plant organs, one particularly promising avenue is to extend the subset string kernel (https://proceedings.neurips.cc/paper_files/paper/2020/hash/b19aa25ff58940d974234b48391b9549-Abstract.html) to allow the inclusion of additional continuous covariates, and developing a custom genetic algorithm to help explore over these augmented strings. The proposed idea should be implemented in code and evaluated on benchmark optimisation problems and on the Helios model. For implementation we suggest using BoTorch, but other tools can also be considered. We will also encourage publication of the project's result.
student_learn: You will learn about multi-objective Bayesian optimisation. You will gain experience of building models using the PyTorch or other frameworks.
project_bigger_picture: The student will be a part of an eco-system with PhD students and research fellows specialising in different areas of machine learning. They will get a chance to refine their project ideas in collaboration with other researchers who specialise in a broad array of research involving Gaussian processes, re-inforcement learning, software engineering, climate science and AI for science.
---
