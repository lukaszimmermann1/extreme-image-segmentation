from scipy.spatial import Voronoi
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import random
from collections import defaultdict
import itertools
from scipy.spatial import voronoi_plot_2d

def neighbourList(delauney):
    neiList = defaultdict(set)
    for p in delauney.vertices:
        for i, j in itertools.combinations(p, 2):
            neiList[i].add(j)
            neiList[j].add(i)
    return neiList

M = 10   # number of final voronoi cells
N = 1000  # number of

points = []

for i in range(8):
    point_x = random.uniform(0, 1)
    point_y = random.uniform(0, 1)
    # point_z = random.uniform(0, 1)
    points.append([point_x, point_y])
    # points.append([point_x, point_y, point_z])

points = np.array(points)

# list = [[0.6, 0.8], [0.8, 0.15], [0.95,  0.3], [0.85, 0.2]]
# points = np.array(list)

voro = Voronoi(points)

print("points: ", voro.points)
print("vertices: ", voro.vertices)
print("ridge_points: ", voro.ridge_points)
print("ridge_vertices: ", voro.ridge_vertices)
print("regions: ", voro.regions)
print("point_region: ", voro.point_region)
print("furthest_site: ", voro.furthest_site)


voronoi_plot_2d(voro)
plt.grid()
plt.show()
