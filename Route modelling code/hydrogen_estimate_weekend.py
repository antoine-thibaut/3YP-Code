#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 15:06:07 2021

@author: Antoine and Akshay
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
                     '0','68','59.5','34','0'],
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


df = pd.DataFrame (data, columns = ['Bus','Times','Distance','Mpg']) #creates dataframe

df["Distance"]=df["Distance"].astype(float) #casts the distance column as floats
grouped_bus = df.groupby(df["Bus"]) # can also group by a different column eg Times!

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

#Total gallon consumption per bus each day
bus_2_gallon_sum = sum(bus_2_gallon)
bus_2A_gallon_sum = sum(bus_2A_gallon)
bus_2B_gallon_sum = sum(bus_2B_gallon)
bus_3_gallon_sum = sum(bus_3_gallon)
bus_3A_gallon_sum = sum(bus_3A_gallon)
bus_4_gallon_sum = sum(bus_4_gallon)
bus_4A_gallon_sum = sum(bus_4A_gallon)
bus_4B_gallon_sum = sum(bus_4B_gallon)
bus_4C_gallon_sum = sum(bus_4C_gallon)
bus_5_gallon_sum = sum(bus_5_gallon)
bus_6_gallon_sum = sum(bus_6_gallon)
bus_8_gallon_sum = sum(bus_8_gallon)
bus_9_gallon_sum = sum(bus_9_gallon)
bus_11X_gallon_sum = sum(bus_11X_gallon)
bus_13X_gallon_sum = sum(bus_13X_gallon)
bus_U6_gallon_sum = sum(bus_U6_gallon)
bus_500_gallon_sum = sum(bus_500_gallon)

hydrogen_volumetric_energy_density = 12.6 # MJ/gallon
hydrogen_density = 23 # kg/m^3


# Total litre consumption per bus each day
bus_2_litre_sum = sum(bus_2_gallon) * 4.546
bus_2A_litre_sum = sum(bus_2A_gallon)* 4.546
bus_2B_litre_sum = sum(bus_2B_gallon)* 4.546
bus_3_litre_sum = sum(bus_3_gallon)* 4.546
bus_3A_litre_sum = sum(bus_3A_gallon)* 4.546
bus_4_litre_sum = sum(bus_4_gallon)* 4.546
bus_4A_litre_sum = sum(bus_4A_gallon)* 4.546
bus_4B_litre_sum = sum(bus_4B_gallon)* 4.546
bus_4C_litre_sum = sum(bus_4C_gallon)* 4.546
bus_5_litre_sum = sum(bus_5_gallon)* 4.546
bus_6_litre_sum = sum(bus_6_gallon)* 4.546
bus_8_litre_sum = sum(bus_8_gallon)* 4.546
bus_9_litre_sum = sum(bus_9_gallon)* 4.546
bus_11X_litre_sum = sum(bus_11X_gallon)* 4.546
bus_13X_litre_sum = sum(bus_13X_gallon)* 4.546
bus_U6_litre_sum = sum(bus_U6_gallon)* 4.546
bus_500_litre_sum = sum(bus_500_gallon)* 4.546

#Total energy consumption per bus each day
bus_2_energy_sum = sum(bus_2_gallon) * 175
bus_2A_energy_sum = sum(bus_2A_gallon)* 175
bus_2B_energy_sum = sum(bus_2B_gallon)* 175
bus_3_energy_sum = sum(bus_3_gallon)* 175
bus_3A_energy_sum = sum(bus_3A_gallon)* 175
bus_4_energy_sum = sum(bus_4_gallon)* 175
bus_4A_energy_sum = sum(bus_4A_gallon)* 175
bus_4B_energy_sum = sum(bus_4B_gallon)* 175
bus_4C_energy_sum = sum(bus_4C_gallon)* 175
bus_5_energy_sum = sum(bus_5_gallon)* 175
bus_6_energy_sum = sum(bus_6_gallon)* 175
bus_8_energy_sum = sum(bus_8_gallon)* 175
bus_9_energy_sum = sum(bus_9_gallon)* 175
bus_11X_energy_sum = sum(bus_11X_gallon)* 175
bus_13X_energy_sum = sum(bus_13X_gallon)* 175
bus_U6_energy_sum = sum(bus_U6_gallon)* 175
bus_500_energy_sum = sum(bus_500_gallon)* 175

# Hydrogen consumption in litres per bus each day
bus_2_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_2_energy_sum * 4.546
bus_2A_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_2A_energy_sum * 4.546
bus_2B_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_2B_energy_sum * 4.546
bus_3_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_3_energy_sum * 4.546
bus_3A_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_3A_energy_sum * 4.546
bus_4_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_4_energy_sum * 4.546
bus_4A_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_4A_energy_sum * 4.546
bus_4B_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_4B_energy_sum * 4.546
bus_4C_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_4C_energy_sum * 4.546
bus_5_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_5_energy_sum * 4.546
bus_6_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_6_energy_sum * 4.546
bus_8_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_8_energy_sum * 4.546
bus_9_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_9_energy_sum * 4.546
bus_11X_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_11X_energy_sum * 4.546
bus_13X_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_13X_energy_sum * 4.546
bus_U6_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_U6_energy_sum * 4.546
bus_500_h2_sum_litres = (1/hydrogen_volumetric_energy_density) * bus_500_energy_sum * 4.546



# Hydrogen consumption in kg per bus each day
bus_2_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_2_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_2A_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_2A_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_2B_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_2B_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_3_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_3_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_3A_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_3A_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_4_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_4_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_4A_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_4A_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_4B_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_4B_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_5_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_5_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_4C_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_4C_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_6_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_6_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_8_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_8_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_9_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_9_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_11X_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_11X_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_13X_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_13X_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_U6_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_U6_energy_sum * 4.546 * 0.001 * hydrogen_density
bus_500_h2_sum_kg = (1/hydrogen_volumetric_energy_density) * bus_500_energy_sum * 4.546 * 0.001 * hydrogen_density

# Create dataframe and plot graphs
data_consumption = {'Bus':  ['2','2A','2B','3','3A',
                 '4','4A','4B','4C','5',
                 '6','8','9','11X','13X',
                 'U6','500',],
        'Daily Diesel Consumption (litres)': [bus_2_litre_sum, bus_2A_litre_sum, bus_2B_litre_sum, bus_3_litre_sum, bus_3A_litre_sum,
                                        bus_4_litre_sum, bus_4A_litre_sum, bus_4B_litre_sum, bus_4C_litre_sum, bus_5_litre_sum,
                                        bus_6_litre_sum, bus_8_litre_sum, bus_9_litre_sum, bus_11X_litre_sum, bus_13X_litre_sum,
                                        bus_U6_litre_sum, bus_500_litre_sum],
        'Daily Energy Consumption (MJ)': [bus_2_energy_sum, bus_2A_energy_sum, bus_2B_energy_sum, bus_3_energy_sum, bus_3A_energy_sum,
                                        bus_4_energy_sum, bus_4A_energy_sum, bus_4B_energy_sum, bus_4C_energy_sum, bus_5_energy_sum,
                                        bus_6_energy_sum, bus_8_energy_sum, bus_9_energy_sum, bus_11X_energy_sum, bus_13X_energy_sum,
                                        bus_U6_energy_sum, bus_500_energy_sum],
        'Daily Hydrogen Consumption (litres)': [bus_2_h2_sum_litres, bus_2A_h2_sum_litres, bus_2B_h2_sum_litres, bus_3_h2_sum_litres, bus_3A_h2_sum_litres,
                                        bus_4_h2_sum_litres, bus_4A_h2_sum_litres, bus_4B_h2_sum_litres, bus_4C_h2_sum_litres, bus_5_h2_sum_litres,
                                        bus_6_h2_sum_litres, bus_8_h2_sum_litres, bus_9_h2_sum_litres, bus_11X_h2_sum_litres, bus_13X_h2_sum_litres,
                                        bus_U6_h2_sum_litres, bus_500_h2_sum_litres],
        'Daily Hydrogen Consumption (kg)': [bus_2_h2_sum_kg, bus_2A_h2_sum_kg, bus_2B_h2_sum_kg, bus_3_h2_sum_kg, bus_3A_h2_sum_kg,
                                        bus_4_h2_sum_kg, bus_4A_h2_sum_kg, bus_4B_h2_sum_kg, bus_4C_h2_sum_kg, bus_5_h2_sum_kg,
                                        bus_6_h2_sum_kg, bus_8_h2_sum_kg, bus_9_h2_sum_kg, bus_11X_h2_sum_kg, bus_13X_h2_sum_kg,
                                        bus_U6_h2_sum_kg, bus_500_h2_sum_kg]}



df_consumption = pd.DataFrame(data_consumption, columns = ['Bus','Daily Diesel Consumption (litres)','Daily Energy Consumption (MJ)','Daily Hydrogen Consumption (litres)','Daily Hydrogen Consumption (kg)']) #create consumption dataframe
df_consumption["Daily Diesel Consumption (litres)"]=df_consumption["Daily Diesel Consumption (litres)"].astype(float) #casts the daily consumption column as floats
df_consumption["Daily Energy Consumption (MJ)"]=df_consumption["Daily Energy Consumption (MJ)"].astype(float)
df_consumption["Daily Hydrogen Consumption (litres)"]=df_consumption["Daily Hydrogen Consumption (litres)"].astype(float)
df_consumption["Daily Hydrogen Consumption (kg)"]=df_consumption["Daily Hydrogen Consumption (kg)"].astype(float)

fig, axes = plt.subplots(nrows=2, ncols=2)

# iterate and plot subplots
for xcol, ax in zip(df_consumption.columns[1:5], [x for v in axes for x in v]):
    df_consumption.plot.bar(x='Bus', y=xcol, ax=ax, rot=0, color='r')

plt.show()




#fig, axes = plt.subplots(nrows=2, ncols=2)
#df_consumption[["Bus","Daily Diesel Consumption (litres)"]].plot(ax=axes[0], kind='bar')
#df_consumption[["Bus", "Daily Energy Consumption (MJ)"]].plot(ax=axes[1], kind='bar')
#df_consumption[["Bus", "Daily Hydrogen Consumption (litres)"]].plot(ax=axes[2], kind='bar')
#df_consumption[["Bus", "Daily Hydrogen Consumption (kg)"]].plot(ax=axes[3], kind='bar')







#df_consumption.plot.bar(x='Bus', y='Daily Diesel Consumption (litres)', ax=axes[0], rot = 0, title='Daily diesel consumption of each bus route', color='#ff007f')
#df_consumption.plot.bar(x='Bus', y='Daily Energy Consumption (MJ)', ax=axes[1], rot = 0, title='Daily energy consumption of each bus route', color='#ff007f')
#df_consumption.plot.bar(x='Bus', y='Daily Hydrogen Consumption (litres)', ax=axes[2], rot = 0, title='Daily hydrogen consumption of each bus route', color='#ff007f')
#df_consumption.plot.bar(x='Bus', y='Daily Hydrogen Consumption (kg)', ax=axes[3], rot = 0, title='Daily hydrogen consumption of each bus route', color='#ff007f')





#plt.ylabel("Daily Diesel Consumption (litres)")



total_gallons_consumed_per_day = bus_2_gallon_sum + bus_2A_gallon_sum + bus_2B_gallon_sum + bus_3_gallon_sum + bus_3A_gallon_sum + bus_4_gallon_sum + bus_4A_gallon_sum + bus_4B_gallon_sum + bus_4C_gallon_sum + bus_5_gallon_sum + bus_6_gallon_sum + bus_8_gallon_sum + bus_9_gallon_sum + bus_11X_gallon_sum + bus_13X_gallon_sum + bus_U6_gallon_sum + bus_500_gallon_sum
total_gallons_consumed_per_day = round(total_gallons_consumed_per_day, 1)
total_litres_consumed_per_day = round(total_gallons_consumed_per_day * 4.546, 1)
print("Total Daily Fuel Consumption = ",total_gallons_consumed_per_day, "gallons = ", total_litres_consumed_per_day, "litres")
diesel_volumetric_energy_density = 175 # MJ/gallon
total_daily_energy_consumption = total_gallons_consumed_per_day * diesel_volumetric_energy_density
print("Total Daily Energy Consumption = ",total_daily_energy_consumption, "MJ")
daily_hydrogen_consumption_gallons = round((1/hydrogen_volumetric_energy_density) * total_daily_energy_consumption, 1)
daily_hydrogen_consumption_litres = round(daily_hydrogen_consumption_gallons * 4.546, 1)
print("Daily Hydrogen Required = ",daily_hydrogen_consumption_gallons, "gallons = ",daily_hydrogen_consumption_litres, "litres")
hydrogen_mass = round(daily_hydrogen_consumption_litres * 0.001 * hydrogen_density, 1)
print("Mass of Hydrogen Required = ",hydrogen_mass, "kg")