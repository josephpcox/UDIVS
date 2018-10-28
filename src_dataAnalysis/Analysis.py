#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 03:24:16 2018

@author: josephcox
"""

#Load the Pandas libraries with alias 'pd' 
import pandas as pd 

#Function to clean dataset with frequencies lower than threshold
def removekeys(d, freq_thresh):
    cleanse = dict(d)
    for key in list(cleanse.keys()):
        if cleanse.get(key) < freq_thresh:
            cleanse.pop(key)
    return cleanse


# Read data from file 'filename.csv' 
# (in the same directory that your python process is based)
# Control delimiters, rows, column names with read_csv (see later) 
joe_app_usage = pd.read_csv("../userdevice_data/Joe_Data/App_Usage/Day1.csv")
joe_timeslots = pd.read_csv("../userdevice_data/Joe_Data/Smarter_time/timeslots.csv")
#joe_geoloc =  pd.read_csv("../userdevice_data/Joe_Data/Smarter_time/geoloc.csv")

#tom_app_usage = pd.read_csv("../userdevice_data/Tom_Data/App_Usage/Day1.csv")
tom_timeslots = pd.read_csv("../userdevice_data/Tom_Data/Smarter_time/SmarterTimeTimeslots.csv")
#tom_geoloc =  pd.read_csv("../userdevice_data/Tom_Data/Smarter_time/SmarterTimegeolocation.csv")


#get frequencies of categories 'Place' and 'Activity" data and clean
joe_loc_frequencies = joe_timeslots['Place'].value_counts().to_dict()
print(joe_loc_frequencies)
joe_loc_frequencies = removekeys(joe_loc_frequencies, 15)

joe_act_frequencies = joe_timeslots['Activity'].value_counts().to_dict()
print(joe_act_frequencies)
clense_joe_act_frequencies = removekeys(joe_act_frequencies, 15)

tom_loc_frequencies = tom_timeslots['Place'].value_counts().to_dict()
print(tom_loc_frequencies)
clense_tom_loc_frequencies = removekeys(tom_loc_frequencies, 15)

tom_act_frequencies = tom_timeslots['Activity'].value_counts().to_dict()
print(tom_act_frequencies)
cleanse_tom_act_frequencies = removekeys(tom_act_frequencies, 15)


#plt.bar(joe_frequencies.keys(), joe_frequencies.values(), width=.8, align='edge', color='g')







#---------------------------------------------------------------------
