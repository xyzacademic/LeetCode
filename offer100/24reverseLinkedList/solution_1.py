"""
Dual pointer
"""

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head:
            return head
        cur = None
        # pre = head
        while head:
            temp = ListNode(head.val)

            temp.next = cur

            head = head.next
            cur = temp

        return cur