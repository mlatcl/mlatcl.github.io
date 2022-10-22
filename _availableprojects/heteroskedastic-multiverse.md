---
layout: project-to-supervise
title: Why 10 random seeds? Exploring a heteroskedastic multiverse
status: Available
categories:
  - MPhil
  - prtiii
overview: >-
    A multiverse analysis, first introduced in psychology [1], is a principled
    toolkit for evaluating the robustness and generality of scientific claims. As
    researchers, we make numerous choices through the course of an investigation
    that could influence the final result. Applying the multiverse analysis to
    machine learning, Bell et al. [2] systematically evaluate how researcher
    choices (e.g., hyperparameters, evaluation dataset) can fundamentally change
    the conclusions drawn. For example, Bell et al. evaluate the role of
    hyperparameters in optimizer choice, and evaluate whether large batch training
    necessarily leads to a drop in generalisation performance.


    In a deep learning setting, the multiverse is large and contains continuous
    dimensions, making it challenging to rigorously explore. To overcome this, Bell
    et al. implement a simple Gaussian Process surrogate and turn to Bayesian
    experimental design to sample experimental configurations to evaluate. This has
    the added benefit of allowing us to quantify our confidence in different
    regions of the multiverse.


    A simplifying assumption in Bell et al.’s approach is that the multiverse is
    homoskedastic: that each point has the same variance. This is unlikely to be
    the case when working with neural networks. This project will extend the
    underlying surrogate to account for heteroskedasticity. One possible approach
    to this is to explicitly model the noise as a function of the inputs using a
    separate Gaussian Process [3].


    This approach has an important consequence. In deep learning, it is typical to
    evaluate models using the mean performance over a number (usually 10) runs with
    different random seeds. But why 10? Whether this is an appropriately large
    sample size for robust inference, i.e. to confidently claim model A outperforms
    model B, remains to be seen (for an example in NLP, see [4]). By accounting for
    heteroskedasticity in a multiverse analysis, we can make an informed decision
    about how many runs are appropriate, and make a principled trade-off between
    re-running the same configuration and sampling a new point in the multiverse
    [5].


    If you’re interested in the project, get in touch with Samuel Bell
    (sjb326@cam.ac.uk) for an informal chat.


    [1] Steegen, S., Tuerlinckx, F., Gelman, A., & Vanpaemel, W. (2016). Increasing transparency through a multiverse analysis. Perspectives on Psychological Science.

    [2] Bell, S. J., Kampman, O. P., Dodge, J., & Lawrence, N. D. (2022). Modeling the Machine Learning Multiverse. NeurIPS.

    [3] Goldberg, P., Williams, C., & Bishop, C. (1997). Regression with input-dependent noise: A Gaussian process treatment. NeurIPS.

    [4] Card, D., Henderson, P., Khandelwal, U., Jia, R., Mahowald, K., & Jurafsky, D. (2020, November). With Little Power Comes Great Responsibility. EMNLP.

    [5] Binois, M., Huang, J., Gramacy, R. B., & Ludkovski, M. (2019). Replication or exploration? Sequential design for stochastic simulation experiments.  Technometrics.
supervisors:
  - samuel-bell
  - neil-d-lawrence
published: 2022-10-22
---
