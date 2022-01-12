class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        if not grid or grid == [[]]:
            return 0

        # f(i, j) = min(f(i-1, j), f(i, j-1)) + 3
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if i == j == 0:
                    continue
                elif i == 0:
                    grid[i][j] = grid[i][j - 1] + grid[i][j]
                elif j == 0:
                    grid[i][j] = grid[i - 1][j] + grid[i][j]
                else:
                    grid[i][j] = min(grid[i - 1][j], grid[i][j - 1]) + grid[i][j]

        return grid[m - 1][n - 1]