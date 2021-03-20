"""
Stack
Time Complexity: O(n)
Space Complexity: O(n)
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) ->list[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next

        return stack[::-1]