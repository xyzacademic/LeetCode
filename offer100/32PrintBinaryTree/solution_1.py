"""
Queue
Time Complexity: O(N)
Space Complexity: O(N)
"""
import collections

class Solution:
    def levelOrder(self, root):
        if not root:
            return []

        result = []
        queue = collections.deque()
        queue.append(root)

        while queue:
            node = queue.popleft()
            result.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return result