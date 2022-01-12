from basic.collection.queue_ import Queue
from basic.collection.tree import Node
from basic.collection.stack import Stack

def postorder_serialize(head=None):

    if not head:
        return '#'

    return postorder_serialize(head.left) + ',' + \
           postorder_serialize(head.right) + ',' + \
            str(head.val)



def inorder_serialize(head=None, results=[]):
    pass



serialize_method = {}
serialize_method['postorder'] = postorder_serialize


def serialize(head, kind='postorder'):

    return serialize_method[kind](head)


def deserialize(sequence, kind='postorder'):

    list = sequence.split(',')

    return deserialize_method[kind](list)


def postorder_deserialize(list):
    if len(list) <= 0:
        return None

    stack = Stack()
    while len(list) > 0:
        stack.push(list.pop(0))

    def deserialize(stack):

        root = None
        val = stack.pop()
        if not val == '#':
            root = Node(int(val))
            root.right = deserialize(stack)
            root.left = deserialize(stack)

        return root

    return deserialize(stack)


deserialize_method = {}
deserialize_method['postorder'] = postorder_deserialize


if __name__ == '__main__':
    """
            0
        1       2
    None   4   5   None

    post-order: 0 1 3 4 2 5 6
    in-order:  3 1 4 0 5 2 6
    post-order:3 4 1 5 6 2 0


    """

    nodes = [Node(i) for i in range(7)]
    head = nodes[0]
    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = None
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[5]
    nodes[2].right = None


    sequence = serialize(head, kind='postorder')
    print('Level traversal: ', sequence)

    k = deserialize(sequence, kind='postorder')
    sequence = serialize(k, kind='postorder')
    print('Level traversal: ', sequence)
