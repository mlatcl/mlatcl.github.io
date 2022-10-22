---
layout: project-to-supervise
title: How fair is fairness? A multiverse analysis of fairness definitions
status: Available
categories:
  - MPhil
  - prtiii
overview: >-
    As machine learning is increasingly deployed into high-stakes settings such as
    healthcare and justice, it’s essential our models behave in a fair and unbiased
    manner. Unfortunately this isn’t the case, as evidenced by a growing number of
    papers showing significant bias and disparate performance (e.g. [1-3]). These
    failures demonstrate the importance of auditing both datasets and models to
    identify biases, harmful associates, and performance gaps across groups.
    
    However, in order to audit, we have a series of choices to make about how we
    measure fairness [4]. Do we define fairness as parity betweens similar
    individuals, or between groups based on demographic attributes? Do we want
    parity of accuracy, or loss, false negatives, or false positives? Which dataset
    do we evaluate on? If we are using demographic data, how are we defining
    socially-constructed terms like race; are we relying on self-identified or
    perceived definitions of gender? We could go on, and each of these
    decisions may impact the resulting outcome of the fairness audit.

    First introduced in psychology, the multiverse analysis [5] is a principled
    framework for evaluating the robustness and reproducibility of claims in
    light of the multitude of possible choices a researcher can make along the
    way [6]. The multiverse entails systematically re-evaluating our analyses
    at each leaf of the decision tree, then transparently reporting and
    visualizing the results. To make this tractable in a machine learning
    search space Bell et al. [6] rely on a Gaussian Process surrogate and
    Bayesian experimental design for efficient exploration of the multiverse of
    choices.

    This project will apply a multiverse analysis to machine learning fairness,
    and systematically evaluate the conclusions of previous fairness audits in
    light of different definitions of fairness, different evaluation protocols,
    and different evaluation datasets. There is also scope to extend the
    project to a dataset audit or to a fairness intervention (e.g. gDRO [7]).

    If you’re interested in the project, get in touch with Samuel Bell
    (sjb326@cam.ac.uk) for an informal chat.

    [1] Buolamwini, J., & Gebru, T. (2018). Gender shades: Intersectional accuracy disparities in commercial gender classification. FAccT.
    [2] De Vries, T., Misra, I., Wang, C., & Van der Maaten, L. (2019). Does object recognition work for everyone?. CVPR.
    [3] Bolukbasi, T., Chang, K. W., Zou, J. Y., Saligrama, V., & Kalai, A. T.  (2016). Man is to computer programmer as woman is to homemaker? Debiasing word embeddings. NeurIPS.
    [4] Jacobs, A., Z., & Wallach, H. (2021). Measurement and Fairness. FAccT.
    [5] Steegen, S., Tuerlinckx, F., Gelman, A., & Vanpaemel, W. (2016).  Increasing transparency through a multiverse analysis. Perspectives on Psychological Science.
    [6] Bell, S. J., Kampman, O. P., Dodge, J., & Lawrence, N. D. (2022).  Modeling the Machine Learning Multiverse. NeurIPS. 
    [7] Sagawa, S., Koh, P. W., Hashimoto, T. B., & Liang, P. (2019).  Distributionally robust neural networks for group shifts: On the importance of regularization for worst-case generalization. ICLR.
supervisors:
  - samuel-bell
  - neil-d-lawrence
published: 2022-10-22
---
