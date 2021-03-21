from basic.collection.tree import Node
from basic.collection.stack import Stack


def postorder_recursive(head, results):
    if not head:
        return

    postorder_recursive(head.left, results)
    postorder_recursive(head.right, results)
    results.append(head.val)

    return


def postorder_stack(head, results):

    if not head:
        return

    # temp_stack = Stack()
    # temp_stack_a = Stack()
    # temp_stack.push(head)
    #
    # while not temp_stack.is_empty():
    #     node = temp_stack.pop()
    #     temp_stack_a.push(node)
    #
    #     if node.left is not None:
    #         temp_stack.push(node.left)
    #
    #     if node.right is not None:
    #         temp_stack.push(node.right)

    # while not temp_stack_a.is_empty():
    #     node = temp_stack_a.pop()
    #     results.append(node.val)

    temp_stack = Stack()
    temp_stack.push(head)

    while not temp_stack.is_empty():
        c = temp_stack.peek()

        if c.left and c.left != head and c.right != head:
            temp_stack.push(c.left)

        elif c.right and c.right != head:
            temp_stack.push(c.right)

        else:
            c = temp_stack.pop()
            results.append(c.val)
            head = c


    return


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

    pro = [0, 1, 3, 4, 2, 5, 6]
    ino = [3, 1, 4, 0, 5, 2, 6]
    poo = [3, 4, 1, 5, 6, 2, 0]

    results = []
    print('postorder: ', poo)
    postorder_recursive(nodes[0], results)
    print('postorder recursive traversal: ', results)

    results = []
    print('postorder: ', poo)
    postorder_stack(nodes[0], results)
    print('postorder stack traversal: ', results)