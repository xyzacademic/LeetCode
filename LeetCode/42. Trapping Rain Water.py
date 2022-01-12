class Solution:
    def trap(self, height: List[int]) -> int:
        """
        left_max = l(i)
        right_max = g(i)
        trap(i) = min(l(i), g(i)) - height(i)
        trap_sum = sum(trap)

        """
        # height = 4 2 0 3 2 5

        #         left_max = [] # 4 4 4 4 4 5
        #         right_max = [] # 5 5 5 5 5 5
        #         trapping = 0 # 0 2 4 1 2 0
        #         left_max_ = 0
        #         right_max_ = 0

        #         for num in height:
        #             left_max_ = max(left_max_, num)
        #             left_max.append(left_max_)

        #         for num in height[::-1]:
        #             right_max_ = max(right_max_, num)
        #             right_max.insert(0, right_max_)

        #         for i in range(len(height)):
        #             trapping += min(left_max[i], right_max[i]) - height[i]

        if not height or len(height) == 0:
            return 0
        i = 0
        j = len(height) - 1
        trapping_sum = 0
        left_max = height[0]
        right_max = height[j]

        while i < j:

            if height[i] <= height[j]:
                # left max will less than right max
                left_max = max(left_max, height[i])
                trapping_sum += left_max - height[i]
                i += 1
            else:
                # right max is higher than left max
                right_max = max(right_max, height[j])
                trapping_sum += right_max - height[j]
                j -= 1

        return trapping_sum