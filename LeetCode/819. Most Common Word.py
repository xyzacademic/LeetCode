class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        if not paragraph:
            return ''

        banned_set = set(banned)

        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")

        table = {}

        for word in paragraph.split():
            if word.lower() not in table:

                table[word.lower()] = 1
            else:
                table[word.lower()] += 1

        results = None
        max_count = 0
        for key in table:
            if table[key] > max_count and key not in banned_set:
                results = key
                max_count = table[key]

        return results
