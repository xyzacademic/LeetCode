
class Solution(object):
    def get_min_cost(self, cities, maps, path):
        n = len(maps)
        # dp = [[0] * len(cities) for i in range(n+1)]
        #
        # for i in range(1, n+1):
        #     # costs_array = [self.convert_cost(path[i], city) for city in cities]
        #     for k, city in enumerate(cities):
        #         dp[i][k] = min([dp[i-1][j] for j in maps[k]]) + \
        #                    self.convert_cost(path[i-1], city)

        current_status = [0] * len(cities)
        for i in range(len(path)):
            next_status = [0] * len(cities)
            for k, city in enumerate(cities):
                next_status[k] = min([current_status[j] for j in maps[k]]) + \
                    self.convert_cost(path[i], city)
            current_status = next_status

        return min(current_status)


    def convert_cost(self, x, y):
        cost = 0
        for xc, yc in zip(x, y):
            cost += 1 if xc != yc else 0

        return cost



if __name__ == '__main__':

    cities = ['aaa', 'bbb', 'ccc']
    maps = [[1, 2], [0], [0]]
    s = Solution()
    path = ['bbb', 'abc', 'ccc']
    print(s.get_min_cost(cities, maps, path))

