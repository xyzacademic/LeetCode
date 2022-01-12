class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        # check
        if not nums or len(nums) < 4:
            return []

        # sort
        nums.sort()

        n = len(nums)
        results = []
        # p1 p2 p3 p4

        # O(n)
        for p1 in range(n - 3):
            if p1 > 0 and nums[p1] == nums[p1 - 1]:
                continue
            if nums[p1] + nums[p1 + 1] + nums[p1 + 2] + nums[p1 + 3] > target:
                break
            if nums[p1] + nums[n - 3] + nums[n - 2] + nums[n - 1] < target:
                continue

            # O(n)
            for p2 in range(p1 + 1, n - 2):
                if p2 > p1 + 1 and nums[p2] == nums[p2 - 1]:
                    continue
                if nums[p1] + nums[p2] + nums[p1 + 1] + nums[p1 + 2] > target:
                    break
                if nums[p1] + nums[p2] + nums[n - 1] + nums[n - 2] < target:
                    continue
                p3 = p2 + 1
                p4 = n - 1
                # O(n)
                while p3 < p4:
                    rest = target - nums[p1] - nums[p2]
                    temp_sum = nums[p3] + nums[p4]
                    if temp_sum == rest:
                        results.append([nums[p1], nums[p2], nums[p3], nums[p4]])
                        p4 -= 1
                        while p3 < p4 and nums[p4] == nums[p4 + 1]:
                            p4 -= 1
                        p3 += 1
                        while p3 < p4 and nums[p3] == nums[p3 - 1]:
                            p3 += 1
                    elif temp_sum > rest:
                        p4 -= 1
                        while p3 < p4 and nums[p4] == nums[p4 + 1]:
                            p4 -= 1
                    elif temp_sum < rest:
                        p3 += 1
                        while p3 < p4 and nums[p3] == nums[p3 - 1]:
                            p3 += 1

        return results

