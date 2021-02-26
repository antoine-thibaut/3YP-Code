#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Antoine + Akshay
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = {'Bus':  ['2','2','2','2','2',
                 '2A','2A','2A','2A','2A',
                 '2B','2B','2B','2B','2B',
                 '3','3','3','3','3',
                 '3A','3A','3A','3A','3A',
                 '4','4','4','4','4',
                 '4A','4A','4A','4A','4A',
                 '4B','4B','4B','4B','4B',
                 '4C','4C','4C','4C','4C',
                 '5','5','5','5','5',
                 '6','6','6','6','6',
                 '8','8','8','8','8',
                 '9','9','9','9','9',
                 '11X','11X','11X','11X','11X',
                 '13X','13X','13X','13X','13X',
                 'U6','U6','U6','U6','U6',
                 '500','500','500','500','500'],
        'Times': ['Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)',
                  'Early (04-08)', 'Mid (08-12)','Afternoon (12-16)','Evening (16-20)','Late (20-24)'],
        'Distance': ['10.4','20.8','20.8','20.8','41.6',
                     '10','20','0','0','0',
                     '10.6','21.2','0','0','0',
                     '10.5','42','42','38.5','28',
                     '0','20','20','20','0',
                     '12.4','24.8','24.8','18.6','0',
                     '8.8','17.6','17.6','13.2','8.8',
                     '0','0','0','4.3','17.2',
                     '0','0','0','0','0',
                     '30.1','107.5','103.2','98.9','64.5',
                     '7.4','37','44.4','44.4','22.2',
                     '17.5','56','56','52.5','42',
                     '0','15.2','15.2','15.2','0',
                     '0','74.8','102','61.2','20.4',
                     '18.9','32.4','32.4','32.4','32.4',
                     '0','0','0','0','0',
                     '0','68','59.5','34','0']}

df = pd.DataFrame (data, columns = ['Bus','Times','Distance'])
df["Distance"]=df["Distance"].astype(float) #casts the distance column as floats
grouped_bus = df.groupby(df["Bus"]) # can also group by a different column eg Times !

# Individual Data Frames for each bus route
df_bus_2 = grouped_bus.get_group("2")
df_bus_2A = grouped_bus.get_group("2A")
df_bus_2B = grouped_bus.get_group("2B")
df_bus_3 = grouped_bus.get_group("3")
df_bus_3A = grouped_bus.get_group("3A")
df_bus_4 = grouped_bus.get_group("4")
df_bus_4A = grouped_bus.get_group("4A")
df_bus_4B = grouped_bus.get_group("4B")
df_bus_4C = grouped_bus.get_group("4C")
df_bus_5 = grouped_bus.get_group("5")
df_bus_6 = grouped_bus.get_group("6")
df_bus_8 = grouped_bus.get_group("8")
df_bus_9 = grouped_bus.get_group("9")
df_bus_11X = grouped_bus.get_group("11X")
df_bus_13X = grouped_bus.get_group("13X")
df_bus_U6 = grouped_bus.get_group("U6")
df_bus_500 = grouped_bus.get_group("500")

# plot for an individual bus line, change the dataframe and title for different lines
df_bus_5.plot.bar(x='Times', y='Distance', rot = 0, title='Distance travelled throught the day by bus 5', color='#ff007f')
plt.ylabel("Distance in miles")
plt.show()