#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 23:11:33 2018

@author: tom
"""
from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
from operator import itemgetter
#import numpy as np
#from sklearn.feature_selection import VarianceThreshold

#def getWeek(DataFrame):

#gets day and location
def getLocation(DataFrame):
    #filters the Day and Place column only
    filtered = DataFrame[['Day', 'Place','Time']].copy()
    
    #remove rows with Nan in any column
    df = filtered.dropna()
    return df

#gets time and activity
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

def getWeek(DataFrame):
    delta = timedelta(days=7)

#       
def getData(DataFrame, Amount):
    lastday = DataFrame.iloc[:,1]
    lastindex = len(lastday.index)
    #count = o
    #lastIndex = Activities
    
    return lastday[lastindex]

def getRecentApp():
    for x in tomDay_df['Activity'][::-1]:
        if "phone:" not in x:
            continue
        ans = x
        break
    return ans

def getRecentLocation():
    pass

def getOptions(n):
    
    options = []
    
    #question options for "which app did you use most recently
    if n == 0:
        """'Which app did you use most recently?'"""
        ans = getRecentApp()
        options.append(ans)
        count = 1
        
        #this loop gives an array of answers called options for the user to choose from
        for x in tomDay_df['Activity']:
            flag = 0
            if "phone:" in x:
                for y in options:
                    if x == y:
                        flag = 1
                if flag == 0:
                    options.append(x)
                    count = count +1
                if count == 4:
                    break
        random.shuffle(options,random.random)
        return ans,options
    
    elif n == 1:
        """'What place were you at most recently?'"""
        ans = getRecentLocation()
        options.append(ans)
        count = 1
        
        #this loop gives an array of answers called options for the user to choose from
        for x in location['Activity']:
            flag = 0
            if "phone:" in x:
                for y in options:
                    if x == y:
                        flag = 1
                if flag == 0:
                    options.append(x)
                    count = count +1
                if count == 4:
                    break
        random.shuffle(options,random.random)
        return ans,options
        pass
    elif n == 2:
        """'which place were you at around:'"""
        pass
    elif n == 3:
        """Which of these places did you go to yesterday?'"""
        pass
    


data = pd.read_csv('../../userdevice_data/Tom_Data/Smarter_time/SmarterTimeTimeslots.csv')

location = getLocation(data)

Activity = getActivity(data)




#------------------------------#
#filter to one day
tomDay_df = data[data.Day == 20181023]

#get location and activity
tomDay_dict = tomDay_df['Activity'].value_counts().to_dict()

#tom's day sorted from greatest to least
sortedTomDay = sorted(tomDay_dict.items(), key=itemgetter(1), reverse = True)

#-------------------------------------------------------------------------------------------------------------------------#
questions=['Which app did you use most recently?','What place were you at most recently?','which place were you at around:','Which of these places did you go to yesterday?']
randomNums=random.sample(range(0,3),3)
score = 0
count = 1
for n in randomNums:
    if n != 0:
        continue
    print(questions[n])
    ans,options = getOptions(n)
    print(ans)
    for o in options:
        print(count,". ",o)
        count= count+1
    userAns=int(input("input answer here: ")) # Utilize Switch CasegetOptions(n)
    if n == 0:
        if ans == options[userAns-1]:
            score = score+1
    if n == 1:
        pass
    if n == 2:
        pass
    if n == 3:
        pass

print(score)