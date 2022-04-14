---
layout: article
title: Differentially Private Regression and Classification with Sparse Gaussian Processes
abstract: |
  A continuing challenge for machine learning is providing methods to perform computation on data while ensuring the data remains private. In this paper we build on the provable privacy guarantees of differential privacy which has been combined with Gaussian processes through the previously published cloaking method, an approach that tackles the problem of providing privacy for the outputs of a training set. In this paper we solve several shortcomings of this method, starting with the problem of predictions in regions with low data density. We experiment with the use of inducing points to provide a sparse approximation and show that these can provide robust differential privacy in outlier areas and at higher dimensions. We then look at classification, and modify the Laplace approximation approach to provide differentially private predictions. We then combine this with the sparse approximation and demonstrate the capability to perform classification in high dimensions. We finally explore the issue of hyperparameter selection and develop a method for their private selection. This paper and associated libraries provide a robust toolkit for combining differential privacy and Gaussian processes in a practical manner.
author:
- family: Smith
  given: Michael Thomas
- family: Álvarez
  given: Mauricio A.
- family: Lawrence
  given: Neil D. 
journal: Journal of Machine Learning Research
volume: 22
number: 188
pages: 1-41
firstpage: 1
lastpage: 41
key: Smith-differentially21
doi: 
html: https://jmlr.org/papers/v22/19-017.html
pdf: https://jmlr.org/papers/volume22/19-017/19-017.pdf
software: https://github.com/lionfish0/dp4gp
year: 2021
published: 2021-10-08
---
