class Solution:
    def longestPalindrome(self, s: str) -> str:

        if not s or len(s) == 1:
            return s

        def process(s, start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                start -= 1
                end += 1

            return start + 1, end - 1

        start = 0
        end = 0

        for i in range(len(s)):
            start_a, end_a = process(s, i, i)
            start_b, end_b = process(s, i, i + 1)

            if end_a - start_a > end - start:
                end = end_a
                start = start_a

            if end_b - start_b > end - start:
                end = end_b
                start = start_b

        return s[start: end + 1]