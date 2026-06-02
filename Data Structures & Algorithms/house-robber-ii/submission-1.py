class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp1 = [-1] * len(nums)
        dp2 = [-1] * len(nums)

        def max_amt(i, dp, min_i, max_i):
            if i < min_i or i > max_i:
                return 0
            if dp[i] != -1:
                return dp[i]
            res = max(max_amt(i + 2, dp, min_i, max_i) + nums[i], 
                max_amt(i + 1, dp, min_i, max_i))
            dp[i] = res
            return res

        return max(max_amt(0, dp1, 0, len(nums) - 2), 
                    max_amt(1, dp2, 1, len(nums) - 1))