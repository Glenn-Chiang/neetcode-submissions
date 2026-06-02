class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def recur(arr):
            if len(arr) == 1:
                return [[], [arr[0]]]
            prev = recur(arr[1:])
            res = []
            for subset in prev:
                res.append(subset)
                res.append(subset + [arr[0]])
            return res
        return recur(nums)