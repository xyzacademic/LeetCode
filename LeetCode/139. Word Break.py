class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return True

        length = len(s)
        cache = [False] * (length + 1)

        # cache[i] represent if s[:i] can be spilted
        # cache[0] is empty ""

        cache[0] = True

        for i in range(length):
            for j in range(i + 1, length + 1):
                if cache[i] and (s[i:j] in wordDict):
                    cache[j] = True

        return cache[-1]
