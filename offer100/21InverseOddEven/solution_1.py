"""
Dual pointer
Time Complexity: O(N)
Space Complexity: O(1)
"""


class Solution:
    def exchange(self, nums: list) -> list:
        odd_pointer = 0
        even_pointer = len(nums) - 1

        while odd_pointer < even_pointer:
            if nums[odd_pointer] % 2 == 0:
                if nums[even_pointer] % 2 != 0:
                    nums[odd_pointer], nums[even_pointer] = nums[even_pointer], nums[odd_pointer]
                even_pointer -= 1
            else:
                odd_pointer += 1

        return nums


if __name__ == '__main__':

    nums = [1, 4, 2, 5, 3, 4, 4]

    solution = Solution()

    print(solution.exchange(nums))
