import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(p):
            return math.sqrt(p[0]**2 + p[1]**2)
        
        heap = []
        for p in points:
            heapq.heappush(heap, (dist(p), p))
        
        closest = []
        for i in range(k):
            closest.append(heapq.heappop(heap)[1])
        return closest