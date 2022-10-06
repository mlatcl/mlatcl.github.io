---
title: Cross-modal alignment  model for  audio to sentence.
layout: project-to-supervise
status: Available
categories:
  - MPhil
year: 2022
overview: |-
 Establishing vector representations of input features  has been crucial to the success of machine learning especially natural language processing. The vector representations( embeddings) are always exploited in downstream tasks such as machine translation where the intuition is that words appearing in similar context  should generate similar word embeddings hence should be aligned. The idea of similar words generating similar representation has been extended to cross-lingual alignment. It has been exploited to perform machine translation between two different languages without any annotated dataset linking these languages. This is due to the discovery that similar words from different languages  share similar structures in a continuous  word embedding space. This eliminates the need for a large parallel training corpus to train machine translation systems. work in [1] extends this  concept to perform cross-modal alignment between  text and  audio   where audio segments are aligned to words with similar embeddings in a joint continuous embedding space. This is helpful to generate audio transcription without any transcribed dataset to train the transcription model. For low resource languages this is crucial.  Despite the remarkable results were reported in [1] and  while the word based  generation from audio may appear natural for speech, it is still not clear how to chunk speech audio in a lengths that correctly generates words. Also the word based generation of textfrom audio may be slow for downstream applications. This project proposes an audio to sentence generation as opposed to existing  audio to word generation. Can we develop a  model where a  whole sentence is generated at once based on a given chunk of  speech. Basically can cross-modal alignment be developed where an audio chunk and a  sentence share a continuous embedding space.  Will this speed up transcription of a recorded speech ?  will the long dependencies within the sentence level audio chunks affect the quality of transcription. How can we effectively identify sentences boundaries  with a given audio ?. In this project, we will utilize the dataset  and model proposed in [1] and extend it to handle sentence level text generation.
 reference
 [1]Chung, Yu-An, et al. "Unsupervised cross-modal alignment of speech and text embedding spaces." Advances in neural information processing systems 31 (2018).
supervisors:
  - peter-ochieng
published: 2022-10-06
---


