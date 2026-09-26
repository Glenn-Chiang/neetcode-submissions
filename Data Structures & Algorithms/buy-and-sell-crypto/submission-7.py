class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        low = prices[0]
        for price in prices:
            max_profit = max(max_profit, price - low)
            low = min(low, price)
        return max_profit