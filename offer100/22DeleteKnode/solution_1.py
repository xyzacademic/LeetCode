"""
Dual pointer
Time Complexity: O(N)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head

        cur_pointer = head
        for i in range(k):
            cur_pointer = cur_pointer.next

        prev_pointer = head

        while cur_pointer:
            cur_pointer = cur_pointer.next
            prev_pointer = prev_pointer.next

        return prev_pointer
