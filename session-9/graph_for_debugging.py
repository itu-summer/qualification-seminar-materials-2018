from episode_4_data import NODE_NAMES, EDGES


class Vertex:
    def __init__(self, key):
        self.key = key
        self.edges_to = []

    def add_edge(self, target):
        self.edges_to.append(target)


class Graph:
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

    def print(self):
        pass


def main():
    # Creating the graph
    g = Graph()

    # Creating the nodes
    for name in NODE_NAMES:
        g.add_vertex(name)

    # Creating the edges
    for source, target in EDGES:
        g.add_edge(source, target)

    g.print()


if __name__ == '__main__':
    main()
