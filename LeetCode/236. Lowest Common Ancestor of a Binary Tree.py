# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        if not root or not p or not q:
            return root

        #         """
        #             r
        #         p       q

        #         """
        #         # case 1 if p and q are in either side of r
        #         if process(root.left) and process(root.right):
        #             return root

        #         # case 2 return p if q in p's subtree
        #         """
        #             r
        #         p
        #             q
        #         """
        #         if process(root.left) and not process(root.right):
        #             return root.left
        #         else:
        #             return root.right

        #         # case 3 return q if p in q's subtree

        def process(root, p, q):
            # find
            if not root or root == p or root == q:
                return root

            #
            a = process(root.left, p, q)
            b = process(root.right, p, q)

            # case 1
            if a is not None and b is not None:
                return root

            if not b:
                return a

            if not a:
                return b

            return None

        return process(root, p, q)

