class Solution:
    def trap(self, height: List[int]) -> int:
        i, j = 0, len(height) - 1
        max_left, max_right = height[i], height[j] 

        area = 0
        while i < j:
            if max_left < max_right:
                i += 1
                area += max(0, max_left - height[i])
                max_left = max(max_left, height[i])
            else:
                j -= 1
                area += max(0, max_right - height[j])
                max_right = max(max_right, height[j])
        
        return area