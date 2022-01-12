class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        if n == 0:
            return [[]]

        left_bound = 0
        right_bound = n
        top_bound = 0
        bottom_bound = n

        results = [[None for i in range(n)] for j in range(n)]
        n = 1

        def process(left_bound, right_bound, top_bound, bottom_bound, results, n):
            i = left_bound
            j = top_bound

            while i < right_bound:
                results[j][i] = n
                n += 1
                i += 1
            i -= 1
            j += 1

            while j < bottom_bound:
                results[j][i] = n
                n += 1
                j += 1
            j -= 1
            i -= 1

            while i > left_bound - 1:
                results[j][i] = n
                n += 1
                i -= 1
            i += 1
            j -= 1

            while j > top_bound:
                results[j][i] = n
                n += 1
                j -= 1

            return n

        while left_bound < right_bound and top_bound < bottom_bound:
            n = process(left_bound, right_bound, top_bound, bottom_bound, results, n)
            left_bound += 1
            right_bound -= 1
            top_bound += 1
            bottom_bound -= 1

        return results

