---
title: Investigating  the Effect of Sequence Length  on the quality of clean speech generated
layout: project-to-supervise
status: Hidden
categories:
  - MPhil
year: 2022
overview: |-
 To effectively perform speech separation, the speech separation tools need to model long sequence dependencies that exist within the audio signal input. The initial speech separation models relied on deep neural network to estimate clean speech from a noisy one. However, feedforward DNN models are ill poised for speech data since they are unable to effectively model long dependencies across time that are present in the speech data. Due to this researchers progressively introduced recurrent neural network (RNN) which has a feedback structure such that the representations at given time step t is a function of the data at time t, the hidden state and memory at time t − 1. One such RNN that has been exploited in speech separation is long-short-term memory (LSTM). Through LSTM structures one can learn sequential prediction networks which are able to exploit use of long-term contextual information. Due to their inherently sequential nature, RNN models are unable to support parallelization of computation. This limits their use when working with large datasets with long sequences. Convectional convolution neural (CNN) has been used to design speech separation models, however they are limited in their ability to model long range dependencies due to limited receptive field. Due to the shortcomings of the CNN and RNN, dilated temporal convolution network (TCN) has been exploited to encode long-range dependencies using hierarchical convolutional layers. Speech separation models have also explored the use of transformers. Transformers are attention based that have been successful in the recent past in modeling sequences and allows uncovering of dependencies that exist within an input without regard to the distance between any two values of the input. One common thing in all these progression is that researchers have focused on designing models that are large to effectively model audio input without looking at the impact of input data size. In audio separation, a typical  model’s input is a sequence of frames, each of which is 25 seconds long.  It is possible to reduce the length of the input hence reducing the burden of modelling long sequence dependencies ? Will this  reduce the training cost of the models without  impacting on the  quality of their output? Basically by focusing on the data side of the training spectrum can we reduce the training cost without impacting on the quality of the separations generated.  The project will focus on utilizing already existing systems such as [1] and evaluating its performance on variable frame size.
 Reference
 [1]  Cem Subakan, Mirco Ravanelli, Samuele Cornell, Mirko Bronzi, and Jianyuan Zhong. Attention is all you need in speech separation. ICASSP, IEEE International Conference on Acoustics, Speech and Signal Processing - Proceedings, 2021-June:21–25, 2021. ISSN 15206149. doi:10.1109/ICASSP39728.2021.9413901. 

supervisors:
  - peter-ochieng
published: 2022-10-06
---
