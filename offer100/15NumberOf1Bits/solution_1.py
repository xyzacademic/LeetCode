"""
bit operation
Time Complexity: O(log2n)
Space Complexity: O(1)

"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res


