import numpy as np
from Bezier import Bezier
import matplotlib.pyplot as plt
import random
import math
from itertools import product, combinations
from PIL import Image


def generateRandomPoints(n):
    points = []
    for i in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        z = random.uniform(0, 1)
        points.append([x, y, z])
    np_points = np.array(points)
    return np_points

def dist_curve_curve(curve1, curve2):
    res = math.sqrt(3)  # maximum possible distance within unit cube
    for i in curve1:
        for j in curve2:
            dist_ij = math.sqrt((i[0] - j[0]) ** 2 +
                                (i[1] - j[1]) ** 2 +
                                (i[2] - j[2]) ** 2)
            if dist_ij < res:
                res = dist_ij
    return res

def dist_point_curve(point, curve):
    res = math.sqrt(3)  # maximum possible distance within unit cube
    for i in curve:
        dist = math.sqrt((i[0] - point[0]) ** 2 +
                         (i[1] - point[1]) ** 2 +
                         (i[2] - point[2]) ** 2)
        if dist < res:
            res = dist
    return res


NUM_CURVES = 10          # number of curves to generate
MAX_DISTANCE = 0        # maximum distance between any two generated curves
IMAGE_RESOLUTION = 16    # amount of pixels per side of the noisy digital image
                        # e.g. IMAGE_RESOLUTION = 16 --> image is 16x16x16

curves = []             # array with all curves
counter = 0             # counter indicating how many curves have been added to
                        # the array
counter_2 = 0           # counter for the overall amount of curves that have
                        # been tested (including those that are too close)

while counter < NUM_CURVES:
    tooClose = False
    points = generateRandomPoints(10)
    t_points = np.arange(0, 1, 0.01)
    curve = Bezier.Curve(t_points, points)
    for i in curves:
        if dist_curve_curve(i, curve) < MAX_DISTANCE:
            tooClose = True
            break
    if tooClose == False:
        curves.append(curve)
        counter += 1
        print("----- counter  = ", counter, "counter_2 = ", counter_2)
    counter_2 += 1
    print("----- counter  = ", counter, "counter_2 = ", counter_2)

ax = plt.axes(projection = "3d")

# plotting the curves
for i in curves:
    ax.plot3D(i[:, 0], i[:, 1], i[:, 2])

# plotting the unit cube
r = [0, 1]
for s, e in combinations(np.array(list(product(r, r, r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        ax.plot3D(*zip(s, e), color="b")

plt.grid()
plt.show()

pixel_values = np.arange(0, 1, 1/IMAGE_RESOLUTION)
pixels = list(product(*[pixel_values, pixel_values, pixel_values]))

grey_values = {}

for p in pixels:
    min_distance = math.sqrt(3) # maximum distance within the unit cube
    for curve in curves:
        distance = dist_point_curve(p, curve)
        if distance < min_distance:
            min_distance = distance
    grey_values[p] = min_distance



grey_values.update((x, y*255) for x, y in grey_values.items())

# print(grey_values)

# max_value = max(grey_values.values())
# min_value = min(grey_values.values())
# print(max_value, min_value)

pixel_list = list(zip(grey_values.values(), grey_values.values(), grey_values.values()))
pixel_list = [pixel_list]
pixel_array = np.array(pixel_list, dtype=np.uint8)

# print(pixel_array)

new_image = Image.fromarray(pixel_array)
new_image.save("grey_values.png")
