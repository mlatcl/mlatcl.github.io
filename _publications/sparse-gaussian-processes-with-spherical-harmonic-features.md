---
layout: inproceedings
title: Sparse Gaussian Processes with Spherical Harmonic Features
abstract: We introduce a new class of inter-domain variational Gaussian
  processes (GP) where data is mapped onto the unit hypersphere in order to use
  spherical harmonic representations. Our inference scheme is comparable to
  variational Fourier features, but it does not suffer from the curse of
  dimensionality, and leads to diagonal covariance matrices between inducing
  variables. This enables a speed-up in inference, because it bypasses the need
  to invert large covariance matrices. Our experiments show that our model is
  able to fit a regression model for a dataset with 6 million entries two orders
  of magnitude faster compared to standard sparse GPs, while retaining state of
  the art accuracy. We also demonstrate competitive performance on classification
  with non-conjugate likelihoods.
published: 2020-05-24
author:
  - given: Vincent
    family: Dutordoir
    person_page: vincent-dutordoir
  - given: Nicolas
    family: Durrande
  - given: James
    family: Hensman
container-title: Proceedings of the 37th International Conference on Machine Learning
website: http://proceedings.mlr.press/v119/dutordoir20a.html
html: http://proceedings.mlr.press/v119/dutordoir20a.html
pdf: http://proceedings.mlr.press/v119/dutordoir20a/dutordoir20a.pdf
arxiv: 2006.16649
year: 2020
---
