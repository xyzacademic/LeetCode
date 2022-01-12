class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root):

        if not root:
            return root

        # in-order

        stack = []
        stack.append(root)

        node = root
        tmp = Node()
        head = prev = tmp

        while stack:
            while node.left != prev and node.left:
                stack.append(node.left)
                node = node.left

            prev = tmp

            node = stack.pop()

            prev.right = node
            node.left = prev
            tmp = node
            if node.right:
                stack.append(node.right)
                node = node.right

        head.right.left = node
        node.right = head.right

        return head.right