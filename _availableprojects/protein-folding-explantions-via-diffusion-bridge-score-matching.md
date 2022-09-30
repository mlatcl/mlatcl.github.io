---
layout: project-to-supervise
title: Protein Folding Explantions via Diffusion Bridge Score Matching
status: Completed
categories:
  - MPhil
  - prtiii
overview: >-
  **Technical Title:** Sampling Transition Paths Between Molecular Conformations
  Using Diffusion Bridges and Score Matching.


  R﻿ecent advances in Schrodinger Bridges \[1,2] have enabled to learn stochastic mappings between 2 probability distributions (p(x) and q(x)) such that the stochastic map (which is modelled by a diffusion / SDE) is regularised by some prior process (wether it be computational or physical).


  T﻿his project seeks to explore these methodologies in particular the simpler case studied in \[3] where both the source and the target distributions are modeled as point masses (dirac delta functions / measures). We seek to apply the approach in \[3] to sampling physically meaningful transition paths between two protein configurations as done in \[4]. Ideally we would aim to start working with simple/toy proteins and then move on to larger scale tasks where one of the protein configuraitions is a flat amino-acid and proteins produced by alpha fold, the end product would be to generate a video which gives a physicallly plausible folding process for alphafold \[5] predictions.


  A﻿n example Time-line of the project could be:\

  1﻿. Get the codebase of \[4] working and reproduce results on simple proteins.\

  2﻿. Extend the work in \[3] to the underdampened version. (Francisco can help with this)\

  3﻿. Apply the extensions and adaptions of \[3] to work on the simple proteins of \[4] and compare to \[4].\

  4﻿. Consider ehnahncements / exentsions, would a full schrodinger bridge work better here ? \

  5﻿. If time allowing , pick some of the most recently exciting discoveries from alphafold \[5] that have a known potential and try and see if we can get it working.\

  \

  5. is an "if time allows" type of objective and I predict most the time will be spent in 3. , succesful completion of 3 could lead to a publication at a top venue whilst 4. could have a broader impact on on the field. \

  \

  I﻿deally a good background in the following could be very helpful for this project:\

  1﻿. Timeseries models (Kalman filters, AR processes, Gaussian processes)\

  2﻿. Introductory calculus (ODEs , Basic PDEs , limits)\

  3. Probability Theory (Limit Theorems, Change of Variables, basic concentration inequalities e.g. Markov/Chebychev)\

  4﻿. Variational Inference (MFVI, Amortised VI, Deep hierarchical latent variable models)\

  \

  \

  \[﻿1] https://arxiv.org/pdf/2106.01357.pdf \

  \[﻿2] https://arxiv.org/pdf/2106.02081.pdf\

  \[﻿3] https://arxiv.org/pdf/2207.02149.pdf\

  \[﻿4] https://arxiv.org/pdf/2111.07243.pdf\

  \[﻿5] https://alphafold.ebi.ac.uk/
supervisors:
  - neil-d-lawrence
  - francisco-vargas
  - pierre-thodoroff
published: 2022-09-30
student_learn: >-
  1﻿. Diffusion Models (Theory and Practice)\

  2﻿. Advanced Probability (Basics of Ito Calculus and Stochastic Differential Equations)\

  3﻿. Physical Inductive Biases for Deep Learning
project_objective: T﻿o apply Diffusion Bridges for the task of generating
  protein folding videos (transition paths).
project_bigger_picture: T﻿his could be used to generate video explanations for Alpha Folds predictions.
---
