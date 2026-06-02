class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            b = nums[i]
            a = target - b
            if a in seen:
                return [seen[a], i]
            seen[b] = i
        

