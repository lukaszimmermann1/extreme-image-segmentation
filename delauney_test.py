from scipy.spatial import Delaunay
from collections import defaultdict
import itertools

points=[[0.0, 0.0], [0.0, 1.0], [0.2, 0.5], [0.3, 0.6], [0.4, 0.5], [0.6, 0.3], [0.6, 0.5], [1.0, 0.0], [1.0, 1.0]]
tri = Delaunay(points)
neiList=defaultdict(set)
for p in tri.vertices:
    for i,j in itertools.combinations(p,2):
        neiList[i].add(j)
        neiList[j].add(i)

print(neiList)


# # This is for visualization
# from scipy.spatial import Voronoi, voronoi_plot_2d
# import matplotlib.pyplot as plt
# vor = Voronoi(points)
# voronoi_plot_2d(vor)
# for i,p in enumerate(x):
#     plt.text(p[0], p[1], '#%d' % i, ha='center')
# plt.show()
