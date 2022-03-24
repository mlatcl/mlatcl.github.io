---
layout: publication-single
title: Adversarial Concept Erasure in Kernel Space
author: Shauli Ravfogel, Francisco Vargas, Yoav Goldberg, Ryan Cotterell
references: Preprint, under review
---
The representation space of neural models for textual data emerges in an unsupervised manner during training. Understanding how human-interpretable concepts, such as gender, are encoded in these representations would improve the ability of users to \emph{control} the content of these representations and analyze the working of the models that rely on them. One prominent approach to the control problem is the identification and removal of linear concept subspaces -- subspaces in the representation space that correspond to a given concept. While those are tractable and interpretable, neural network do not necessarily represent concepts in linear subspaces. We propose a kernalization of the linear concept-removal objective of \[Ravfogel et al. 2022], and show that it is effective in guarding against the ability of certain nonlinear adversaries to recover the concept. Interestingly, our findings suggest that the division between linear and nonlinear models is overly simplistic: when considering the concept of binary gender and its neutralization, we do not find a single kernel space that exclusively contains all the concept-related information. It is therefore challenging to protect against \emph{all} nonlinear adversaries at once.

For further information, please visit: [arXiv:2201.12191](https://arxiv.org/abs/2201.12191) \[cs.LG]