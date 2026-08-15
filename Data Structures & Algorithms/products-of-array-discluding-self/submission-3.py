class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefixes = [0] * n
        prefix = 1
        for i in range(n):
            prefixes[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        res = [0] * n
        for i in range(n - 1, -1, -1):
            res[i] = prefixes[i] * suffix
            suffix *= nums[i]

        return res