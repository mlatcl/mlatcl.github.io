---
layout: techreport
title: Efficient Representations for Privacy-Preserving Inference
author: 
- given: Han 
  family: Xuanyuan
- given: Francisco 
  family: Vargas
- given: Stephen 
  family: Cummins
arxiv: 2110.08321
published: 2021-10-15
year: 2021
abstract: "Deep neural networks have a wide range of applications across multiple domains such as computer vision and medicine. In many cases, the input of a model at inference time can consist of sensitive user data, which raises questions concerning the levels of privacy and trust guaranteed by such services. Much existing work has leveraged homomorphic encryption (HE) schemes that enable computation on encrypted data to achieve private inference for multi-layer perceptrons and CNNs. An early work along this direction was CryptoNets, which takes 250 seconds for one MNIST inference. The main limitation of such approaches is that of compute, which is due to the costly nature of the NTT (number theoretic transform)operations that constitute HE operations. Others have proposed the use of model pruning and efficient data representations to reduce the number of HE operations required. In this paper, we focus on improving upon existing work by proposing changes to the representations of intermediate tensors during CNN inference. We construct and evaluate private CNNs on the MNIST and CIFAR-10 datasets, and achieve over a two-fold reduction in the number of operations used for inferences of the CryptoNets architecture."
---

