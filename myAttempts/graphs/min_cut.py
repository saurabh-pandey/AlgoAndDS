#Description
"""
Finding minimum cut of graph using Karger's randomized minimum cut algorithm for connected graphs. 

NOTE: This problem was discussed in Tim's algo-1 course as a first motivating problem for i
introducing graph data structures and algorithms.
"""
import math
import random

class Graph:
    def __init__(self, fileName) -> None:
        pass

    def num_vertices(self):
        pass

    def num_edges(self):
        pass

    def get_degree(self, index):
        pass


def get_random_edge(g):
    num_verts = g.num_vertices()
    rand_vert = random.randrange(num_verts)
    vert_degree = g.get_degree(rand_vert)
    rand_edge = random.randrange(vert_degree)
    return (rand_vert, rand_edge)

def collapse_edge(edge):
    # Pick the two vertices
    # Merge
    # Remove this edge
    pass

def clear_self_loops(edge):
    # Post edge collapse now remove any self-loops
    pass

def find_min_cut(graphFile):
    g = Graph(graphFile)
    num_verts = g.num_vertices()
    if num_verts == 0:
        return 0
    num_iterations = num_verts * num_verts * math.ceil(math.log(num_verts))
    min_cut_sz = num_verts * (num_verts - 1)//2
    iteration = 0
    while iteration < num_iterations:
        while g.num_vertices() > 2:
            edge = get_random_edge(g)
            collapse_edge(edge)
            clear_self_loops(edge)
        num_edges = g.num_edges()
        if num_edges < min_cut_sz:
            min_cut_sz = num_edges
    return min_cut_sz
