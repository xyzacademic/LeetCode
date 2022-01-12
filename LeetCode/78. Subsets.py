class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        if not nums or len(nums) == 0:
            return [[]]

        results = []
        n = len(nums)

        def process(nums, i, path):
            if i == n:
                results.append(path[:])
                return
            path.append(nums[i])
            process(nums, i + 1, path)
            path.pop()
            process(nums, i + 1, path)

        process(nums, 0, [])

        return results
