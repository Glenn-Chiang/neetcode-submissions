class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        for num in freq:
            buckets[freq[num]].append(num)
        
        res = []
        for i in range(n, -1, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) >= k:
                    return res
        
           

