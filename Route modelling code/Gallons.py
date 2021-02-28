#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:13:38 2020

@author: Antoine
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:13:20 2020
@author: Antoine + Akshay
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# generic mpg ratings:
hybrid = 7
diesel = 5.3

# specific mpg ratings:
bus_2_mpg = diesel
bus_2A_mpg = diesel
bus_2B_mpg = diesel
bus_3_mpg = 9
bus_3A_mpg = 9
bus_4_mpg = diesel
bus_4A_mpg = diesel
bus_4B_mpg = diesel
bus_4C_mpg = diesel
bus_5_mpg = 9
bus_6_mpg = diesel
bus_8_mpg = 9
bus_9_mpg = 9
bus_11X_mpg = diesel
bus_13X_mpg = diesel
bus_U6_mpg = hybrid
bus_500_mpg = 9

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
        'Distance': ['20','30','30','30','40',
                     '22','33','33','27.5','0',
                     '22','33','33','22','0',
                     '17.5','45.5','42','38.5','28',
                     '10','15','20','20','0',
                     '18.4','24.8','24.8','24.8','18.6',
                     '8.8','17.6','17.6','17.6','15.4',
                     '4.3','17.2','17.2','17.2','0',
                     '0','9.3','3.1','6.2','0',
                     '51.6','133.3','107.5','116.1','68.8',
                     '18.5','44.4','44.4','44.4','22.2',
                     '28','56','56','52.5','42',
                     '0','15.2','15.2','15.2','0',
                     '10.2','88.4','102','61.2','20.4',
                     '29.7','43.2','43.2','40.5','32.4',
                     '10.4','5.2','0','0','0',
                     '17','68','65.3','46.6','0'],
        'Mpg': [bus_2_mpg,bus_2_mpg,bus_2_mpg,bus_2_mpg,bus_2_mpg,
                bus_2A_mpg,bus_2A_mpg,bus_2A_mpg,bus_2A_mpg,bus_2A_mpg,
                bus_2B_mpg,bus_2B_mpg,bus_2B_mpg,bus_2B_mpg,bus_2B_mpg,
                bus_3_mpg,bus_3_mpg,bus_3_mpg,bus_3_mpg,bus_3_mpg,
                bus_3A_mpg,bus_3A_mpg,bus_3A_mpg,bus_3A_mpg,bus_3A_mpg,
                bus_4_mpg,bus_4_mpg,bus_4_mpg,bus_4_mpg,bus_4_mpg,
                bus_4A_mpg,bus_4A_mpg,bus_4A_mpg,bus_4A_mpg,bus_4A_mpg,
                bus_4B_mpg,bus_4B_mpg,bus_4B_mpg,bus_4B_mpg,bus_4B_mpg,
                bus_4C_mpg,bus_4C_mpg,bus_4C_mpg,bus_4C_mpg,bus_4C_mpg,
                bus_5_mpg,bus_5_mpg,bus_5_mpg,bus_5_mpg,bus_5_mpg,
                bus_6_mpg,bus_6_mpg,bus_6_mpg,bus_6_mpg,bus_6_mpg,
                bus_8_mpg,bus_8_mpg,bus_8_mpg,bus_8_mpg,bus_8_mpg,
                bus_9_mpg,bus_9_mpg,bus_9_mpg,bus_9_mpg,bus_9_mpg,
                bus_11X_mpg,bus_11X_mpg,bus_11X_mpg,bus_11X_mpg,bus_11X_mpg,
                bus_13X_mpg,bus_13X_mpg,bus_13X_mpg,bus_13X_mpg,bus_13X_mpg,
                bus_U6_mpg,bus_U6_mpg,bus_U6_mpg,bus_U6_mpg,bus_U6_mpg,
                bus_500_mpg,bus_500_mpg,bus_500_mpg,bus_500_mpg,bus_500_mpg]}


df = pd.DataFrame (data, columns = ['Bus','Times','Distance','Mpg'])

print(df)


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


# Plotting:
# data to plot
n_groups = 5
# Bus = {early, mid, afternoon, evening, late}

# Bus distances:

bus_2_distance = (df_bus_2.iloc[0][2],df_bus_2.iloc[1][2],df_bus_2.iloc[2][2],df_bus_2.iloc[3][2],df_bus_2.iloc[4][2])
bus_2A_distance = (df_bus_2A.iloc[0][2],df_bus_2A.iloc[1][2],df_bus_2A.iloc[2][2],df_bus_2A.iloc[3][2],df_bus_2A.iloc[4][2])
bus_2B_distance = (df_bus_2B.iloc[0][2],df_bus_2B.iloc[1][2],df_bus_2B.iloc[2][2],df_bus_2B.iloc[3][2],df_bus_2B.iloc[4][2])
bus_3_distance = (df_bus_3.iloc[0][2],df_bus_3.iloc[1][2],df_bus_3.iloc[2][2],df_bus_3.iloc[3][2],df_bus_3.iloc[4][2])
bus_3A_distance = (df_bus_3A.iloc[0][2],df_bus_3A.iloc[1][2],df_bus_3A.iloc[2][2],df_bus_3A.iloc[3][2],df_bus_3A.iloc[4][2])
bus_4_distance = (df_bus_4.iloc[0][2],df_bus_4.iloc[1][2],df_bus_4.iloc[2][2],df_bus_4.iloc[3][2],df_bus_4.iloc[4][2])
bus_4A_distance = (df_bus_4A.iloc[0][2],df_bus_4A.iloc[1][2],df_bus_4A.iloc[2][2],df_bus_4A.iloc[3][2],df_bus_4A.iloc[4][2])
bus_4B_distance = (df_bus_4B.iloc[0][2],df_bus_4B.iloc[1][2],df_bus_4B.iloc[2][2],df_bus_4B.iloc[3][2],df_bus_4B.iloc[4][2])
bus_4C_distance = (df_bus_4C.iloc[0][2],df_bus_4C.iloc[1][2],df_bus_4C.iloc[2][2],df_bus_4C.iloc[3][2],df_bus_4C.iloc[4][2])
bus_5_distance = (df_bus_5.iloc[0][2],df_bus_5.iloc[1][2],df_bus_5.iloc[2][2],df_bus_5.iloc[3][2],df_bus_5.iloc[4][2])
bus_6_distance = (df_bus_6.iloc[0][2],df_bus_6.iloc[1][2],df_bus_6.iloc[2][2],df_bus_6.iloc[3][2],df_bus_6.iloc[4][2])
bus_8_distance = (df_bus_8.iloc[0][2],df_bus_8.iloc[1][2],df_bus_8.iloc[2][2],df_bus_8.iloc[3][2],df_bus_8.iloc[4][2])
bus_9_distance = (df_bus_9.iloc[0][2],df_bus_9.iloc[1][2],df_bus_9.iloc[2][2],df_bus_9.iloc[3][2],df_bus_9.iloc[4][2])
bus_11X_distance = (df_bus_11X.iloc[0][2],df_bus_11X.iloc[1][2],df_bus_11X.iloc[2][2],df_bus_11X.iloc[3][2],df_bus_11X.iloc[4][2])
bus_13X_distance = (df_bus_13X.iloc[0][2],df_bus_13X.iloc[1][2],df_bus_13X.iloc[2][2],df_bus_13X.iloc[3][2],df_bus_13X.iloc[4][2])
bus_U6_distance = (df_bus_U6.iloc[0][2],df_bus_U6.iloc[1][2],df_bus_U6.iloc[2][2],df_bus_U6.iloc[3][2],df_bus_U6.iloc[4][2])
bus_500_distance = (df_bus_500.iloc[0][2],df_bus_500.iloc[1][2],df_bus_500.iloc[2][2],df_bus_500.iloc[3][2],df_bus_500.iloc[4][2])

# Multiplying by 2 to account for return trips:
bus_2_distance = [i * 2 for i in bus_2_distance]
bus_2A_distance = [i * 2 for i in bus_2A_distance]
bus_2B_distance = [i * 2 for i in bus_2B_distance]
bus_3_distance = [i * 2 for i in bus_3_distance]
bus_3A_distance = [i * 2 for i in bus_3A_distance]
bus_4_distance = [i * 2 for i in bus_4_distance]
bus_4A_distance = [i * 2 for i in bus_4A_distance]
bus_4B_distance = [i * 2 for i in bus_4B_distance]
bus_4C_distance = [i * 2 for i in bus_4C_distance]
bus_5_distance = [i * 2 for i in bus_5_distance]
bus_6_distance = [i * 2 for i in bus_6_distance]
bus_8_distance = [i * 2 for i in bus_8_distance]
bus_9_distance = [i * 2 for i in bus_9_distance]
bus_11X_distance = [i * 2 for i in bus_11X_distance]
bus_13X_distance = [i * 2 for i in bus_13X_distance]
bus_U6_distance = [i * 2 for i in bus_U6_distance]
bus_500_distance = [i * 2 for i in bus_500_distance]


# Bus gallons:
    
bus_2_gallon = (bus_2_distance[0]/df_bus_2.iloc[0][3],bus_2_distance[1]/df_bus_2.iloc[1][3],bus_2_distance[2]/df_bus_2.iloc[2][3],bus_2_distance[3]/df_bus_2.iloc[3][3],bus_2_distance[4]/df_bus_2.iloc[4][3])
bus_2A_gallon = (bus_2A_distance[0]/df_bus_2A.iloc[0][3],bus_2A_distance[1]/df_bus_2A.iloc[1][3],bus_2A_distance[2]/df_bus_2A.iloc[2][3],bus_2A_distance[3]/df_bus_2A.iloc[3][3],bus_2A_distance[4]/df_bus_2A.iloc[4][3])
bus_2B_gallon = (bus_2B_distance[0]/df_bus_2B.iloc[0][3],bus_2B_distance[1]/df_bus_2B.iloc[1][3],bus_2B_distance[2]/df_bus_2B.iloc[2][3],bus_2B_distance[3]/df_bus_2B.iloc[3][3],bus_2B_distance[4]/df_bus_2B.iloc[4][3])
bus_3_gallon = (bus_3_distance[0]/df_bus_3.iloc[0][3],bus_3_distance[1]/df_bus_3.iloc[1][3],bus_3_distance[2]/df_bus_3.iloc[2][3],bus_3_distance[3]/df_bus_3.iloc[3][3],bus_3_distance[4]/df_bus_3.iloc[4][3])
bus_3A_gallon = (bus_3A_distance[0]/df_bus_3A.iloc[0][3],bus_3A_distance[1]/df_bus_3A.iloc[1][3],bus_3A_distance[2]/df_bus_3A.iloc[2][3],bus_3A_distance[3]/df_bus_3A.iloc[3][3],bus_3A_distance[4]/df_bus_3A.iloc[4][3])
bus_4_gallon = (bus_4_distance[0]/df_bus_4.iloc[0][3],bus_4_distance[1]/df_bus_4.iloc[1][3],bus_4_distance[2]/df_bus_4.iloc[2][3],bus_4_distance[3]/df_bus_4.iloc[3][3],bus_4_distance[4]/df_bus_4.iloc[4][3])
bus_4A_gallon = (bus_4A_distance[0]/df_bus_4A.iloc[0][3],bus_4A_distance[1]/df_bus_4A.iloc[1][3],bus_4A_distance[2]/df_bus_4A.iloc[2][3],bus_4A_distance[3]/df_bus_4A.iloc[3][3],bus_4A_distance[4]/df_bus_4A.iloc[4][3])
bus_4B_gallon = (bus_4B_distance[0]/df_bus_4B.iloc[0][3],bus_4B_distance[1]/df_bus_4B.iloc[1][3],bus_4B_distance[2]/df_bus_4B.iloc[2][3],bus_4B_distance[3]/df_bus_4B.iloc[3][3],bus_4B_distance[4]/df_bus_4B.iloc[4][3])
bus_4C_gallon = (bus_4C_distance[0]/df_bus_4C.iloc[0][3],bus_4C_distance[1]/df_bus_4C.iloc[1][3],bus_4C_distance[2]/df_bus_4C.iloc[2][3],bus_4C_distance[3]/df_bus_4C.iloc[3][3],bus_4C_distance[4]/df_bus_4C.iloc[4][3])
bus_5_gallon = (bus_5_distance[0]/df_bus_5.iloc[0][3],bus_5_distance[1]/df_bus_5.iloc[1][3],bus_5_distance[2]/df_bus_5.iloc[2][3],bus_5_distance[3]/df_bus_5.iloc[3][3],bus_5_distance[4]/df_bus_5.iloc[4][3])
bus_6_gallon = (bus_6_distance[0]/df_bus_6.iloc[0][3],bus_6_distance[1]/df_bus_6.iloc[1][3],bus_6_distance[2]/df_bus_6.iloc[2][3],bus_6_distance[3]/df_bus_6.iloc[3][3],bus_6_distance[4]/df_bus_6.iloc[4][3])
bus_8_gallon = (bus_8_distance[0]/df_bus_8.iloc[0][3],bus_8_distance[1]/df_bus_8.iloc[1][3],bus_8_distance[2]/df_bus_8.iloc[2][3],bus_8_distance[3]/df_bus_8.iloc[3][3],bus_8_distance[4]/df_bus_8.iloc[4][3])
bus_9_gallon = (bus_9_distance[0]/df_bus_9.iloc[0][3],bus_9_distance[1]/df_bus_9.iloc[1][3],bus_9_distance[2]/df_bus_9.iloc[2][3],bus_9_distance[3]/df_bus_9.iloc[3][3],bus_9_distance[4]/df_bus_9.iloc[4][3])
bus_11X_gallon = (bus_11X_distance[0]/df_bus_11X.iloc[0][3],bus_11X_distance[1]/df_bus_11X.iloc[1][3],bus_11X_distance[2]/df_bus_11X.iloc[2][3],bus_11X_distance[3]/df_bus_11X.iloc[3][3],bus_11X_distance[4]/df_bus_11X.iloc[4][3])
bus_13X_gallon = (bus_13X_distance[0]/df_bus_13X.iloc[0][3],bus_13X_distance[1]/df_bus_13X.iloc[1][3],bus_13X_distance[2]/df_bus_13X.iloc[2][3],bus_13X_distance[3]/df_bus_13X.iloc[3][3],bus_13X_distance[4]/df_bus_13X.iloc[4][3])
bus_U6_gallon = (bus_U6_distance[0]/df_bus_U6.iloc[0][3],bus_U6_distance[1]/df_bus_U6.iloc[1][3],bus_U6_distance[2]/df_bus_U6.iloc[2][3],bus_U6_distance[3]/df_bus_U6.iloc[3][3],bus_U6_distance[4]/df_bus_U6.iloc[4][3])
bus_500_gallon = (bus_500_distance[0]/df_bus_500.iloc[0][3],bus_500_distance[1]/df_bus_500.iloc[1][3],bus_500_distance[2]/df_bus_500.iloc[2][3],bus_500_distance[3]/df_bus_500.iloc[3][3],bus_500_distance[4]/df_bus_500.iloc[4][3])

# create plot
fig, ax = plt.subplots()
index = np.arange(n_groups)
bar_width = 0.05
opacity = 0.8

rects1 = plt.bar(index, bus_2_gallon, bar_width,
alpha=opacity,
color='#800000',
label='Bus 2')

rects2 = plt.bar(index + bar_width, bus_2A_gallon, bar_width,
alpha=opacity,
color='#9a6324',
label='Bus 2A')

rects3 = plt.bar(index + bar_width*2, bus_2B_gallon, bar_width,
alpha=opacity,
color='#808000',
label='Bus 2B')

rects4 = plt.bar(index + bar_width*3, bus_3_gallon, bar_width,
alpha=opacity,
color='#469990',
label='Bus 3')

rects5 = plt.bar(index + bar_width*4, bus_3A_gallon, bar_width,
alpha=opacity,
color='#000075',
label='Bus 3A')

rects6 = plt.bar(index + bar_width*5, bus_4_gallon, bar_width,
alpha=opacity,
color='#000000',
label='Bus 4')

rects7 = plt.bar(index + bar_width*5, bus_4A_gallon, bar_width,
alpha=opacity,
color='#000065',
label='Bus 4A')

rects8 = plt.bar(index + bar_width*5, bus_4B_gallon, bar_width,
alpha=opacity,
color='#000055',
label='Bus 4B')

rects9 = plt.bar(index + bar_width*5, bus_4C_gallon, bar_width,
alpha=opacity,
color='#000045',
label='Bus 4C')


rects10 = plt.bar(index + bar_width*6, bus_5_gallon, bar_width,
alpha=opacity,
color='#e6194b',
label='Bus 5')

rects11 = plt.bar(index + bar_width*7, bus_6_gallon, bar_width,
alpha=opacity,
color='#f58231',
label='Bus 6')

rects12 = plt.bar(index + bar_width*8, bus_8_gallon, bar_width,
alpha=opacity,
color='#ffe119',
label='Bus 8')

rects13 = plt.bar(index + bar_width*9, bus_9_gallon, bar_width,
alpha=opacity,
color='#bfef45',
label='Bus 9')

rects14 = plt.bar(index + bar_width*10, bus_11X_gallon, bar_width,
alpha=opacity,
color='#3cb44b',
label='Bus 11X')

rects15 = plt.bar(index + bar_width*11, bus_13X_gallon, bar_width,
alpha=opacity,
color='#42d4f4',
label='Bus 13X')

rects16 = plt.bar(index + bar_width*12, bus_U6_gallon, bar_width,
alpha=opacity,
color='#4363d8',
label='Bus U6')

rects17 = plt.bar(index + bar_width*13, bus_500_gallon, bar_width,
alpha=opacity,
color='#911eb4',
label='Bus 500')


plt.xlabel('Time of day')
plt.ylabel('Gallons')
plt.title('Gallons of diesel consumed by each bus route during a weekday')
plt.xticks(index + bar_width, ('Early (4am - 8am)', 'Mid (8am - 12am)','Afternoon (12am - 4pm)','Evening (4pm - 8pm)', 'Late (8pm - 12pm)'))
plt.legend()

plt.tight_layout()
plt.show()
