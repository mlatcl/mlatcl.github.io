---
title: Empirical Bayes Transductive Meta-Learning with Synthetic Gradients
tex_title: Empirical {B}ayes Transductive Meta-Learning with Synthetic Gradients
abstract: |
  We propose a meta-learning approach that learns from multiple tasks
  in a transductive setting, by leveraging the unlabeled query set in
  addition to the support set to generate a more powerful model for
  each task. To develop our framework, we revisit the empirical Bayes
  formulation for multi-task learning.  The evidence lower bound of
  the marginal log-likelihood of empirical Bayes decomposes as a sum
  of local KL divergences between the variational posterior and the
  true posterior on the query set of each task.  We derive a novel
  amortized variational inference that couples all the variational
  posteriors via a meta-model, which consists of a synthetic gradient
  network and an initialization network. Each variational posterior is
  derived from synthetic gradient descent to approximate the true
  posterior on the query set, although where we do not have access to
  the true gradient.  Our results on the Mini-ImageNet and CIFAR-FS
  benchmarks for episodic few-shot classification outperform previous
  state-of-the-art methods. Besides, we conduct two zero-shot learning
  experiments to further explore the potential of the synthetic
  gradient.
author:
- family: Hu
  given: Shell Xu
- family: Garcia Moreno
  given: Pablo
  url: https://www.linkedin.com/in/pablo-garc%C3%ADa-moreno-4b812087/?originalSubdomain=uk
  institute: Amazon
- family: Xiao
  given: Yang
- family: Shen
  given: Xi
- family: Obozinski
  given: Guillaume
  url: https://people.epfl.ch/guillaume.obozinski/?lang=en
- family: Lawrence
  given: Neil D.
  gscholar: r3SJcvoAAAAJ
  institute: University of Cambridge
  twitter: lawrennd
  url: http://inverseprobability.com
- family: Damianou
  given: Andreas
  url: https://adamian.github.io/
  institute: Amazon
software: https://github.com/amzn/xfer
booktitle: International Conference on Learning Representations
categories:
- Hu-empirical20
key: Hu-empirical20
id: Hu-empirical20
layout: inproceedings
pdf: https://openreview.net/attachment?id=Hkg-xgrYvH&name=original_pdf
openreview: Hkg-xgrYvH
month: 12
publish: 2020-04-26
year: 2020
---
