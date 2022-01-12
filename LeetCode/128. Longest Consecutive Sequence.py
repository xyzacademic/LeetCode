class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums or len(nums) == 0:
            return 0

        table = {}
        for num in set(nums):
            table[num] = True

        max_score = 0
        min_ = min(nums)
        max_ = max(nums)

        start = min_
        i = 0
        n = len(nums)
        # 0 2 3 4 7
        temp_score = 0
        while start <= max_ and n - i > max_score:

            if start in table:
                temp_score += 1  # 4
            else:
                i += temp_score  # 4
                temp_score = 0
            max_score = max(temp_score, max_score)  # 4
            start += 1  # 6

        return max_score
