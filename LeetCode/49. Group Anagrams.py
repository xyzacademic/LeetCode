class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        if not strs:
            return strs

        # return hash key
        def get_key(strs):

            count_array = [0] * 26
            for char in strs:
                count_array[ord(char) - ord('a')] += 1

            return tuple(count_array)

        table = {}

        for sub_strs in strs:
            key = get_key(sub_strs)
            if key not in table:

                table[key] = [sub_strs]
            else:
                table[key].append(sub_strs)

        return table.values()