class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        results = []

        for num in nums:
            idx = abs(num) - 1
            if nums[idx] < 0:
                results.append(abs(num))
            nums[idx] = - nums[idx]

        return results