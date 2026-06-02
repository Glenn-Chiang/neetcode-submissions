class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            amount = (j - i) * min(heights[i], heights[j])
            maxAmount = max(maxAmount, amount)
            if heights[i] <= heights[j]:
                i += 1
            elif heights[i] > heights[j]:
                j -=1
        return maxAmount