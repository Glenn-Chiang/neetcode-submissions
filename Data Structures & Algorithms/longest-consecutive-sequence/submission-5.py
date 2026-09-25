class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        max_len = 0
        for num in nums:
            if num - 1 in num_set:
                continue
            i = 1
            while num + i in num_set:
                i += 1
            max_len = max(max_len, i)
        return max_len