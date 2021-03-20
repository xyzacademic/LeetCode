"""
Recurrent
Time Complexity: O(MN)
Space Complexity: O(M)
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        return bool(A and B) and (self.check(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B))

    def check(self, root_a, root_b):
        if not root_b:
            return True
        if not root_a or root_a.val != root_b.val:
            return False

        return self.check(root_a.left, root_b.left) and self.check(root_a.right, root_b.right)