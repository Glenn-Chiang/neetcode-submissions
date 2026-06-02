class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax = 1
        curMin = 1
        for num in nums:
            tmp = curMax * num
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(tmp, curMin * num, num)
            res = max(res, curMax)
        return res
