class Solution:
    def maxArea(self, height: List[int]) -> int:
        if not height or len(height) == 0:
            return 0

        area = 0

        i = 0
        j = len(height) - 1
        """
        1 8 6 2 5 4 8 3 7
        0 1 2 3 4 5 6 7 8

        8 49 18
        """
        while i < j:
            # area = max(area, min(height[i], height[j]) * (j-i))
            if height[i] < height[j]:
                area = max(area, height[i] * (j - i))
                i += 1
            else:
                area = max(area, height[j] * (j - i))
                j -= 1

        return area