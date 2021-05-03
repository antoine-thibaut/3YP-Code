#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  2 17:21:20 2021

@author: Antoine
"""

# Note: This code borrows some code and structuring which was used by Akshay Pal in route modelling

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
non_refrigerated_time = 11                 # Time to refuel a single bus for non-refrigerated system [mintues] (derived from H2Bus)
refrigerated_time = 6                      # Time taken to refuel a single bus for refrigerated system [minutes] (derived from H2Bus)
bus_number = 148                           # Total number of buses to refuel (from Oxford bus company fleet list)

data = {'Number of hydrogen dispensers':  ['1','2','3','4','5','6',
                                           '1','2','3','4','5','6'],
        'System': ['non-refrigerated','non-refrigerated','non-refrigerated','non-refrigerated','non-refrigerated','non-refrigerated',
                   'refrigerated','refrigerated','refrigerated','refrigerated','refrigerated','refrigerated'],
        'Total refuelling time': [bus_number*non_refrigerated_time,bus_number*non_refrigerated_time/2,bus_number*non_refrigerated_time/3,bus_number*non_refrigerated_time/4,bus_number*non_refrigerated_time/5,bus_number*non_refrigerated_time/6,
                                  bus_number*refrigerated_time,bus_number*refrigerated_time/2,bus_number*refrigerated_time/3,bus_number*refrigerated_time/4,bus_number*refrigerated_time/5,bus_number*refrigerated_time/6]}

df = pd.DataFrame (data, columns = ['Number of hydrogen dispensers','System','Total refuelling time'])

print(df)

df["Number of hydrogen dispensers"]=df["Number of hydrogen dispensers"].astype(float) # Setting number of hydrogen dispensers as a float
df["Total refuelling time"]=df["Total refuelling time"].astype(float) # Setting total refuelling time as a float
grouped_system = df.groupby(df["System"])

# Individual Data Frames for each staff hour:
df_non_refrigerated = grouped_system.get_group("non-refrigerated")
df_refrigerated = grouped_system.get_group("refrigerated")


# Plotting:
# data to plot
n_groups = 6

non_refrigerated = (df_non_refrigerated.iloc[0][2],df_non_refrigerated.iloc[1][2],df_non_refrigerated.iloc[2][2],df_non_refrigerated.iloc[3][2],df_non_refrigerated.iloc[4][2],df_non_refrigerated.iloc[5][2])
refrigerated = (df_refrigerated.iloc[0][2],df_refrigerated.iloc[1][2],df_refrigerated.iloc[2][2],df_refrigerated.iloc[3][2],df_refrigerated.iloc[4][2],df_refrigerated.iloc[5][2])



# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.4
opacity = 0.8

rects1 = plt.bar(index-bar_width/2, non_refrigerated, bar_width,
alpha=opacity,
color='#800000',
label='non-refrigerated')

rects2 = plt.bar(index+bar_width/2, refrigerated, bar_width,
alpha=opacity,
color='#3776ab',
label='refrigerated')

plt.xlabel('Number of hydrogen dispensers')
plt.ylabel('Time taken to refuel 148 buses [hours]')
plt.plot([-1,0,1,2,3,4,5,6],[480,480,480,480,480,480,480,480],color = 'r')
plt.xticks(index, ('1', '2','3','4','5','6'))
plt.xlim([-1,6])
plt.yticks((120,240,360,480,600,720,840,960,1080,1200,1320,1440,1560,1680), ('2','4','6','8','10','12','14','16','18','20','22','24','26','28'))
plt.legend()
plt.tight_layout()
plt.savefig('refrigeration_model.svg', format='svg', dpi=1200,bbox_inches = "tight")

plt.show()