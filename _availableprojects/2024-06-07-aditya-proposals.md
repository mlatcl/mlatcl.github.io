---
layout: project-to-supervise
title: Improving Probabilistic Models for Machine Learning in Science
status: Available
categories:
  - MPhil
  - prtiii
overview: >-
  Each of the **six** following projects involves understanding and extending an existing
  probabilistic model commonly used in a scientific context to improve usability
  and model understanding. Please email me (ar847@cam.ac.uk) if interested.


  These projects will be supervised by Aditya Ravuri (4th year PhD student). If you're
  thinking of applying, please ensure that you're comfortable with the following
  or are willing to learn somewhat independently:
  
  
  1. basic statistical modelling: representation of models as collections of random
  variables, inference by maximizing the posterior or approximating it
  (variational inference).  
  
  2. a vague idea of the construction of the model discussed in the project that interests you.  
  
  3. using python for implementations: most of the existing code for these projects is
  written in torch in Python, but I'm happy to support the usage of other languages, such
  as R or Julia (although I don't have experience with using Julia) if there are good
  probabilistic programming abstractions available in them.  
  
  
  I'm willing to be very hands-on with the project (e.g. going through the technical
  background, the premise, suggesting experiments, debugging etc.) but expect some
  level of ability to work and learn independently. The projects are listed in order of
  personal preference.  
  

  **Project One: Can diffusion models match the performance of misspecified Hidden Markov
  Models for ice-core dating in very low data regimes?**   
  

  This is a follow-up to the work: https://arxiv.org/pdf/2210.16568  
  

  In Antarctica, ice formed by many years of precipitation is extracted as large cylinders
  called ice-cores, and by studying the oscillating abundances of certain chemicals in the
  ice, or soot from known volcanic eruptions, we can get an idea of what depth of the
  ice-core corresponds to which time period.  
    
    
  The problem can be represented statistically as inference for a latent variable t,
  assuming a graphical model: d -> t -> s, where d and s correspond to the observed random
  variables depth of the ice core and the chemical concentration.  
    
    
  Hidden Markov Models (HMMs) are a very natural model with this graphical structure.
  The model for s is: s|t ~ normal (a cyclical function of t, sigma) and the transition
  matrix for the latent time t_2 | t_1 is set up in such a way we can either stay in state
  2012 (for example, when the ice core was collected) or advance to 2011.9, ensuring
  monotonicity.  
  
  
  These models are highly misspecified in practice, i.e. the discrete states representing
  time is very coarse (like 2012, 2011.75, 2011.5, ...), and I believe that making these
  models continuous in a naive way (which leads to stochastic differential equations SDEs /
  diffusions) breaks them because this misspecification is important. Moreover, exact
  inference is possible in HMMs and not with the SDEs I've constructed, which I think also
  plays a part.  
    
    
  The project will explore if it's possible to construct an SDE that matches the performance of
  the HMM using very little data. The project will mainly be about stochastic differential
  equations used as models (note that integrators are available online, for example: https://github.com/google-research/torchsde
  so there's no expectation to code any of this up from scratch, the main experimentation
  should be on the model side, as automatic inference is of importance).  
    
    
  **Project Two: Automatic detection and classification of monkey calls from bioacoustic data**  
    
    
  We have a lot of soundscape data collected from monkey enclosures in zoos in the UK.
  A straightforward machine learning goal: identify when the monkeys scream and what
  they're screaming about.  
    
    
  We have a baseline model (a simple RNN that takes spectrograms/MFCCs and outputs
  probabilities of call/not call by time point) working and a classification model that
  shows promise when applied to audio that definitely corresponds to calls. However, a 
  unified online (streaming) model still needs to be developed. I'm
  currently in the process of showing that contrastive (SSL) models like wav2vec are also
  good featurizers.  
    
    
  This project will most likely involve experimenting with which featurizers work best, but
  most importantly robustly across different zoos, data augmentation and classification
  model design to ensure some level of robustness against calls that aren't identified
  quite right, potentially combining the activity detection and classification models and
  improving the GUI (dash web app) that exists at the moment to view the outputs of these
  models.  
    
    
  **Project Three: Application of the sparse variational GPLVM (Gaussian process latent variable model) for the analysis of single-cell data and eQTLs**  
    
    
  This is a follow-up project from: https://arxiv.org/pdf/2405.03879, https://arxiv.org/pdf/2209.06716  
    
    
  For a specific study on immune cells, gene expression data was collected at scale, and a
  dimensionality reduction on this data using a GPLVM extracted dimensions of genetically
  important variation and confounding effects.  
    
    
  The Gaussian process model used was: gene expression vector ~ multivariate_normal(a simple
  mean, an interesting GP kernel based on science).  
    
    
  Inference in this model is very slow, hence, we proposed a sparse variational Gaussian
  process that accounts for both the biological and confounding variables that speeds it
  up a lot, and we've improved this model so that it matches performance of scVI (the
  benchmark in the field that uses a very non-traditional variational autoencoder). This was
  done by using a Poisson observation model and a non-trivial variational distribution.  
    
    
  The code for this can be found at: https://github.com/InfProbSciX/scvi-ablation/blob/main/covid_trial.py  
    
    
  This project will extend this code to identify the amount of variation expressed by the
  biological factors when a condition is introduced, accounting for confounders. 

  Practically
  this will mean making very small modifications to the model and re-training some of the
  existing models. I foresee that the main complexity with this project will be trying to
  explain why / which parts of the model fail if the benchmark figures cannot be recovered,
  and potentially rewriting bits of the existing API (using gpytorch).  
    
    
  **Project Four: Defining a language that describes models in R's GLMs, MGCV's GAMs, Stan's BRMS, PYMC's bambi**  
    
    
  I'm interested in explicitly defining the grammar of a probabilistic programming
  language that is implicitly used by the APIs in the title and exploring limitations
  of such a high-level simplified grammar (e.g. it's said that the data dictionary is
  needed in addition to these statements for transpilation). An example of what some
  model statements look like:  
  
  
  ```
  y ~ x
  y ~ x_a + s(x_b), sigma ~ 0 + x_c
  ```
  
  
  corresponding to:  
  
  
  ```
  y | x ~ N(a + b*x, sigma^2) 
  y | x ~ N(a * x_a + f_theta(x_b), exp(x_c))
  ```
  
   
  **Project Five: Exploring immediate applications of ProbDR**  
    
    
  Based on: https://arxiv.org/pdf/2405.17412, https://arxiv.org/pdf/2304.07658  
    
    
  I've shown that most dimensionality reduction methods that compress
  a high dimensional matrix Y (n rows of independently sampled d dimensional data points)
  into a lower q dimensional representation held by the matrix X (n by q) are inference
  algorithms of a probabilistic model that looks like:  
    
    
  `S(Y) | X ~ Wishart {^-1} (lin_kernel(X) + non_lin_kernel(X) + noise_kernel, nu) ` 
    
    
  The model however, is in some ways mis-specified. Potential projects include trying to
  recover interpretability and explainability results achieved by other probabilistic
  DR models such as PCA, GPLVMs using the ProbDR interpretations directly and see if this
  offers any advantages in model extensions when more data is available. Another potential
  project is to uncover what it is exactly that S(Y) measures - my hunch is that this is a
  biased covariance estimate, or an estimate that is more robust to data distribution
  misspecification and small data, but I don't know the nature of the bias exactly. There
  is also a possibility on working on the theory to make some of these interpretations
  better by tightening the bounds or coming up with better approximations by
  moment-matching.  
   
   
  **Project Six: LLMs for statistics**  
   
   
  Also a less defined project, would be happy to supervise an LLM fine-tuning project looking
  at question answering for statistical questions (I'd imagine that it'd be easy to get these
  question answer pairs by sampling statements from texts and using another LLM to form sets of
  plausible questions). This can instead be stan (a probabilistic programming language) code
  completion type thing instead. In either case, I'm interested to see if a level of statistical
  modelling intuition can be recovered from these models. My experience with chatgpt4 ad 3.5 is
  that they're rather bad.  
  

  Happy to consider other ideas along such topics.
supervisors:
  - aditya-ravuri
  - neil-d-lawrence
published: 2024-06-07
student_learn: probabilistic modelling
project_objective: improving existing probabilistic models for scientific applications and/or contributing to their understanding
project_bigger_picture: accelerating science with probabilistic models
---
