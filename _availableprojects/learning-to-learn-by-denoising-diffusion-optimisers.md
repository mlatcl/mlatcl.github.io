---
layout: project-to-supervise
title: Learning to Learn by Denoising Diffusion Optimisers
status: Hidden
categories:
  - MPhil
  - prtiii
overview: >-
  The seminal paper Learning to Learn by Gradient Descent By Gradient Descent
  \[1] explores learning optimisers (rather than using SGD or Adam) through an
  RNN architecture which models time steps as training steps and an RL based
  loss. 


  In this project we aim to achieve a similar product but rather than RNNs and RL we would like to explore the closely linked diffusion models \[5,6] and stochastic control. In particular there is already theoretical work that motivates the use of these methodologies for global optimisation \[2], what now remains is to explore it in practice.


  W﻿e expect the student to lightly adapt the methods in \[3,4] to the optimisation setting in \[2] (This simply amounts to exploring low temperatures in the artificial target distribution induced by the loss function).  Furthermore, exploring tasks in engineering as in \[1] might require being creative about the inductive biases baked into the NN parametrisation that we are working with.


  The nature of this project will be mostly ML-engineering and playing around / being creative about NN inductive biases. That said if the student is more mathematically/theory oriented we could explore extending the results in \[2] (which apply to the method in \[4] only) to the method in in \[3] using the mixing rates in \[7] and maybe comparing to things like \[8] (last bit would be very bonus/extra type of thing).


  A﻿s always the student should explore simple 1d and 2d toy optimisation examples to assess the validity of the method before moving onto real world examples.


  \[﻿1] [https://arxiv.org/pdf/1606.04474.pdf](https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2Farxiv.org%2Fpdf%2F1606.04474.pdf&data=05%7C01%7Cfav25%40cam.ac.uk%7Ca14bb2a0a3084b79cd9808daabbed5b1%7C49a50445bdfa4b79ade3547b4f3986e9%7C0%7C0%7C638011133352555862%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=muiHl7wxQCMJLQDDj7Nam9deOKTyzwb%2BreDb9ouRk3Q%3D&reserved=0) 


  \[﻿2] [https://arxiv.org/abs/2111.00402](https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2Farxiv.org%2Fabs%2F2111.00402&data=05%7C01%7Cfav25%40cam.ac.uk%7Ca14bb2a0a3084b79cd9808daabbed5b1%7C49a50445bdfa4b79ade3547b4f3986e9%7C0%7C0%7C638011133352555862%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=%2B0prnqNoRPKqYXWiL8L%2FDRGCuOR6yjywCJWBqddhkYU%3D&reserved=0)


  \[﻿3] [https://openreview.net/forum?id=8pvnfTAbu1f](https://eur03.safelinks.protection.outlook.com/?url=https%3A%2F%2Fopenreview.net%2Fforum%3Fid%3D8pvnfTAbu1f&data=05%7C01%7Cfav25%40cam.ac.uk%7Ca14bb2a0a3084b79cd9808daabbed5b1%7C49a50445bdfa4b79ade3547b4f3986e9%7C0%7C0%7C638011133352555862%7CUnknown%7CTWFpbGZsb3d8eyJWIjoiMC4wLjAwMDAiLCJQIjoiV2luMzIiLCJBTiI6Ik1haWwiLCJXVCI6Mn0%3D%7C3000%7C%7C%7C&sdata=S%2Fodk%2FZBDwbkGpQ6d%2FjJCIEd3ATbwmxR%2BvaVEopE%2FlI%3D&reserved=0)


  \[﻿4] <https://arxiv.org/abs/2111.15141> 


  \[﻿5] <https://arxiv.org/abs/2006.11239> 


  \[﻿6] <https://arxiv.org/abs/2006.11239> 


  \[﻿7] <https://arxiv.org/pdf/2209.11215.pdf>


  \[﻿8] <https://arxiv.org/abs/1707.06618>
supervisors:
  - francisco-vargas
  - neil-d-lawrence
published: 2022-10-21
student_learn: |-
  

  \-﻿ Latest Advances in Diffusion Generative Models

  \-﻿ A bit on SDEs / Stochastic Calculus

  \-﻿ Using autodiff frameworks such as jax/torch
project_objective: I﻿n short the objective is to adapt the Denoising Diffusion
  Sampler or the Path Integral Sampler to instead work as an optimiser (rather
  than a sampler), additionally we want to explore how baking in inductive
  biases into the network being trained can help further.
project_bigger_picture: A﻿s mentioned before denoising diffusion based
  generative models are taking off, however the question remains if we can apply
  these to more meaningfully scientific / engineering tasks. This particular
  setting we aim to explore has direct applications in control, engineering and
  desing.
---
