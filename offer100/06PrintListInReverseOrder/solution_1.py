"""
Recurrent
Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> list[int]:
        return self.reversePrint(head.next) + [head.val] if head else []