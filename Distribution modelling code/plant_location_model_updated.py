import numpy as np
import matplotlib.pyplot as plt

# Note: Coordinates were taken from:
# [1]: Google Maps. (n.d.). Google Maps. [Online] 
#      Available at: https://www.google.co.uk/maps/. 
#      [Accessed 7th of April 2021].

xc_range = np.linspace(-1.5,-1.1,num = 1000)                              # 1000 different x coordinates will be tried
yc_range = np.linspace(51.5,51.8,num = 1000)                              # 1000 different y coordinates will be tried

# Coordinates of each depot and Redbridge Park and Ride:
coord = np.array([[-1.21726,-1.19719,-1.19285,-1.4946,-1.24657,-1.26362],
                  [51.71164,51.72743,51.73705,51.78529,51.6224,51.74548]])
# Coordinates taken from [1]

for k in range(0,len(xc_range)):                                    # For every x coordinate possible
    for q in range(0,len(yc_range)):                                # For every y coordinate possible

        d1_prev = np.sqrt((coord[0,0]-coord[0,1])**2 + (coord[1,0]-coord[1,1])**2)
        d2_prev = np.sqrt((coord[0,0]-coord[0,2])**2 + (coord[1,0]-coord[1,2])**2)
        d3_prev = np.sqrt((coord[0,0]-coord[0,3])**2 + (coord[1,0]-coord[1,3])**2)
        d4_prev = np.sqrt((coord[0,0]-coord[0,4])**2 + (coord[1,0]-coord[1,4])**2)
        d5_prev = np.sqrt((coord[0,0]-coord[0,5])**2 + (coord[1,0]-coord[1,5])**2)
        d_total_prev = d1_prev+d2_prev+d3_prev+d4_prev+d5_prev

        d1 = np.sqrt((xc_range[k]-coord[0,1])**2 + (yc_range[q]-coord[1,1])**2) # Distance between plant and first depot 
        d2 = np.sqrt((xc_range[k]-coord[0,2])**2 + (yc_range[q]-coord[1,2])**2) # Distance between plant and second depot 
        d3 = np.sqrt((xc_range[k]-coord[0,3])**2 + (yc_range[q]-coord[1,3])**2) # Distance between plant and third depot 
        d4 = np.sqrt((xc_range[k]-coord[0,4])**2 + (yc_range[q]-coord[1,4])**2) # Distance between plant and fourth depot 
        d5 = np.sqrt((xc_range[k]-coord[0,5])**2 + (yc_range[q]-coord[1,5])**2) # Distance between plant and fifth depot 
        d_total_now = d1+d2+d3+d4+d5

        if d_total_now < d_total_prev:
            coord[0,0] = xc_range[k]
            coord[1,0] = yc_range[q]

# Plotting points:
plt.figure(facecolor="white")                                                   # Removing grey background
plt.scatter(coord[0,0],coord[1,0],color='red')
plt.scatter(coord[0,1:len(coord[1,:])],coord[1,1:len(coord[1,:])],color='blue')

# Plotting connections between points:
plt.plot([coord[0,0],coord[0,1]],[coord[1,0],coord[1,1]],color='blue')
plt.plot([coord[0,0],coord[0,2]],[coord[1,0],coord[1,2]],color='blue')
plt.plot([coord[0,0],coord[0,3]],[coord[1,0],coord[1,3]],color='blue')
plt.plot([coord[0,0],coord[0,4]],[coord[1,0],coord[1,4]],color='blue')
plt.plot([coord[0,0],coord[0,5]],[coord[1,0],coord[1,5]],color='blue')
plt.show()

print('Optimised plant location is', [coord[1,0],coord[0,0]])
