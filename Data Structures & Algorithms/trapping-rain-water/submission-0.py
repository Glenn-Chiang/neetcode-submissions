class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = [0] * len(height)
        max_right = [0] * len(height)

        max_height = 0
        for i in range(len(height)):
            max_left[i] = max_height
            max_height = max(max_height, height[i])
        
        max_height = 0
        for i in range(len(height) - 1, -1, -1):
            max_right[i] = max_height
            max_height = max(max_height, height[i])
        
        area = 0
        for i in range(len(height)):
            area += max(0, min(max_left[i], max_right[i]) - height[i])

        return area