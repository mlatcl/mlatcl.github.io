---
layout: techreport
title: "Modelling Technical and Biological Effects in scRNA-seq Data with Scalable GPLVMs"
date: 2022-09-14
published: 2022-11-06
abstract: |
  Single-cell RNA-seq datasets are growing in size and complexity, enabling the study of cellular composition changes in various biological/clinical contexts. Scalable dimensionality reduction techniques are in need to disentangle biological variation in them, while accounting for technical and biological confounders. In this work, we extend a popular approach for probabilistic non-linear dimensionality reduction, the Gaussian process latent variable model, to scale to massive single-cell datasets while explicitly accounting for technical and biological confounders. The key idea is to use an augmented kernel which preserves the factorisability of the lower bound allowing for fast stochastic variational inference. We demonstrate its ability to reconstruct latent signatures of innate immunity recovered in Kumasaka et al. (2021) with 9x lower training time. We further analyze a COVID dataset and demonstrate across a cohort of 130 individuals, that this framework enables data integration while capturing interpretable signatures of infection. Specifically, we explore COVID severity as a latent dimension to refine patient stratification and capture disease-specific gene expression.
author:
  - given: Vidhi
    family: Lalchand
  - given: Aditya
    family: Ravuri
  - given: Emma
    family: Dann
  - given: Natsuhiko
    family: Kumasaka
  - given: Dinithi
    family: Sumanaweera
  - given: Rik G.H.
    family: Lindeboom
  - given: Shaista
    family: Madad
  - given: Sarah A.
    family: Teichmann
  - given: Neil D.
    family: Lawrence
arxiv: 2209.06716
website: https://arxiv.org/abs/2209.06716
doi: 10.48550/arXiv.2209.06716
subjects:
  - Machine Learning (cs.LG)
  - Genomics (q-bio.GN)
  - Applications (stat.AP)
  - Machine Learning (stat.ML)
submission_history:
  - version: v1
    date: 2022-09-14
    size: 12,682 KB
    submitter: Vidhi Lalchand Miss
    email: view email
  - version: v2
    date: 2022-11-06
    size: 12,682 KB
comments: Machine Learning and Computational Biology Symposium (Oral), 2022
---
