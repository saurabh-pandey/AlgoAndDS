#Description
"""
Finding minimum cut of graph using Karger's randomized minimum cut algorithm for connected graphs. 

NOTE: This problem was discussed in Tim's algo-1 course as a first motivating problem for i
introducing graph data structures and algorithms.
"""
import math
import random

class Vertex:
    def __init__(self, value) -> None:
        assert value, "Value of vertex can't be empty"
        self.val = value
    
    def get_value(self):
        return self.val

class Edge:
    def __init__(self, vert1, vert2) -> None:
        assert vert1, "Vertex 1 of edge is None"
        assert vert2, "Vertex 2 of edge is None"
        self.verts = (vert1, vert2)
    
    def get_vertices(self):
        return self.verts


class Graph:
    def __init__(self, fileName) -> None:
        # IDEA
        # Will go for all the features needed in Vertex, Edge and Graph DS.
        # Need to randomly pick edges so getAllEdges()
        # Given a random edge now collapse()
        # Collapse also changes the vertices by fusing some
        # Vertex has a unique id and some indexes it represents
        # Initially id and index is the same but as we merge vertices indexes append and build-up
        # Need the ability to clean self-loops in the graph after an edge collapse
        # Self-loop is edge with same vertex on both ends
        # Start with undirected version first
        self.vertices = []
        self.edges = []
        with open(fileName) as graphFile:
            for line in graphFile:
                # print("  Line = ", line)
                verts_row = line.split()
                if verts_row:
                    if len(verts_row) == 1:
                        self.add_vertex(verts_row[0])
                    else:
                        root_vert = verts_row[0]
                        for vert in verts_row[1:]:
                            self.add_edge(root_vert, vert)

    def add_vertex(self, value):
        new_vert = Vertex(value)
        self.vertices.append(new_vert)
        return new_vert
    
    def remove_vertex(self, index):
        del self.vertices[index]
    
    def add_edge(self, value1, value2):
        new_vert1 = Vertex(value1)
        new_vert2 = Vertex(value2)
        self.vertices.append(new_vert1)
        self.vertices.append(new_vert2)
        new_edge = Edge(new_vert1, new_vert2)
        self.edges.append(new_edge)
    
    def num_vertices(self):
        return len(self.vertices)

    def num_edges(self):
        return len(self.edges)
    
    def get_edge(self, index):
        assert index < len(self.edges), "Edge index out of range"
        return self.edges[index]

    def get_degree(self, index):
        pass

    def print(self):
        for e in self.edges:
            print(e.verts[0].val, " ", e.verts[1].val)


def get_random_edge(g):
    num_edges = g.num_edges()
    rand_edge_index = random.randrange(num_edges)
    return g.get_edge(rand_edge_index)

def collapse_edge(g, edge):
    # Pick the two vertices
    vert1, vert2 = edge.get_vertices()
    # Merge
    merged_vert = g.add_vertex([vert1.get_value(), vert2.get_value()])
    
    # Update all edges with v1 or v2 as end point to point to merged vertex
    # all_edges_with_vert1 as end-point
    # for each with vert1 as end-point replace vert1 with merged vert
    # for each with vert2 as end-point replace vert2 with merged vert
    # all_edges_with_vert2 as end-point
    
    # Delete vert1 and vert2
    
    # Remove this edge
    pass

def clear_self_loops(edge):
    # Post edge collapse now remove any self-loops
    pass

def find_min_cut(graphFile):
    print("\nFile = ", graphFile)
    g = Graph(graphFile)
    g.print()
    # return
    num_verts = g.num_vertices()
    if num_verts == 0:
        return 0
    num_iterations = num_verts * num_verts * math.ceil(math.log(num_verts))
    min_cut_sz = num_verts * (num_verts - 1)//2
    iteration = 0
    while iteration < num_iterations:
        while g.num_vertices() > 2:
            edge = get_random_edge(g)
            collapse_edge(g, edge)
            clear_self_loops(edge)
        num_edges = g.num_edges()
        if num_edges < min_cut_sz:
            min_cut_sz = num_edges
    return min_cut_sz
