class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if not prices or len(prices) < 2:
            return 0

        # cache = [0] * len(prices)

        min_price = prices[0]
        max_profit = 0
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i] - min_price)
            min_price = min(min_price, prices[i])

        return max_profit
