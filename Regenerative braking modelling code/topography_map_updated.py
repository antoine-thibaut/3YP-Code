# NOTE: This code was taken and modified from::
# [1] F. Faraj, Towards Data Science. (2020). Plotting Regional Topographic Maps from Scratch in Python. [Online]. 
#     Available at: https://towardsdatascience.com/plotting-regional-topographic-maps-from-scratch-in-python-8452fd770d9d. 
#     [Accessed 26th of March 2021]

# Other references:
# Elevations and coordinates were taken from:
# [2] FreeMapTools. (2019). Elevation Finder. [Online]. 
#     Available at: https://www.freemaptools.com/elevation-finder.htm. 
#     [Accessed 26h of March 2021]
# Bus route data was taken from:
# [3] Oxford Bus Company. (2020). park&ride500 Covid-19 Timetables from 1st June 2020. [Pdf]. 
#     Available at: https://assets.goaheadbus.com/media/cms_page_media/8103/200601_parkride500_COVID-19_Coronavirus_Timetable.pdf. 
#     [Accessed 26th of March 2021]
# [4] Oxford Bus Company. (2020). park&ride400 Covid-19 Timetables from 24th October 2020. [Pdf]. 
#     Available at: https://assets.goaheadbus.com/media/cms_page_media/8103/201024_parkride400_COVID-19_Coronavirus_TimetableV2.pdf. 
#     [Accessed 26th of March 2021]
# [5] LiveBus.org. (2021). City Centre and Pear Tree Park and Ride. [Online]. 
#     Available at: http://www.livebus.org/oxfordshire/routes/obc/300/city-centre-and-pear-tree-park-and-ride/. 
#     [Accessed 26th of March 2021]
# [6] Stagecoach. (2021). S5 Bus Route & Timetable: Oxford-Bicester. [Online]. 
#     Available at: https://www.stagecoachbus.com/routes/oxfordshire/s5/oxford-bicester/xoas005.o. 
#     [Accessed 26th of March 2021]
# [7] Google Maps. Google Maps. [Online] 
#     Available at: https://www.google.co.uk/maps/. 
#     [Accessed 7th of April 2021]
# [8] matplotlib. (2017). Legend guide. [Online].
#     Available at: https://matplotlib.org/2.0.2/users/legend_guide.html  
#     [Accessed 12th of May 2021]

# This code produces a topography map of Oxford with traced Park and Ride routes. The code outputs a topography map and a separate legend. 

import numpy as np
from scipy.interpolate import griddata
# From https://towardsdatascience.com/plotting-regional-topographic-maps-from-scratch-in-python-8452fd770d9d
import pandas as pd
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt

data_500 = {'Latitude': [51.75311,51.75466,51.77678,51.80353,51.80325,51.82896,51.84759],
        'Longitude': [-1.26942,-1.25913,-1.26474,-1.275,-1.27328,-1.30759,-1.3538],
        'Elevation': [61,70,66,66,64,68,100]}
df_500 = pd.DataFrame (data_500, columns = ['Latitude','Longitude','Elevation'])
x_500 = df_500.Longitude[:]  # x coordinates for map
y_500 = df_500.Latitude[:]   # x coordinates for map

data_400 = {'Latitude': [51.74548,51.74901,51.74994,51.76004,51.76228],
        'Longitude': [-1.26362,-1.26272,-1.25687,-1.21158,-1.18265],
        'Elevation': [59,59,65,108,103]}
df_400 = pd.DataFrame (data_400, columns = ['Latitude','Longitude','Elevation'])
x_400 = df_400.Longitude[:]  # x coordinates for map
y_400 = df_400.Latitude[:]   # x coordinates for map

data_300 = {'Latitude': [51.72979,51.75409,51.75197,51.74994,
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
df_300 = pd.DataFrame (data_300, columns = ['Latitude','Longitude','Elevation'])
x_300 = df_300.Longitude[:]  # x coordinates for map
y_300 = df_300.Latitude[:]   # x coordinates for map

# Used for plotting routes:
data_300_plot  = {'Latitude': [51.72979,51.74994,51.73516,51.75151,
                     51.75466,51.77826,51.79375],
                  'Longitude': [-1.24861,-1.25687,-1.24805,-1.26131,
                      -1.25913,-1.26722,-1.2817626020596353],
                  'Elevation': [57,65,57,66,
                      70,65,66]}
df_300_plot = pd.DataFrame (data_300_plot, columns = ['Latitude','Longitude','Elevation'])
x_300_plot = df_300_plot.Longitude[:]  # x coordinates for map
y_300_plot = df_300_plot.Latitude[:]   # x coordinates for map

data_S5 = {'Latitude': [51.75466,51.77748,51.81788,51.8861,
                     51.89244,51.8975,51.90947],
        'Longitude': [-1.25913,-1.26491,-1.2726,-1.17199,
                      -1.14937,-1.15271,-1.13795],
        'Elevation': [70,67,63,65,
                      70,72,78]}
df_S5 = pd.DataFrame (data_S5, columns = ['Latitude','Longitude','Elevation'])
x_S5 = df_S5.Longitude[:]   # x coordinates for map
y_S5 = df_S5.Latitude[:]    # x coordinates for map

data_corners ={'Latitude': [51.90947,51.7298,51.7298],
               'Longitude': [-1.3538,-1.3538,-1.13795],
               'Elevation': [127,85,114]}
df_corners = pd.DataFrame (data_corners, columns = ['Latitude','Longitude','Elevation'])


data_grid ={'Latitude': [51.7298,51.7298,51.7298,51.7747,
                         51.7747,51.7747,51.7747,51.7747,
                         51.8196,51.8196,51.8196,51.8196,
                         51.8196,51.8646,51.8646,51.8646,
                         51.8646,51.8646,51.9095,51.9095,
                         51.9095],
               'Longitude': [-1.2998,-1.2459,-1.1919,-1.3538,
                             -1.2998,-1.2459,-1.1919,-1.138,
                             -1.3538,-1.2998,-1.2459,-1.1919,
                             -1.138,-1.3538,-1.2998,-1.2459,
                             -1.1919,-1.138,-1.2998,-1.2459,
                             -1.1919],
               'Elevation': [148,56,76,63,
                             63,62,108,62,
                             100,63,62,61,
                             62,88,73,71,
                             68,61,72,103,
                             95]}
df_grid = pd.DataFrame (data_grid, columns = ['Latitude','Longitude','Elevation'])

# Adding all data frames
df_all = df_500
for i in range(0,1):
    df_all = df_all.append(df_400)
for i in range(0,1):
    df_all = df_all.append(df_300)
for i in range(0,1):
    df_all = df_all.append(df_S5)
for i in range(0,1):
    df_all = df_all.append(df_corners)
for i in range(0,1):
    df_all = df_all.append(df_grid)
print(df_all)

# Extracting coordinates and elevations
x_all = df_all.Longitude[:]   # x coordinates for map
y_all = df_all.Latitude[:]    # y coordinates for map
z_all = df_all.Elevation[:]   # z coordinates for map

# The code below has been taken and modified from [1]:
points=200**2;               # Number of points 

[x,y]=np.meshgrid(np.linspace(np.min(x_all),np.max(x_all),np.sqrt(points).astype(int)),
                              np.linspace(np.min(y_all),np.max(y_all),np.sqrt(points).astype(int))); 
z = griddata((x_all, y_all), z_all, (x, y), method='linear');
x = np.matrix.flatten(x); # Gridded x coordinates
y = np.matrix.flatten(y); # Gridded y coordinates
z = np.matrix.flatten(z); # Gridded z coordinates

# Plotting topographic map:
# From [1]:
plt.scatter(x,y,1,z)
plt.colorbar(label='Elevation [m]')
plt.xlabel('Longitude [°]')
plt.ylabel('Latitude [°]')
# ADDED ROUTE MAP:
plt.plot(x_500, y_500, c='r', marker='.')                              # Plotting 500 stops
plt.plot(x_500[0], y_500[0], c='r', marker='s')                        # Plotting 500 first station
plt.plot(x_500[len(x_500)-1], y_500[len(x_500)-1], c='r', marker='s')  # Plotting 500 last station

plt.plot(x_400, y_400, c='b', marker='.')                              # Plotting 400 stops
plt.plot(x_400[0], y_400[0], c='b', marker='s')                        # Plotting 400 first station
plt.plot(x_400[len(x_400)-1], y_400[len(x_400)-1], c='b', marker='s')  # Plotting 400 last station

plt.plot(x_300_plot, y_300_plot, c='g', marker='.')                                        # Plotting 300 stops
plt.plot(x_300_plot[0], y_300_plot[0], c='g', marker='s')                                  # Plotting 400 first station
plt.plot(x_300_plot[len(x_300_plot)-1], y_300_plot[len(x_300_plot)-1], c='g', marker='s')  # Plotting 400 last station

plt.plot(x_S5, y_S5, c='m', marker='.')                            # Plotting S5 stops
plt.plot(x_S5[0], y_S5[0], c='m', marker='s')                      # Plotting 400 first station
plt.plot(x_S5[len(x_S5)-1], y_S5[len(x_S5)-1], c='m', marker='s')  # Plotting 400 last station
plt.axis('off') 

plt.savefig('topography_model.svg', format='svg', dpi=1200)


# Plotting the legend:
plt.clf()
plt.plot(0,0)
plt.axis('off') 

# Note: The following code was borrowed from [8]:
red_patch = mpatches.Patch(color='red', label='500 (Oxford Parkway Park&Ride)')
blue_patch = mpatches.Patch(color='blue', label='400 (Seacourt and Thornhill Park&Ride)')
green_patch = mpatches.Patch(color='green',label='300 (Redbridge and Pear Tree Park&Ride)')
magenta_patch = mpatches.Patch(color='magenta',label='S5 (Bicester Park&Ride)')
plt.legend(handles=[red_patch,blue_patch,green_patch,magenta_patch])
plt.savefig('topography_legend.svg', format='svg', dpi=1200)



