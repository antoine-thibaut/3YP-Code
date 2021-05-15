# NOTE: MUCH CODE WAS TAKEN FROM:
# https://towardsdatascience.com/plotting-regional-topographic-maps-from-scratch-in-python-8452fd770d9d


import numpy as np
from scipy.interpolate import griddata
# From https://towardsdatascience.com/plotting-regional-topographic-maps-from-scratch-in-python-8452fd770d9d
import pandas as pd
import math
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

data_500 = {'Stop':  ['Oxford Rail Station', 'Oxford Magdalen Street', 'Summertown shops', 'Oxford Parkway Station',
                      'Oxford Parkway Park and Ride','Kidlington, Oxford motor park', 'Woodstock, Marlborough Arms'],
        'Latitude': [51.75311,51.75466,51.77678,51.80353,51.80325,51.82896,51.84759],
        'Longitude': [-1.26942,-1.25913,-1.26474,-1.275,-1.27328,-1.30759,-1.3538],
        'Elevation': [61,70,66,66,64,68,100]}
df_500 = pd.DataFrame (data_500, columns = ['Stop','Latitude','Longitude','Elevation'])

data_400 = {'Stop':  ['Seacourt Park&Ride', 'Oxford, Westgate Shopping Centre', 'Oxford, St Aldates', 'Headington Shops',
                      'Thornhill Park&Ride'],
        'Latitude': [51.74548,51.74901,51.74994,51.76004,51.76228],
        'Longitude': [-1.26362,-1.26272,-1.25687,-1.21158,-1.18265],
        'Elevation': [59,59,65,108,103]}
df_400 = pd.DataFrame (data_400, columns = ['Stop','Latitude','Longitude','Elevation'])

data_300 = {'Stop':  ['Redbridge Park and Ride','Queens Lane','Carfax','St Aldates',
                      'Canning Crescent','Chatham Road','Lincoln Road','Lake Street',
                      'Newton Road','Whitehouse Road','Police Station','County Hall',
                      'George Street','Magdalen Street','Radcliffe Infirmary','Plantation Road',
                      'Canterbury Road','St Margarets Road','Lathbury Road','Beech Croft Road',
                      'South Parade','Osberton Road','Squitchey Lane','Woodstock Close',
                      'First Turn','Pear Tree Park & Ride'],
        'Latitude': [51.72979,51.75409,51.75197,51.74994,
                     51.73320,51.73516,51.73656,51.73887,
                     51.74188,51.74483,51.74788,51.75151,
                     51.75363,51.75466,51.76010,51.76227,
                     51.76530,51.76780,51.77254,51.77435,
                     51.77826,51.77952,51.78299,51.78503,
                     51.78565,51.79375],
        'Longitude': [-1.24861,-1.25252,-1.25780,-1.25687,
                      -1.24797,-1.24805,-1.25256,-1.25674,
                      -1.25717,-1.26139,-1.25659,-1.26131,
                      -1.26103,-1.25913,-1.26239,-1.26798,
                      -1.26282,-1.26571,-1.26521,-1.26586,
                      -1.26722,-1.27052,-1.26942,-1.27373,
                      -1.27988,-1.2817626020596353],
        'Elevation': [57,71,72,65,
                      57,57,58,58,
                      57,61,61,66,
                      68,70,68,63,
                      68,68,67,66,
                      65,66,73,74,
                      72,66]}
df_300 = pd.DataFrame (data_300, columns = ['Stop','Latitude','Longitude','Elevation'])

data_S5 = {'Stop':  ['Oxford City Centre Magdalen Street','Summertown Shops','Gosford Kings Arms','Kingsmere Bicester Park and Ride',
                     'Bicester, Bicester Village','Bicester Town Centre Manorsfield Road','Glory Farm Bicester Road'],
        'Latitude': [51.75466,51.77748,51.81788,51.8861,
                     51.89244,51.8975,51.90947],
        'Longitude': [-1.25913,-1.26491,-1.2726,-1.17199,
                      -1.14937,-1.15271,-1.13795],
        'Elevation': [70,67,63,65,
                      70,72,78]}
df_S5 = pd.DataFrame (data_S5, columns = ['Stop','Latitude','Longitude','Elevation'])

# Adding all data frames
df_all = df_500
for i in range(0,1):
    df_all = df_all.append(df_400)
for i in range(0,1):
    df_all = df_all.append(df_300)
for i in range(0,1):
    df_all = df_all.append(df_S5)
print(df_all)

'''
df_all["Latitude"]=df_all["Latitude"].astype(int)         # Casts as floats
df_all["Longitude"]=df_all["Longitude"].astype(int)         # Casts as floats
df_all["Elevation"]=df_all["Elevation"].astype(int)         # Casts as floats
'''
# Extracting coordinates and elevations
x_all = df_all.Longitude[:]   # x coordinates for map
y_all = df_all.Latitude[:]    # x coordinates for map
z_all = df_all.Elevation[:]

#x_test = pd.dplyr::pull(df_all, Longitude)

points=10000;               # Number of points here
#sqrt_points = 

[x,y]=np.meshgrid(np.linspace(np.min(x_all),np.max(x_all),np.sqrt(points).astype(int)),np.linspace(np.min(y_all),np.max(y_all),np.sqrt(points).astype(int)));
z = griddata((x_all, y_all), z_all, (x, y), method='linear');
x = np.matrix.flatten(x); #Gridded longitude
y = np.matrix.flatten(y); #Gridded latitude
z = np.matrix.flatten(z); #Gridded elevation

# Plotting topographic map:
# FROM:https://towardsdatascience.com/plotting-regional-topographic-maps-from-scratch-in-python-8452fd770d9d
plt.scatter(x,y,1,z)
plt.colorbar(label='Elevation [m]')
plt.xlabel('Longitude [°]')
plt.ylabel('Latitude [°]')
plt.savefig('Elevationmap.svg', format='pdf', dpi=1200)

