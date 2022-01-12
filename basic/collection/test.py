class UnionFind(object):
    def __init__(self, n):
        self.n = n
        self.part = n
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def union(self, x, y):
        root_x = self.parent[x]
        root_y = self.parent[y]

        if root_x == root_y:
            return

        if self.size[root_x] > self.size[y]:
            root_x, root_y = root_y, root_x

        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.part -= 1

        return

    def find(self, x):
        r = x
        while self.parent[x] != x:
            x = self.parent[x]

        while r != x:
            self.parent[r] = x
            r = self.parent[r]

        return self.parent[x]

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_part_size(self, x):
        return self.size[self.find(x)]