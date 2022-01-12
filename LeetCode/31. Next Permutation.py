class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # check
        if not nums or len(nums) == 0:
            return []

        if len(nums) == 1:
            return nums

        n = len(nums)

        i = n - 2
        while i > -1 and nums[i] >= nums[i + 1]:
            i -= 1

        if i >= 0:
            j = i + 1
            while j < n and nums[j] > nums[i]:
                j += 1
            j -= 1
            # swap
            nums[i], nums[j] = nums[j], nums[i]

        j = n - 1
        i += 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1

        return nums