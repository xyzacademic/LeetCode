"""
Time Complexity: O(MN)
Space Complexity: O(1)
"""

class Solution:
    def spiralOrder(self, matrix:[[int]]) -> [int]:
        if not matrix or not matrix[0]:
            return []

        left_edge = 0
        right_edge = len(matrix[0]) - 1
        top_edge = 0
        bottom_edge = len(matrix) - 1
        result = []

        while True:
            for j in range(left_edge, right_edge + 1):
                result.append(matrix[top_edge][j])
            top_edge += 1
            if left_edge > right_edge:
                break
            for j in range(top_edge, bottom_edge + 1):
                result.append(matrix[j][right_edge])
            right_edge -= 1
            if top_edge > bottom_edge:
                break

            for j in range(right_edge, left_edge - 1, -1):
                result.append(matrix[bottom_edge][j])
            bottom_edge -= 1
            if left_edge > right_edge:
                break

            for j in range(bottom_edge, top_edge - 1, -1):
                result.append(matrix[j][left_edge])
            left_edge += 1
            if top_edge > bottom_edge:
                break

        return result


if __name__ == '__main__':

    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    solution = Solution()
    print(solution.spiralOrder(matrix))



