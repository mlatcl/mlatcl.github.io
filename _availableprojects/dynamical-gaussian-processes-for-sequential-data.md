---
layout: project-to-supervise
title: "Dynamical Gaussian processes for Sequential Data "
status: Available
categories:
  - MPhil
  - prtiii
overview: >-
  Gaussian process dynamical models (state-space models) builds upon a  long
  line of work combining Gaussian processes (GP) with latent variable models for
  unsupervised learning tasks. Specifically, we narrow our focus on modelling
  high-dimensional sequential data ubiquitous in nature. The dynamics in
  observed space are captured by a smoothly evolving latent variable indexed by
  time and governed by a latent Gaussian process prior. The idea behind the
  project is to develop a scalable algorithm for sequential data which does not
  rely on holding the complete sequence in memory but can process the
  time-series or sequence in chunks. We also want to amortise the model with a
  suitable encoder like a recurrent neural network, LSTM or an Attention-based
  transformer. 


  The model is basically an extension of the model proposed here: https://gregorygundersen.com/blog/2020/07/24/gpdm/


  R﻿equired reading: 


  \[1] G﻿aussian process dynamical model: https://gregorygundersen.com/blog/2020/07/24/gpdm/


  \[2] V﻿ariational GPDM: https://proceedings.neurips.cc/paper/2011/file/af4732711661056eadbf798ba191272a-Paper.pdf


  \[3] V﻿ariational GPSSM: https://proceedings.neurips.cc/paper/2014/file/139f0874f2ded2e41b0393c4ac5644f7-Paper.pdf


  \[4] R﻿ecurrent Gaussian processes with SVI: https://arxiv.org/abs/1511.06644


  \[5] GPVAE for interpretable latent dynamics: http://proceedings.mlr.press/v118/pearce20a/pearce20a.pdf
supervisors:
  - vidhi-lalchand
  - neil-d-lawrence
published: 2022-10-24
student_learn: T﻿he student will have to learn the basic comparitive models
  which work on sequential data processing in an unsupervised context - like
  Hidden markov models, GP-VAEs and RNNs. T﻿hey will also learn the fundamentals
  of learning with a Gaussian process as well as coding it up within one of the
  popular python frameworks like gpytorch. S﻿ince this is methodological work,
  the student will have to perform experiments on a range of datasets so they
  will learn how to write code and conduct experiments at scale.
project_objective: A Gaussian process dynamical model
  (GPDM) [](https://gregorygundersen.com/blog/2020/07/24/gpdm/#wang2006gaussian)can
  be viewed as a [Gaussian process latent variable model
  (GPLVM)](https://gregorygundersen.com/blog/2020/07/14/pca-to-gplvm/) with the
  latent variable evolving according to its own Gaussian process. Put more
  simply, imagine a latent variable evolves according to some smooth, nonlinear
  dynamics, and that the mapping from latent- to observation-space is also a
  smooth, nonlinear map. For example, imagine a mouse is moving in a maze, but
  we only record the firing rates of its hippocampal place cells. The latent
  variable is the mouse position, which we know is a relatively smooth
  trajectory in 3D space, and the observations, neuron firing rates, are a
  nonlinear function of this latent variable. Can we infer the position of the
  mouse given just its firing rates?  This is the type of question the project
  attempts to answer. The goal of this project is to work through this model in
  detail.
project_bigger_picture: >-
  D﻿ynamical models are essentially time-indexed models where their properties
  evolve over time. At any given time, a dynamical system has a 
  [state](https://en.wikipedia.org/wiki/State_(controls) "State
  (controls)") representing a point in an appropriate [state
  space](https://en.wikipedia.org/wiki/State_space "State space"). This state is
  often given by a [tuple](https://en.wikipedia.org/wiki/Tuple "Tuple") of [real
  numbers](https://en.wikipedia.org/wiki/Real_numbers "Real numbers") or by
  a [vector](https://en.wikipedia.org/wiki/Vector_space "Vector space") in a
  geometrical manifold. The *evolution rule* of the dynamical system is a
  function that describes what future states follow from the current state.
  Often the function
  is [deterministic](https://en.wikipedia.org/wiki/Deterministic_system_(mathematics)
  "Deterministic system (mathematics)"), that is, for a given time interval only
  one future state follows from the current
  state.[](https://en.wikipedia.org/wiki/Dynamical_system#cite_note-1) However,
  some systems are [stochastic](https://en.wikipedia.org/wiki/Stochastic_system
  "Stochastic system"), in that random events also affect the evolution of the
  state variables. 


  While models are very precise for many processes, for some of the most challenging applications of dynamical systems (such as climate dynamics, brain dynamics, biological systems or the financial markets), the development of such models is notably difficult.


  How to analyse dynamical systems on the basis of observed data rather than attempt to study models analytically? The machine learning approach is invaluable in settings where no explicit model is formulated, but measurement data is available. This is frequently the case in many systems of interest, and the development of data-driven technologies is becoming increasingly important in many applications.
---
