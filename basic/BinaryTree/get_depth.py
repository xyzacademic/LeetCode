from basic.collection.queue_ import Queue
from basic.collection.tree import Node


def get_max_depth_recursive(head=None):
    """
    recursive
    Time O(n)  have to traversal all nodes
    Space O(height)

    :param head:
    :return:
    """
    if not head:
        return 0

    return max(get_max_depth_recursive(head.left),
               get_max_depth_recursive(head.right)) + 1


def get_min_depth_recursive(head=None):
    """
    key point: check if a node is a leaf
    time: O(n)
    space: O(height)
    :param head:
    :return:
    """

    if not head:
        return 0

    # if a node has less than two children, return
    # the deeper sub tree's height

    if not head.left or not head.right:
        return max(get_min_depth_recursive(head.left), 
                   get_min_depth_recursive(head.right)) + 1

    return min(get_min_depth_recursive(head.left), 
               get_min_depth_recursive(head.right)) + 1


def get_max_depth_queue(head=None):

    if not head:
        return 0

    queue = Queue()
    queue.enqueue(head)
    max_depth = 1
    current_width = 1

    while not queue.is_empty():
        next_level_width = 0

        for i in range(current_width):
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
                next_level_width += 1

            if node.right:
                queue.enqueue(node.right)
                next_level_width += 1

        current_width = next_level_width
        if next_level_width:
            max_depth += 1

    return max_depth


def get_min_depth_queue(head=None):
    """
    return the first leaf
    time: O(n)
    space: O(n)
    :param head:
    :return:
    """

    if not head:
        return 0

    queue = Queue()
    queue.enqueue(head)
    min_depth = 1
    current_level_width = 1

    while not queue.is_empty():
        next_level_width = 0

        for i in range(current_level_width):
            node = queue.dequeue()

            if node.left:
                queue.enqueue(node.left)
                next_level_width += 1

            if node.right:
                queue.enqueue(node.right)
                next_level_width += 1

            if not node.left and not node.right:
                return min_depth

        min_depth += 1

    return min_depth


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

    max_depth = get_max_depth_recursive(nodes[0])
    print(f'Recursive aximum depth is {max_depth}')

    max_depth = get_max_depth_queue(nodes[0])
    print(f'Queue aximum depth is {max_depth}')