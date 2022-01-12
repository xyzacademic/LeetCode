from basic.collection.tree import Node
from basic.collection.stack import Stack

def inorder_recursive(head, results):
    if not head:
        return



    inorder_recursive(head.left, results)
    results.append(head.val)
    inorder_recursive(head.right, results)

    return


def inorder_stack(head, results):

    if not head:
        return

    temp_stack = Stack()
    temp_stack.push(head)

    node = head

    while not temp_stack.is_empty():

        while node.left is not None:
            temp_stack.push(node.left)
            node = node.left

        cur = temp_stack.pop()
        results.append(cur.val)

        if cur.right is not None:
            temp_stack.push(cur.right)
            node = cur.right

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
    print('inorder: ', ino)
    inorder_recursive(nodes[0], results)
    print('inorder recursive traversal: ', results)

    results = []
    print('inorder: ', ino)
    inorder_stack(nodes[0], results)
    print('inorder stack traversal: ', results)