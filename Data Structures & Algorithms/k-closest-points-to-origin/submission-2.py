import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for point in points:
            dist = math.sqrt(point[0] ** 2 + point[1] ** 2)
            # Add (distance, point) to heap, using distance as priority value
            heapq.heappush(heap, (dist, point))
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res