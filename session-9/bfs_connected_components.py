import sys
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
        for v in self.vertices.values():
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

    def bfs_connected_component(self, start_vertex):
        visit_queue = Queue()
        visit_queue.enqueue(start_vertex)
        while not visit_queue.is_empty():
            current_vertex = visit_queue.dequeue()
            target_vertices = self.vertices[current_vertex.key].edges_to
            for neighbor in target_vertices:
                if neighbor.get_color() == 'white':
                    neighbor.set_color('gray')
                    visit_queue.enqueue(neighbor)
            current_vertex.set_color('black')

            # This is code that allows you to generate plots of the graph with
            # white, gray, and black nodes that visualize the 'seen' nodes,
            # which are gray and those on the queue, which are black
            # To enable generation of plots uncomment the following code:
            #
            if plot_single_steps:
                if 'count' not in locals():
                    count = 0
                self.plot(w_node_color=True,
                          graph_file=f'tmp_graph{count}.html')
                count += 1

    def print_members_of_connected(self):
        for vertex in self.vertices.values():
            if vertex.get_color() == 'black':
                print(vertex.key)

    # finds shortest path between 2 nodes of a graph using BFS
    def bfs_shortest_path(self, start_vertex, goal_vertex):
        # explored = []
        # keep track of all the paths to be checked
        paths_queue = Queue()
        paths_queue.enqueue([start_vertex])
        # return path if start is goal
        if start_vertex == goal_vertex:
            return [repr(start_vertex)]
        # keeps looping until all possible paths have been checked
        while not paths_queue.is_empty():
            # pop the first path from the queue
            path = paths_queue.dequeue()
            # get the last node from the path
            node = path[-1]
            if node.get_color() == 'white':
                neighbors = node.edges_to
                # go through all neighbor nodes, construct a new path and
                # push it into the queue
                for neighbor in neighbors:
                    # We have to create a new copy of the path list
                    new_path = list(path)
                    new_path.append(neighbor)
                    paths_queue.enqueue(new_path)
                    # return path if neighbor is goal
                    if neighbor == goal_vertex:
                        return new_path
                # mark node as explored
                node.set_color('black')
        # in case there's no path between the 2 nodes
        return []


plot_single_steps = False


def main():
    g = Graph()
    for name in ep4.NODE_NAMES:
        g.add_vertex(name)
    for source, target in ep4.EDGES:
        g.add_edge(source, target)

    print(g)
    g.plot()
    g.bfs_connected_component(g.vertices['Biggs'])
    g.print_members_of_connected()

    print('The shortest path from Biggs to Jabba is:')
    g.whiten_out()
    print(g.bfs_shortest_path(g.vertices['Biggs'], g.vertices['Jabba']))


if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'plot_steps':
        plot_single_steps = True
    main()
