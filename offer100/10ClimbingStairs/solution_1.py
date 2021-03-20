"""
Change it to fibonacci problem
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution:
    def numWays(self, n: int) -> int:
        a = 1
        b = 1
        if n == 0:
            return 1
        elif n == 1:
            return 1
        else:
            for i in range(2, n + 1):
                a, b = b, a + b

            return a % 1000000007