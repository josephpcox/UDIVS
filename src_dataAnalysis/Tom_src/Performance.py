#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 02:24:23 2018

@author: tom
"""
    
import numpy as np
import pandas as pd
    
    
genuine_scores = pd.read_csv('../raw_scores/survey_score_genuine.csv')
imposter_scores = pd.read_csv('../raw_scores/survey_score_imposter.csv')

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


genuine = genuine_scores.values
imposter = imposter_scores.values

mean_g = genuine.mean()
mean_i = imposter.mean()

sigma_g = np.std(genuine)
sigma_i = np.std(imposter)

d_prime =  (math.sqrt(2) * abs(mu_g - mu_i))/math.sqrt((sigma_g ** (2)) + (sigma_i ** (2)))