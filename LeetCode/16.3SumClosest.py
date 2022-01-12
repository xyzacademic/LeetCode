class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # check
        if not nums or len(nums) < 3:
            return None

        nums.sort()
        n_length = len(nums)
        best_rest = inf

        for k in range(n_length):
            if k > 0 and nums[k] == nums[k - 1]:
                continue
            i = k + 1
            j = n_length - 1
            rest = target - nums[k]

            while i < j:
                temp_sum = nums[i] + nums[j]
                if temp_sum == rest:
                    return target
                if abs(rest - temp_sum) < best_rest:
                    best_rest = abs(rest - temp_sum)
                    best_sum = temp_sum + nums[k]
                if temp_sum < rest:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                else:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

        return best_sum