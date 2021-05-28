import random
import pyvoro
import matplotlib.pyplot as plt

M = 10     # number of voronoi cells to use
N = M*10   # number of initial voronoi cells

# points = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
points = []
limits = [[0,10],[0,10],[0,10]]
# print(points)

for i in range(M):
    rand_x = random.uniform(0,1)
    rand_y = random.uniform(0,1)
    rand_z = random.uniform(0,1)
    points.append([rand_x,rand_y,rand_z])
    # print(points)

vor = pyvoro.compute_voronoi(points,limits,2)

print(vor)
