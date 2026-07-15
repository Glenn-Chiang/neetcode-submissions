class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        left_bounds = [-1] * len(heights)
        right_bounds = [len(heights)] * len(heights)

        # Find left bound for each bar
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                left_bounds[i] = stack[-1]
            stack.append(i)
        
        stack = [] # Reset stack
        # Find right bound for each bar
        for i in range(len(heights) - 1, -1, -1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                right_bounds[i] = stack[-1]
            stack.append(i)
        
        max_area = 0
        for i in range(len(heights)):
            left = left_bounds[i] + 1
            right = right_bounds[i] - 1
            area = heights[i] * (right - left + 1)
            max_area = max(max_area, area)
        
        return max_area




