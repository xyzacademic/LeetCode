"""

Time Complexity: O(log2N)
Space Complexity: O(1)
"""

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        result = 1
        if n < 0:
            x = 1 / x
            n = -n

        while n:
            if n & 1:
                result *= x
            x *= x
            n >>= 1

        return result