#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 11:13:38 2020

@author: Antoine
"""

# Note: weekend values are used 

import numpy as np
import pandas as pd
import math
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt


# Parameters:

# Creating a class to store model parameters
class bus5:
    def __init__(parameters):
        parameters.bus_5_mpg = 9
        parameters.M = 6800             # Bus mass
        parameters.g = 9.81             # Free fall accceleration
        parameters.Mg = parameters.M*parameters.g # Bus weight
        parameters.v_mph = 20                         # Bus speed in Mph
        parameters.v = parameters.v_mph*0.4470        # Bus speed in m/s
        parameters.Cd = 0.6                           # Bus drag coefficient             # Energy density of diesel   
        parameters.bus_5_total_distance = 477.3             # Total distance travelled in a day for one way [miles]
        parameters.trips = 111                           # Number of trips in one day
        parameters.R = 6371*10^3                      # Earth radius
        
# Fuel parameters:
bus_mpg = 9                                # mpg rating for all park and ride buses
diesel_energy_density = 38.6*10**6         # J/L
hydrogen_energy_density = 120              # MJ/kg
hydrogen_energy_efficiency = 0.6           # Conversion efficiency for converting hydrogen into useful work
conv_g_l = 4.546                           # Gallons to littres conversion



# Bus speed:
v_mph = 20
v = v_mph*0.4470


# Earth radius:
R = 6371*10^3

# Bus parameters:
Cd = 0.6         # Drag coefficient
rho = 1.225      # Air density
A = 6            # Bus cross section  
M = 6800         # Bus mass
g = 9.81
Mg = M*g 
Fa = 0.5*Cd*rho*v**2 # Air resistance force:

# Route parameters:
bus_500_total_distance_weekend = 161.5     # Weekend
bus_500_trips_weekend = 19               # Number of trips in a day, weekend
bus_500_stops = 7                
bus_500_gallons_weekend = bus_500_total_distance_weekend/bus_mpg # Gallons consumed by bus 500
bus_500_litres_weekend = bus_500_gallons_weekend*4.546
bus_500_total_energy_weekend = bus_500_litres_weekend*diesel_energy_density # Energy equivalent
bus_500_trip_energy_weekend = bus_500_total_energy_weekend/bus_500_trips_weekend # Energy for 1 trip
bus_500_kinetic_energy = 0.5*M*v**2  # Kinetic energy of bus 500
bus_500_total_stop_energy = bus_500_kinetic_energy*bus_500_stops # Recoverable kinetic energy for start-stops

bus_400_total_distance_weekend = 297.6       # Weekend
bus_400_trips_weekend = 48                   # Number of trips in a day, weekend
bus_400_stops = 5                    
bus_400_gallons_weekend = bus_400_total_distance_weekend/bus_mpg # Gallons consumed by bus 400
bus_400_litres_weekend = bus_400_gallons_weekend*4.546
bus_400_total_energy_weekend = bus_400_litres_weekend*diesel_energy_density # Energy equivalent
bus_400_trip_energy_weekend = bus_400_total_energy_weekend/bus_400_trips_weekend    # Energy for 1 trip
bus_400_kinetic_energy = 0.5*M*v**2  # Kinetic energy of bus 400
bus_400_total_stop_energy = bus_400_kinetic_energy*bus_400_stops # Recoverable kinetic energy for start-stops

bus_300_total_distance_weekend = 511.2        # Weekend
bus_300_trips_weekend = 72                    # Number of trips in a day, weekend
bus_300_stops = 26                    
bus_300_gallons_weekend = bus_300_total_distance_weekend/bus_mpg # Gallons consumed by bus 300
bus_300_litres_weekend = bus_300_gallons_weekend*4.546
bus_300_total_energy_weekend = bus_300_litres_weekend*diesel_energy_density # Energy equivalent
bus_300_trip_energy_weekend = bus_300_total_energy_weekend/bus_300_trips_weekend # Energy for 1 trip:
bus_300_kinetic_energy = 0.5*M*v**2 # Kinetic energy of bus 300
bus_300_total_stop_energy = bus_300_kinetic_energy*bus_300_stops # Recoverable kinetic energy for start-stops

bus_S5_total_distance_weekend = 532          # Weekend
bus_S5_trips_weekend = 38                    # Number of trips in a day
bus_S5_stops = 7                     
bus_S5_gallons_weekend = bus_S5_total_distance_weekend/bus_mpg # Gallons consumed by bus S5
bus_S5_litres_weekend = bus_S5_gallons_weekend*4.546
bus_S5_total_energy_weekend = bus_S5_litres_weekend*diesel_energy_density # Energy equivalent
bus_S5_trip_energy_weekend = bus_S5_total_energy_weekend/bus_S5_trips_weekend # Energy for 1 trip
bus_S5_kinetic_energy = 0.5*M*v**2  # Kinetic energy of bus S5
bus_S5_total_stop_energy = bus_S5_kinetic_energy*bus_S5_stops # Recoverable kinetic energy for start-stops

# Function for calculating inclination from road distance
def getinclination_2(elevation_previous,elevation_now,road_distance):
    stop_distance = road_distance
    theta = math.atan((elevation_previous-elevation_now)/stop_distance)
    return theta
             
'''
FOR 500
'''
    
data_500_outbound = {'Stop':  ['Oxford Rail Station', 'Oxford Magdalen Street', 'Summertown shops', 'Oxford Parkway Station',
                      'Oxford Parkway Park and Ride','Kidlington, Oxford motor park', 'Woodstock, Marlborough Arms'],
        'Latitude': [51.75311,51.75466,51.77678,51.80353,51.80325,51.82896,51.84759],
        'Longitude': [-1.26942,-1.25913,-1.26474,-1.275,-1.27328,-1.30759,-1.3538],
        'Elevation': [61,70,66,66,64,68,100],
        'Distance': [0,729,2490,3058,122,3706,3791]}
data_500_inbound = {'Stop':  ['Woodstock, Marlborough Arms','Kidlington, Oxford motor park','Oxford Parkway Park and Ride','Oxford Parkway Station',
                              'Summertown shops','Oxford Magdalen Street','Oxford Rail Station'],
        'Latitude': [51.84759,51.82896,51.80325,51.80353,51.77678,51.75466,51.75311],
        'Longitude': [-1.3538,-1.30759,-1.27328,-1.275,
                      -1.26474,-1.25913,-1.26942],
        'Elevation': [100,68,64,66,
                      66,70,61],
        'Distance': [0,3791,3706,122,
                     3058,2490,729]}

df_500_outbound = pd.DataFrame (data_500_outbound, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])
df_500_inbound = pd.DataFrame (data_500_inbound, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])

x_500 = df_500_outbound.Longitude[:]   # x coordinates for map
y_500 = df_500_outbound.Latitude[:]   # x coordinates for map

# FOR OUTBOUND
# Grouping stops:
grouped_stop = df_500_outbound.groupby(df_500_outbound["Stop"]) # can also group by a different column eg Times !
df_stop_1 = grouped_stop.get_group("Oxford Rail Station")
df_stop_2 = grouped_stop.get_group("Oxford Magdalen Street")
df_stop_3 = grouped_stop.get_group("Summertown shops")
df_stop_4 = grouped_stop.get_group("Oxford Parkway Station")
df_stop_5 = grouped_stop.get_group("Oxford Parkway Park and Ride")
df_stop_6 = grouped_stop.get_group("Kidlington, Oxford motor park")
df_stop_7 = grouped_stop.get_group("Woodstock, Marlborough Arms")
# Calculating inclinations from road distance NOTE THESE ARE IN RADIANS:
stop1_road_theta = 0  # We can't calculate inclination since we do not have the previous stop
#getinclination(coordinate_previous,coordinate_now,elevation_previous,elevation_now):
stop2_road_theta = getinclination_2(df_stop_1.iloc[0][3],df_stop_2.iloc[0][3],df_stop_2.iloc[0][4])
stop3_road_theta = getinclination_2(df_stop_2.iloc[0][3],df_stop_3.iloc[0][3],df_stop_3.iloc[0][4])
stop4_road_theta = getinclination_2(df_stop_3.iloc[0][3],df_stop_4.iloc[0][3],df_stop_4.iloc[0][4])
stop5_road_theta = getinclination_2(df_stop_4.iloc[0][3],df_stop_5.iloc[0][3],df_stop_5.iloc[0][4])
stop6_road_theta = getinclination_2(df_stop_5.iloc[0][3],df_stop_6.iloc[0][3],df_stop_6.iloc[0][4])
stop7_road_theta = getinclination_2(df_stop_6.iloc[0][3],df_stop_7.iloc[0][3],df_stop_7.iloc[0][4])
# Adding theta column:
df_500_outbound = df_500_outbound.assign(theta = [stop1_road_theta, stop2_road_theta, stop3_road_theta,
                                                  stop4_road_theta, stop5_road_theta, stop6_road_theta,
                                                  stop7_road_theta])
# Weight components
df_500_outbound = df_500_outbound.assign(weight_component = [Mg*math.sin(stop1_road_theta), Mg*math.sin(stop2_road_theta), Mg*math.sin(stop3_road_theta),
                                   Mg*math.sin(stop4_road_theta), Mg*math.sin(stop5_road_theta), Mg*math.sin(stop6_road_theta),
                                   Mg*math.sin(stop7_road_theta)])
# Time spent between each stop:
df_500_outbound = df_500_outbound.assign(time = df_500_outbound.Distance/v)
# Regenerative force:
df_500_outbound = df_500_outbound.assign(regenerative_force = df_500_outbound.weight_component - Fa)
# Available energy:
df_500_outbound = df_500_outbound.assign(available_energy = df_500_outbound.regenerative_force*v*df_500_outbound.time)
# Replacing all available energy by zero:
df_500_outbound.available_energy[df_500_outbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_500_outbound_total_braking_energy = sum(df_500_outbound.available_energy)
# Energy with regenerative system:
bus_500_outbound_regenerative_trip_energy = bus_500_trip_energy_weekend - bus_500_outbound_total_braking_energy

# FOR INBOUND
# Grouping stops:
grouped_stop = df_500_inbound.groupby(df_500_inbound["Stop"]) # can also group by a different column eg Times !
df_stop_1 = grouped_stop.get_group("Woodstock, Marlborough Arms")
df_stop_2 = grouped_stop.get_group("Kidlington, Oxford motor park")
df_stop_3 = grouped_stop.get_group("Oxford Parkway Park and Ride")
df_stop_4 = grouped_stop.get_group("Oxford Parkway Station")
df_stop_5 = grouped_stop.get_group("Summertown shops")
df_stop_6 = grouped_stop.get_group("Oxford Magdalen Street")
df_stop_7 = grouped_stop.get_group("Oxford Rail Station")
# Calculating inclinations from road distance NOTE THESE ARE IN RADIANS:
stop1_road_theta = 0  # We can't calculate inclination since we do not have the previous stop
#getinclination(coordinate_previous,coordinate_now,elevation_previous,elevation_now):
stop2_road_theta = getinclination_2(df_stop_1.iloc[0][3],df_stop_2.iloc[0][3],df_stop_2.iloc[0][4])
stop3_road_theta = getinclination_2(df_stop_2.iloc[0][3],df_stop_3.iloc[0][3],df_stop_3.iloc[0][4])
stop4_road_theta = getinclination_2(df_stop_3.iloc[0][3],df_stop_4.iloc[0][3],df_stop_4.iloc[0][4])
stop5_road_theta = getinclination_2(df_stop_4.iloc[0][3],df_stop_5.iloc[0][3],df_stop_5.iloc[0][4])
stop6_road_theta = getinclination_2(df_stop_5.iloc[0][3],df_stop_6.iloc[0][3],df_stop_6.iloc[0][4])
stop7_road_theta = getinclination_2(df_stop_6.iloc[0][3],df_stop_7.iloc[0][3],df_stop_7.iloc[0][4])
# Adding theta column:
df_500_inbound = df_500_inbound.assign(theta = [stop1_road_theta, stop2_road_theta, stop3_road_theta,
                                                stop4_road_theta, stop5_road_theta, stop6_road_theta,
                                                stop7_road_theta])
# Weight components
df_500_inbound = df_500_inbound.assign(weight_component = [Mg*math.sin(stop1_road_theta), Mg*math.sin(stop2_road_theta), Mg*math.sin(stop3_road_theta),
                                   Mg*math.sin(stop4_road_theta), Mg*math.sin(stop5_road_theta), Mg*math.sin(stop6_road_theta),
                                   Mg*math.sin(stop7_road_theta)])
# Time spent between each stop:
df_500_inbound = df_500_inbound.assign(time = df_500_inbound.Distance/v)
# Regenerative force:
df_500_inbound = df_500_inbound.assign(regenerative_force = df_500_inbound.weight_component - Fa)
# Available energy:
df_500_inbound = df_500_inbound.assign(available_energy = df_500_inbound.regenerative_force*v*df_500_inbound.time)
# Replacing all available energy by zero:
df_500_inbound.available_energy[df_500_inbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_500_inbound_total_braking_energy = sum(df_500_inbound.available_energy)
# Energy with regenerative system:
bus_500_inbound_regenerative_trip_energy = bus_500_trip_energy_weekend - bus_500_inbound_total_braking_energy

"""
For 400
"""

data_400_outbound = {'Stop':  ['Seacourt Park&Ride', 'Oxford, Westgate Shopping Centre', 'Oxford, St Aldates', 'Headington Shops',
                      'Thornhill Park&Ride'],
        'Latitude': [51.74548,51.74901,51.74994,51.76004,51.76228],
        'Longitude': [-1.26362,-1.26272,-1.25687,-1.21158,-1.18265],
        'Elevation': [59,59,65,108,103],
        'Distance': [0,1918,416,3313,2007]}
data_400_inbound = {'Stop':  ['Thornhill Park&Ride','Headington Shops','Oxford, St Aldates','Oxford, Westgate Shopping Centre',
                              'Seacourt Park&Ride'],
        'Latitude': [51.76228,51.76004,51.74994,51.74901,51.74548],
        'Longitude': [-1.18265,-1.21158,-1.25687,-1.26272,-1.26362],
        'Elevation': [103,108,65,59,59],
        'Distance': [0,2007,3313,416,1918]}

df_400_outbound = pd.DataFrame (data_400_outbound, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])
df_400_inbound = pd.DataFrame (data_400_inbound, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])

x_400 = df_400_outbound.Longitude[:]   # x coordinates for map
y_400 = df_400_outbound.Latitude[:]   # x coordinates for map

# FOR OUTBOUND
# Grouping stops:
grouped_stop = df_400_outbound.groupby(df_400_outbound["Stop"]) # can also group by a different column eg Times !
df_stop_1 = grouped_stop.get_group("Seacourt Park&Ride")
df_stop_2 = grouped_stop.get_group("Oxford, Westgate Shopping Centre")
df_stop_3 = grouped_stop.get_group("Oxford, St Aldates")
df_stop_4 = grouped_stop.get_group("Headington Shops")
df_stop_5 = grouped_stop.get_group("Thornhill Park&Ride")
# Calculating inclinations from road distance NOTE THESE ARE IN RADIANS:
stop1_road_theta = 0  # We can't calculate inclination since we do not have the previous stop
#getinclination(coordinate_previous,coordinate_now,elevation_previous,elevation_now):
stop2_road_theta = getinclination_2(df_stop_1.iloc[0][3],df_stop_2.iloc[0][3],df_stop_2.iloc[0][4])
stop3_road_theta = getinclination_2(df_stop_2.iloc[0][3],df_stop_3.iloc[0][3],df_stop_3.iloc[0][4])
stop4_road_theta = getinclination_2(df_stop_3.iloc[0][3],df_stop_4.iloc[0][3],df_stop_4.iloc[0][4])
stop5_road_theta = getinclination_2(df_stop_4.iloc[0][3],df_stop_5.iloc[0][3],df_stop_5.iloc[0][4])
# Adding theta column:
df_400_outbound = df_400_outbound.assign(theta = [stop1_road_theta, stop2_road_theta, stop3_road_theta,
                        stop4_road_theta, stop5_road_theta])
# Weight components
df_400_outbound = df_400_outbound.assign(weight_component = [Mg*math.sin(stop1_road_theta), Mg*math.sin(stop2_road_theta), Mg*math.sin(stop3_road_theta),
                                   Mg*math.sin(stop4_road_theta), Mg*math.sin(stop5_road_theta)])
# Time spent between each stop:
df_400_outbound = df_400_outbound.assign(time = df_400_outbound.Distance/v)
# Regenerative force:
df_400_outbound = df_400_outbound.assign(regenerative_force = df_400_outbound.weight_component - Fa)
# Available energy:
df_400_outbound = df_400_outbound.assign(available_energy = df_400_outbound.regenerative_force*v*df_400_outbound.time)
# Replacing all available energy by zero:
df_400_outbound.available_energy[df_400_outbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_400_outbound_total_braking_energy = sum(df_400_outbound.available_energy)
# Energy with regenerative system:
bus_400_outbound_regenerative_trip_energy = bus_400_trip_energy_weekend - bus_400_outbound_total_braking_energy

# FOR INBOUND
# Grouping stops:
grouped_stop = df_400_inbound.groupby(df_400_inbound["Stop"]) # can also group by a different column eg Times !
df_stop_1 = grouped_stop.get_group("Thornhill Park&Ride")
df_stop_2 = grouped_stop.get_group("Headington Shops")
df_stop_3 = grouped_stop.get_group("Oxford, St Aldates")
df_stop_4 = grouped_stop.get_group("Oxford, Westgate Shopping Centre")
df_stop_5 = grouped_stop.get_group("Seacourt Park&Ride")
# Calculating inclinations from road distance NOTE THESE ARE IN RADIANS:
stop1_road_theta = 0  # We can't calculate inclination since we do not have the previous stop
#getinclination(coordinate_previous,coordinate_now,elevation_previous,elevation_now):
stop2_road_theta = getinclination_2(df_stop_1.iloc[0][3],df_stop_2.iloc[0][3],df_stop_2.iloc[0][4])
stop3_road_theta = getinclination_2(df_stop_2.iloc[0][3],df_stop_3.iloc[0][3],df_stop_3.iloc[0][4])
stop4_road_theta = getinclination_2(df_stop_3.iloc[0][3],df_stop_4.iloc[0][3],df_stop_4.iloc[0][4])
stop5_road_theta = getinclination_2(df_stop_4.iloc[0][3],df_stop_5.iloc[0][3],df_stop_5.iloc[0][4])
# Adding theta column:
df_400_inbound = df_400_inbound.assign(theta = [stop1_road_theta, stop2_road_theta, stop3_road_theta,
                                                stop4_road_theta, stop5_road_theta])
# Weight components
df_400_inbound = df_400_inbound.assign(weight_component = [Mg*math.sin(stop1_road_theta), Mg*math.sin(stop2_road_theta), Mg*math.sin(stop3_road_theta),
                                   Mg*math.sin(stop4_road_theta), Mg*math.sin(stop5_road_theta)])
# Time spent between each stop:
df_400_inbound = df_400_inbound.assign(time = df_400_inbound.Distance/v)
# Regenerative force:
df_400_inbound = df_400_inbound.assign(regenerative_force = df_400_inbound.weight_component - Fa)
# Available energy:
df_400_inbound = df_400_inbound.assign(available_energy = df_400_inbound.regenerative_force*v*df_400_inbound.time)
# Replacing all available energy by zero:
df_400_inbound.available_energy[df_400_inbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_400_inbound_total_braking_energy = sum(df_400_inbound.available_energy)
# Energy with regenerative system:
bus_400_inbound_regenerative_trip_energy = bus_400_trip_energy_weekend - bus_400_inbound_total_braking_energy

"""
For 300
"""

data_300_outbound = {'Stop':  ['Redbridge Park and Ride','Queens Lane','Carfax','St Aldates',
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
                      72,66],
        'Distance': [0,2716,433,234,
                     1960,218,348,385,
                     336,438,474,518,
                     238,173,645,454,
                     490,342,528,206,
                     445,267,393,374,
                     429,982]}
data_300_inbound = {'Stop': ['Pear Tree Park & Ride','First Turn','Woodstock Close','Squitchey Lane',
                             'Osberton Road','South Parade','Beech Croft Road','Lathbury Road',
                             'St Margarets Road','Canterbury Road','Plantation Road','Radcliffe Infirmary',
                             'Magdalen Street','George Street','County Hall','Police Station',
                             'Whitehouse Road','Newton Road','Lake Street','Lincoln Road',
                             'Chatham Road','Canning Crescent','St Aldates','Carfax',
                             'Queens Lane','Redbridge Park and Ride'],
        'Latitude': [51.79374799403658,51.78565,51.78503,51.78299,
                     51.77952,51.77826,51.77435,51.77254,
                     51.7678,51.7653,51.76227,51.7601,
                     51.75466,51.75363,51.75151,51.74788,
                     51.74483,51.74188,51.73887,51.73656,
                     51.73516,51.7332,51.74994,51.75197,
                     51.75409,51.72979],
        'Longitude': [-1.2817626020596353,-1.27988,-1.27373,-1.26942,
                      -1.27052,-1.26722,-1.26586,-1.26521,
                      -1.26571,-1.26282,-1.26798,-1.26239,
                      -1.25913,-1.26103,-1.26131,-1.25659,
                      -1.26139,-1.25717,-1.25674,-1.25256,
                      -1.24805,-1.24797,-1.25687,-1.2578,
                      -1.25252,-1.24861],
        'Elevation': [66,72,74,73,
                      66,65,66,67,
                      68,68,63,68,
                      70,68,66,61,
                      61,57,58,58,
                      57,57,65,72,
                      71,57],
        'Distance': [0,982,429,374,
                     393,267,445,206,
                     528,342,490,454,
                     645,173,238,518,
                     474,438,336,385,
                     348,218,1960,234,
                     433,2716]}

df_300_outbound = pd.DataFrame (data_300_outbound, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])
df_300_inbound = pd.DataFrame (data_300_inbound, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])

x_300 = df_300_outbound.Longitude[:]   # x coordinates for map
y_300 = df_300_outbound.Latitude[:]   # x coordinates for map

# FOR OUTBOUND
# Grouping stops:
grouped_stop = df_300_outbound.groupby(df_300_outbound["Stop"]) # can also group by a different column eg Times !
df_stop_1 = grouped_stop.get_group("Redbridge Park and Ride")
df_stop_2 = grouped_stop.get_group("Queens Lane")
df_stop_3 = grouped_stop.get_group("Carfax")
df_stop_4 = grouped_stop.get_group("St Aldates")
df_stop_5 = grouped_stop.get_group("Canning Crescent")
df_stop_6 = grouped_stop.get_group("Chatham Road")
df_stop_7 = grouped_stop.get_group("Lincoln Road")
df_stop_8 = grouped_stop.get_group("Lake Street")
df_stop_9 = grouped_stop.get_group("Newton Road")
df_stop_10 = grouped_stop.get_group("Whitehouse Road")
df_stop_11 = grouped_stop.get_group("Police Station")
df_stop_12 = grouped_stop.get_group("County Hall")
df_stop_13 = grouped_stop.get_group("George Street")
df_stop_14 = grouped_stop.get_group("Magdalen Street")
df_stop_15 = grouped_stop.get_group("Radcliffe Infirmary")
df_stop_16 = grouped_stop.get_group("Plantation Road")
df_stop_17 = grouped_stop.get_group("Canterbury Road")
df_stop_18 = grouped_stop.get_group("St Margarets Road")
df_stop_19 = grouped_stop.get_group("Lathbury Road")
df_stop_20 = grouped_stop.get_group("Beech Croft Road")
df_stop_21 = grouped_stop.get_group("South Parade")
df_stop_22 = grouped_stop.get_group("Osberton Road")
df_stop_23 = grouped_stop.get_group("Squitchey Lane")
df_stop_24 = grouped_stop.get_group("Woodstock Close")
df_stop_25 = grouped_stop.get_group("First Turn")
df_stop_26 = grouped_stop.get_group("Pear Tree Park & Ride")
# Calculating inclinations from road distance NOTE THESE ARE IN RADIANS:
stop1_road_theta = 0  # We can't calculate inclination since we do not have the previous stop
#getinclination(coordinate_previous,coordinate_now,elevation_previous,elevation_now):
stop2_road_theta = getinclination_2(df_stop_1.iloc[0][3],df_stop_2.iloc[0][3],df_stop_2.iloc[0][4])
stop3_road_theta = getinclination_2(df_stop_2.iloc[0][3],df_stop_3.iloc[0][3],df_stop_3.iloc[0][4])
stop4_road_theta = getinclination_2(df_stop_3.iloc[0][3],df_stop_4.iloc[0][3],df_stop_4.iloc[0][4])
stop5_road_theta = getinclination_2(df_stop_4.iloc[0][3],df_stop_5.iloc[0][3],df_stop_5.iloc[0][4])
stop6_road_theta = getinclination_2(df_stop_5.iloc[0][3],df_stop_6.iloc[0][3],df_stop_6.iloc[0][4])
stop7_road_theta = getinclination_2(df_stop_6.iloc[0][3],df_stop_7.iloc[0][3],df_stop_7.iloc[0][4])
stop8_road_theta = getinclination_2(df_stop_7.iloc[0][3],df_stop_8.iloc[0][3],df_stop_8.iloc[0][4])
stop9_road_theta = getinclination_2(df_stop_8.iloc[0][3],df_stop_9.iloc[0][3],df_stop_9.iloc[0][4])
stop10_road_theta = getinclination_2(df_stop_9.iloc[0][3],df_stop_10.iloc[0][3],df_stop_10.iloc[0][4])
stop11_road_theta = getinclination_2(df_stop_10.iloc[0][3],df_stop_11.iloc[0][3],df_stop_11.iloc[0][4])
stop12_road_theta = getinclination_2(df_stop_11.iloc[0][3],df_stop_12.iloc[0][3],df_stop_12.iloc[0][4])
stop13_road_theta = getinclination_2(df_stop_12.iloc[0][3],df_stop_13.iloc[0][3],df_stop_13.iloc[0][4])
stop14_road_theta = getinclination_2(df_stop_13.iloc[0][3],df_stop_14.iloc[0][3],df_stop_14.iloc[0][4])
stop15_road_theta = getinclination_2(df_stop_14.iloc[0][3],df_stop_15.iloc[0][3],df_stop_15.iloc[0][4])
stop16_road_theta = getinclination_2(df_stop_15.iloc[0][3],df_stop_16.iloc[0][3],df_stop_16.iloc[0][4])
stop17_road_theta = getinclination_2(df_stop_16.iloc[0][3],df_stop_17.iloc[0][3],df_stop_17.iloc[0][4])
stop18_road_theta = getinclination_2(df_stop_17.iloc[0][3],df_stop_18.iloc[0][3],df_stop_18.iloc[0][4])
stop19_road_theta = getinclination_2(df_stop_18.iloc[0][3],df_stop_19.iloc[0][3],df_stop_19.iloc[0][4])
stop20_road_theta = getinclination_2(df_stop_19.iloc[0][3],df_stop_20.iloc[0][3],df_stop_20.iloc[0][4])
stop21_road_theta = getinclination_2(df_stop_20.iloc[0][3],df_stop_21.iloc[0][3],df_stop_21.iloc[0][4])
stop22_road_theta = getinclination_2(df_stop_21.iloc[0][3],df_stop_22.iloc[0][3],df_stop_22.iloc[0][4])
stop23_road_theta = getinclination_2(df_stop_22.iloc[0][3],df_stop_23.iloc[0][3],df_stop_23.iloc[0][4])
stop24_road_theta = getinclination_2(df_stop_23.iloc[0][3],df_stop_24.iloc[0][3],df_stop_24.iloc[0][4])
stop25_road_theta = getinclination_2(df_stop_24.iloc[0][3],df_stop_25.iloc[0][3],df_stop_25.iloc[0][4])
stop26_road_theta = getinclination_2(df_stop_25.iloc[0][3],df_stop_26.iloc[0][3],df_stop_26.iloc[0][4])
# Adding theta column:
df_300_outbound = df_300_outbound.assign(theta = [stop1_road_theta, stop2_road_theta, stop3_road_theta,
                                stop4_road_theta, stop5_road_theta, stop6_road_theta, 
                                stop7_road_theta, stop8_road_theta, stop9_road_theta, 
                                stop10_road_theta, stop11_road_theta, stop12_road_theta,
                                stop13_road_theta, stop14_road_theta, stop15_road_theta,
                                stop16_road_theta, stop17_road_theta, stop18_road_theta,
                                stop19_road_theta, stop20_road_theta, stop21_road_theta,
                                stop22_road_theta, stop23_road_theta, stop24_road_theta,
                                stop25_road_theta, stop26_road_theta])
# Weight components
df_300_outbound = df_300_outbound.assign(weight_component = [Mg*math.sin(stop1_road_theta), Mg*math.sin(stop2_road_theta), Mg*math.sin(stop3_road_theta),
                                           Mg*math.sin(stop4_road_theta), Mg*math.sin(stop5_road_theta), Mg*math.sin(stop6_road_theta),
                                           Mg*math.sin(stop7_road_theta), Mg*math.sin(stop8_road_theta), Mg*math.sin(stop9_road_theta),
                                           Mg*math.sin(stop10_road_theta), Mg*math.sin(stop11_road_theta), Mg*math.sin(stop12_road_theta),
                                           Mg*math.sin(stop13_road_theta), Mg*math.sin(stop14_road_theta), Mg*math.sin(stop15_road_theta),
                                           Mg*math.sin(stop16_road_theta), Mg*math.sin(stop17_road_theta), Mg*math.sin(stop18_road_theta),
                                           Mg*math.sin(stop19_road_theta), Mg*math.sin(stop20_road_theta), Mg*math.sin(stop21_road_theta),
                                           Mg*math.sin(stop22_road_theta), Mg*math.sin(stop23_road_theta), Mg*math.sin(stop24_road_theta),
                                           Mg*math.sin(stop25_road_theta), Mg*math.sin(stop26_road_theta)])
# Time spent between each stop:
df_300_outbound = df_300_outbound.assign(time = df_300_outbound.Distance/v)
# Regenerative force:
df_300_outbound = df_300_outbound.assign(regenerative_force = df_300_outbound.weight_component - Fa)
# Available energy:
df_300_outbound = df_300_outbound.assign(available_energy = df_300_outbound.regenerative_force*v*df_300_outbound.time)
# Replacing all available energy by zero:
df_300_outbound.available_energy[df_300_outbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_300_outbound_total_braking_energy = sum(df_300_outbound.available_energy)
# Energy with regenerative system:
bus_300_outbound_regenerative_trip_energy = bus_300_trip_energy_weekend - bus_300_outbound_total_braking_energy

# FOR INBOUND
# Grouping stops:
grouped_stop = df_300_inbound.groupby(df_300_inbound["Stop"]) # can also group by a different column eg Times !
df_stop_1 = grouped_stop.get_group("Pear Tree Park & Ride")
df_stop_2 = grouped_stop.get_group("First Turn")
df_stop_3 = grouped_stop.get_group("Woodstock Close")
df_stop_4 = grouped_stop.get_group("Squitchey Lane")
df_stop_5 = grouped_stop.get_group("Osberton Road")
df_stop_6 = grouped_stop.get_group("South Parade")
df_stop_7 = grouped_stop.get_group("Beech Croft Road")
df_stop_8 = grouped_stop.get_group("Lathbury Road")
df_stop_9 = grouped_stop.get_group("St Margarets Road")
df_stop_10 = grouped_stop.get_group("Canterbury Road")
df_stop_11 = grouped_stop.get_group("Plantation Road")
df_stop_12 = grouped_stop.get_group("Radcliffe Infirmary")
df_stop_13 = grouped_stop.get_group("Magdalen Street")
df_stop_14 = grouped_stop.get_group("George Street")
df_stop_15 = grouped_stop.get_group("County Hall")
df_stop_16 = grouped_stop.get_group("Police Station")
df_stop_17 = grouped_stop.get_group("Whitehouse Road")
df_stop_18 = grouped_stop.get_group("Newton Road")
df_stop_19 = grouped_stop.get_group("Lake Street")
df_stop_20 = grouped_stop.get_group("Lincoln Road")
df_stop_21 = grouped_stop.get_group("Chatham Road")
df_stop_22 = grouped_stop.get_group("Canning Crescent")
df_stop_23 = grouped_stop.get_group("St Aldates")
df_stop_24 = grouped_stop.get_group("Carfax")
df_stop_25 = grouped_stop.get_group("Queens Lane")
df_stop_26 = grouped_stop.get_group("Redbridge Park and Ride")
# Calculating inclinations from road distance NOTE THESE ARE IN RADIANS:
stop1_road_theta = 0  # We can't calculate inclination since we do not have the previous stop
#getinclination(coordinate_previous,coordinate_now,elevation_previous,elevation_now):
stop2_road_theta = getinclination_2(df_stop_1.iloc[0][3],df_stop_2.iloc[0][3],df_stop_2.iloc[0][4])
stop3_road_theta = getinclination_2(df_stop_2.iloc[0][3],df_stop_3.iloc[0][3],df_stop_3.iloc[0][4])
stop4_road_theta = getinclination_2(df_stop_3.iloc[0][3],df_stop_4.iloc[0][3],df_stop_4.iloc[0][4])
stop5_road_theta = getinclination_2(df_stop_4.iloc[0][3],df_stop_5.iloc[0][3],df_stop_5.iloc[0][4])
stop6_road_theta = getinclination_2(df_stop_5.iloc[0][3],df_stop_6.iloc[0][3],df_stop_6.iloc[0][4])
stop7_road_theta = getinclination_2(df_stop_6.iloc[0][3],df_stop_7.iloc[0][3],df_stop_7.iloc[0][4])
stop8_road_theta = getinclination_2(df_stop_7.iloc[0][3],df_stop_8.iloc[0][3],df_stop_8.iloc[0][4])
stop9_road_theta = getinclination_2(df_stop_8.iloc[0][3],df_stop_9.iloc[0][3],df_stop_9.iloc[0][4])
stop10_road_theta = getinclination_2(df_stop_9.iloc[0][3],df_stop_10.iloc[0][3],df_stop_10.iloc[0][4])
stop11_road_theta = getinclination_2(df_stop_10.iloc[0][3],df_stop_11.iloc[0][3],df_stop_11.iloc[0][4])
stop12_road_theta = getinclination_2(df_stop_11.iloc[0][3],df_stop_12.iloc[0][3],df_stop_12.iloc[0][4])
stop13_road_theta = getinclination_2(df_stop_12.iloc[0][3],df_stop_13.iloc[0][3],df_stop_13.iloc[0][4])
stop14_road_theta = getinclination_2(df_stop_13.iloc[0][3],df_stop_14.iloc[0][3],df_stop_14.iloc[0][4])
stop15_road_theta = getinclination_2(df_stop_14.iloc[0][3],df_stop_15.iloc[0][3],df_stop_15.iloc[0][4])
stop16_road_theta = getinclination_2(df_stop_15.iloc[0][3],df_stop_16.iloc[0][3],df_stop_16.iloc[0][4])
stop17_road_theta = getinclination_2(df_stop_16.iloc[0][3],df_stop_17.iloc[0][3],df_stop_17.iloc[0][4])
stop18_road_theta = getinclination_2(df_stop_17.iloc[0][3],df_stop_18.iloc[0][3],df_stop_18.iloc[0][4])
stop19_road_theta = getinclination_2(df_stop_18.iloc[0][3],df_stop_19.iloc[0][3],df_stop_19.iloc[0][4])
stop20_road_theta = getinclination_2(df_stop_19.iloc[0][3],df_stop_20.iloc[0][3],df_stop_20.iloc[0][4])
stop21_road_theta = getinclination_2(df_stop_20.iloc[0][3],df_stop_21.iloc[0][3],df_stop_21.iloc[0][4])
stop22_road_theta = getinclination_2(df_stop_21.iloc[0][3],df_stop_22.iloc[0][3],df_stop_22.iloc[0][4])
stop23_road_theta = getinclination_2(df_stop_22.iloc[0][3],df_stop_23.iloc[0][3],df_stop_23.iloc[0][4])
stop24_road_theta = getinclination_2(df_stop_23.iloc[0][3],df_stop_24.iloc[0][3],df_stop_24.iloc[0][4])
stop25_road_theta = getinclination_2(df_stop_24.iloc[0][3],df_stop_25.iloc[0][3],df_stop_25.iloc[0][4])
stop26_road_theta = getinclination_2(df_stop_25.iloc[0][3],df_stop_26.iloc[0][3],df_stop_26.iloc[0][4])
# Adding theta column:
df_300_inbound = df_300_inbound.assign(theta = [stop1_road_theta, stop2_road_theta, stop3_road_theta,
                                                stop4_road_theta, stop5_road_theta, stop6_road_theta, 
                                                stop7_road_theta, stop8_road_theta, stop9_road_theta, 
                                                stop10_road_theta, stop11_road_theta, stop12_road_theta,
                                                stop13_road_theta, stop14_road_theta, stop15_road_theta,
                                                stop16_road_theta, stop17_road_theta, stop18_road_theta,
                                                stop19_road_theta, stop20_road_theta, stop21_road_theta,
                                                stop22_road_theta, stop23_road_theta, stop24_road_theta,
                                                stop25_road_theta, stop26_road_theta])
# Weight components
df_300_inbound = df_300_inbound.assign(weight_component = [Mg*math.sin(stop1_road_theta), Mg*math.sin(stop2_road_theta), Mg*math.sin(stop3_road_theta),
                                                           Mg*math.sin(stop4_road_theta), Mg*math.sin(stop5_road_theta), Mg*math.sin(stop6_road_theta),
                                                           Mg*math.sin(stop7_road_theta), Mg*math.sin(stop8_road_theta), Mg*math.sin(stop9_road_theta),
                                                           Mg*math.sin(stop10_road_theta), Mg*math.sin(stop11_road_theta), Mg*math.sin(stop12_road_theta),
                                                           Mg*math.sin(stop13_road_theta), Mg*math.sin(stop14_road_theta), Mg*math.sin(stop15_road_theta),
                                                           Mg*math.sin(stop16_road_theta), Mg*math.sin(stop17_road_theta), Mg*math.sin(stop18_road_theta),
                                                           Mg*math.sin(stop19_road_theta), Mg*math.sin(stop20_road_theta), Mg*math.sin(stop21_road_theta),
                                                           Mg*math.sin(stop22_road_theta), Mg*math.sin(stop23_road_theta), Mg*math.sin(stop24_road_theta),
                                                           Mg*math.sin(stop25_road_theta), Mg*math.sin(stop26_road_theta)])
# Time spent between each stop:
df_300_inbound = df_300_inbound.assign(time = df_300_inbound.Distance/v)
# Regenerative force:
df_300_inbound = df_300_inbound.assign(regenerative_force = df_300_inbound.weight_component - Fa)
# Available energy:
df_300_inbound = df_300_inbound.assign(available_energy = df_300_inbound.regenerative_force*v*df_300_inbound.time)
# Replacing all available energy by zero:
df_300_inbound.available_energy[df_300_inbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_300_inbound_total_braking_energy = sum(df_300_inbound.available_energy)
# Energy with regenerative system:
bus_300_inbound_regenerative_trip_energy = bus_300_trip_energy_weekend - bus_300_inbound_total_braking_energy

"""
For S5
"""

data_S5_outbound = {'Stop':  ['Oxford City Centre Magdalen Street','Summertown Shops','Gosford Kings Arms','Kingsmere Bicester Park and Ride',
                     'Bicester, Bicester Village','Bicester Town Centre Manorsfield Road','Glory Farm Bicester Road'],
        'Latitude': [51.75466,51.77748,51.81788,51.8861,
                     51.89244,51.8975,51.90947],
        'Longitude': [-1.25913,-1.26491,-1.2726,-1.17199,
                      -1.14937,-1.15271,-1.13795],
        'Elevation': [70,67,63,65,
                      70,72,78],
        'Distance': [0,2569,4523,10260,
                     1705,607,1672]}
data_S5_inbound = {'Stop': ['Glory Farm Bicester Road','Bicester Town Centre Manorsfield Road','Bicester, Bicester Village','Kingsmere Bicester Park and Ride',
                            'Gosford Kings Arms','Summertown Shops','Oxford City Centre Magdalen Street'],
        'Latitude': [51.90947,51.8975,51.89244,51.8861,
                     51.81788,51.77748,51.75466],
        'Longitude': [-1.13795,-1.15271,-1.14937,-1.17199,
                      -1.2726,-1.26491,-1.25913],
        'Elevation': [78,72,70,65,
                      63,67,70],
        'Distance': [0,1672,607,1705,
                     10260,4523,2569]}

df_S5_outbound = pd.DataFrame (data_S5_outbound, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])
df_S5_inbound = pd.DataFrame (data_S5_inbound, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])

x_S5 = df_S5_outbound.Longitude[:]   # x coordinates for map
y_S5 = df_S5_outbound.Latitude[:]   # x coordinates for map

# FOR OUTBOUND
# Grouping stops:
grouped_stop = df_S5_outbound.groupby(df_S5_outbound["Stop"]) # can also group by a different column eg Times !
df_stop_1 = grouped_stop.get_group("Oxford City Centre Magdalen Street")
df_stop_2 = grouped_stop.get_group("Summertown Shops")
df_stop_3 = grouped_stop.get_group("Gosford Kings Arms")
df_stop_4 = grouped_stop.get_group("Kingsmere Bicester Park and Ride")
df_stop_5 = grouped_stop.get_group("Bicester, Bicester Village")
df_stop_6 = grouped_stop.get_group("Bicester Town Centre Manorsfield Road")
df_stop_7 = grouped_stop.get_group("Glory Farm Bicester Road")
# Calculating inclinations from road distance NOTE THESE ARE IN RADIANS:
stop1_road_theta = 0  # We can't calculate inclination since we do not have the previous stop
#getinclination(coordinate_previous,coordinate_now,elevation_previous,elevation_now):
stop2_road_theta = getinclination_2(df_stop_1.iloc[0][3],df_stop_2.iloc[0][3],df_stop_2.iloc[0][4])
stop3_road_theta = getinclination_2(df_stop_2.iloc[0][3],df_stop_3.iloc[0][3],df_stop_3.iloc[0][4])
stop4_road_theta = getinclination_2(df_stop_3.iloc[0][3],df_stop_4.iloc[0][3],df_stop_4.iloc[0][4])
stop5_road_theta = getinclination_2(df_stop_4.iloc[0][3],df_stop_5.iloc[0][3],df_stop_5.iloc[0][4])
stop6_road_theta = getinclination_2(df_stop_5.iloc[0][3],df_stop_6.iloc[0][3],df_stop_6.iloc[0][4])
stop7_road_theta = getinclination_2(df_stop_6.iloc[0][3],df_stop_7.iloc[0][3],df_stop_7.iloc[0][4])
# Adding theta column:
df_S5_outbound = df_S5_outbound.assign(theta = [stop1_road_theta, stop2_road_theta, stop3_road_theta,
                                stop4_road_theta, stop5_road_theta, stop6_road_theta, 
                                stop7_road_theta])
# Weight components
df_S5_outbound = df_S5_outbound.assign(weight_component = [Mg*math.sin(stop1_road_theta), Mg*math.sin(stop2_road_theta), Mg*math.sin(stop3_road_theta),
                                           Mg*math.sin(stop4_road_theta), Mg*math.sin(stop5_road_theta), Mg*math.sin(stop6_road_theta),
                                           Mg*math.sin(stop7_road_theta)])
# Time spent between each stop:
df_S5_outbound = df_S5_outbound.assign(time = df_S5_outbound.Distance/v)
# Regenerative force:
df_S5_outbound = df_S5_outbound.assign(regenerative_force = df_S5_outbound.weight_component - Fa)
# Available energy:
df_S5_outbound = df_S5_outbound.assign(available_energy = df_S5_outbound.regenerative_force*v*df_S5_outbound.time)
# Replacing all available energy by zero:
df_S5_outbound.available_energy[df_S5_outbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_S5_outbound_total_braking_energy = sum(df_S5_outbound.available_energy)
# Energy with regenerative system:
bus_S5_outbound_regenerative_trip_energy = bus_S5_trip_energy_weekend - bus_S5_outbound_total_braking_energy

# FOR INBOUND
# Grouping stops:
grouped_stop = df_S5_inbound.groupby(df_S5_inbound["Stop"]) # can also group by a different column eg Times !
df_stop_1 = grouped_stop.get_group("Glory Farm Bicester Road")
df_stop_2 = grouped_stop.get_group("Bicester Town Centre Manorsfield Road")
df_stop_3 = grouped_stop.get_group("Bicester, Bicester Village")
df_stop_4 = grouped_stop.get_group("Kingsmere Bicester Park and Ride")
df_stop_5 = grouped_stop.get_group("Gosford Kings Arms")
df_stop_6 = grouped_stop.get_group("Summertown Shops")
df_stop_7 = grouped_stop.get_group("Oxford City Centre Magdalen Street")
# Calculating inclinations from road distance NOTE THESE ARE IN RADIANS:
stop1_road_theta = 0  # We can't calculate inclination since we do not have the previous stop
#getinclination(coordinate_previous,coordinate_now,elevation_previous,elevation_now):
stop2_road_theta = getinclination_2(df_stop_1.iloc[0][3],df_stop_2.iloc[0][3],df_stop_2.iloc[0][4])
stop3_road_theta = getinclination_2(df_stop_2.iloc[0][3],df_stop_3.iloc[0][3],df_stop_3.iloc[0][4])
stop4_road_theta = getinclination_2(df_stop_3.iloc[0][3],df_stop_4.iloc[0][3],df_stop_4.iloc[0][4])
stop5_road_theta = getinclination_2(df_stop_4.iloc[0][3],df_stop_5.iloc[0][3],df_stop_5.iloc[0][4])
stop6_road_theta = getinclination_2(df_stop_5.iloc[0][3],df_stop_6.iloc[0][3],df_stop_6.iloc[0][4])
stop7_road_theta = getinclination_2(df_stop_6.iloc[0][3],df_stop_7.iloc[0][3],df_stop_7.iloc[0][4])
# Adding theta column:
df_S5_inbound = df_S5_inbound.assign(theta = [stop1_road_theta, stop2_road_theta, stop3_road_theta,
                                              stop4_road_theta, stop5_road_theta, stop6_road_theta, 
                                              stop7_road_theta])
# Weight components
df_S5_inbound = df_S5_inbound.assign(weight_component = [Mg*math.sin(stop1_road_theta), Mg*math.sin(stop2_road_theta), Mg*math.sin(stop3_road_theta),
                                                         Mg*math.sin(stop4_road_theta), Mg*math.sin(stop5_road_theta), Mg*math.sin(stop6_road_theta),
                                                         Mg*math.sin(stop7_road_theta)])
# Time spent between each stop:
df_S5_inbound = df_S5_inbound.assign(time = df_S5_inbound.Distance/v)
# Regenerative force:
df_S5_inbound = df_S5_inbound.assign(regenerative_force = df_S5_inbound.weight_component - Fa)
# Available energy:
df_S5_inbound = df_S5_inbound.assign(available_energy = df_S5_inbound.regenerative_force*v*df_S5_inbound.time)
# Replacing all available energy by zero:
df_S5_inbound.available_energy[df_S5_inbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_S5_inbound_total_braking_energy = sum(df_S5_inbound.available_energy)
# Energy with regenerative system:
bus_S5_inbound_regenerative_trip_energy = bus_S5_trip_energy_weekend - bus_S5_inbound_total_braking_energy


"""
Plotting
"""
data_energies = {'Type':  ['A', 'B','C'],
                 'Trip energies': [bus_500_trip_energy_weekend/(10**6), bus_500_outbound_regenerative_trip_energy/(10**6), (bus_500_outbound_regenerative_trip_energy-bus_500_total_stop_energy)/(10**6)]}

df_energies = pd.DataFrame (data_energies, columns = ['Type','Trip energies'])
df_energies["Trip energies"]=df_energies["Trip energies"].astype(float) #casts the distance column as floats

# Plotting coordinates
plt.plot(x_500, y_500, c='r', marker='.') # Plotting 500 stops
plt.plot(x_500[0], y_500[0], c='r', marker='s')  # Plotting 500 first station
plt.plot(x_500[len(x_500)-1], y_500[len(x_500)-1], c='r', marker='s')  # Plotting 500 last station

plt.plot(x_400, y_400, c='b', marker='.') # Plotting 400 stops
plt.plot(x_400[0], y_400[0], c='b', marker='s')  # Plotting 400 first station
plt.plot(x_400[len(x_400)-1], y_400[len(x_400)-1], c='b', marker='s')  # Plotting 400 last station

plt.plot(x_300, y_300, c='g', marker='.') # Plotting 300 stops
plt.plot(x_300[0], y_300[0], c='g', marker='s')  # Plotting 400 first station
plt.plot(x_300[len(x_300)-1], y_300[len(x_300)-1], c='g', marker='s')  # Plotting 400 last station

plt.plot(x_S5, y_S5, c='m', marker='.') # Plotting S5 stops
plt.plot(x_S5[0], y_S5[0], c='m', marker='s')  # Plotting 400 first station
plt.plot(x_S5[len(x_S5)-1], y_S5[len(x_S5)-1], c='m', marker='s')  # Plotting 400 last station
plt.savefig('Figure.svg', format='svg', dpi=1200)
plt.axis('off') 
red_patch = mpatches.Patch(color='red', label='500 (Oxford Parkway Park&Ride)')
blue_patch = mpatches.Patch(color='blue', label='400 (Seacourt and Thornhill Park&Ride)')
green_patch = mpatches.Patch(color='green',label='300 (Redbridge and Pear Tree Park&Ride)')
magenta_patch = mpatches.Patch(color='magenta',label='S5 (Bicester Park&Ride)')
plt.legend(handles=[red_patch,blue_patch,green_patch,magenta_patch])
plt.xlim(-1.4,-1.1)
plt.ylim((51.7,52))
plt.savefig('Parkandrides.svg', format='svg', dpi=1200)
plt.show()

# Returning energy saved

bus_500_outbound_RBS_energy_saved = (bus_500_outbound_total_braking_energy+bus_500_total_stop_energy)/(10**6)
bus_500_inbound_RBS_energy_saved = (bus_500_inbound_total_braking_energy+bus_500_total_stop_energy)/(10**6)
bus_400_outbound_RBS_energy_saved = (bus_400_outbound_total_braking_energy+bus_400_total_stop_energy)/(10**6)
bus_400_inbound_RBS_energy_saved = (bus_400_inbound_total_braking_energy+bus_400_total_stop_energy)/(10**6)
bus_300_outbound_RBS_energy_saved = (bus_300_outbound_total_braking_energy+bus_300_total_stop_energy)/(10**6)
bus_300_inbound_RBS_energy_saved = (bus_300_inbound_total_braking_energy+bus_300_total_stop_energy)/(10**6)
bus_S5_outbound_RBS_energy_saved = (bus_S5_outbound_total_braking_energy+bus_S5_total_stop_energy)/(10**6)
bus_S5_inbound_RBS_energy_saved = (bus_S5_inbound_total_braking_energy+bus_S5_total_stop_energy)/(10**6)

print('Bus 500 outbound regenerative energy in MJ = ', bus_500_outbound_RBS_energy_saved)
print('Bus 500 inbound regenerative energy in MJ = ', bus_500_inbound_RBS_energy_saved)
print('Bus 400 outbound regenerative energy in MJ = ', bus_400_outbound_RBS_energy_saved)
print('Bus 400 inbound regenerative energy in MJ = ', bus_400_inbound_RBS_energy_saved)
print('Bus 300 outbound regenerative energy in MJ = ', bus_300_outbound_RBS_energy_saved)
print('Bus 300 inbound regenerative energy in MJ = ', bus_300_inbound_RBS_energy_saved)
print('Bus S5 outbound regenerative energy in MJ = ', bus_S5_outbound_RBS_energy_saved)
print('Bus S5 inbound regenerative energy in MJ = ', bus_S5_inbound_RBS_energy_saved)

# Creating dataframe:
data_saved_energies = {'Route':  ['500 (outbound)','500 (inbound)','400 (outbound)','400 (inbound)',
                                  '300 (outbound)','300 (inbound)','S5 (outbound)','S5 (inbound)'],
                       'Energy saved trough RBS for one trip [MJ]': [bus_500_outbound_RBS_energy_saved,bus_500_inbound_RBS_energy_saved,
                                                        bus_400_outbound_RBS_energy_saved,bus_400_inbound_RBS_energy_saved,
                                                        bus_300_outbound_RBS_energy_saved,bus_300_inbound_RBS_energy_saved,
                                                        bus_S5_outbound_RBS_energy_saved,bus_S5_inbound_RBS_energy_saved],
                       'Energy saved trough RBS one year [MJ]': [bus_500_outbound_RBS_energy_saved*bus_500_trips_weekend*365*(5/7),bus_500_inbound_RBS_energy_saved*bus_500_trips_weekend*365*(5/7),
                                                                 bus_400_outbound_RBS_energy_saved*bus_400_trips_weekend*365*(5/7),bus_400_inbound_RBS_energy_saved*bus_400_trips_weekend*365*(5/7),
                                                                 bus_300_outbound_RBS_energy_saved*bus_300_trips_weekend*365*(5/7),bus_300_inbound_RBS_energy_saved*bus_300_trips_weekend*365*(5/7),
                                                                 bus_S5_outbound_RBS_energy_saved*bus_S5_trips_weekend*365*(5/7),bus_S5_inbound_RBS_energy_saved*bus_S5_trips_weekend*365*(5/7)]}

df_saved_energies = pd.DataFrame (data_saved_energies, columns = ['Route','Energy saved trough RBS [MJ]'])

df_saved_energies = df_saved_energies.assign(kg_hydrongen_saved_trip = [(bus_500_outbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency,
                                                                        (bus_500_inbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency,
                                                                        (bus_400_outbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency,
                                                                        (bus_400_inbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency,
                                                                        (bus_300_outbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency,
                                                                        (bus_300_inbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency,
                                                                        (bus_S5_outbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency,
                                                                        (bus_S5_inbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency])

df_saved_energies = df_saved_energies.assign(kg_hydrongen_saved_year = [((bus_500_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_500_trips_weekend*365*(5/7))/hydrogen_energy_efficiency,
                                                                        ((bus_500_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_500_trips_weekend*365*(5/7))/hydrogen_energy_efficiency,
                                                                        ((bus_400_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_400_trips_weekend*365*(5/7))/hydrogen_energy_efficiency,
                                                                        ((bus_400_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_400_trips_weekend*365*(5/7))/hydrogen_energy_efficiency,
                                                                        ((bus_300_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_300_trips_weekend*365*(5/7))/hydrogen_energy_efficiency,
                                                                        ((bus_300_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_300_trips_weekend*365*(5/7))/hydrogen_energy_efficiency,
                                                                        ((bus_S5_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_S5_trips_weekend*365*(5/7))/hydrogen_energy_efficiency,
                                                                        ((bus_S5_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_S5_trips_weekend*365*(5/7))/hydrogen_energy_efficiency])

df_saved_energies = df_saved_energies.assign(kg_hydrongen_saved_weekend = [((bus_500_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_500_trips_weekend)/hydrogen_energy_efficiency,
                                                                        ((bus_500_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_500_trips_weekend)/hydrogen_energy_efficiency,
                                                                        ((bus_400_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_400_trips_weekend)/hydrogen_energy_efficiency,
                                                                        ((bus_400_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_400_trips_weekend)/hydrogen_energy_efficiency,
                                                                        ((bus_300_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_300_trips_weekend)/hydrogen_energy_efficiency,
                                                                        ((bus_300_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_300_trips_weekend)/hydrogen_energy_efficiency,
                                                                        ((bus_S5_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_S5_trips_weekend)/hydrogen_energy_efficiency,
                                                                        ((bus_S5_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_S5_trips_weekend)/hydrogen_energy_efficiency])
print(df_saved_energies)
df_saved_energies.to_csv('saved_energies_weekends.csv', index=False)

