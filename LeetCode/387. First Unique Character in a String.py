class Solution:
    def firstUniqChar(self, s: str) -> int:

        if not s or s == " ":
            return 0

        count_array = [0] * 26

        for char in s:
            count_array[ord(char) - ord('a')] += 1

        for idx, char in enumerate(s):
            if count_array[ord(char) - ord('a')] == 1:
                return idx

        return -1
