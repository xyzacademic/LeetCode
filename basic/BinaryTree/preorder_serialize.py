from basic.collection.queue_ import Queue
from basic.collection.tree import Node


def preorder_serialize(head=None):

    if not head:
        return '#'

    return str(head.val) + ',' + str(preorder_serialize(head.left)) + \
           ',' + str(preorder_serialize(head.right))



def inorder_serialize(head=None, results=[]):
    pass



serialize_method = {}
serialize_method['preorder'] = preorder_serialize


def serialize(head, kind='preorder'):

    return serialize_method[kind](head)


def deserialize(sequence, kind='preorder'):

    list = sequence.split(',')

    return deserialize_method[kind](list)


def preorder_deserialize(list):
    if len(list) <= 0:
        return None

    root = None
    val = list.pop(0)

    if val != '#':
        root = Node(int(val))
        root.left = preorder_deserialize(list)
        root.right = preorder_deserialize(list)

    return root

deserialize_method = {}
deserialize_method['preorder'] = preorder_deserialize


if __name__ == '__main__':
    """
            0
        1       2
    None   4   5   None

    pre-order: 0 1 3 4 2 5 6
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


    sequence = serialize(head, kind='preorder')
    print('Level traversal: ', sequence)

    k = deserialize(sequence, kind='preorder')
    sequence = serialize(k, kind='preorder')
    print('Level traversal: ', sequence)
