'''
Binary Search Tree
Time Complexity: O(M+N) M is the number of rows, N is the number of columns.
Space Complexity: O(1), space for index row, col
'''

class Solution:
    def findNumberIn2DArray(self, matrix: [int], target: int) -> bool:
        if not self.__check(matrix):
            return False

        row = 0
        col = len(matrix[0]) - 1
        while col >= 0 and row < len(matrix):
            if target > matrix[row][col]:
                row += 1
            elif target < matrix[row][col]:
                col -= 1
            else:
                return True

        return False


    def __check(self, matrix):
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return False
        else:
            return True


if __name__ == '__main__':

    test_case = [
        ([[1, 4, 7, 11, 15], [2, 5, 8, 12, 19], [3, 6, 9, 16, 22], [10, 13, 14, 17, 24], [18, 21, 23, 26, 30]], 5),
        ([], 3),
        ([[1, 1]], 2)
        ]


    solution = Solution()

    for tc in test_case:
        print(solution.findNumberIn2DArray(matrix=tc[0], target=tc[1]))