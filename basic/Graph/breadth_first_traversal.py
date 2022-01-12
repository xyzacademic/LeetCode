"""
Breadth first traversal
"""
from basic.collection.graph import Graph
from basic.collection.queue_ import Queue


def bft(head=None, results=[]):
    if not head:
        return

    queue = Queue
    queue.enqueue(head)

    while not queue.is_empty():
        node = queue.dequeue()
        results.append(node.key)

        if node.neighbors is not {}:
            for key in node.neighbors:
                if key not in results:
                    queue.enqueue(node.neighbors[key])

    