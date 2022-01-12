from basic.collection.queue_ import Queue
from basic.collection.tree import Node


def level_traversal(head, results):

    if not head:
        return

    queue = Queue()

    queue.enqueue(head)

    while not queue.is_empty():
        node = queue.dequeue()
        results.append(node.val)

        if node.left is not None:
            queue.enqueue(node.left)

        if node.right is not None:
            queue.enqueue(node.right)

    return results


if __name__ == '__main__':
    """
            0
        1       2
      3   4   5   6

    pre-order: 0 1 3 4 2 5 6
    in-order:  3 1 4 0 5 2 6
    post-order:3 4 1 5 6 2 0


    """

    nodes = [Node(i) for i in range(7)]
    head = nodes[0]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = nodes[6]

    results = []

    level_traversal(nodes[0], results)
    print('Level traversal: ', results)

