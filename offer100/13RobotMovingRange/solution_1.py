"""
DFS
Time Complexity: O(MN)
Space Complexity: O(MN)
"""


class Solution:
    def movingCount(self, m: int, n: int, k: int) -> int:

        self.m = m
        self.n = n
        self.k = k
        self.visited = set()

        results = self.dfs(0, 0, 0, 0)
        return results

    def getSum(self, x):
        s = 0
        while x != 0:
            s += x % 10
            x = x // 10

        return s

    def dfs(self, row_index, col_index, s_row, s_col):

        results = 1

        if self.k < s_row + s_col or row_index >= self.m or \
                col_index >= self.n or (row_index, col_index) in self.visited:
            return 0

        self.visited.add((row_index, col_index))

        results += self.dfs(row_index + 1, col_index, s_row + 1 if (row_index + 1) % 10 else s_row - 8, s_col) + \
                    self.dfs(row_index, col_index + 1, s_row, s_col + 1 if (col_index + 1) % 10 else s_col - 8)

        return results







if __name__ == '__main__':
    m = 20
    n = 20
    k = 6

    solution = Solution()
    print(solution.movingCount(m, n, k))