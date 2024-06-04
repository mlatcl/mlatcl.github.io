---
layout: project-to-supervise
title: Latent Probabilistic Models for Unsupervised Structure Learning in
  Massively Missing Data
status: Hidden
categories:
  - prtiii
  - MPhil
overview: >-
  Real-world datasets often contain entries with missing elements e.g. in a
  medical dataset, a patient is unlikely to have taken all possible diagnostic
  tests. Variational Autoencoders (VAEs) are popular generative models often
  used for unsupervised learning. Despite their widespread use it is unclear how
  best to apply VAEs to datasets with missing data.


  I﻿n this projects we intend to explore a novel incarnation of a Gaussian process latent variables which can work seamlessly with missing data, the architecture would include a pointNet encoder which will encode every partial data point as a set with indicator variables (capturing the dimension identity) and a classical Gaussian process decoder.


  T﻿he focus would be on assessing the quality of uncertainty calibration, structure learning in latent space, and reconstruction quality on previously unseen data.
supervisors:
  - vidhi-lalchand
  - neil-d-lawrence
published: 2022-10-24
student_learn: >-
  The student will have to learn the foundations of probabilistic modelling and
  latent variable models both mathematically and develop dexterity with coding
  them up in pytorch  or any other probabilistic programming framework. They
  will also learn about the key models in literature in this space.


  Comparative benchmarks: 


  \-﻿ VAEs for partially missing data: https://arxiv.org/pdf/1807.03653.pdf


  \- Deep probabilistic time-series imputation: https://arxiv.org/abs/1907.04155  


  \-﻿ Generalised GPLVM with SVI: https://proceedings.mlr.press/v151/lalchand22a.html
project_objective: >-
  T﻿o build a novel probabilistic latent variable model for a single case-study
  entailing massively missing data in the observation space The project is in
  the domain of unsupervised learning with probabilistic modelling. 


  T﻿he model should be capable to capturing salient information from partially observed vectors in data space and render these high-dimensional vectors in a low-dimensional manifold capturing the key axis of variations - this should lead to clustering of similar observations in a visualisable latent space. 


  E﻿xample case-studies include: Movie ratings database, Electronic health records (mixed data type)
project_bigger_picture: >-
  Deep generative models have have become a central plank in generative
  modelling and latent variable modelling,  They efficiently emulate complex
  distributions from large high-dimensional datasets, generating new data points
  similar to the original real-world data, post training (Kingma and Welling,
  2014; Rezende and Mohamed, 2015; Li et al., 2018). So far, the main focus in
  the literature is to enrich the prior or posterior of explicit generative
  models such as variational autoencoders (VAEs); or to propose alternative
  training objectives to the log-likelihood, leading to implicit generative
  models such as, e.g., generative adversarial networks (GANs) (Mescheder et
  al., 2017). We are witnessing a race between an ever-growing spectrum of VAE
  models, but the deployment of these models to practically relevant real-world
  datasets which are often incomplete and missing is being overlooked. 


  In this project we aim to look the missing data use-case in greater detail and propose a novel formulation which combines point nets, indicator variables and Gaussian processes.
---
