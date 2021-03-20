"""
Binary Search
Time Complexity: O(logn)
Space Complexity: O(1)
"""


class Solution:
    def minArray(self, numbers: List[int]) -> int:
        i = 0
        j = len(numbers) - 1

        while i < j:
            m = (i + j) // 2
            if numbers[m] < numbers[j]:
                j = m
            elif numbers[m] > numbers[j]:
                i = m + 1
            else:
                j -= 1

        return numbers[i]