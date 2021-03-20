"""
Recurrent

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True

        return self.check(root.left, root.right)

    def check(self, node_a, node_b):
        if not node_a and not node_b:
            return True

        if not node_a or not node_b or node_a.val != node_b.val:
            return False

        return self.check(node_a.left, node_b.right) and self.check(node_a.right, node_b.left)