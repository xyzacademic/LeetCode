# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def check(root1, root2):

            if not root1 and not root2:
                return True
            elif not (root1 and root2) or root1.val != root2.val:
                return False
            else:
                return check(root1.left, root2.left) and check(root1.right, root2.right)

        def recursive(root1, root2):

            if not root1:
                return False

            return check(root1, root2) or recursive(root1.left, root2) or recursive(root1.right,
                                                                                    root2)

        return recursive(s, t)