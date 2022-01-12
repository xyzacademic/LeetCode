class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # check
        if not nums or len(nums) < 3:
            return []

        nums.sort()
        n = len(nums)
        results = []

        for k in range(n):
            if nums[k] > 0:
                break

            if k > 0 and nums[k] == nums[k - 1]:
                continue

            i = k + 1
            j = n - 1

            while i < j:
                temp_sum = nums[k] + nums[i] + nums[j]

                if temp_sum == 0:
                    results.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

                elif temp_sum > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

                else:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1

        return results


if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    s = Solution()
    print(s.findThreeSum(nums) == [[-1,-1,2],[-1,0,1]])