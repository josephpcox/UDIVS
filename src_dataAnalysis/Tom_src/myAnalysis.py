#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 23:11:33 2018

@author: tom
"""
import pandas as pd
import matplotlib.pyplot as plt
import random
import numpy as np
from operator import itemgetter
from datetime import datetime,timedelta

#import numpy as np
#from sklearn.feature_selection import VarianceThreshold

#def getWeek(DataFrame):

#gets day and location-------------------------------------------------------------------------------#
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
    #get data of one day
    #last_index = len(DataFrame) - 1
    #day = DataFrame.loc[last_index, 'Day']
    df = DataFrame[DataFrame.Day == day]
    df = getLocation(df)
    
    return df

#get all data from yesterday
#   uses datetime library to grab the all data from yesterday
#   returns all the location from yesterday as a dataframe  
def getYesterdayLoc(DataFrame):
    
    day = int(datetime.strftime(datetime.now() - timedelta(1), '%Y%m%d'))
    df = DataFrame[DataFrame.Day == day]
    df = getLocation(df)
    return df

# steps------------------------------------------------------------------------------------------------# 
# 1 creates a list of all the places visited in yesterday in placesVistedList
# 2 make an empty list that stores incorrect locations called inCorrect_loc
# iterate untill you have a list of 3
# 2 grab a random place from the data set, check it against the placesvisitedList
# if the random place does not exitst inside the place visted list 
#   append it to the inCorrect_loc list:
# else:
# continue 
def checkLocList(DataFrame):
    
    df = getYesterdayLoc(DataFrame)
    df = df.drop_duplicates(subset = 'Place', keep = 'first')
    df = df['Place']
    return df

#this returns the time of place in the format HH:MM AM/PM----------------------------------------------#
def getHourTime(DataFrame):
    
    date_time = DataFrame['Time'].iloc[0]
    time = datetime.strptime(date_time, '%a %b %d %H:%M:%S %Z %Y')
    hour_time = time.strftime('%I:%M %p')
    return hour_time

# This grabs location --------------------------------------------------------------------------------- #   
def getData(DataFrame, Amount):
    lastday = DataFrame.iloc[:,1]
    lastindex = len(lastday.index)
    #count = o
    #lastIndex = Activities
    return lastday[lastindex]

# -----------------------------------------------------------------------------------------------------#
def getRecentApp():
    for x in tomDay_df['Activity'][::-1]:
        if "phone:" not in x:
            continue
        ans = x
        break
    return ans

#-------------------------------------------------------------------------------------------------------#
# get the first location that is not the current location, generate incorrect answeres 
def getRecentLocation():
    pass

# Produces the options for the UDIVS---------------------------------------------------------------------#
def getOptions(n):
    
    options = []
    
    #question options for "which app did you use most recently
    if n == 0:
        """'Which app did you use most recently?'"""
        ans = getRecentApp()
        options.append(ans)
        count = 1
        print('Which app did you use most recently?\n')
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
        
        print('What place were you at most recently?\n')
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

    elif n == 2:
        """'which place were you at around:'"""
        
        time_loc = getTodayLoc(data)
        ans_data = time_loc.sample(n=1)
        ans = ans_data['Place'].iloc[0]
        options.append(ans)
        
        print('which place were you at around', getHourTime(ans_data), 'today\n')
        dummy_data = getLocation(data)
        count = 1
        
        while count < 4:
            random_day = dummy_data.sample(n=1)
            place = random_day['Place'].iloc[0]
            flag = 0
            for y in options:
                if y == place:
                    flag = 1
            if flag == 1:
                pass
            else:
                options.append(place)
                count = count + 1
        random.shuffle(options,random.random)
        return ans,options

    elif n == 3:
        """Which of these places did you go to yesterday?'"""
        time_loc = getYesterdayLoc(data)
        ans_data = time_loc.sample(n = 1)
        ans = ans_data['Place'].iloc[0]
        options.append(ans)
        placesVisited = checkLocList(data)
        
        print('Which of these places did you go to yesterday?\n')
        dummy_data = getLocation(data)
        count = 1
        while count < 4:
            random_day = dummy_data.sample(n=1)
            place = random_day['Place'].iloc[0]
            flag = 0
            for z in placesVisited:
                if z == place:
                    flag = 1
            for y in options:
                if y == place:
                    flag = 1
            if flag == 1:
                pass
            else:
                options.append(place)
                count = count + 1
        random.shuffle(options,random.random)
        return ans,options
        
        

data = pd.read_csv('../../userdevice_data/Tom_Data/Smarter_time/SmarterTimeTimeslots.csv')

#-----Week-and-Day-of-data-------------------------#
#get a weeks worth of data
#week = data.query('20181016 <= Day <= 20181023')

#new version of filter to one day without hardcoding
last_index = len(data) - 1
day = data.loc[last_index, 'Day']
tomDay_df = data[data.Day == day]

#------------------------------#
#get location
# week_loc = week[['Time', 'Place']]
# 4sorted_week =  week_loc[['Time', 'Place']].to_dict()

#------------------------------------------------------------#
#get the frequency of apps used for one day
tomDay_dict = tomDay_df['Activity'].value_counts().to_dict()

#tom's day sorted from greatest to least
sortedTomDay = sorted(tomDay_dict.items(), key=itemgetter(1), reverse = True)

#-------------------------------------------------------------------------------------------------------------------------#
questions=['Which app did you use most recently?','What place were you at most recently?','which place were you at around ','Which of these places did you go to yesterday?', 'How long were you on this app?']
randomNums=random.sample(range(0,4),3)
print(randomNums)
score = 0
count = 1
for n in randomNums:
    if n == 1:
        continue
    ans,options = getOptions(n)
    #print(ans)
    for o in options:
        print(count,". ",o)
        count = count+1
    userAns=int(input("input answer here: ")) # Utilize Switch CasegetOptions(n)
    if ans == options[userAns-1]:
            score = score+1
    count = 1
    #print(score)