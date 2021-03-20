"""
DFS
Time Complexity: O(3^k)
Space Complexity: O(MN)
"""

class Solution:
    def exist(self, board, word) -> bool:
        self.board = board
        self.word = word
        if len(board) == 0 or len(board[0]) == 0:
            return False
        start_candidates = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    start_candidates.append((i, j))
        self.len_row = i + 1
        self.len_col = j + 1

        if start_candidates:
            for (row_index, col_index) in start_candidates:
                if self.dfs(row_index, col_index, 0):
                    return True

        return False

    def dfs(self, row_index, col_index, character_index):
        if not 0 <= row_index < self.len_row or not 0 <= col_index < self.len_col or \
                self.board[row_index][col_index] != self.word[character_index]:
            return False
        if character_index == len(self.word) - 1:
            return True

        tmp = self.board[row_index][col_index]
        self.board[row_index][col_index] = '/'
        result = self.dfs(row_index + 1, col_index, character_index + 1) or \
            self.dfs(row_index - 1, col_index, character_index + 1) or \
            self.dfs(row_index, col_index + 1, character_index + 1) or \
            self.dfs(row_index, col_index - 1, character_index + 1)

        self.board[row_index][col_index] = tmp
        del tmp

        return result


if __name__ == '__main__':

    matrix = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    target = "ABCCED"

    solution = Solution()
    solution.exist(matrix, target)