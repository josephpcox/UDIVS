#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 13:53:54 2018

@author: tom
"""

import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
from operator import itemgetter
from datetime import datetime,timedelta
import math

def getLocation(DataFrame):
    #filters the Day and Place column only
    filtered = DataFrame[['Place','Time']].copy()
    
    #remove rows with Nan in any column
    df = filtered.dropna()
    return df

#gets time and activity------------------------------------------------------------------------------#
def getActivity(DataFrame):
    #filters the Day and Place column only
    filtered = DataFrame[['Day','Time', 'Activity']]
    
    #remove rows with Nam in any column
    df = filtered.dropna()
    
    final = df[(df.Activity != 'walk')]
    final = final[(final.Activity != 'lesson')]
    final = final[(final.Activity != 'home time')]
    final = final[(final.Activity != 'vehicle')]
    final = final[(final.Activity != 'groceries')]
    final = final[(final.Activity != 'sleep')]
    final = final[(final.Activity != 'drinks')]
    final = final[(final.Activity != 'religion')]
    final = final[(final.Activity != 'exhibition')]
    return df

#this returns a dataframe of location data for one day-------------------------------------------------#
#   grabs the last index in the file (indicating today's date)
#   use index to return all the locations from today as Dataframe
def getTodayLoc(DataFrame):
    
    day = int(datetime.strftime(datetime.now(), '%Y%m%d'))
    df = DataFrame[DataFrame.Day == day]
    df = getLocation(df)
    
    return df

data = pd.read_csv('../../userdevice_data/Tom_Data/Smarter_time/SmarterTimeTimeslots.csv')

day = int(datetime.strftime(datetime.now()- timedelta(2), '%Y%m%d'))
df = data[data.Day == day]
df = df[['Time', 'Activity', 'Duration ms']].copy()
df = df.dropna()
df = df[df['Activity'].str.contains("phone:")]
group = df.groupby('Activity').sum()
activity = group.sample(n=1)
app = activity.index[0]
miliseconds = int(activity['Duration ms'])
minutes = (miliseconds/(1000*60))
minutes = math.floor(minutes)

if minutes <= 10:
    ans = '0-10'
elif minutes <= 20:
    ans = '11-20'
elif minutes <= 30:
    ans = '21-30'
else: 
    ans = '+30'
