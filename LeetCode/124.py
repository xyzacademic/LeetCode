class Solution:

    def maxPathSum(self, root: TreeNode) -> int:
        self.max_ = -inf

        def local_sum(root):

            if not root.left and not root.right:
                max_ = root.val
                self.max_ = max(self.max_, max_)
                return max_

            max_ = root.val
            left = 0
            right = 0

            if root.left:
                left = local_sum(root.left)
                max_ = max(max_, max_ + left)

            if root.right:
                right = local_sum(root.right)
                max_ = max(max_, max_ + right)

            self.max_ = max(self.max_, max_)
            r_m = max(root.val, root.val + max(left, right))
            return r_m

        local_sum(root)
        return self.max_