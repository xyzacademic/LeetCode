"""
Dual pointer
Time Complexity: O(N)
Space Complexity: O(1)
"""

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_index = 0
        right_index = len(height) - 1
        area = 0

        while left_index < right_index:

            if height[left_index] < height[right_index]:
                area = max(area, height[left_index] * (right_index - left_index))
                left_index += 1
            else:
                area = max(area, height[right_index] * (right_index - left_index))
                right_index -= 1

        return area