"""
definition in grash
"""


class Vertex(object):
    def __init__(self, key):
        self.key = key
        self.in_degree = 0
        self.out_degree = 0
        self.neighbors = {}
        self.edges = {}
        
        
class Edge(object):
    def __init__(self, from_vertex, to_vertex, weight):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight


class Graph(object):
    def __init__(self):
        self.vertices = {}
        self.edges = {}



def matrix_to_graph(matrix):
    if matrix == [] or matrix == [[]]:
        raise ValueError(f'Input matrix {matrix} is empty')

    g = Graph()

    for i in range(len(matrix)):
        weight = matrix[i][0]
        from_key = matrix[i][1]
        to_key = matrix[i][2]

        if from_key not in g.vertices:
            g.vertices[from_key] = Vertex(from_key)

        if to_key not in g.vertices:
            g.vertices[to_key] = Vertex(to_key)

        new_edge = Edge(g.vertices[from_key], g.vertices[to_key], weight)
        g.edges.append(new_edge)
        g.vertices[from_key].out_degree += 1
        g.vertices[to_key].in_degree += 1
        g.vertices[from_key].neighbors[to_key] = g.vertices[to_key]
        g.vertices[from_key].edges[to_key] = new_edge

    return g

if __name__ == '__main__':
    matrix = []

    g = matrix_to_graph(matrix)