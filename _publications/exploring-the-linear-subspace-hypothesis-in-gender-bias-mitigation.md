---
layout: publication-single
title: Exploring the Linear Subspace Hypothesis in Gender Bias Mitigation
author: Francisco Vargas, Ryan Cotterell (2020)
references: Proceedings of the 2020 Conference on Empirical Methods in Natural
  Language Processing
---
Bolukbasi et al. (2016) presents one of the first gender bias mitigation techniques for word embeddings. Their method takes pre-trained word embeddings as input and attempts to isolate a linear subspace that captures most of the gender bias in the embeddings. As judged by an analogical evaluation task, their method virtually eliminates gender bias in the embeddings. However, an implicit and untested assumption of their method is that the bias sub-space is actually linear. In this work, we generalize their method to a kernelized, non-linear version. We take inspiration from kernel principal component analysis and derive a non-linear bias isolation technique. We discuss and overcome some of the practical drawbacks of our method for non-linear gender bias mitigation in word embeddings and analyze empirically whether the bias subspace is actually linear. Our analysis shows that gender bias is in fact well captured by a linear subspace, justifying the assumption of Bolukbasi et al. (2016).

For further information, visit: [arXiv:2009.09435](https://arxiv.org/abs/2009.09435) \[cs.LG]