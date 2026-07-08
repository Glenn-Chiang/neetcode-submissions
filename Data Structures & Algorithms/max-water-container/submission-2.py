class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            amount = (right - left) * min(heights[left], heights[right])
            maxAmount = max(maxAmount, amount)
            if heights[left] <= heights[right]:
                left += 1
            elif heights[right] < heights[left]:
                right -= 1
        return maxAmount