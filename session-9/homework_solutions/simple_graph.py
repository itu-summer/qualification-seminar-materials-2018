from episode_4_data import NODE_NAMES, EDGES


class Vertex:
    """ The Vertex from the lecture slides."""
    def __init__(self, key):
        self.key = key
        self.edges_to = []

    def add_edge(self, target):
        self.edges_to.append(target)


class Graph:
    """ The graph from the lecture slides."""
    def __init__(self):
        self.vertices = {}
        self.num_of_vertices = 0

    def add_vertex(self, key):
        self.num_of_vertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex

    def add_edge(self, source, target):
        self.vertices[source].add_edge(self.vertices[target])

    def __iter__(self):
        return iter(self.vertices.values())

    def __str__(self):
        self_str = ''
        for _, vertex in self.vertices.items():
            self_str += str(vertex) + '\n'
        return self_str