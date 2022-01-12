class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        if not nums:
            return []

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                nums[idx] *= -1
                return idx + 1
            nums[idx] *= -1

