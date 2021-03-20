"""
Save temp results
Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def fib(self, n: int) -> int:
        fib = [0, 1]
        if n < 0:
            return None

        for i in range(2, n + 1):
            fib[i].append(fib[i - 1] + fib[i - 2]) % 1000000007

        return fib[n]
