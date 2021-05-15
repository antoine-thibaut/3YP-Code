# NOTE: This code borrows a similar structure used for route modelling in Section 4

# References:
# [1]: FreeMapTools. (2019). Elevation Finder. [Online]. 
#      Available at: https://www.freemaptools.com/elevation-finder.htm. 
#      [Accessed 26h of March 2021]
# [2]: Oxford Bus Company. (2020). park&ride500 Covid-19 Timetables from 1st June 2020. [Pdf]. 
#      Available at: https://assets.goaheadbus.com/media/cms_page_media/8103/200601_parkride500_COVID-19_Coronavirus_Timetable.pdf. 
#      [Accessed 26th of March 2021]
# [3]: Oxford Bus Company. (2020). park&ride400 Covid-19 Timetables from 24th October 2020. [Pdf]. 
#      Available at: https://assets.goaheadbus.com/media/cms_page_media/8103/201024_parkride400_COVID-19_Coronavirus_TimetableV2.pdf. 
#      [Accessed 26th of March 2021]
# [4]: LiveBus.org. (2021). City Centre and Pear Tree Park and Ride. [Online]. 
#      Available at: http://www.livebus.org/oxfordshire/routes/obc/300/city-centre-and-pear-tree-park-and-ride/. 
#      [Accessed 26th of March 2021]
# [5]: Stagecoach. (2021). S5 Bus Route & Timetable: Oxford-Bicester. [Online]. 
#      Available at: https://www.stagecoachbus.com/routes/oxfordshire/s5/oxford-bicester/xoas005.o. 
#      [Accessed 26th of March 2021]
# [6]: Google Maps. (n.d.). Google Maps. [online].
#      Available at: https://www.google.co.uk/maps/. 
#      [Accessed 7th of April 2021].
# [7]: H. Hwang, A. Varma. (2014). Hydrogen storage for fuel cell vehicles. [Pdf]. 
#      Available at: https://doi.org/10.1016/j.coche.2014.04.004. 
#      [Accessed 23rd of March 2021]
# [8]: M. Islameka, E. Leksono, B. Yuliarto, Journal of Physics: Conference Series. (2019). Modelling of regenerative braking system for electric bus. [Pdf]. 
#      Available at: https://iopscience.iop.org/article/10.1088/1742-6596/1402/4/044054. 
#      [Accessed 20th of March 2021] 
# [9] R. Folkson. (2014). Alternative Fuels and Advanced Vehicle Technologies for Improved Environmental Performance Towards Zero Carbon Transportation. [Pdf] 
# [10]: A. Doyle, T. Muneer. (2017). Traction energy and battery performance modelling. [Online]. 
#       Available at: https://www.sciencedirect.com/topics/engineering/regenerative-braking. 
#       [Accessed 24th of March 2021]
# [11]: P.G. Lund A.M. Howatson and J.D. Todd. (2009). 
#       Engineering tables and data. Department of Engineering Science, University of Oxford, 2009. 
#       [Accessed 29th of November 2020]
# [12]: The Engineering ToolBox. (2004). Drag Coefficient. [Online]. 
#       Available at: https://www.engineeringtoolbox.com/drag-coefficient-d_627.html. 
#       [Accessed 22nd of March 2021]
# [13]: Hydrogen Mobility Australia. Capability Statement, Hydrogen Fuel Cell Buses. [Pdf]. 
#       Available at: https://static1.squarespace.com/static/5a668f1080bd5e34d18a7e76/t/5c9401cd71c10b2160f88c2f/1553203697824/Hydrogen+Fuel+Cell+Buses.pdf. 
#       [Accessed 22nd of March 2021]
# [14]: Oxford bus company. When2Travel. [Online]. 
#       Available at: https://www.oxfordbus.co.uk/covid-19/when-2-travel/. 
#       [Accessed 20th November 2020]


# This code computes how much regenerative braking systems save in terms of energy and kg of hydrogen on Park and Ride routes in Oxford

# NOTE: Distances, coordinates and elevations used in this code were found from [1]


import pandas as pd
import math


# Fuel parameters:
hydrogen_energy_density = 120              # MJ/kg [7]
hydrogen_energy_efficiency = 0.6           # Conversion efficiency for converting hydrogen into useful work [9]
regenerative_efficiency = 0.7              # Efficiency of a regenerative braking system [10]

# Bus speed:
v_mph = 40
v = v_mph*0.4470

# Bus parameters:
Cd = 0.6              # Drag coefficient [12]
rho = 1.225           # Air density [11]
A = 11.34             # Bus cross section [13]  
M = 11350             # Bus mass [13]
g = 9.81 	          # Acceleration of free fall [11]
Mg = M*g 	          # Bus weight
Fa = 0.5*Cd*rho*v**2  # Air resistance force [8]
KE = 0.5*M*v**2       # Kinetic energy of bus

# Route parameters:
bus_500_trips_weekday = 22                 # Number of trips in a day, weekday (17th of February 2021) [14]
bus_500_trips_weekend = 19                 # Number of trips in a day, weekend (23rd of January 2021) [14]
bus_500_stops = 7                          # Number of stops on 500 route [2]             
bus_500_total_stop_energy = regenerative_efficiency*KE*bus_500_stops # Recoverable kinetic energy for start-stops

bus_400_trips_weekday = 59                 # Number of trips in a day, weekday (17th of February 2021) [14]
bus_400_trips_weekend = 48                 # Number of trips in a day, weekend (20th of February 2021) [14]
bus_400_stops = 5                          # Number of stops on 400 route [3]
bus_400_total_stop_energy = regenerative_efficiency*KE*bus_400_stops # Recoverable kinetic energy for start-stops

bus_300_trips_weekday = 72                 # Number of trips in a day, weekday (17th of February 2021) [14]
bus_300_trips_weekend = 72                 # Number of trips in a day, weekend (20th of February 2021) [14]
bus_300_stops = 7			               # Number of stops on 300 route [4]                    
bus_300_total_stop_energy = regenerative_efficiency*KE*bus_300_stops # Recoverable kinetic energy for start-stops

bus_S5_trips_weekday = 53                  # Number of trips in a day, weekday (17th of February 2021) [14]
bus_S5_trips_weekend = 38                  # Number of trips in a day, weekend (20th of February 2021) [14]
bus_S5_stops = 7                           # Number of stops on S5 route [5]
bus_S5_total_stop_energy = regenerative_efficiency*KE*bus_S5_stops # Recoverable kinetic energy for start-stops

# Function for calculating inclination from road distance
def getinclination_2(elevation_previous,elevation_now,road_distance):
    stop_distance = road_distance
    theta = math.atan((elevation_previous-elevation_now)/stop_distance)
    return theta
             
'''
FOR 500 [1, 2]
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

# FOR OUTBOUND
# Grouping stops:
grouped_stop = df_500_outbound.groupby(df_500_outbound["Stop"])
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
# Regenerative force:
df_500_outbound = df_500_outbound.assign(regenerative_force = df_500_outbound.weight_component - Fa)
# Available energy:
df_500_outbound = df_500_outbound.assign(available_energy = df_500_outbound.regenerative_force*df_500_outbound.Distance)
# Replacing all available energy by zero if smaller than 0 (if bus is climbing):
df_500_outbound.available_energy[df_500_outbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_500_outbound_total_braking_energy = sum(df_500_outbound.available_energy)*regenerative_efficiency

# FOR INBOUND
# Grouping stops:
grouped_stop = df_500_inbound.groupby(df_500_inbound["Stop"])
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
# Regenerative force:
df_500_inbound = df_500_inbound.assign(regenerative_force = df_500_inbound.weight_component - Fa)
# Available energy:
df_500_inbound = df_500_inbound.assign(available_energy = df_500_inbound.regenerative_force*df_500_inbound.Distance)
# Replacing all available energy by zero if smaller than 0 (if bus is climbing):
df_500_inbound.available_energy[df_500_inbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_500_inbound_total_braking_energy = sum(df_500_inbound.available_energy)*regenerative_efficiency

"""
For 400 [1, 3]
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

# FOR OUTBOUND
# Grouping stops:
grouped_stop = df_400_outbound.groupby(df_400_outbound["Stop"])
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
# Regenerative force:
df_400_outbound = df_400_outbound.assign(regenerative_force = df_400_outbound.weight_component - Fa)
# Available energy:
df_400_outbound = df_400_outbound.assign(available_energy = df_400_outbound.regenerative_force*df_400_outbound.Distance)
# Replacing all available energy by zero if smaller than 0 (if bus is climbing):
df_400_outbound.available_energy[df_400_outbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_400_outbound_total_braking_energy = sum(df_400_outbound.available_energy)*regenerative_efficiency

# FOR INBOUND
# Grouping stops:
grouped_stop = df_400_inbound.groupby(df_400_inbound["Stop"])
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
# Regenerative force:
df_400_inbound = df_400_inbound.assign(regenerative_force = df_400_inbound.weight_component - Fa)
# Available energy:
df_400_inbound = df_400_inbound.assign(available_energy = df_400_inbound.regenerative_force*df_400_inbound.Distance)
# Replacing all available energy by zero if smaller than 0 (if bus is climbing):
df_400_inbound.available_energy[df_400_inbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_400_inbound_total_braking_energy = sum(df_400_inbound.available_energy)*regenerative_efficiency

"""
For 300 [1, 4]
"""

data_300_outbound = {'Stop':  ['Redbridge Park and Ride','St Aldates','Chatham Road',
                               'County Hall','Magdalen Street','South Parade',
                               'Pear Tree Park & Ride'],
        'Latitude': [51.72979,51.74994,51.73516,51.75151,
                     51.75466,51.77826,51.79375],
        'Longitude': [-1.24861,-1.25687,-1.24805,-1.26131,
                      -1.25913,-1.26722,-1.2817626020596353],
        'Elevation': [57,65,57,66,
                      70,65,66],
        'Distance': [0,234,218,518,
                     173,445,982]}
data_300_inbound = {'Stop': ['Pear Tree Park & Ride','South Parade','Magdalen Street','County Hall',
                             'Chatham Road','St Aldates','Redbridge Park and Ride'],
        'Latitude': [51.79374799403658,51.77826,51.75466,51.75151,
                     51.73516,51.74994,51.72979],
        'Longitude': [-1.2817626020596353,-1.26722,-1.25913,-1.26131,
                      -1.24805,-1.25687,-1.24861],
        'Elevation': [66,65,70,66,
                      57,65,57],
        'Distance': [0,267,645,238,
                     348,1960,2716]}

df_300_outbound = pd.DataFrame (data_300_outbound, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])
df_300_inbound = pd.DataFrame (data_300_inbound, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])

# FOR OUTBOUND
# Grouping stops:
grouped_stop = df_300_outbound.groupby(df_300_outbound["Stop"])
df_stop_1 = grouped_stop.get_group("Redbridge Park and Ride")
df_stop_2 = grouped_stop.get_group("St Aldates")
df_stop_3 = grouped_stop.get_group("Chatham Road")
df_stop_4 = grouped_stop.get_group("County Hall")
df_stop_5 = grouped_stop.get_group("Magdalen Street")
df_stop_6 = grouped_stop.get_group("South Parade")
df_stop_7 = grouped_stop.get_group("Pear Tree Park & Ride")
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
df_300_outbound = df_300_outbound.assign(theta = [stop1_road_theta, stop2_road_theta, stop3_road_theta,
                                stop4_road_theta, stop5_road_theta, stop6_road_theta, 
                                stop7_road_theta])
# Weight components
df_300_outbound = df_300_outbound.assign(weight_component = [Mg*math.sin(stop1_road_theta), Mg*math.sin(stop2_road_theta), Mg*math.sin(stop3_road_theta),
                                           Mg*math.sin(stop4_road_theta), Mg*math.sin(stop5_road_theta), Mg*math.sin(stop6_road_theta),
                                           Mg*math.sin(stop7_road_theta)])
# Regenerative force:
df_300_outbound = df_300_outbound.assign(regenerative_force = df_300_outbound.weight_component - Fa)
# Available energy:
df_300_outbound = df_300_outbound.assign(available_energy = df_300_outbound.regenerative_force*df_300_outbound.Distance)
# Replacing all available energy by zero if smaller than 0 (if bus is climbing):
df_300_outbound.available_energy[df_300_outbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_300_outbound_total_braking_energy = sum(df_300_outbound.available_energy)*regenerative_efficiency

# FOR INBOUND
# Grouping stops:
grouped_stop = df_300_inbound.groupby(df_300_inbound["Stop"])
df_stop_1 = grouped_stop.get_group("Pear Tree Park & Ride")
df_stop_2 = grouped_stop.get_group("South Parade")
df_stop_3 = grouped_stop.get_group("Magdalen Street")
df_stop_4 = grouped_stop.get_group("County Hall")
df_stop_5 = grouped_stop.get_group("Chatham Road")
df_stop_6 = grouped_stop.get_group("St Aldates")
df_stop_7 = grouped_stop.get_group("Redbridge Park and Ride")
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
df_300_inbound = df_300_inbound.assign(theta = [stop1_road_theta, stop2_road_theta, stop3_road_theta,
                                                stop4_road_theta, stop5_road_theta, stop6_road_theta, 
                                                stop7_road_theta])
# Weight components
df_300_inbound = df_300_inbound.assign(weight_component = [Mg*math.sin(stop1_road_theta), Mg*math.sin(stop2_road_theta), Mg*math.sin(stop3_road_theta),
                                                           Mg*math.sin(stop4_road_theta), Mg*math.sin(stop5_road_theta), Mg*math.sin(stop6_road_theta),
                                                           Mg*math.sin(stop7_road_theta)])
# Regenerative force:
df_300_inbound = df_300_inbound.assign(regenerative_force = df_300_inbound.weight_component - Fa)
# Available energy:
df_300_inbound = df_300_inbound.assign(available_energy = df_300_inbound.regenerative_force*df_300_inbound.Distance)
# Replacing all available energy by zero if smaller than 0 (if bus is climbing):
df_300_inbound.available_energy[df_300_inbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_300_inbound_total_braking_energy = sum(df_300_inbound.available_energy)*regenerative_efficiency

"""
For S5 [1, 5]
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

# FOR OUTBOUND
# Grouping stops:
grouped_stop = df_S5_outbound.groupby(df_S5_outbound["Stop"])
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
# Regenerative force:
df_S5_outbound = df_S5_outbound.assign(regenerative_force = df_S5_outbound.weight_component - Fa)
# Available energy:
df_S5_outbound = df_S5_outbound.assign(available_energy = df_S5_outbound.regenerative_force*df_S5_outbound.Distance)
# Replacing all available energy by zero if smaller than 0 (if bus is climbing):
df_S5_outbound.available_energy[df_S5_outbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_S5_outbound_total_braking_energy = sum(df_S5_outbound.available_energy)*regenerative_efficiency

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
# Regenerative force:
df_S5_inbound = df_S5_inbound.assign(regenerative_force = df_S5_inbound.weight_component - Fa)
# Available energy:
df_S5_inbound = df_S5_inbound.assign(available_energy = df_S5_inbound.regenerative_force*df_S5_inbound.Distance)
# Replacing all available energy by zero if smaller than 0 (if bus is climbing):
df_S5_inbound.available_energy[df_S5_inbound.available_energy < 0] = 0
# Total available energy for recovery:
bus_S5_inbound_total_braking_energy = sum(df_S5_inbound.available_energy)*regenerative_efficiency


# Returning energy saved (also converting to MJ)

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

df_saved_energies = pd.DataFrame (data_saved_energies, columns = ['Route'])

df_saved_energies = df_saved_energies.assign(MJ_of_energy_recovered_one_trip = [(bus_500_outbound_RBS_energy_saved),
                                                                                (bus_500_inbound_RBS_energy_saved),
                                                                                (bus_400_outbound_RBS_energy_saved),
                                                                                (bus_400_inbound_RBS_energy_saved),
                                                                                (bus_300_outbound_RBS_energy_saved),
                                                                                (bus_300_inbound_RBS_energy_saved),
                                                                                (bus_S5_outbound_RBS_energy_saved),
                                                                                (bus_S5_inbound_RBS_energy_saved)])

df_saved_energies = df_saved_energies.assign(kg_hydrogen_saved_trip = [(bus_500_outbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency,
                                                                        (bus_500_inbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency,
                                                                        (bus_400_outbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency,
                                                                        (bus_400_inbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency,
                                                                        (bus_300_outbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency,
                                                                        (bus_300_inbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency,
                                                                        (bus_S5_outbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency,
                                                                        (bus_S5_inbound_RBS_energy_saved/hydrogen_energy_density)/hydrogen_energy_efficiency])

df_saved_energies = df_saved_energies.assign(kg_hydrogen_saved_weekday = [((bus_500_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_500_trips_weekday)/hydrogen_energy_efficiency,
                                                                        ((bus_500_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_500_trips_weekday)/hydrogen_energy_efficiency,
                                                                        ((bus_400_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_400_trips_weekday)/hydrogen_energy_efficiency,
                                                                        ((bus_400_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_400_trips_weekday)/hydrogen_energy_efficiency,
                                                                        ((bus_300_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_300_trips_weekday)/hydrogen_energy_efficiency,
                                                                        ((bus_300_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_300_trips_weekday)/hydrogen_energy_efficiency,
                                                                        ((bus_S5_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_S5_trips_weekday)/hydrogen_energy_efficiency,
                                                                        ((bus_S5_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_S5_trips_weekday)/hydrogen_energy_efficiency])

df_saved_energies = df_saved_energies.assign(kg_hydrogen_saved_weekend = [((bus_500_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_500_trips_weekend)/hydrogen_energy_efficiency,
                                                                        ((bus_500_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_500_trips_weekend)/hydrogen_energy_efficiency,
                                                                        ((bus_400_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_400_trips_weekend)/hydrogen_energy_efficiency,
                                                                        ((bus_400_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_400_trips_weekend)/hydrogen_energy_efficiency,
                                                                        ((bus_300_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_300_trips_weekend)/hydrogen_energy_efficiency,
                                                                        ((bus_300_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_300_trips_weekend)/hydrogen_energy_efficiency,
                                                                        ((bus_S5_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_S5_trips_weekend)/hydrogen_energy_efficiency,
                                                                        ((bus_S5_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_S5_trips_weekend)/hydrogen_energy_efficiency])

df_saved_energies = df_saved_energies.assign(kg_hydrogen_saved_year = [(((bus_500_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_500_trips_weekday*365*(5/7))+((bus_500_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_500_trips_weekend*365*(2/7)))/hydrogen_energy_efficiency,
                                                                        (((bus_500_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_500_trips_weekday*365*(5/7))+((bus_500_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_500_trips_weekend*365*(2/7)))/hydrogen_energy_efficiency,
                                                                        (((bus_400_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_400_trips_weekday*365*(5/7))+((bus_400_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_400_trips_weekend*365*(2/7)))/hydrogen_energy_efficiency,
                                                                        (((bus_400_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_400_trips_weekday*365*(5/7))+((bus_400_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_400_trips_weekend*365*(2/7)))/hydrogen_energy_efficiency,
                                                                        (((bus_300_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_300_trips_weekday*365*(5/7))+((bus_300_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_300_trips_weekend*365*(2/7)))/hydrogen_energy_efficiency,
                                                                        (((bus_300_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_300_trips_weekday*365*(5/7))+((bus_300_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_300_trips_weekend*365*(2/7)))/hydrogen_energy_efficiency,
                                                                        (((bus_S5_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_S5_trips_weekday*365*(5/7))+((bus_S5_outbound_RBS_energy_saved/hydrogen_energy_density)*bus_S5_trips_weekend*365*(2/7)))/hydrogen_energy_efficiency,
                                                                        (((bus_S5_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_S5_trips_weekday*365*(5/7))+((bus_S5_inbound_RBS_energy_saved/hydrogen_energy_density)*bus_S5_trips_weekend*365*(2/7)))/hydrogen_energy_efficiency])

print(df_saved_energies)
df_saved_energies.to_csv('saved_energies.csv', index=False)
