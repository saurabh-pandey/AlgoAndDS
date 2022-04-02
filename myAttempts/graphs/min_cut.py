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
        self.edges = []
    
    def get_value(self):
        return self.val
    
    def add_edge(self, edge):
        self.edges.append(edge)
    
    def get_edges(self):
        return self.edges

class Edge:
    def __init__(self, v0, v1) -> None:
        assert v0, "Vertex 0 of edge is None"
        assert v1, "Vertex 1 of edge is None"
        self.v0 = v0
        self.v1 = v1
    
    def get_vertices(self):
        return (self.v0, self.v1)
    
    def get_vertex0(self):
        return self.v0
    
    def set_vertex0(self, v):
        assert v, "Null cannot be set as vertex 0"
        self.v0 = v
    
    def get_vertex1(self):
        return self.v1

    def set_vertex1(self, v):
        assert v, "Null cannot be set as vertex 1"
        self.v1 = v


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
    
    def remove_vertex(self, value):
        for i, v in enumerate(self.vertices):
            if v.get_value() == value:
                del self.vertices[i]
                return
        
    
    def add_edge(self, value1, value2):
        new_vert1 = Vertex(value1)
        new_vert2 = Vertex(value2)
        self.vertices.append(new_vert1)
        self.vertices.append(new_vert2)
        new_edge = Edge(new_vert1, new_vert2)
        self.edges.append(new_edge)
        new_vert1.add_edge(new_edge)
        new_vert2.add_edge(new_edge)
    
    def remove_edge(self, edge):
        for i, e in enumerate(self.edges):
            if ((e.get_vertex0().get_value() == edge.get_vertex0().get_value())
            and (e.get_vertex1().get_value() == edge.get_vertex1().get_value())):
                del self.edges[i]
                return
            if ((e.get_vertex0().get_value() == edge.get_vertex1().get_value())
            and (e.get_vertex1().get_value() == edge.get_vertex0().get_value())):
                del self.edges[i]
                return
    
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
            print(e.v0.val, " ", e.v1.val)


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
    for e in vert1.get_edges():
        if e.get_vertex0().get_value() == vert1.get_value():
            e.set_vertex0(merged_vert)
        if e.get_vertex1().get_value() == vert1.get_value():
            e.set_vertex1(merged_vert)
    for e in vert2.get_edges():
        if e.get_vertex0().get_value() == vert2.get_value():
            e.set_vertex0(merged_vert)
        if e.get_vertex1().get_value() == vert2.get_value():
            e.set_vertex1(merged_vert)
    
    # Delete vert1 and vert2
    g.remove_vertex(vert1)
    g.remove_vertex(vert2)
    
    # Remove this edge
    g.remove_edge(edge)
    

def clear_self_loops(edge):
    # Post edge collapse now remove any self-loops
    pass

def find_min_cut(graphFile):
    print("\nFile = ", graphFile)
    g = Graph(graphFile)
    g.print()
    # return
    num_verts = g.num_vertices()
    if num_verts < 2:
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
