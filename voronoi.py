import random
import pyvoro
import matplotlib.pyplot as plt

M = 2     # number of voronoi cells to use
N = M*3   # number of initial voronoi cells

#points = [[0,0,0],[0,0,1],[0,1,0],[0,1,1],[1,0,0],[1,0,1],[1,1,0],[1,1,1]]
points = []
limits = [[0,1],[0,1],[0,1]]
# print(points)

for i in range(M):
    points.append([random.uniform(0,1),random.uniform(0,1),random.uniform(0,1)])
    # print(points)

vor = pyvoro.compute_voronoi(points,limits,2)


for i in vor['vertices']:
