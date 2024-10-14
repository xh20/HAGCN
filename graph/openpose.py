import numpy as np
import sys

sys.path.extend(['../'])
from graph import tools
import networkx as nx

# for Body 25 model
#     {0,  "Nose"},
#     {1,  "Neck"},
#     {2,  "RShoulder"},
#     {3,  "RElbow"},
#     {4,  "RWrist"},
#     {5,  "LShoulder"},
#     {6,  "LElbow"},
#     {7,  "LWrist"},
#     {8,  "MidHip"},
#     {9,  "RHip"},
#     {10, "RKnee"},
#     {11, "RAnkle"},
#     {12, "LHip"},
#     {13, "LKnee"},
#     {14, "LAnkle"},
#     {15, "REye"},
#     {16, "LEye"},
#     {17, "REar"},
#     {18, "LEar"},
#     {19, "LBigToe"},
#     {20, "LSmallToe"},
#     {21, "LHeel"},
#     {22, "RBigToe"},
#     {23, "RSmallToe"},
#     {24, "RHeel"},

# Edge format: (origin, neighbor)
num_node = 25
self_link = [(i, i) for i in range(num_node)]
inward = [(0, 1), (2, 1), (3, 2), (4, 3), (5, 1), (6, 5), (7, 6), (8, 1), (9, 8), (10, 9), (11, 10), (12, 8), (13, 12),
          (14, 13), (15, 0), (16, 0), (17, 15), (18, 16), (19, 14), (20, 19), (21, 14), (22, 11), (23, 22), (24, 11)]
# (0, 4), (0, 7), (0, 10), (0, 13), (4, 7), (4, 10), (4, 13), (7, 10), (7, 13), (10, 13)
outward = [(j, i) for (i, j) in inward]
neighbor = inward + outward


class Graph:
    def __init__(self, labeling_mode='spatial'):
        self.A = self.get_adjacency_matrix(labeling_mode)
        self.num_node = num_node
        self.self_link = self_link
        self.inward = inward
        self.outward = outward
        self.neighbor = neighbor

    def get_adjacency_matrix(self, labeling_mode=None):
        if labeling_mode is None:
            return self.A
        if labeling_mode == 'spatial':
            A = tools.get_spatial_graph(num_node, self_link, inward, outward)
        else:
            raise ValueError()
        return A


if __name__ == '__main__':
    A = Graph('spatial').get_adjacency_matrix()
    print('')
