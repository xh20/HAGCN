import numpy as np

epsilon = 1e-6


def normalize_incidence_matrix(im: np.ndarray, full_im: np.ndarray) -> np.ndarray:

    degree_mat = full_im.sum(-1) * np.eye(len(full_im))
    # Since all nodes should have at least some edge, degree matrix is invertible
    inv_degree_mat = np.linalg.inv(degree_mat)
    return (inv_degree_mat @ im) + epsilon


def edge2mat(link, num_node):
    A = np.zeros((num_node, num_node))
    for i, j in link:
        A[j, i] = 1
    return A


def normalize_digraph(A):  # 除以每列的和
    Dl = np.sum(A, 0)
    h, w = A.shape
    Dn = np.zeros((w, w))
    for i in range(w):
        if Dl[i] > 0:
            Dn[i, i] = Dl[i] ** (-1)
    AD = np.dot(A, Dn)
    return AD


def get_spatial_graph(num_node, self_link, inward, outward):
    I = edge2mat(self_link, num_node)
    In = normalize_digraph(edge2mat(inward, num_node))
    Out = normalize_digraph(edge2mat(outward, num_node))
    A = np.stack((I, In, Out))
    return A


def get_bone_graph(num_node, self_link, edges):
    I = edge2mat(self_link, num_node)
    inward = np.zeros((num_node, num_node))
    outward = np.zeros((num_node, num_node))
    # for edge_id in range(num_node):
    #     pos = [item[1] for item in edges if edge_id in item]
    #     inward[edge_id, pos] += 1
    #     outward[pos, edge_id] += 1
    # In = normalize_digraph(inward)
    # Out = normalize_digraph(outward)
    for edge_id, (source_node, target_node) in enumerate(edges):
        inward[source_node, target_node] = 1.
        outward[target_node, edge_id] = 1.
    full_graph = inward + outward
    # In = normalize_digraph(inward)
    # Out = normalize_digraph(outward)
    In = normalize_incidence_matrix(inward, full_graph)
    Out = normalize_incidence_matrix(outward, full_graph)
    A = np.stack((I, In, Out))
    return A