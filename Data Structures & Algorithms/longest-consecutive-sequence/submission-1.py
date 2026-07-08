class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Add all elements to set
        numSet = set(nums)
        
        maxLength = 0

        for num in nums:
            # Consider only elements that are the start of a sequence
            if num - 1 not in numSet:
                # Extend sequence starting from num
                n = 1 # Current length - 1
                while num + n in numSet:
                    n += 1
                maxLength = max(maxLength, n)

        return maxLength