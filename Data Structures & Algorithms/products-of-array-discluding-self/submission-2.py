class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create prefix product array
        prefix = 1
        prefixes = []
        for num in nums:
            prefixes.append(prefix)
            prefix *= num
        
        output = [1] * len(nums) # Initialize output array
        suffix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = prefixes[i] * suffix
            suffix *= nums[i]

        return output

            


