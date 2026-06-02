class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        maxLen = 0

        for num in nums:
            if num - 1 in numSet:
                continue
            # Start of sequence
            next = num + 1
            while next in numSet:
                next += 1
            length = next - num
            if length > maxLen:
                maxLen = length

        return maxLen