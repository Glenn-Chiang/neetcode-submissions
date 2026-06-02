class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        max_profit = 0
        low = prices[0] # Keep track of lowest buy price
        for i in range(1, n):
            profit = prices[i] - low
            max_profit = max(max_profit, profit)
            if prices[i] < low:
                low = prices[i]
        return max_profit