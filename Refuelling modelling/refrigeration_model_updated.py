# References: 
# [1]: matplotlib. 2017. pylab_examples example code: barchart_demo.py. [Online]
#       Available at: https://matplotlib.org/2.0.2/examples/pylab_examples/barchart_demo.html
#      [Accessed 12th of May 2021]    

# This code compares refuelling times for refrigerated and non-refrigerated systems

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
non_refrigerated_time = 23                 # Time to refuel a single bus for non-refrigerated system [mintues] (derived from H2Bus)
refrigerated_time = 8                      # Time taken to refuel a single bus for refrigerated system [minutes] (derived from H2Bus)
bus_number = 148                           # Total number of buses to refuel (from Oxford bus company fleet list)

data = {'Number of hydrogen dispensers':  ['1','2','3','4','5','6','7','8',
                                           '1','2','3','4','5','6','7','8'],
        'System': ['non-refrigerated','non-refrigerated','non-refrigerated','non-refrigerated','non-refrigerated','non-refrigerated','non-refrigerated','non-refrigerated',
                   'refrigerated','refrigerated','refrigerated','refrigerated','refrigerated','refrigerated','refrigerated','refrigerated'],
        'Total refuelling time': [bus_number*non_refrigerated_time/(60),bus_number*non_refrigerated_time/(2*60),bus_number*non_refrigerated_time/(3*60),bus_number*non_refrigerated_time/(4*60),bus_number*non_refrigerated_time/(5*60),bus_number*non_refrigerated_time/(6*60),bus_number*non_refrigerated_time/(7*60),bus_number*non_refrigerated_time/(8*60),
                                  bus_number*refrigerated_time/(60),bus_number*refrigerated_time/(2*60),bus_number*refrigerated_time/(3*60),bus_number*refrigerated_time/(4*60),bus_number*refrigerated_time/(5*60),bus_number*refrigerated_time/(6*60),bus_number*refrigerated_time/(7*60),bus_number*refrigerated_time/(8*60)]}

# Note: Refuelling times are in hours

df = pd.DataFrame (data, columns = ['Number of hydrogen dispensers','System','Total refuelling time'])

print(df)

df["Number of hydrogen dispensers"]=df["Number of hydrogen dispensers"].astype(float) # Setting number of hydrogen dispensers as a float
df["Total refuelling time"]=df["Total refuelling time"].astype(float) # Setting total refuelling time as a float
grouped_system = df.groupby(df["System"])

# Individual Data Frames for each staff hour:
df_non_refrigerated = grouped_system.get_group("non-refrigerated")
df_refrigerated = grouped_system.get_group("refrigerated")


# Plotting:
# Data to plot:
dispensers = 8

non_refrigerated = (df_non_refrigerated.iloc[0][2],df_non_refrigerated.iloc[1][2],df_non_refrigerated.iloc[2][2],df_non_refrigerated.iloc[3][2],df_non_refrigerated.iloc[4][2],df_non_refrigerated.iloc[5][2],df_non_refrigerated.iloc[6][2],df_non_refrigerated.iloc[7][2])
refrigerated = (df_refrigerated.iloc[0][2],df_refrigerated.iloc[1][2],df_refrigerated.iloc[2][2],df_refrigerated.iloc[3][2],df_refrigerated.iloc[4][2],df_refrigerated.iloc[5][2],df_refrigerated.iloc[6][2],df_refrigerated.iloc[7][2])



# Creating bar chart, code adapted from [1]:
fig, ax = plt.subplots()
number_used = np.arange(dispensers)
width_of_bar = 0.4

rects1 = plt.bar(number_used-width_of_bar/2, non_refrigerated, width_of_bar,
color='#FC9938',
label='Non-refrigerated')

rects2 = plt.bar(number_used+width_of_bar/2, refrigerated, width_of_bar,
color='b',
label='Refrigerated')

plt.xlabel('Number of hydrogen dispensers')
plt.ylabel('Time taken to refuel 148 buses (hours)')
plt.plot([-1,0,1,2,3,4,5,6,7,8],[8,8,8,8,8,8,8,8,8,8],color = 'r')
plt.xticks([0,1,2,3,4,5,6,7], ('1', '2','3','4','5','6','7','8'))
plt.xlim([-1,8])
plt.yticks((4,8,12,16,20,24,28,32,36,40,44,48,52,56,60), ('4','8','12','16','20','24','28','32','36','40','44','48','52','56','60'))
plt.legend()
plt.tight_layout()
plt.savefig('refrigeration_model.svg', format='svg', dpi=1200,bbox_inches = "tight")

plt.show()
