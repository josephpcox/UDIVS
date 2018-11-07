#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 23:11:33 2018

@author: tom
"""
from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt

#import numpy as np
#from sklearn.feature_selection import VarianceThreshold

#def getWeek(DataFrame):

#gets day and location
def getLocation(DataFrame):
    #filters the Day and Place column only
    filtered = DataFrame[['Day', 'Place']].copy()
    
    #remove rows with Nan in any column
    df = filtered.dropna()
    return df

#gets time and activity
def getActivity(DataFrame):
    #filters the Day and Place column only
    filtered = DataFrame[['Day','Time', 'Activity']]
    
    #remove rows with Nam in any column
    df = filtered.dropna()
    
#    final = df[(df.Activity != 'walk')]
#    final = final[(final.Activity != 'lesson')]
#    final = final[(final.Activity != 'home time')]
#    final = final[(final.Activity != 'vehicle')]
#    final = final[(final.Activity != 'groceries')]
#    final = final[(final.Activity != 'sleep')]
#    final = final[(final.Activity != 'drinks')]
#    final = final[(final.Activity != 'religion')]
#    final = final[(final.Activity != 'exhibition')]
    return df

def getWeek(DataFrame):
    delta = timedelta(days=7)

#       
def getData(DataFrame, Amount):
    lastday = DataFrame.iloc[:,1]
    lastindex = len(lastday.index)
    #count = o
    #lastIndex = Activities
    
    return lastday[lastindex]


data = pd.read_csv('../../userdevice_data/Tom_Data/Smarter_time/SmarterTimeTimeslots.csv')

location = getLocation(data)

Activity = getActivity(data)

data1 = getData(Activity, 1)    

#lastday = Activity.iloc[:,1]
#lastindex = len(Activity.index)


#------------------------------#
#filter to one day
tomDay = data[data.Day == 20181023]


#get location and activity
tomDay = tomDay['Activity'].value_counts().to_dict()

from operator import itemgetter
sortedList = sorted(tomDay.items(), key=itemgetter(1), reverse = True)
#plt.bar(sortedList.keys(), sortedList.values(), width=.8, align='edge', color='g')

