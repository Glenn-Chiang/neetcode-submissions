class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # If new interval ends before current interval starts, 
            # append new interval followed by remaining intervals
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res
            
            # If new interval starts after current interval ends,
            # append current interval (no overlap)
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            
            # If new interval overlaps with current interval,
            # merge new interval with current interval
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1])
                ]
        
        res.append(newInterval)
        return res