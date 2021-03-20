'''
Switch

Time Complexity O(n)
Space Complexity O(1)

'''


class Solution:
    def findRepeatNumber(self, nums: [int]) -> int:
        self.__check(nums=nums)
        current_index = 0
        while current_index < len(nums):
            if nums[current_index] == current_index:
                current_index += 1
                continue
            if nums[nums[current_index]] == nums[current_index]:
                return nums[current_index]
            nums[nums[current_index]], nums[current_index] = nums[current_index], nums[nums[current_index]]

        return -1

    def __check(self, nums):
        if not isinstance(nums, list):
            raise TypeError("Expect input type of {LIST}, "
                            "but found {OTHER}".format(LIST='list', OTHER=str(type(nums))))
        elif not nums:
            return -1


if __name__ == '__main__':

    test_case = [
        [],
        [2, 3, 1, 0, 2, 5, 3],
        [0, 1, 2, 3, 4, 11, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        [2, 3, 1, 2, 5, 3],
        (2, 3),
    ]

    solution = Solution()

    for tc in test_case:
        print(solution.findRepeatNumber(tc))