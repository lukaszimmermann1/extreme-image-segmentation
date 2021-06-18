import scipy as sp
import matplotlib.pyplot as plt
import numpy as np
import random
import itertools
from scipy.interpolate import splprep, splev, interp2d

def dist(curve1,curve2):
    return 9


N = 10
points = []

while len(points) < 20:
    x = np.linspace(random.uniform(0,1), random.uniform(0,1),num = 20)   #list of known x coordinates
    y = np.linspace(random.uniform(0,1), random.uniform(0,1),num = 20)   #list of known y coordinates
    z = np.linspace(random.uniform(0,1), random.uniform(0,1), num = 20)   #list of known z coordinates
    ## Note: You must have more points than degree of the spline. if k = 3, must have 4 points min.

    #print([x,y,z])

    tck, u = splprep([x,y,z], s=26)  # Generate function out of provided points, default k = 3
    newPoints = splev(u, tck)          # Creating spline points
    #print(newPoints)
    #print("---------")
    #print(newPoints[0])
    #print("---------")
    #print(newPoints[0][0])
    tooClose = False
    # for i in points:
    #     if dist(i,newPoints) < 10:
    #         tooClose = True
    # if tooClose == False:
    points.append(newPoints)


ax = plt.axes(projection = "3d")
#ax.plot3D(x, y, z, 'go')     # Green is the actual 3D function

for i in points:
    ax.plot3D(i[:][0], i[:][1], i[:][2], 'r-')   # Red is the spline
plt.show()
