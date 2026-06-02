class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1] * n
        acc = 1
        for i in range(1, n):
            acc *= nums[i - 1]
            prefix[i] = acc
        
        res = [1] * n
        acc = 1
        for i in range(n - 1, -1, -1):
            res[i] = prefix[i] * acc
            acc *= nums[i]
        return res

            


