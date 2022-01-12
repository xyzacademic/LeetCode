class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if not nums or len(nums) == 0:
            return None

        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if candidate == num else -1

        return candidate
