class Solution:
    def jump(self, nums: List[int]) -> int:

        if not nums or len(nums) < 2:
            return 0

        current_idx = 0
        steps = 0
        while nums[current_idx] + current_idx < len(nums) - 1:
            max_distance = 0
            for i in range(nums[current_idx] + 1):
                if nums[current_idx + i] + i > max_distance:
                    next_position = i
                    max_distance = nums[current_idx + i] + i
            current_idx += next_position
            steps += 1

        return steps + 1