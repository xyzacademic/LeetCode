class Solution:
    def isValid(self, s: str) -> bool:

        if not s:
            return False

        stack = []
        table = {
            '{': '}',
            '(': ')',
            '[': ']',
        }
        for char in s:
            if char in table:
                stack.append(char)
            else:
                if not len(stack) or table[stack.pop()] != char:
                    return False
        return len(stack) == 0