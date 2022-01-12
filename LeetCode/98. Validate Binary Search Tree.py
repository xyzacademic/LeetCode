# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        if not root:
            return True

        # # recursive return True and max value
        # """
        # case 1, dont' have children
        #         return root.val if not root.left and not root.right
        # case 2, have only one child
        #         if not root.left and f(fl) < root.val return root.val
        #         if not root.right and f(fr) > root.val return f(fr)
        # case 3, have both left and right child

        # func check_is_bst:
        # if left tree is True, right tree is true, return max val
        # """
        # def check_is_bst(root):

        #     # case 1
        #     if not root.left and not root.right:
        #         return True, root.val

        #     if root.left is not None and root.right is not None:
        #     fl = check_is_bst(root.left)
        #     fr = check_is_bst(root.right)

        #     # case 2
        #     if root.left is not None and not root.right:
        #         # isBst, max_val = check_is_bst(root.left)
        #         # if not isBst:
        #         #     return False, max_val
        #         # return True, max_val
        #         return check_is_bst(root.left)

        # in order traversal should be ascend order

        """
                5
            4       6
          N   N   3    7 
        """

        current_value = -inf

        stack = []

        stack.append(root)
        head = root
        while stack:
            while head.left:
                stack.append(head.left)
                head = head.left
            node = stack.pop()
            if node.val <= current_value:
                return False
            current_value = node.val
            if node.right:
                stack.append(node.right)
                head = node.right

        return True