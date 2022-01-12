

class Solution:
    def twoSum(self, nums, target):

        if not nums or len(nums) == 0:
            return []
        look_up = {}

        # O(n)
        for idx, num in enumerate(nums):
            rest = target - num  # O(1)
            if rest in look_up:
                return [look_up[rest], idx]

            look_up[num] = idx

        return []


if __name__ == '__main__':
    a = [2, 4, 8, 10]

    s = Solution()
    print(s.twoSum(a, 10))

