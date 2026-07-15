class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start
        intervals.sort(key=lambda x: x[0])

        res = []
        prev_interval = intervals[0]
        for interval in intervals:
            # If current interval overlaps with previous interval, 
            # merge current interval into previous interval
            if interval[0] <= prev_interval[1]:
                prev_interval[1] = max(prev_interval[1], interval[1])
            
            # If current interval does not overlap with previous interval,
            # add the previous interval to result and start a new interval
            else:
                res.append([prev_interval[0], prev_interval[1]])
                prev_interval = [interval[0], interval[1]]
        
        res.append(prev_interval)
        return res