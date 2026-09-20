---
layout: techreport
title: "Scalable Amortized GPLVMs for Single Cell Transcriptomics Data"
published: 2024-05-07
abstract: |
  Dimensionality reduction is crucial for analyzing large-scale single-cell RNA-seq data. Gaussian Process Latent Variable Models (GPLVMs) offer an interpretable dimensionality reduction method, but current scalable models lack effectiveness in clustering cell types. We introduce an improved model, the amortized stochastic variational Bayesian GPLVM (BGPLVM), tailored for single-cell RNA-seq with specialized encoder, kernel, and likelihood designs. This model matches the performance of the leading single-cell variational inference (scVI) approach on synthetic and real-world COVID datasets and effectively incorporates cell-cycle and batch information to reveal more interpretable latent structures as we demonstrate on an innate immunity dataset.
author:
  - given: Sarah
    family: Zhao
  - given: Aditya
    family: Ravuri
  - given: Vidhi
    family: Lalchand
  - given: Neil D.
    family: Lawrence
arxiv: 2405.03879
website: https://arxiv.org/abs/2405.03879
---
