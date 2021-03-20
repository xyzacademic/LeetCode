from pythonds.graphs import Graph

def buildGraph(wordFile):
    d = {}
    g = Graph()
    with open(wordFile, 'r') as wfile:
        for line in wfile:
            word = line.strip()

            for i in range(len(word)):
                bucket = word[:i] + '_' + word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]

    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)

    return g