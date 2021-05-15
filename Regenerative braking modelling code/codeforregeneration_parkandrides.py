# Note: Weekday values are used 
# NOTE: This code borrows a similar code structure code used for route modelling

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
hydrogen_energy_density = 120              #MJ/kg
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

# Route parameters:
bus_500_total_distance = 187     # Weekday
bus_500_trips = 22               # Number of trips in a day, weekday
bus_500_stops = 7                # Weekday

bus_400_total_distance = 365.8       # Weekday
bus_400_trips = 59                   # Number of trips in a day
bus_400_stops = 5                    # Weekday

bus_300_total_distance = 511.2        # Weekday
bus_300_trips = 72                    # Number of trips in a day
bus_300_stops = 26                    # Weekday

bus_S5_total_distance = 742          # Weekday
bus_S5_trips = 53                    # Number of trips in a day
bus_S5_stops = 7                     # Weekday


# Function for calculating distance between coordinates (this function is not working as of Jan 20 2021):
def getdistance(coordinate_previous,coordinate_now):
    # Extracting coordinates and converting to radians:
    latitude_previous = coordinate_previous.iloc[0]*math.pi/180
    latitude_now = coordinate_now.iloc[0]*math.pi/180
    
    longitude_previous = coordinate_previous.iloc[1]*math.pi/180
    longitude_now = coordinate_now.iloc[1]*math.pi/180
    
    phi = (latitude_now-latitude_previous)
    lam = (longitude_now-longitude_previous)
    a = (math.sin(phi/2))**2 + math.cos(latitude_previous)*math.cos(latitude_now)*(math.sin(lam/2))**2
    c = math.atan2(a**0.5, (1-a)**0.5)*2
    d = R*c
    return d

# Function for calculating inclination from coordinates
def getinclination_1(coordinate_previous,coordinate_now,elevation_previous,elevation_now):
    stop_distance = getdistance(coordinate_previous,coordinate_now)
    theta = math.atan((elevation_previous-elevation_now)/stop_distance)
    return theta

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

df_500_outbound = pd.DataFrame (data_500_outbound, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])

x_500 = df_500_outbound.Longitude[:]   # x coordinates for map
y_500 = df_500_outbound.Latitude[:]   # x coordinates for map

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

# Air resistance force:
Fa = 0.5*Cd*rho*v**2

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
# Finding gallons consumed by bus 5
bus_500_gallons = bus_500_total_distance/bus_mpg
bus_500_litres = bus_500_gallons*4.546
# Energy equivalent:
bus_500_total_energy = bus_500_litres*diesel_energy_density
# Energy for 1 trip:
bus_500_trip_energy = bus_500_total_energy/bus_500_trips
# Energy with regenerative system:
bus_500_outbound_regenerative_trip_energy = bus_500_trip_energy - bus_500_outbound_total_braking_energy
# Bus kinetic energy:
bus_500_kinetic_energy = 0.5*M*v**2
# Recoverable kinetic energy for start-stops
bus_500_total_stop_energy = bus_500_kinetic_energy*bus_500_stops
print(df_500_outbound)

"""
For 400
"""

data_400_outbound = {'Stop':  ['Seacourt Park&Ride', 'Oxford, Westgate Shopping Centre', 'Oxford, St Aldates', 'Headington Shops',
                      'Thornhill Park&Ride'],
        'Latitude': [51.74548,51.74901,51.74994,51.76004,51.76228],
        'Longitude': [-1.26362,-1.26272,-1.25687,-1.21158,-1.18265],
        'Elevation': [59,59,65,108,103],
        'Distance': [0,1918,416,3313,2007]}

df_400_outbound = pd.DataFrame (data_400_outbound, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])

x_400 = df_400_outbound.Longitude[:]   # x coordinates for map
y_400 = df_400_outbound.Latitude[:]   # x coordinates for map

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

# Air resistance force:
Fa = 0.5*Cd*rho*v**2

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
# Finding gallons consumed by bus 5
bus_400_gallons = bus_400_total_distance/bus_mpg
bus_400_litres = bus_400_gallons*4.546
# Energy equivalent:
bus_400_total_energy = bus_400_litres*diesel_energy_density
# Energy for 1 trip:
bus_400_trip_energy = bus_400_total_energy/bus_400_trips
# Energy with regenerative system:
bus_400_outbound_regenerative_trip_energy = bus_400_trip_energy - bus_400_outbound_total_braking_energy
# Bus kinetic energy:
bus_400_kinetic_energy = 0.5*M*v**2
# Recoverable kinetic energy for start-stops
bus_400_total_stop_energy = bus_400_kinetic_energy*bus_400_stops
print(df_400_outbound)

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

df_300_outbound = pd.DataFrame (data_300_outbound, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])

x_300 = df_300_outbound.Longitude[:]   # x coordinates for map
y_300 = df_300_outbound.Latitude[:]   # x coordinates for map

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

# Air resistance force:
Fa = 0.5*Cd*rho*v**2

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
# Finding gallons consumed by bus 5
bus_300_gallons = bus_300_total_distance/bus_mpg
bus_300_litres = bus_300_gallons*4.546
# Energy equivalent:
bus_300_total_energy = bus_300_litres*diesel_energy_density
# Energy for 1 trip:
bus_300_trip_energy = bus_300_total_energy/bus_400_trips
# Energy with regenerative system:
bus_300_outbound_regenerative_trip_energy = bus_300_trip_energy - bus_300_outbound_total_braking_energy
# Bus kinetic energy:
bus_300_kinetic_energy = 0.5*M*v**2
# Recoverable kinetic energy for start-stops
bus_300_total_stop_energy = bus_300_kinetic_energy*bus_300_stops
print(df_300_outbound)

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

df_S5_outbound = pd.DataFrame (data_S5_outbound, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])

x_S5 = df_S5_outbound.Longitude[:]   # x coordinates for map
y_S5 = df_S5_outbound.Latitude[:]   # x coordinates for map

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

# Air resistance force:
Fa = 0.5*Cd*rho*v**2

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
# Finding gallons consumed by bus 5
bus_S5_gallons = bus_S5_total_distance/bus_mpg
bus_S5_litres = bus_S5_gallons*4.546
# Energy equivalent:
bus_S5_total_energy = bus_S5_litres*diesel_energy_density
# Energy for 1 trip:
bus_S5_trip_energy = bus_S5_total_energy/bus_S5_trips
# Energy with regenerative system:
bus_S5_outbound_regenerative_trip_energy = bus_S5_trip_energy - bus_S5_outbound_total_braking_energy
# Bus kinetic energy:
bus_S5_kinetic_energy = 0.5*M*v**2
# Recoverable kinetic energy for start-stops
bus_S5_total_stop_energy = bus_S5_kinetic_energy*bus_S5_stops
print(df_S5_outbound)
    
# Plotting:
# data to plot
#n_groups = 5
# Bus = {early, mid, afternoon, evening, late}
"""
Plotting
"""
data_energies = {'Type':  ['A', 'B','C'],
                 'Trip energies': [bus_500_trip_energy/(10**6), bus_500_outbound_regenerative_trip_energy/(10**6), (bus_500_outbound_regenerative_trip_energy-bus_500_total_stop_energy)/(10**6)]}

df_energies = pd.DataFrame (data_energies, columns = ['Type','Trip energies'])
df_energies["Trip energies"]=df_energies["Trip energies"].astype(float) #casts the distance column as floats


# plot for an individual bus line, change the dataframe and title for different lines
#df_energies.plot.bar(x='Type', y='Trip energies', rot = 0, title='Comparing different types of energy recovery systems', color='#ff007f')
#plt.ylabel("Energy required for one trip in MJ")



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
plt.savefig('Figure.svg', format='svg', dpi=1200)
plt.show()

# Returning energy saved

bus_500_outbound_RBS_energy_saved = (bus_500_outbound_total_braking_energy+bus_500_total_stop_energy)/(10**6)
bus_400_outbound_RBS_energy_saved = (bus_400_outbound_total_braking_energy+bus_400_total_stop_energy)/(10**6)
bus_300_outbound_RBS_energy_saved = (bus_300_outbound_total_braking_energy+bus_300_total_stop_energy)/(10**6)
bus_S5_outbound_RBS_energy_saved = (bus_S5_outbound_total_braking_energy+bus_S5_total_stop_energy)/(10**6)

print('Bus 500 regenerative energy in MJ = ', bus_500_outbound_RBS_energy_saved)
print('Bus 400 regenerative energy in MJ = ', bus_400_outbound_RBS_energy_saved)
print('Bus 300 regenerative energy in MJ = ', bus_300_outbound_RBS_energy_saved)
print('Bus S5 regenerative energy in MJ = ', bus_S5_outbound_RBS_energy_saved)

# Creating dataframe:
data_saved_energies = {'Route':  ['500 (outbound)','400 (outbound)','300 (outbound)','S5 (outbound)'],
                       'Energy saved trough RBS [MJ]': [bus_500_outbound_RBS_energy_saved,bus_400_outbound_RBS_energy_saved,bus_300_outbound_RBS_energy_saved,bus_S5_outbound_RBS_energy_saved]}

df_saved_energies = pd.DataFrame (data_saved_energies, columns = ['Route','Energy saved trough RBS [MJ]'])

df_saved_energies = df_saved_energies.assign(kg_hydrongen_saved = [bus_500_outbound_RBS_energy_saved/hydrogen_energy_density,bus_400_outbound_RBS_energy_saved/hydrogen_energy_density,
                                                                  bus_300_outbound_RBS_energy_saved/hydrogen_energy_density,bus_S5_outbound_RBS_energy_saved/hydrogen_energy_density])

print(df_saved_energies)

