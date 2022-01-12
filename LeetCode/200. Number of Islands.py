class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # check
        if not grid or grid == [[]]:
            return 0

        # BFS
        m = len(grid)
        n = len(grid[0])

        count = 0
        queue = []

        # init point
        def process(queue):

            while len(queue) != 0:
                (i, j) = queue.pop(0)
                # check
                if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0':
                    continue
                grid[i][j] = '0'
                queue.append((i - 1, j))
                queue.append((i + 1, j))
                queue.append((i, j - 1))
                queue.append((i, j + 1))

        # main
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    queue.append((i, j))
                    process(queue)
                    count += 1

        return count