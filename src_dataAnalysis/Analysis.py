#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 03:24:16 2018

@author: josephcox
"""

# Load the Pandas libraries with alias 'pd' 
import pandas as pd 
import matplotlib.pyplot as plt
#import numpy as np
# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
joe_app_usage = pd.read_csv("../userdevice_data/Joe_Data/App_Usage/Day1.csv")
joe_timeslots = pd.read_csv("../userdevice_data/Joe_Data/Smarter_time/timeslots.csv")
joe_geoloc =  pd.read_csv("../userdevice_data/Joe_Data/Smarter_time/geoloc.csv")

joe_frequencies = joe_timeslots['Place'].value_counts().to_dict()
print(joe_frequencies)

#joe_frequencies.plot(kind='hist')
#plt.xlabel('Joe_location')
plt.bar(joe_frequencies.keys(), joe_frequencies.values(), width=.8, align='edge', color='g')
