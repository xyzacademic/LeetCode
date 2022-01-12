# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        if not root:
            return root

        """
        i = even
        pop(0)
        3
        append(left, right)
        i = odd
        pop() right, left
        insert(0, right, left)
        [15 7 9]
        i = even
        [1 2 15 7]
        pop(0)


        """

        queue = []
        queue.append(root)

        results = []

        even = True
        current_node = 1
        while queue:

            temp = []
            next_level_node = 0

            if even:
                for i in range(current_node):

                    node = queue.pop(0)
                    temp.append(node.val)
                    if node.left:
                        queue.append(node.left)
                        next_level_node += 1
                    if node.right:
                        queue.append(node.right)
                        next_level_node += 1
                even = False

            else:
                for i in range(current_node):
                    node = queue.pop()
                    temp.append(node.val)
                    if node.right:
                        queue.insert(0, node.right)
                        next_level_node += 1
                    if node.left:
                        queue.insert(0, node.left)
                        next_level_node += 1
                even = True

            current_node = next_level_node
            results.append(temp)

        return results
