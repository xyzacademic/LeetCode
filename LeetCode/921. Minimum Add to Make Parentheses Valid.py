class Solution:
    def minAddToMakeValid(self, S: str) -> int:

        if S is '':
            return 0

        stack_a = []
        stack_b = []

        count = 0
        for char in S:
            if char == '(':
                stack_a.append(char)
            else:
                if len(stack_a) != 0:
                    stack_a.pop()
                else:
                    count += 1

        return count + len(stack_a)
