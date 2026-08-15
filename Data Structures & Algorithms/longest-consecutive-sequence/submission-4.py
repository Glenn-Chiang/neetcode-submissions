class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in nums:
            if (num - 1) in num_set:
                continue
            i = 0
            while (num + i) in num_set:
                max_len = max(max_len, i + 1)
                i += 1
            
        return max_len