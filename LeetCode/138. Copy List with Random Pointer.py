"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':

        if not head:
            return head

        p_original = head

        # insert new node
        while p_original:
            new_node = Node(p_original.val, p_original.next, None)
            p_original.next = new_node
            p_original = new_node.next

        # build random link
        p_original = head

        while p_original:
            p_original.next.random = p_original.random.next if p_original.random is not None else None
            p_original = p_original.next.next

        # delete link
        p_original = head
        p_new = head.next
        pn = head.next

        while p_original:
            p_original.next = p_original.next.next
            p_new.next = p_new.next.next if p_new.next is not None else None
            p_original = p_original.next
            p_new = p_new.next

        return pn