class Solution:
    def connect(self, root):

        if not root:
            return root

        cur = root

        current_nodes = 1
        # traversal cross current layer connect next layer
        # next_left = root.left if root.left else root.right
        while current_nodes:
            next_nodes = 0

            while not cur.left and not cur.right:
                # print(cur.val)
                cur = cur.next
                if not cur:
                    return root
            next_left = cur.left if cur.left else cur.right
            next_nodes += 1
            tmp = next_left

            if cur.left and cur.right:
                tmp.next = cur.right
                tmp = tmp.next
                next_nodes += 1

            while cur.next:
                cur = cur.next
                if cur.left:
                    tmp.next = cur.left
                    tmp = tmp.next
                    next_nodes += 1
                if cur.right:
                    tmp.next = cur.right
                    tmp = tmp.next
                    next_nodes += 1

            current_nodes = next_nodes
            cur = next_left