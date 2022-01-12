class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if s == "":
            return 0

        table = {}

        # move pointer and check if s[idx] in table, and update position of char s[idx]
        # if failed, start from the next position of previous char s[idx]

        left = 0
        max_length = 0
        # abba
        # left 2
        # end 2
        # a:0 b:2
        # max_length: 2
        for end, char in enumerate(s):
            if char in table:
                left = max(table[char] + 1, left)  # ignore previous idx

            max_length = max(max_length, end - left + 1)
            table[char] = end

        return max_length



