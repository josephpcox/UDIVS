#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 31 20:31:34 2018

@author: josephcox
"""

import numpy as np
import matplotlib.pyplot as plt
import math
#genuine_scores =
#0.29,0.1,0.28,0.26,0.23,0.22,0.32,0.32,0.4,0.3,0.08,0.39,0.37,0.22,0.24,0.34,0.22,0.38,0.29,0.38
#impostor_scores =
#0.46,0.56,0.57,0.63,0.34,0.55,0.5,0.38,0.57,0.34,0.72,0.54,0.32,0.6,0.41,0.72,0.6,0.7,0.39,0.32,
#0.31,0.67,0.43,0.51,0.49,0.53,0.4,0.39,0.38,0.26,0.53,0.45,0.25,0.32,0.5,0.5,0.57,0.5,0.42,0.35,
#0.36,0.51,0.42,0.69,0.38,0.64,0.56,0.3,0.52,0.33
#• Generate the score distribution graph using 100 thresholds equally spaced from 0.0 to 1.0.
#Include the d-prime value in the title.
#• What is the FRR when the FAR is approximately (closest to) 0.05?
#• What is the FRR when the FAR is approximately 0.10?
#• What is the FRR when the FAR is approximately 0.20?
#• What is the EER?
#----------------------------------------------------------------------------
print('# system 1---------------------------------------------------')
genuine = np.array([0.29,0.1,0.28,0.26,0.23,0.22,0.32,0.32,0.4,0.3,0.08,0.39,0.37,0.22,0.24,0.34,0.22,0.38,0.29,0.38])
imposter = np.array([0.46,0.56,0.57,0.63,0.34,0.55,0.5,0.38,0.57,0.34,0.72,0.54,0.32,0.6,0.41,0.72,0.6,0.7,0.39,0.32,
0.31,0.67,0.43,0.51,0.49,0.53,0.4,0.39,0.38,0.26,0.53,0.45,0.25,0.32,0.5,0.5,0.57,0.5,0.42,0.35,0.36,0.51,0.42,0.69,0.38,0.64,0.56,0.3,0.52,0.33])

meanG = np.mean(genuine)

meanI = np.mean(imposter)

stdG =np.std(genuine)**2

stdI=np.std(imposter)**2


plt.hist(genuine, bins = 'auto',range = [0.0,1.0],density = True, alpha=0.5, color = 'g')

plt.hist(imposter, bins = 'auto',range = [0.0,1.0],density = True, alpha=0.5, color = 'r')


#caluate dPrime: 
d_prime = math.sqrt(2) * abs(meanG - meanI)
d_prime /= math.sqrt((stdG + stdI))
plt.xlim([0,1]) 
plt.title('dPrime = ' + str(d_prime))
plt.xlabel('scores')
plt.ylabel('frequency')
plt.show()
#plt.close()
# generate 200 threshold values between 0 and 1 
thresholds = np.linspace(0.0,1.0,100) 

# Generate the empty lists 
far = []
tpr = []
frr = []
fpr = []
err = []
for t in thresholds:
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for g_s in genuine:
        if g_s <= t:
            tp += 1
        else:
            fn += 1
    for i_s in imposter:
        if i_s <= t:
            fp += 1
        else:
            tn += 1

    far.append(fp/(fp + tn))
    tpr.append(tp/(tp + fn))
    frr.append(fn/(fn + tp))
    
#Calculate the EQUAL ERROR RATE
mini= abs(far[0] - frr[0])
for (r,a) in zip(frr,far):
    if abs(a-r)<mini:
        mini = abs(a - r)
        i = frr.index(r)
    

ERR = (far[i] + frr[i])/2

# set 1---------------------------------------------------
print('Err' , ERR)
count = 0
minimum = 100000
minIndex = 0
for f in far:
    count = count + 1
    if (f - 0.05)<minimum:
        minimum = f - 0.05
        minIndex = count
print('frr',frr[minIndex])

# set 2---------------------------------------------------
print('Err' , ERR)
count = 0
minimum = 100000
minIndex = 0
for f in far:
    count = count + 1
    if (f - 0.05)<minimum:
        minimum = f - 0.10
        minIndex = count
print('frr',frr[minIndex])

# set 3---------------------------------------------------
print('Err' , ERR)
count = 0
minimum = 100000
minIndex = 0
for f in far:
    count = count + 1
    if (f - 0.05)<minimum:
        minimum = f - 0.20
        minIndex = count
print('frr',frr[minIndex])

print('# system 2---------------------------------------------------')
# system 2---------------------------------------------------
#------------------------------------------------------------


genuine = np.array([0.15,0.21,0.5,0.43,0.25,0.11,0.18,0.26,0.13,0.5,0.19,0.11,0.38,0.46,0.14,0.44,0.3,0.47,0.31,0.33])
imposter = np.array([0.34,0.18,0.44,0.67,0.51,0.38,0.48,0.88,0.7,0.22,0.67,0.85,0.23,0.52,0.12,0.44,0.21,0.77,0.31, 0.73,0.38,0.55,0.26,0.67,0.88,0.14,0.32,0.15,0.69,0.29,0.77,0.81,0.38,0.55,0.25,0.76,0.15,0.18, 0.64,0.5,0.77,0.43,0.67,0.65,0.87,0.47,0.39,0.28,0.81,0.52])




meanG = np.mean(genuine)

meanI = np.mean(imposter)

stdG =np.std(genuine)**2

stdI=np.std(imposter)**2


plt.hist(genuine, bins = 'auto',range = [0.0,1.0],density = True, alpha=0.5, color = 'g')

plt.hist(imposter, bins = 'auto',range = [0.0,1.0],density = True, alpha=0.5, color = 'r')

#caluate dPrime: 
d_prime = math.sqrt(2) * abs(meanG - meanI)
d_prime /= math.sqrt((stdG + stdI))
plt.xlim([0,1]) 
plt.title('dPrime = ' + str(d_prime))
plt.xlabel('scores')
plt.ylabel('frequency')
plt.show()
# generate 200 threshold values between 0 and 1 
thresholds = np.linspace(0.0,1.0,100) 

# Generate the empty lists 
far = []
tpr = []
frr = []
fpr = []
err = []
for t in thresholds:
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for g_s in genuine:
        if g_s <= t:
            tp += 1
        else:
            fn += 1
    for i_s in imposter:
        if i_s <= t:
            fp += 1
        else:
            tn += 1

    far.append(fp/(fp + tn))
    tpr.append(tp/(tp + fn))
    frr.append(fn/(fn + tp))
    
#Calculate the EQUAL ERROR RATE
mini= abs(far[0] - frr[0])
for (r,a) in zip(frr,far):
    if abs(a-r)<mini:
        mini = abs(a - r)
        i = frr.index(r)
    

ERR = (far[i] + frr[i])/2

# set 1---------------------------------------------------
print('Err' , ERR)
count = 0
minimum = 100000
minIndex = 0
for f in far:
    count = count + 1
    if (f - 0.05)<minimum:
        minimum = f - 0.05
        minIndex = count
print('frr',frr[minIndex])

# set 2---------------------------------------------------
print('Err' , ERR)
count = 0
minimum = 100000
minIndex = 0
for f in far:
    count = count + 1
    if (f - 0.05)<minimum:
        minimum = f - 0.10
        minIndex = count
print('frr',frr[minIndex])

# set 3---------------------------------------------------
print('Err' , ERR)
count = 0
minimum = 100000
minIndex = 0
for f in far:
    count = count + 1
    if (f - 0.05)<minimum:
        minimum = f - 0.20
        minIndex = count
print('frr',frr[minIndex])

print('# system 3---------------------------------------------------')
#------------------------------------------------------------


genuine = np.array([0.45,0.47,0.33,0.33,0.39,0.46,0.45,0.44,0.48,0.35,0.49,0.43,0.43,0.41,0.41,0.33,0.41,0.32,0.42, 0.42])
imposter = np.array([0.52,0.5,0.54,0.46,0.45,0.47,0.48,0.48,0.53,0.51,0.53,0.55,0.51,0.46,0.47,0.46,0.49,0.54,0.52, 0.51,0.49,0.5,0.53,0.54,0.54,0.51,0.46,0.51,0.48,0.47,0.51,0.52,0.51,0.52,0.46,0.54,0.48,0.46, 0.53,0.45,0.48,0.48,0.5,0.46,0.46,0.49,0.53,0.54,0.53,0.47])




meanG = np.mean(genuine)

meanI = np.mean(imposter)

stdG =np.std(genuine)**2

stdI=np.std(imposter)**2


plt.hist(genuine, bins = 'auto',range = [0.0,1.0],density = True, alpha=0.5, color = 'g')

plt.hist(imposter, bins = 'auto',range = [0.0,1.0],density = True, alpha=0.5, color = 'r')

#caluate dPrime: 
d_prime = math.sqrt(2) * abs(meanG - meanI)
d_prime /= math.sqrt((stdG + stdI))
plt.xlim([0,1]) 
plt.title('dPrime = ' + str(d_prime))
plt.xlabel('scores')
plt.ylabel('frequency')
plt.show()
# generate 200 threshold values between 0 and 1 
thresholds = np.linspace(0.0,1.0,100) 

# Generate the empty lists 
far = []
tpr = []
frr = []
fpr = []
err = []
for t in thresholds:
    tp = 0
    tn = 0
    fp = 0
    fn = 0
    for g_s in genuine:
        if g_s <= t:
            tp += 1
        else:
            fn += 1
    for i_s in imposter:
        if i_s <= t:
            fp += 1
        else:
            tn += 1

    far.append(fp/(fp + tn))
    tpr.append(tp/(tp + fn))
    frr.append(fn/(fn + tp))
    
#Calculate the EQUAL ERROR RATE
mini= abs(far[0] - frr[0])
for (r,a) in zip(frr,far):
    if abs(a-r)<mini:
        mini = abs(a - r)
        i = frr.index(r)
    

ERR = (far[i] + frr[i])/2

# set 1---------------------------------------------------
print('Err' , ERR)
count = 0
minimum = 100000
minIndex = 0
for f in far:
    count = count + 1
    if (f - 0.05)<minimum:
        minimum = f - 0.05
        minIndex = count
print('frr',frr[minIndex])

# set 2---------------------------------------------------
print('Err' , ERR)
count = 0
minimum = 100000
minIndex = 0
for f in far:
    count = count + 1
    if (f - 0.05)<minimum:
        minimum = f - 0.10
        minIndex = count
print('frr',frr[minIndex])

# set 3---------------------------------------------------
print('Err' , ERR)
count = 0
minimum = 100000
minIndex = 0
for f in far:
    count = count + 1
    if (f - 0.05)<minimum:
        minimum = f - 0.20
        minIndex = count
print('frr',frr[minIndex])
