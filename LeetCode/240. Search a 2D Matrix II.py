class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or matrix == [[]]:
            return False

        n_rows = len(matrix)
        # n_cols = len(matrix[0])

        row = 0
        col = len(matrix[0]) - 1

        while col >= 0 and row < n_rows:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1

        return False