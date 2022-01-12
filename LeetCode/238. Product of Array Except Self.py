class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        if not nums:
            return []

        n = len(nums)
        results = [1] * n

        for i in range(1, n):
            results[i] = results[i - 1] * nums[i - 1]

        r = 1

        for i in range(n - 1, -1, -1):
            results[i] *= r
            r *= nums[i]

        return results