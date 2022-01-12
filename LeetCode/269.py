class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) <= 1:
            return "".join(set(list(words[0])))

        in_degree = {}
        edges = {}
        points = set()

        for word in words:
            for c in word:
                points.add(c)

        # build graph
        for i in range(len(words)):
            word_i = words[i]
            for j in range(i+1, len(words)):
                word_j = words[j]

                for k in range(min(len(word_i), len(word_j))):
                    if word_i[k] != word_j[k]:
                        if word_i[k] not in edges:
                            edges[word_i[k]] = set()
                        edges[word_i[k]].add(word_j[k])
                        break

        # count in degree

        for v1, vs2 in edges.items():
            if v1 not in in_degree:
                in_degree[v1] = 0
            for v2 in vs2:
                if v2 not in in_degree:
                    in_degree[v2] = 0
                in_degree[v2] += 1

        results = []

        queue = []

        for char in points:
            if char not in in_degree:
                in_degree[char] = 0
            if in_degree[char] == 0:
                queue.append(char)

        while queue:
            char = queue.pop(0)
            results.append(char)
            if char in edges:
                for target in edges[char]:
                    in_degree[target] -= 1
                    if in_degree[target] == 0:
                        queue.append(target)

        if len(results) != len(points):
            return ""

        has_reverse = False
        for i in range(len(words)):
            if has_reverse:
                break

            word_i = words[i]
            for j in range(i+1, len(words)):
                word_j = words[j]
                l_i = len(word_i)
                l_j = len(word_j)
                if l_i > l_j and word_i[:l_j] == word_j:
                    has_reverse = True
                    break

        if has_reverse:
            return ""

        return "".join(results)