"""
Recurrent
Time Complexity: O(N)
Space Complexity: O(N) Height
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        tmp = root.left

        root.left = self.mirrorTree(root.right)
        root.right = self.mirrorTree(tmp)

        return root