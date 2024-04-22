import math
import numpy as np

def graph_normalize(graph):
    return graph * 2 - 1

def graph_dot(graph):
    # This is faster / more concise
    transpose = np.transpose(graph)
    return np.dot(graph, transpose)

    '''
    out = np.zeros(graph.shape)
    for i in range(graph.shape[0]):
        for j in range(graph.shape[0]):
            out[i, j] = np.dot(graph[i], graph[j])
    return out
    '''

def cutoff(graph, c):
    f = lambda x: 0 if x < c else 1
    return f(graph)

