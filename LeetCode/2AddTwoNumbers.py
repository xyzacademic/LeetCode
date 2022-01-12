# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode()
        count = 0
        temp = head

        while l1 or l2 or count:
            temp_sum = 0
            if l1:
                temp_sum += l1.val
                l1 = l1.next
            if l2:
                temp_sum += l2.val
                l2 = l2.next
            if count:
                temp_sum += count

            count, rest = divmod(temp_sum, 10)
            temp.next = ListNode(rest)
            temp = temp.next

        return head.next