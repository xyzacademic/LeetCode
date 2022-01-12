class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if not grid or grid == [[]]:
            return -1

        queue = []

        n_rows, n_cols = len(grid), len(grid[0])

        # status
        current_time = 0

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 2:
                    queue.append((i, j, current_time))

        def add_queue(grid, i, j, current_time, queue):
            if 0 <= i < n_rows and 0 <= j < n_cols and grid[i][j] == 1:
                grid[i][j] = 2
                queue.append((i, j, current_time + 1))

            return

        while len(queue) != 0:
            i, j, current_time = queue.pop(0)
            # four direction
            add_queue(grid, i + 1, j, current_time, queue)
            add_queue(grid, i - 1, j, current_time, queue)
            add_queue(grid, i, j + 1, current_time, queue)
            add_queue(grid, i, j - 1, current_time, queue)

        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j] == 1:
                    return -1

        return current_time
