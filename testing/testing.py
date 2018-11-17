#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 16 00:30:17 2018

@author: tom
"""
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
from operator import itemgetter
from datetime import datetime,timedelta

def getLocation(DataFrame):
    #filters the Day and Place column only
    filtered = DataFrame[['Place','Time']].copy()
    
    #remove rows with Nan in any column
    #filtered = filtered[(filtered.Place != 'home')]
    df = filtered.dropna()
    return df

def getYesterdayLoc(DataFrame):
    
    day = int(datetime.strftime(datetime.now() - timedelta(2), '%Y%m%d'))
    df = DataFrame[DataFrame.Day == day]
    df = getLocation(df)
    return df

def checkLocList(DataFrame):
    
    df = getYesterdayLoc(DataFrame)
    df = df.drop_duplicates(subset = 'Place', keep = 'first')
    df = df['Place']
    return df
    
data = pd.read_csv('biometric/userdevice_data/Tom_Data/Smarter_time/SmarterTimeTimeslots.csv')

placesVisitedList = checkLocList(data)