class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start
        intervals.sort(key=lambda x: x[0])

        res = [intervals[0]]
        for interval in intervals:
            # If current interval overlaps with previous interval, 
            # merge current interval into previous interval
            if interval[0] <= res[-1][1]:
                res[-1][1] = max(res[-1][1], interval[1])
            
            # If current interval does not overlap with previous interval,
            # start a new interval
            else:
                res.append([interval[0], interval[1]])
        
        return res