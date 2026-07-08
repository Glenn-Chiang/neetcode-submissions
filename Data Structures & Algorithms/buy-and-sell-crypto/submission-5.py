class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowestPrice = prices[0]
        profitMax = 0
        for price in prices:
            profit = price - lowestPrice
            profitMax = max(profitMax, profit)
            lowestPrice = min(lowestPrice, price)
        return profitMax