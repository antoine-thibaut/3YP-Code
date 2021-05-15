# Note: Weekday values are used 
# NOTE: This code borrows a similar code structure code used for route modelling

import numpy as np
import pandas as pd
import math
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
bus_5_mpg = 9
diesel_energy_density = 38.6*10**6          # J/L
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
bus_5_total_distance = 477.3    # Distance in miles
bus_5_trips = 111               # Number of trips in a day
bus_5_stops = 18



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
                 
data = {'Stop':  ['Oxford Station','Park End Street','Westgate','Speedwell Street','St Aldates',
                  'Queens Lane','The Plain','James Street east','Manzil Way','Magdalen Road east',
                  'Howard Street east','Shelley Road','Marsh Road','Clive Road','The Original Swan',
                  'Templars Square','Barns Road','Kersington Crescent'],
        'Latitude': [51.75401, 51.75274,51.75082,51.74880,51.75041,
                     51.75374, 51.74992,51.747829805668474,51.74734,51.74220,
                     51.73993, 51.73985,51.73835,51.73470,51.73407,
                     51.73193, 51.73243,51.72653],
        'Longitude': [-1.26962,-1.26879,-1.26067,-1.26257,-1.25680,
                      -1.25124,-1.24412,-1.2371465349732302,-1.23185,-1.23530,
                      -1.23314,-1.22547,-1.21956,-1.21862,-1.21175,
                      -1.21677,-1.21453,-1.20846],
        'Elevation': [60,60,60,59,65,
                      69,62,68,70,66,
                      66,61.0,61.0,63,78,
                      78,75,70],
        'Distance': [0,207,461,114,138,
                     612,640,550,357,390,
                     250,274,478,423,484,
                     265,463,326]}

df = pd.DataFrame (data, columns = ['Stop','Latitude','Longitude','Elevation','Distance'])

#df["Latitude"] = df["Latitude"].astype(int) 
#df["Longitude"] = df["Longitude"].astype(int) 
#df["Elevation"] = df["Elevation"].astype(int) 

# Grouping stops:
grouped_stop = df.groupby(df["Stop"]) # can also group by a different column eg Times !
df_stop_1 = grouped_stop.get_group("Oxford Station")
df_stop_2 = grouped_stop.get_group("Park End Street")
df_stop_3 = grouped_stop.get_group("Westgate")
df_stop_4 = grouped_stop.get_group("Speedwell Street")
df_stop_5 = grouped_stop.get_group("St Aldates")
df_stop_6 = grouped_stop.get_group("Queens Lane")
df_stop_7 = grouped_stop.get_group("The Plain")
df_stop_8 = grouped_stop.get_group("James Street east")
df_stop_9 = grouped_stop.get_group("Manzil Way")
df_stop_10 = grouped_stop.get_group("Magdalen Road east")
df_stop_11 = grouped_stop.get_group("Howard Street east")
df_stop_12 = grouped_stop.get_group("Shelley Road")
df_stop_13 = grouped_stop.get_group("Marsh Road")
df_stop_14 = grouped_stop.get_group("Clive Road")
df_stop_15 = grouped_stop.get_group("The Original Swan")
df_stop_16 = grouped_stop.get_group("Templars Square")
df_stop_17 = grouped_stop.get_group("Barns Road")
df_stop_18 = grouped_stop.get_group("Kersington Crescent")

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

# Adding theta column:
df = df.assign(theta = [stop1_road_theta, stop2_road_theta, stop3_road_theta,
                        stop4_road_theta, stop5_road_theta, stop6_road_theta,
                        stop7_road_theta, stop8_road_theta, stop9_road_theta,
                        stop10_road_theta, stop11_road_theta, stop12_road_theta,
                        stop13_road_theta, stop14_road_theta, stop15_road_theta,
                        stop16_road_theta, stop17_road_theta, stop18_road_theta])

print(df)


# Air resistance force:
Fa = 0.5*Cd*rho*v**2

# Weight components
df = df.assign(weight_component = [Mg*math.sin(stop1_road_theta), Mg*math.sin(stop2_road_theta), Mg*math.sin(stop3_road_theta),
                                   Mg*math.sin(stop4_road_theta), Mg*math.sin(stop5_road_theta), Mg*math.sin(stop6_road_theta),
                                   Mg*math.sin(stop7_road_theta), Mg*math.sin(stop8_road_theta), Mg*math.sin(stop9_road_theta),
                                   Mg*math.sin(stop10_road_theta), Mg*math.sin(stop11_road_theta), Mg*math.sin(stop12_road_theta),
                                   Mg*math.sin(stop13_road_theta), Mg*math.sin(stop14_road_theta), Mg*math.sin(stop15_road_theta),
                                   Mg*math.sin(stop16_road_theta), Mg*math.sin(stop17_road_theta), Mg*math.sin(stop18_road_theta)])

# Time spent between each stop:
df = df.assign(time = df.Distance/v)

# Regenerative force:
df = df.assign(regenerative_force = df.weight_component - Fa)

# Available energy:
df = df.assign(available_energy = df.regenerative_force*v*df.time)

# Replacing all available energy by zero:
df.available_energy[df.available_energy < 0] = 0

# Total available energy for recovery:
total_braking_energy = sum(df.available_energy)

# Finding gallons consumed by bus 5
bus_5_gallons = bus_5_total_distance/bus_5_mpg
bus_5_litres = bus_5_gallons*4.546

# Energy equivalent:
bus_5_total_energy = bus_5_litres*diesel_energy_density

# Energy for 1 trip:
bus_5_trip_energy = bus_5_total_energy/bus_5_trips

# Energy with regenerative system:
bus_5_regenerative_trip_energy = bus_5_trip_energy - total_braking_energy

# Bus kinetic energy:
bus_5_kinetic_energy = 0.5*M*v**2

# Recoverable kinetic energy for start-stops
total_stop_energy = bus_5_kinetic_energy*bus_5_stops

    
# Plotting:
# data to plot
#n_groups = 5
# Bus = {early, mid, afternoon, evening, late}

data_energies = {'Type':  ['A', 'B','C'],
                 'Trip energies': [bus_5_trip_energy/(10**6), bus_5_regenerative_trip_energy/(10**6), (bus_5_regenerative_trip_energy-total_stop_energy)/(10**6)]}

df_energies = pd.DataFrame (data_energies, columns = ['Type','Trip energies'])
df_energies["Trip energies"]=df_energies["Trip energies"].astype(float) #casts the distance column as floats


# plot for an individual bus line, change the dataframe and title for different lines
df_energies.plot.bar(x='Type', y='Trip energies', rot = 0, title='Comparing different types of energy recovery systems', color='#ff007f')
plt.ylabel("Energy required for one trip in MJ")
plt.savefig('Figure.svg', format='svg', dpi=1200)
plt.show()


