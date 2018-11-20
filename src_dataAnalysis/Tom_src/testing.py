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

#-----Week-and-Day-of-data-------------------------#
#get a weeks worth of data
#week = data.query('20181016 <= Day <= 20181023')

#new version of filter to one day without hardcoding
#last_index = len(data) - 1
#day = data.loc[last_index, 'Day']
#tomDay_df = data[data.Day == day]

#------------------------------#
#get location
# week_loc = week[['Time', 'Place']]
# 4sorted_week =  week_loc[['Time', 'Place']].to_dict()

#------------------------------------------------------------#
#get the frequency of apps used for one day
#tomDay_dict = tomDay_df['Activity'].value_counts().to_dict()

#tom's day sorted from greatest to least

#sortedTomDay = sorted(tomDay_dict.items(), key=itemgetter(1), reverse = True)
#def getLocation(DataFrame):
#    #filters the Day and Place column only
#    filtered = DataFrame[['Place','Time']].copy()
#    
#    #remove rows with Nan in any column
#    df = filtered.dropna()
#    return df
#
##gets time and activity------------------------------------------------------------------------------#
#def getActivity(DataFrame):
#    #filters the Day and Place column only
#    filtered = DataFrame[['Day','Time', 'Activity']]
#    
#    #remove rows with Nam in any column
#    df = filtered.dropna()
#    
#    final = df[(df.Activity != 'walk')]
#    final = final[(final.Activity != 'lesson')]
#    final = final[(final.Activity != 'home time')]
#    final = final[(final.Activity != 'vehicle')]
#    final = final[(final.Activity != 'groceries')]
#    final = final[(final.Activity != 'sleep')]
#    final = final[(final.Activity != 'drinks')]
#    final = final[(final.Activity != 'religion')]
#    final = final[(final.Activity != 'exhibition')]
#    return df
#
##this returns a dataframe of location data for one day-------------------------------------------------#
##   grabs the last index in the file (indicating today's date)
##   use index to return all the locations from today as Dataframe
#def getTodayLoc(DataFrame):
#    
#    day = int(datetime.strftime(datetime.now(), '%Y%m%d'))
#    df = DataFrame[DataFrame.Day == day]
#    df = getLocation(df)
#    
#    return df
#
#data = pd.read_csv('../../userdevice_data/Tom_Data/Smarter_time/SmarterTimeTimeslots.csv')

import csv   
fields = ['1']

with open(r'Q1Genuine.csv', 'a') as f:
    writer = csv.writer(f)
    writer.write(1)


