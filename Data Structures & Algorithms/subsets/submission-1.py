class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i >= len(nums):
                return [[]]

            prev = dfs(i + 1)
            res = []
            for subset in prev:
                res.append(subset)
                res.append(subset + [nums[i]])
            return res
        
        return dfs(0)
            
