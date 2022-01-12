class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or board == [[]]:
            return board

        n_rows = len(board)
        n_cols = len(board[0])

        neighbors = []
        for op in [-1, 0, 1]:
            for op2 in [-1, 0, 1]:
                if [op, op2] != [0, 0]:
                    neighbors.append((op, op2))

        for row in range(n_rows):
            for col in range(n_cols):
                nb_count = 0
                for op in neighbors:
                    new_row = row + op[0]
                    new_col = col + op[1]

                    if new_row >= 0 and new_row < n_rows and new_col >= 0 and \
                            new_col < n_cols and abs(board[new_row][new_col]) == 1:
                        nb_count += 1

                if board[row][col] == 0 and nb_count == 3:
                    board[row][col] = 2

                if board[row][col] == 1 and (nb_count < 2 or nb_count > 3):
                    board[row][col] = -1

        for row in range(n_rows):
            for col in range(n_cols):
                board[row][col] = 1 if board[row][col] > 0 else 0

        return board
