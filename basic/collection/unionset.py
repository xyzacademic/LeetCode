class Disjointset(object):
    def __init__(self, n):
        self.n = n
        self.part = n
        self.parent = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, x):
        # if self.parent[x] == x:
        #     return x
        # self.parent[x] = self.find(self.parent[x])
        r = x
        while self.parent[x] != x:
            x = self.parent[x]
        while r != x:
            # k = self.parent[r]
            # self.parent[r] = x
            # r = k
            self.parent[r], r = x, self.parent[r]

        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.size[x] > self.size[y]:
            root_x, root_y = root_y, root_x
        self.parent[root_x] = root_y
        self.size[root_y] += self.size[root_x]
        self.part -= 1
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_part_size(self, x):
        return self.size[self.find(x)]


if __name__ == '__main__':
    union = Disjointset(5)


class DisjointSet(object):
    def __init__(self, n):
        self.n = n
        self.part = n
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        r = x
        while self.parent[x] != x:
            x = self.parent[x]

        while r != x:
            self.parent[r], r = x, self.parent[r]

        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        if self.size[root_x] > self.size[root_y]:
            root_x, root_y = root_y, root_x

        self.size[root_y] += self.size[root_x]
        self.parent[root_x] = root_y
        self.part -= 1

        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

    def get_part_size(self, x):
        return self.size[self.find(x)]