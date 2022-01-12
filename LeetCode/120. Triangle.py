class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        2
        3 4
        6 5 7
        4 1 8 3
        """
        if not triangle or triangle == []:
            return None

        n = len(triangle)
        #         cache = [inf] * n

        #         cache[0] = triangle[0][0]

        #         for row in range(1, n):
        #             for col in range(row, -1, -1):
        #                 if col == 0:
        #                     cache[col] = cache[col] + triangle[row][col]
        #                 else:
        #                     cache[col] = min(cache[col], cache[col-1]) + triangle[row][col]

        cache = triangle[-1]

        for row in range(n - 2, -1, -1):
            for col in range(row + 1):
                cache[col] = min(cache[col], cache[col + 1]) + triangle[row][col]

        return cache[0]
