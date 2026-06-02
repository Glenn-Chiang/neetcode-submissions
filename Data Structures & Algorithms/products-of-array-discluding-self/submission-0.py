class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixes = [0] * len(nums)
        for i, num in enumerate(nums):
            if i == 0:
                prefixes[i] = nums[i]
            else:
                prefixes[i] = nums[i] * prefixes[i - 1]
        
        res = [0] * len(nums)
        acc = 1
        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                res[i] = acc
            else:
                res[i] = prefixes[i - 1] * acc
                acc *= nums[i]
        
        return res

