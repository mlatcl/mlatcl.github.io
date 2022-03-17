---
layout: project-single
title: Data-Oriented Architectures for AI-based Systems
excerpt: Data Oriented Architecture (DOA) is an software architecture pattern
  that creates data-driven, loosely coupled, decentralised, and open systems.
  DOA achieves these goals by exposing systems' data as first class citizen to
  distributed, stateless, and asynchronous systems’ components. These design
  decisions enable DOA-based systems to achieve desirable properties such as
  data availability, reusability, and monitoring, as well as systems
  adaptability, scalability, and autonomy.
featured_image: /assets/uploads/doa.jpg
people:
  - andrei-paleyes
  - christian-cabrera-jojoa
  - eric-meissner
  - neil-lawrence
---
Across the last decade novel machine learning (ML) algorithms have been used to solve problems in computer vision, speech and language that were previously considered highly challenging. This has triggered an upsurge in interest in artificial intelligence (AI). These algorithms originated in the academic community but are now being deployed in real-world environments that differ considerably from their development domains in terms of scale, complexity, and dynamic nature. Real-world environments produce large amounts of heterogeneous, variable and high dimensional data that poses new challenges to the deployment of ML algorithms in real-world systems. These challenges are present along the whole ML algorithms workflow from data management to deployment, monitoring and redeployment of ML models. 

Data Oriented Architecture (DOA) is an emerging software architecture pattern that aims to create data-driven, loosely coupled, decentralised, and open systems. DOA proposes to achieve such goals by exposing systems' data as first class citizen to distributed, stateless, and asynchronous systems’ components. These design decisions enable DOA-based systems to achieve desirable properties such as data availability, reusability, and monitoring, as well as systems adaptability, scalability, and autonomy. Such properties have the potential to benefit the adoption and deployment of ML algorithms in real-world systems. For example, a DOA-based system can automatically store results from different treatments a data engineer applies to a data-set in the form of snapshots. An ML engineer can reuse these snapshots to select the most suitable ML model based on the available data. Similarly, the loosely coupled and asynchronous communication between system components in DOA can benefit the integration of ML algorithms into larger real-world systems. 

This project aims to materialise these benefits in the form of architectural principles, as well as software tools that support the development, testing, deployment, and evolution of real world AI-based systems. We first focus on defining the DOA principles by surveying the design decisions that current research and industrial ML deployments have adopted to address the challenges that real-world systems pose. Then, we will design, implement, and evaluate software tools that enable the creation of systems that follow each identified principle.