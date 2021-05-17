# NOTE: This code borrows a similar structure used for route modelling in Section 4

import pandas as pd

# References:
# [1]: Google Maps. Google Maps. [Online] 
#      Available at: https://www.google.co.uk/maps/. 
#      [Accessed 7th of April 2021]
# [2]: Oxford bus company. When2Travel. [Online]. 
#      Available at: https://www.oxfordbus.co.uk/covid-19/when-2-travel/. 
#      [Accessed 20th November 2020]
# [3]: P.G. Lund A.M. Howatson and J.D. Todd (2009). Engineering tables and data. Department of Engineering Science, University of Oxford, 2009. 
#      [Accessed 29th of November 2020]
# Note: Data corresponding to timetables for the 17th of February 2021 was taken from [2]

# Distances for one trip between first and last station (miles) [1]
d_300 = 7.1
d_400 = 6.2
d_500 = 8.5
d_S5 = 14

# For 300 (number of trips taken from [2]):
data_300 = {'Times': ['(04-08)', '(08-12)','(12-16)','(16-20)','(20-24)'],
            'Number of trips': [8,20,20,17,7]}
df_300 = pd.DataFrame (data_300, columns = ['Times','Number of trips'])
# Note: The number of trips was taken from Oxford Bus Company timetables [2]
# Adding total distances travelled:
df_300 = df_300.assign(total_distance_miles = [(df_300.iloc[0][1])*d_300*2,
                                               (df_300.iloc[1][1])*d_300*2,
                                               (df_300.iloc[2][1])*d_300*2,
                                               (df_300.iloc[3][1])*d_300*2,
                                               (df_300.iloc[4][1])*d_300*2])
# Note: A factor of 2 is applied for distances to account for return trips
# Total distance traveled on a weekday:
df_300['total distance travelled in miles'] = df_300['total_distance_miles'].sum()   

# For 400 (number of trips taken from [2]):
data_400 = {'Times': ['(04-08)', '(08-12)','(12-16)','(16-20)','(20-24)'],
            'Number of trips': [5,16,16,15,7]}
df_400 = pd.DataFrame (data_400, columns = ['Times','Number of trips'])
# Note: The number of trips was taken from Oxford Bus Company timetables [2]
# Adding total distances travelled:
df_400 = df_400.assign(total_distance_miles = [(df_400.iloc[0][1])*d_400*2,
                                               (df_400.iloc[1][1])*d_400*2,
                                               (df_400.iloc[2][1])*d_400*2,
                                               (df_400.iloc[3][1])*d_400*2,
                                               (df_400.iloc[4][1])*d_400*2])
# Note: A factor of 2 is applied for distances to account for return trips
# Total distance traveled on a weekday:
df_400['total distance travelled in miles'] = df_400['total_distance_miles'].sum()   

# For 500 (number of trips taken from [2]):
data_500 = {'Times': ['(04-08)', '(08-12)','(12-16)','(16-20)','(20-24)'],
            'Number of trips': [2,8,7,5,0]}
df_500 = pd.DataFrame (data_500, columns = ['Times','Number of trips'])
# Note: The number of trips was taken from Oxford Bus Company timetables [2]
# Adding total distances travelled:
df_500 = df_500.assign(total_distance_miles = [(df_500.iloc[0][1])*d_500*2,
                                               (df_500.iloc[1][1])*d_500*2,
                                               (df_500.iloc[2][1])*d_500*2,
                                               (df_500.iloc[3][1])*d_500*2,
                                               (df_500.iloc[4][1])*d_500*2])
# Note: A factor of 2 is applied for distances to account for return trips
# Total distance traveled on a weekday:
df_500['total distance travelled in miles'] = df_500['total_distance_miles'].sum()   

# For S5 (number of trips taken from [2]):
data_S5 = {'Times': ['(04-08)', '(08-12)','(12-16)','(16-20)','(20-24)'],
           'Number of trips': [2,14,16,12,9]}
df_S5 = pd.DataFrame (data_S5, columns = ['Times','Number of trips'])
# Note: The number of trips was taken from Oxford Bus Company timetables [2]
# Adding total distances travelled:
df_S5 = df_S5.assign(total_distance_miles = [(df_S5.iloc[0][1])*d_S5*2,
                                             (df_S5.iloc[1][1])*d_S5*2,
                                             (df_S5.iloc[2][1])*d_S5*2,
                                             (df_S5.iloc[3][1])*d_S5*2,
                                             (df_S5.iloc[4][1])*d_S5*2])
# Note: A factor of 2 is applied for distances to account for return trips
# Total distance traveled on a weekday:
df_S5['total distance travelled in miles'] = df_S5['total_distance_miles'].sum()   

# Total distance travelled:
total_distance_miles = df_300.iloc[0][3]+df_400.iloc[0][3]+df_500.iloc[0][3]+df_S5.iloc[0][3]
total_distance_km = total_distance_miles*1.609             # Conversion factor taken from [3]
print('total distance =', total_distance_miles, 'miles or',total_distance_km,'km')






