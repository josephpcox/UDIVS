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
    
def dprime(mean_gen, mean_imp, std_gen, std_imp):
    
    x = np.sqrt(2) * abs(mean_gen - mean_imp)
    y = np.sqrt((std_gen**2) + (std_imp**2))
    return x / y

def plot_questions(Q_scores, title):
    
    plt.figure()
    zeros = []
    ones = []
    for x in Q_scores:
        if x == 0:
            zeros.append(0)
        else:
            ones.append(1)
    plt.hist(zeros, color='red', lw=2, histtype='step', hatch='//', label='Negatives', range = (0,1), bins = 2)
    plt.hist(ones, color='green', lw=2, histtype='step', hatch='\\', label='Positives', range = (0,1), bins = 2)
    plt.legend(loc='best')
    #dp = dprime(gen_scores, imp_scores)
    plt.title(title)
    plt.show()
    return
 

def plot_scoreDist(gen_scores, imp_scores, dp):
    
    plt.figure()
    plt.hist(gen_scores, color='green', lw=2, histtype='step', hatch='//', label='Genuine Scores', range = (0,4), bins = 4)
    plt.hist(imp_scores, color='red', lw=2, histtype='step', hatch='\\', label='Impostor Scores', range = (0,4), bins = 4)
    plt.legend(loc='best')
    #dp = dprime(gen_scores, imp_scores)
    plt.title('Score Distribution (d-prime= %.10f)' %  dp)
    plt.show()
    return
    
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

Q6_gen = pd.read_csv('../raw_scores/question6_genuine.csv')
Q6_imp = pd.read_csv('../raw_scores/question6_imposter.csv')


q = Q1_gen.values
plot_questions(q[:,0], "Question 1 Genuine Scores")
q = Q1_imp.values
plot_questions(q[:,0], "Question 1 Imposter Scores")

q = Q2_gen.values
plot_questions(q[:,0], "Question 2 Genuine Scores")
q = Q2_imp.values
plot_questions(q[:,0], "Question 2 Imposter Scores")

q = Q3_gen.values
plot_questions(q[:,0], "Question 3 Genuine Scores")
q = Q3_imp.values
plot_questions(q[:,0], "Question 3 Imposter Scores")

q = Q4_gen.values
plot_questions(q[:,0], "Question 4 Genuine Scores")
q = Q4_imp.values
plot_questions(q[:,0], "Question 4 Imposter Scores")

q = Q5_gen.values
plot_questions(q[:,0], "Question 5 Genuine Scores")
q = Q5_imp.values
plot_questions(q[:,0], "Question 5 Imposter Scores")

q = Q6_gen.values
plot_questions(q[:,0], "Question 6 Genuine Scores")
q = Q6_imp.values
plot_questions(q[:,0], "Question 6 Imposter Scores")

#scores = genuine[0]
genuine_scores = genuine.values
imposter_scores = imposter.values
genuine_scores = genuine_scores[:,0]
imposter_scores = imposter_scores[:,0]
print(genuine_scores)
print('NEXT IS IMPOSTER')
print(imposter_scores)

mu_g = genuine.mean()
mu_i = imposter.mean()

sigma_g = np.std(genuine)
sigma_i = np.std(imposter)

dp = dprime(mean_gen = mu_g,mean_imp=mu_i,std_gen=sigma_g,std_imp=sigma_i)

plot_scoreDist(genuine_scores, imposter_scores, dp)

#d_prime =  (math.sqrt(2) * abs(mu_g - mu_i))/math.sqrt((sigma_g ** (2)) + (sigma_i ** (2)))
#
#plt.figure()
#plt.hist(genuine_scores, color='green', alpha = 0.5)
#plt.hist(imposter_scores, color='red', alpha = 0.5)
#plt.ylabel('Frequency')
#plt.xlabel('Matching Score')
#plt.title('Score Distribution with d\' = ' + str(round(int(d_prime), 2)))
#plt.xlim([0.0, 1.0])
#plt.show()
#
#thresholds = np.linspace(0.0, 1.0, 7)
#far = []
#tpr = []
#frr = []
#
#for t in thresholds:
#    tp = 0
#    tn = 0
#    fp = 0
#    fn = 0
#    
#    for g_s in genuine_scores:
#        if g_s <= t:
#            tp += 1
#        else: 
#            fn += 1
#    
#    for i_s in imposter_scores:
#        if i_s <= t:
#            fp += 1
#        else:
#            tn += 1
#            
#    far.append(fp / (fp + tn))
#    tpr.append(tp / (tp + fn))
#    frr.append(fn / (fn + tp))
#
#min_distance = abs(frr[1] - far[1])       
#
#for (i,j) in zip(frr, far):
#    distance = abs(i - j)
#    
#    if distance < min_distance:
#        min_distance = distance
#        x = i
#        y = j
#
#EER = (x + y)/2
#        
#plt.figure()
#plt.plot(far,frr,lw = 1,color = 'blue')
#plt.xlabel('False Reject Rate')
#plt.ylabel('False Accept Rate')
#plt.title('Detection Error Tradeoff with EER = ' + str(round(EER, 3)))
#plt.show()
#
#plt.figure()
#plt.plot(far, tpr, color='darkorange', lw=1)
#plt.plot([0, 1], [0, 1], color='navy', lw=1, linestyle='--')
#plt.xlim([0.0, 1.0])
#plt.ylim([0.0, 1.05])
#plt.xlabel('False Positive Rate')
#plt.ylabel('True Positive Rate')
#plt.title('Receiver Operating Characteristic')
#plt.legend(loc="lower right")
#plt.show()
