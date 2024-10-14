import sys
import numpy as np

sys.path.extend(['../'])
from graph import tools

num_node = 17
self_link = [(i, i) for i in range(num_node)]
split_body = [(0, 1), (0, 2), (1, 3), (2, 4), (5, 6), (5, 7), (6, 8), (5, 11),
              (6, 12), (11, 13), (12, 14), (13, 15), (14, 16),
              # additional edge
              (0, 10), (0, 9), (0, 15), (0, 16), (9, 10), (9, 15), (9, 16), (10, 15), (10, 16), (15, 16)
              ]
inward = [(i, j) for (i, j) in split_body]  # inward_ori_index
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
            A = tools.get_spatial_graph(num_node, self_link, inward, outward)  # outward
        else:
            raise ValueError()
        return A


if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import os

    # os.environ['DISPLAY'] = 'localhost:11.0'
    A = Graph('spatial').get_adjacency_matrix()
    print(A.shape)
    plt.clf()
    plt.figure().clear()

    plt.close('all')
    index = 0
    for i in A:
        plt.imshow(i, cmap='gray')
        plt.title("image graph{}".format(index))
        # plt.show()
        plt.savefig('../visulization/graph_original_A_{}.png'.format(index))

        index += 1

