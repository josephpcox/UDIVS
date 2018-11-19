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


data = pd.read_csv('../../userdevice_data/Tom_Data/Smarter_time/SmarterTimeTimeslots.csv')

day = int(datetime.strftime(datetime.now(), '%Y%m%d'))