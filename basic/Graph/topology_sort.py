"""
Topology sort
"""
from basic.collection.graph import Graph
from basic.collection.queue_ import Queue


def topology_sort(g):
    if g.vertices == {}:
        return

    queue = Queue()
    results = []
    in_map = {}

    for vertex in g.vertices:
        if vertex.in_degree == 0:
            queue.enqueue(vertex)
        in_map[vertex.key] = vertex.in_degree

    while not queue.is_empty():
        vertex = queue.dequeue()
        results.append(vertex)

        for next_vertex in vertex.neighbors:
            in_map[next_vertex.key] -= 1
            if in_map[next_vertex.key] == 0:
                queue.enqueue(next_vertex)

    return results