class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if matrix == [] or matrix == [[]]:
            return []

        results = []

        n_rows = len(matrix)
        n_cols = len(matrix[0])

        row = 0
        col = 0

        left_bound = 0
        right_bound = n_cols
        top_bound = 0
        bottom_bound = n_rows
        """
        1 2 3 4
        5 6 7 8
        9 10 11 12
        """

        while left_bound < right_bound and top_bound < bottom_bound:
            for col in range(left_bound, right_bound):
                results.append(matrix[row][col])

            for row in range(top_bound + 1, bottom_bound):
                results.append(matrix[row][col])

            if left_bound < right_bound - 1 and top_bound < bottom_bound - 1:
                for col in range(right_bound - 2, left_bound - 1, -1):
                    results.append(matrix[row][col])

                for row in range(bottom_bound - 2, top_bound, -1):
                    results.append(matrix[row][col])

            left_bound += 1
            right_bound -= 1
            top_bound += 1
            bottom_bound -= 1

        return results