#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 02:24:23 2018

@author: tom
"""
    
import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt
    
    
genuine = pd.read_csv('../raw_scores/survey_score_genuine.csv')
imposter = pd.read_csv('../raw_scores/survey_score_imposter.csv')

Q1_gen = pd.read_csv('../raw_scores/question1_genuine.csv')
Q1_imp = pd.read_csv('../raw_scores/question1_imposter.csv')

Q2_gen = pd.read_csv('../raw_scores/question2_genuine.csv')
Q2_imp = pd.read_csv('../raw_scores/question2_imposter.csv')

Q3_gen = pd.read_csv('../raw_scores/question3_genuine.csv')
Q3_imp = pd.read_csv('../raw_scores/question3_imposter.csv')

Q4_gen = pd.read_csv('../raw_scores/question4_genuine.csv')
Q4_imp = pd.read_csv('../raw_scores/question4_imposter.csv')

Q5_gen = pd.read_csv('../raw_scores/question5_genuine.csv')
Q5_imp = pd.read_csv('../raw_scores/question5_imposter.csv')


genuine_scores = genuine.values
imposter_scores = imposter.values

mu_g = genuine.mean()
mu_i = imposter.mean()

sigma_g = np.std(genuine)
sigma_i = np.std(imposter)

d_prime =  (math.sqrt(2) * abs(mu_g - mu_i))/math.sqrt((sigma_g ** (2)) + (sigma_i ** (2)))

plt.figure()
plt.hist(genuine_scores, color='green', alpha = 0.5)
plt.hist(imposter_scores, color='red', alpha = 0.5)
plt.ylabel('Frequency')
plt.xlabel('Matching Score')
plt.title('Score Distribution with d\' = ' + str(round(int(d_prime), 2)))
plt.xlim([0.0, 1.0])
plt.show()

thresholds = np.linspace(0.0, 1.0,)
far = []
tpr = []
frr = []

for t in thresholds:
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    
    for g_s in genuine_scores:
        if g_s <= t:
            tp += 1
        else: 
            fn += 1
    
    for i_s in imposter_scores:
        if i_s <= t:
            fp += 1
        else:
            tn += 1
            
    far.append(fp / (fp + tn))
    tpr.append(tp / (tp + fn))
    frr.append(fn / (fn + tp))

min_distance = abs(frr[1] - far[1])       

for (i,j) in zip(frr, far):
    distance = abs(i - j)
    
    if distance < min_distance:
        min_distance = distance
        x = i
        y = j

EER = (x + y)/2
        
plt.figure()
plt.plot(far,frr,lw = 1,color = 'blue')
plt.xlabel('False Reject Rate')
plt.ylabel('False Accept Rate')
plt.title('Detection Error Tradeoff with EER = ' + str(round(EER, 3)))
plt.show()

plt.figure()
plt.plot(far, tpr, color='darkorange', lw=1)
plt.plot([0, 1], [0, 1], color='navy', lw=1, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic')
plt.legend(loc="lower right")
plt.show()
