class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [-1] * (len(cost) + 1)
        def min_cost(i):
            if i == 0 or i == 1:
                dp[i] = cost[i]
                return cost[i]
            if dp[i] != -1:
                return dp[i]
            res = min(min_cost(i - 1), min_cost(i - 2)) + (cost[i] if i < len(cost) else 0)
            dp[i] = res
            return res  
        return min_cost(len(cost))