class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_product = nums[0]
        cur_min = 1
        cur_max = 1
        for num in nums:
            tmp = num * cur_max
            cur_max = max(num, num * cur_min, tmp)
            cur_min = min(num, num * cur_min, tmp)
            max_product = max(max_product, cur_max)
        return max_product