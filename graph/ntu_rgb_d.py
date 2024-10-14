import sys
import numpy as np

sys.path.extend(['../'])
from graph import tools

num_node = 25
self_link = [(i, i) for i in range(num_node)]
inward_ori_index = [(1, 2), (2, 21), (3, 21), (4, 3), (5, 21), (6, 5), (7, 6),
                    (8, 7), (9, 21), (10, 9), (11, 10), (12, 11), (13, 1),
                    (14, 13), (15, 14), (16, 15), (17, 1), (18, 17), (19, 18),
                    (20, 19), (22, 8), (23, 7), (24, 12), (25, 11)]
edges = [(i-1, j-1) for i, j in [
    (1, 2), (2, 21), (3, 21), (4, 3), (5, 21), (6, 5), (7, 6), (8, 7), (9, 21), (10, 9), (11, 10), (12, 11),
    (13, 1),
    (14, 13), (15, 14), (16, 15), (17, 1), (18, 17), (19, 18), (20, 19), (21, 21),  (22, 23), (23, 8), (24, 25),
    (25, 12)    # Add self loop for Node 21 (the centre) to avoid singular matrices
]]
split_body = [(1, 2), (2, 21), (3, 21), (4, 3), (5, 21), (6, 5), (7, 6),
              (8, 7), (9, 21), (10, 9), (11, 10), (12, 11), (13, 1),
              (14, 13), (15, 14), (16, 15), (17, 1), (18, 17), (19, 18),
              (20, 19), (22, 8), (23, 7), (24, 12), (25, 11),
              # additional edge
              (4, 7), (4, 11), (4, 15), (4, 19), (7, 11), (7, 15), (7, 19), (11, 15), (11, 19), (15, 19)
              ]
inward = [(i - 1, j - 1) for (i, j) in split_body]  # inward_ori_index
outward = [(j, i) for (i, j) in inward]
neighbor = inward + outward
split_edges = [(i-1, j-1) for (i,j) in split_body]


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
        elif labeling_mode == 'multi':
            A = tools.get_spatial_graph(num_node, self_link, inward, outward)
            A1 = tools.get_bone_graph(num_node, self_link, edges)
            A = np.concatenate((A, A, A1), axis=0)
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

