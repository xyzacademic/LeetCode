class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        cache = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],

        }

        results = []

        path = []

        def process(idx, digits, path):
            if idx == len(digits):
                results.append("".join(path))
                return

            for char in cache[digits[idx]]:
                path.append(char)
                process(idx + 1, digits, path)
                path.pop()

        process(0, digits, path)
        return results
