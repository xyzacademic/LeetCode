class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        #         cache = [None] * len(nums)
        #         cache[0] = nums[0]
        #         def process(i, cache):
        #             if cache[i] != None:
        #                 return cache[i]
        #             # max of f(i) and f(i-1)
        #             cache[i] = max(process(i-1, cache)+nums[i], nums[i])
        #             return cache[i]

        #         for i in range(len(nums)):
        #             process(i, cache)

        max_score = nums[0]
        prev_score = 0
        for num in nums:
            prev_score = max(prev_score + num, num)
            max_score = max(max_score, prev_score)

        return max_score
