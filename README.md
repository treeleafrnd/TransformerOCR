# Transformer_OCR   
TrOCR to train and predict scanned text documents.

A TrOCR consists of encoder and a decoder where a encoder uses a pretrained model such as Vision image Transformer (ViT), BERT image Transformer (BEiT), and Dual Intent and Entity Transformer (DiET) and decoder uses a pretrained models such as BERT, and RoBERTa. 
This model can be trained in printed, handwritten or scene text dataset. An self attention model is required to overcome vanishing problem in LSTM. An attention model simply predicts the next word in a sequence, thus making OCR more accurate. The model is trained and fine tuned in IAM handwriting dataset.  
This is an implementation of Transformer OCR in order to train handwritten documents for english and nepali text documents. The repository simply consists of a google colaboratory notebook for training and python files which can be used to integrate with larger industrial projects.

For training and implementation entire credit goes to https://github.com/rsommerfeld/trocr.git 

# Results:

Before training:

![before t](https://user-images.githubusercontent.com/99968233/220820434-c52e1dec-802f-4e37-a0d6-d6d60b6d9c10.png)

After training:

![after t](https://user-images.githubusercontent.com/99968233/220820428-f61f0e60-f2a9-4d3e-8687-8d8303a681c5.png)

# Architecture: 

![architecture](https://user-images.githubusercontent.com/99968233/220820315-0643d0f0-6d26-4b62-a15b-7f9d9233a56a.jpg)

# Implementation: 
Reducing the Batch size to 5. GPU Ram utilization is 9.2 GB. Training continues smoothly.
Training is done in 10,000 images and validation in 3000 images.
Since the batch size is 5 and training samples are 10,000, in order to complete the first epoch it requires ~ 10000/5 = 2000 iterations, followed by prediction of ~ 3000/5 = 600 batches. 

![epoch8](https://user-images.githubusercontent.com/99968233/220820238-c99a44bf-d423-4f11-aea8-8c2f82148095.png)

Clearly more epoches are needed to improve accuracy rate.

# 1.Setup:
  Clone this repository
  Inside Clone https://github.com/rsommerfeld/trocr.git
  
    1.1 Install Dependencies:
      conda env create -n trocr --file environment.yml (use environment-cpu.yml for CPU only)
      conda activate trocr

# 2. Using the repository:
  
    2.1 For integration:
      use trocr.py
    2.2 For training:
      open trocr_google_colab.ipynb in google colab
      
# 3. Data
   1. Models can be found in https://huggingface.co/microsoft/trocr-base-handwritten
   2. Dataset can be found in https://www.kaggle.com/code/samfc10/handwriting-recognition-using-crnn-in-keras/notebook
