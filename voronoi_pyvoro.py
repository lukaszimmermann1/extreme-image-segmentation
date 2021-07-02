from scipy.spatial import Voronoi
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import random
from collections import defaultdict
import itertools
from scipy.spatial import voronoi_plot_2d
import pyvoro
from sympy import Plane, Point3D
from shapely.geometry import Polygon, Point
from itertools import product, combinations
import math
from PIL import Image


def divisorGenerator(n):
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(n / i)
    for divisor in reversed(large_divisors):
        yield divisor

IMAGE_RESOLUTION = 32

points = []

for i in range(3):
    point_x = random.uniform(0, 1)
    point_y = random.uniform(0, 1)
    point_z = random.uniform(0, 1)
    # points.append([point_x, point_y])
    points.append([point_x, point_y, point_z])

# list = [[0.6, 0.8], [0.8, 0.15], [0.95,  0.3], [0.85, 0.2]]
# points = np.array(list)

voro = pyvoro.compute_voronoi(points, [[0, 1], [0, 1], [0, 1]], 2)

all_faces = []

for i in voro:
    for j in i["faces"]:
        plane = []
        for k in j["vertices"]:
            plane.append(i["vertices"][k])
        all_faces.append(plane)

s = []

for i in all_faces:
    if i not in s:
        s.append(i)

all_faces = s

# print(all_faces[3])

all_polygons = []

for i in all_faces:
    polygon = []
    for j in i:
        polygon.append(j)
    newpoly = Polygon(polygon)
    all_polygons.append(newpoly)

pixel_values = np.arange(0, 1, 1/IMAGE_RESOLUTION)
pixels = list(product(*[pixel_values, pixel_values, pixel_values]))
print(pixels)

grey_values = {}
for p in pixels:
    min_distance = math.sqrt(3) # maximum distance within the unit cube
    for polygon in all_polygons:
        distance = polygon.distance(Point(p))
        #print(distance)
        #print(Point(p), polygon, "distance: ", distance)
        if distance < min_distance:
            min_distance = distance
    #print(min_distance)
    if min_distance != 0:
        print("!!!!!!!!!!")
    grey_values[p] = min_distance

pixel_list = list(grey_values.values())
# print(pixel_list)
pixel_array = np.array(pixel_list)

divisors = list(divisorGenerator(pixel_array.size))
length = len(list(divisorGenerator(pixel_array.size)))
center = math.ceil(length / 2)

# print(divisors, center, divisors[center])


pixel_array = np.reshape(pixel_array, (int(divisors[center - 1]), -1))

new_image = Image.fromarray(pixel_array, "L")
new_image.save("voronoi.png")

# #print(all_faces)
#
# all_faces_point3d = []
#
# for i in all_faces:
#     x = []
#     for j in range(3):
#         x.append(Point3D(i[j]))
#     all_faces_point3d.append(x)
#
# #print(all_faces_point3d)
#
# all_planes = []
# for i in all_faces_point3d:
#     x = []
#     for j in i:
#         x.append(j)
#     p = Plane(x[0], x[1], x[2])
#     all_planes.append(p)
#
# # print(all_planes)
# # print("=======================================")
# # o = Point3D(0.5, 0.5, 0.5)
# # print(all_planes[0].distance(o))
#
# # print(voro[0]["vertices"])
# # outF = open("voronoi_pyvoro", "w")
# # outF.write(str(voro[0]["vertices"]))
#
# test_plane = Plane(Point3D(1, 1, 1), Point3D(1, 1, 0.9), Point3D(1, 0.9, 1))
# test_point = Point3D(0, 0, 0)
# print(test_plane.distance(test_point))
