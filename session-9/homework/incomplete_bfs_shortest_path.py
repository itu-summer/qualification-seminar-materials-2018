from itu_queue import Queue


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
