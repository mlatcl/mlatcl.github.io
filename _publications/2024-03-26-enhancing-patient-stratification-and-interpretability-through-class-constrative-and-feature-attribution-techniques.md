---
layout: techreport
title: "Enhancing patient stratification and interpretability through class-contrastive and feature attribution techniques"
abstract: |
  A crucial component of the treatment of genetic disorders is identifying and 
  characterising the genes and gene modules that drive disease processes. 
  Recent advances in Next-Generation Sequencing (NGS) improve the prospects 
  for achieving this goal. However, many machine learning techniques are not 
  explainable and fail to account for gene correlations. In this work, we 
  develop a comprehensive set of explainable machine learning techniques to 
  perform patient stratification for inflammatory bowel disease. We focus on 
  Crohn’s disease (CD) and its subtypes: CD with deep ulcer, CD without deep 
  ulcer and IBD-controls. We produce an interpretable probabilistic model over 
  disease subtypes using Gaussian Mixture Modelling. We then apply 
  class-contrastive and feature-attribution techniques to identify potential 
  target genes and modules. We modify the widely used kernelSHAP (Shapley 
  Additive Explanations) algorithm to account for gene correlations. We 
  obtain relevant gene modules for each disease subtype. We develop a 
  class-contrastive technique to visually explain why a particular patient is 
  predicted to have a particular subtype of the disease. We show that our 
  results are relevant to the disease through Gene Ontology enrichment 
  analysis and a review of the literature. We also uncover some novel 
  findings, including currently uncharacterised genes. These approaches 
  maybe beneficial, in personalised medicine, to inform decision-making 
  regarding the diagnosis and treatment of genetic disorders. Our approach 
  is model-agnostic and can potentially be applied to other diseases and 
  domains where explainability and feature correlations are important.
author:
  - given: Sharday
    family: Olowu
  - given: Neil D.
    family: Lawrence
  - given: Soumya
    family: Banerjee
venue: medRxiv
date: 2024-03-26
doi: 10.1101/2024.03.25.24304824
website: https://www.medrxiv.org/content/10.1101/2024.03.25.24304824v1
---
