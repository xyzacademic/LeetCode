


class Solution:
    def __init__(self, change, coins):
        self.change = change
        self.coins = coins
        self.look_up_table = [0] * (change + 1)

    def returnMinimum(self, change):
        minimum_coins = change
        if change in self.coins:
            return 1

        elif self.look_up_table[change] > 0:
            return self.look_up_table[change]

        else:
            for cents in [c for c in self.coins if c < change]:
                current_counts = 1 + self.returnMinimum(change - cents)
                if current_counts < minimum_coins:
                    minimum_coins = current_counts
                    self.look_up_table[change] = minimum_coins
            return minimum_coins






if __name__ == '__main__':

    coins = [1, 5, 20, 21, 25]
    change = 63
    solution = Solution(change, coins)
    print(solution.returnMinimum(change))