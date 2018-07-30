from itu_queue import Queue
import episode_4_data as ep4
from graph_plotter import make_plot


class Vertex:
    def __init__(self, key):
        self.key = key
        self.edges_to = []
        # needed for bfs
        self.color = 'white'


    def __str__(self):
        edges_str = str([target.key for target in self.edges_to])
        self_str = '{} -> {}'.format(str(self.key), edges_str)
        return self_str


    def __repr__(self):
        return f"Vertex('{self.key}')"


    def __eq__(self, other):
        return self.key == other.key


    def add_edge(self, target):
        self.edges_to.append(target)


    # needed for bfs
    def set_color(self, color):
        self.color = color


    def get_color(self):
        return self.color


class Graph:
    def __init__(self):
        self.vertices = {}
        self.num_of_vertices = 0
        self.all_paths = []


    def whiten_out(self):
        for v in self.vertices:
            v.set_color('white')

 
    def add_vertex(self, key):
        self.num_of_vertices += 1
        new_vertex = Vertex(key)
        self.vertices[key] = new_vertex
        return new_vertex


    def add_edge(self, source, target):
        self.vertices[source].add_edge(self.vertices[target])


    def get_edges(self):
        edges = []
        for _, vertex in self.vertices.items():
            edges += [(vertex.key, target.key) for target in vertex.edges_to]
        return edges


    def __iter__(self):
        return iter(self.vertices.values())


    def __str__(self):
        self_str = ''
        for _, vertex in self.vertices.items():
            self_str += str(vertex) + '\n'
        return self_str


    def plot(self, w_node_color=False, graph_file='tmp_graph.html'):
        make_plot(self, w_node_color=w_node_color, graph_file=graph_file)

    def dfs(self, start_vertex):
        visit_queue = Queue()
        visit_queue.enqueue(start_vertex)
        while not visit_queue.is_empty():
            current_vertex = visit_queue.left_dequeue() 
            if current_vertex.get_color() == 'white':
                target_vertex = self.vertices[current_vertex.key].edges_to
                for neighbor in target_vertex:
                    if neighbor.get_color() == 'white':
                        visit_queue.enqueue(neighbor)
                current_vertex.set_color('black')
                # This is code that allows you to generate plots of the graph with
                # white, gray, and black nodes that visualize the 'seen' nodes,
                # which are gray and those on the queue, which are black
                # To enable generation of plots uncomment the following code:
                #
                # if 'count' not in locals():
                #     count = 0
                # self.plot(w_node_color=True, graph_file=f'tmp_graph{count}.html')
                # count += 1


def main():
    g = Graph()
    for name in ep4.NODE_NAMES:
        g.add_vertex(name)
    for source, target in ep4.EDGES:
        g.add_edge(source, target)

    print(g)
    g.plot()
    g.dfs(g.vertices['Biggs'])


if __name__ == '__main__':
    main()
