class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        self.dic = {}
        self.po = preorder

        for i in range(len(inorder)):
            self.dic[inorder[i]] = i

        return self.recur(0, 0, len(inorder) - 1)

    def recur(self, root_index_preorder, left_inorder, right_inorder):
        if left_inorder > right_inorder:
            return

        root = TreeNode(self.po[root_index_preorder])
        i = self.dic[self.po[root_index_preorder]]
        root.left = self.recur(root_index_preorder + 1, left_inorder, i - 1)
        root.right = self.recur(i - left_inorder + root_index_preorder + 1, i + 1, right_inorder)

        return root
