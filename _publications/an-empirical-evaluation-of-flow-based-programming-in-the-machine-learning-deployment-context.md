---
layout: publication-single
title: An Empirical Evaluation of Flow Based Programming in the Machine Learning
  Deployment Context.
author: Paleyes, A., Cabrera, C. and Lawrence, N.D. (2022)
references: " 1st International Conference on AI Engineering – Software
  Engineering for AI (2022)"
---
Despite huge successes reported by the field of machine learning, such as speech assistants or self-driving cars, businesses still observe very high failure rate when it comes to deployment of ML in production. We argue that part of the reason is infrastructure that was not designed for activities around data collection and analysis. We propose to consider flow-based programming with data streams as an alternative to commonly used service-oriented architectures for building software applications. To compare flow-based programming with the widespread service-oriented approach, we develop a data processing application, and formulate two subsequent ML-related tasks that constitute a complete cycle of ML deployment while allowing us to assess characteristics of each programming paradigm in the ML context. Employing both code metrics and empirical observations, we show that when it comes to ML deployment each paradigm has certain advantages and drawbacks. Our main conclusion is that while FBP shows great potential for providing infrastructural benefits for deployment of machine learning, it requires a lot of boilerplate code to define and manipulate the dataflow graph. We believe that with better developer tools in place this problem can be alleviated, establishing FBP as a strong alternative to currently prevalent SOA-driven software design approach. Additionally, we provide an insight into the trend of prioritising model development over data quality management.

For code associated with this project, please visit: <https://github.com/mlatcl/fbp-vs-soa>