class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recur(arr):
            if len(arr) == 1:
                return [[arr[0]]]
            prev = recur(arr[1:])
            res = []
            for perm in prev:
                for i in range(len(perm) + 1):
                    new_perm = perm.copy()
                    new_perm.insert(i, arr[0])
                    res.append(new_perm)
            return res
        return recur(nums)