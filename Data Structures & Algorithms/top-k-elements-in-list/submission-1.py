class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of element, map each element to its frequency
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        # Initialize frequency array
        # freq[i] = list of elements with frequency i
        freq = [0] * (len(nums) + 1)
        for i in range(len(freq)):
            freq[i] = []

        # Add each element to its frequency bucket
        for num in count:
            freq[count[num]].append(num)

        res = []
        # Add elements with highest frequency to res, starting from most frequent bucket
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                # If we have reached k most frequent elements, return result
                if len(res) == k:
                    return res
