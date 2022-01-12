# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        if not root:
            return ''

        queue = []
        results = []
        queue.append(root)

        while queue:
            node = queue.pop(0)
            if node:
                results.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                results.append('#')

        return ",".join(results)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '#' or data == '':
            return None

        queue = data.split(',')
        val = queue[0]
        root = TreeNode(int(val))
        node = root
        temp_queue = []
        temp_queue.append(root)

        idx = 1
        while temp_queue:
            node = temp_queue.pop(0)
            if queue[idx] != '#':
                node.left = TreeNode(int(queue[idx]))
                temp_queue.append(node.left)
            idx += 1
            if queue[idx] != '#':
                node.right = TreeNode(int(queue[idx]))
                temp_queue.append(node.right)
            idx += 1

        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))