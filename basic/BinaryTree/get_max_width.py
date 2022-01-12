from basic.collection.queue_ import Queue
from basic.collection.tree import Node


def get_max_width(head=None):

    if not head:
        return 0, 0

    max_width = 1
    current_level = 0
    max_width_level = 0
    current_level_width = 1

    queue = Queue()
    queue.enqueue(head)

    while not queue.is_empty():
        # initial next level width
        next_level_width = 0

        for i in range(current_level_width):
            node = queue.dequeue()

            if node.left is not None:
                next_level_width += 1
                queue.enqueue(node.left)

            if node.right is not None:
                next_level_width += 1
                queue.enqueue(node.right)

        if next_level_width > max_width:
            max_width = next_level_width
            max_width_level = current_level + 1

        current_level += 1
        current_level_width = next_level_width

    return max_width, max_width_level


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

    max_width, level = get_max_width(nodes[0])
    print(f'Maximum width is {max_width}, at level {level}')

