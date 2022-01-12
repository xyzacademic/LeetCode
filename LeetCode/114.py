class Solution:
    def flatten(self, root):

        if not root:
            return root

        def find_right(cur):
            # find rightest
            while cur.left or cur.right:
                cur = cur.right if cur.right else cur.left
            return cur

        cur = root
        while cur:
            if cur.left:
                tmp = find_right(cur.left)
                if cur.right:
                    tmp.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right

        return root



