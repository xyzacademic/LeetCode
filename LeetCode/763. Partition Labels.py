class Solution:
    def partitionLabels(self, S: str) -> List[int]:

        if not S:
            return []

        table = [0 for i in range(26)]

        for i, char in enumerate(S):
            table[ord(char) - ord('a')] = i

        start = 0
        end = 0
        results = []

        # tracking the last idx for each char
        for i, char in enumerate(S):
            end = max(end, table[ord(char) - ord('a')])
            if end == i:
                results.append(end + 1 - start)
                start = end + 1

        return results
