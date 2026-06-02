class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        lowestPrice = prices[0]
        for price in prices:
            profit = price - lowestPrice
            maxProfit = max(profit, maxProfit)
            lowestPrice = min(price, lowestPrice)
        return maxProfit