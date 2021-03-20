"""
Recurrent
Time Complexity: O(n)
Space Complexity: O(n)
Pre-order: Root | Left | Right
In-order: Left | Root | Right
Post-order: Left | Right | Root
"""



class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self, ):
        self.dic = {}  # look up table for in-order sequence
        self.po = None

    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        self.po = preorder

        # build look up table for index
        for i in range(len(preorder)):
            self.dic[inorder[i]] = i

        # return root node
        return self.recur(0, 0, len(inorder) - 1)

    def recur(self, root_index_preorder, left_inorder, right_inorder):
        """

        :param root_index_preorder: tree's root index in pre-order sequence
        :param left_inorder: the left index
        :param right_inorder: the right index
        :return: TreeNode
        """

        # check subtree is empty
        if left_inorder > right_inorder:
            return None

        root = TreeNode(self.po[root_index_preorder])
        root_index_inorder = self.dic[root.val]
        root.left = self.recur(
            root_index_preorder + 1, left_inorder, root_index_inorder - 1
        )
        root.right = self.recur(
            root_index_inorder + 1 - left_inorder + root_index_preorder, root_index_inorder + 1, right_inorder
        )

        return root