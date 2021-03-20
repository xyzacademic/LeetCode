"""
Additional stack
Time Complexity: O(1)
Space Complexity: O(n)
"""

class MinStack:
    def __init__(self):
        self.A, self.B = [], []

    def push(self, x):
        self.A.append(x)
        if not self.B or self.B[-1] >= x:
            self.B.append(x)

    def pop(self):
        if self.A.pop() == self.B[-1]:
            self.B.pop()

    def top(self):
        return self.A[-1]

    def min(self):
        return self.B[-1]
