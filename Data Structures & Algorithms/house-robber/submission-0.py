class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)
        def max_amt(i):
            if i < 0 or i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]
            res = max(max_amt(i + 2) + nums[i], max_amt(i + 1))
            dp[i] = res
            return res
        return max_amt(0)