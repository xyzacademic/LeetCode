class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        # check
        if not nums or len(nums) < 2:
            return len(nums)

        left = 0
        right = 1

        while right < len(nums):
            if nums[left] == nums[right]:
                right += 1
            else:
                nums[left + 1] = nums[right]
                left += 1
                right += 1

        return left + 1
