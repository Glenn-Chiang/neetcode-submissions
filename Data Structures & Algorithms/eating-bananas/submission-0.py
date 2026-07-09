class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        minSpeed = high
        while low <= high:
            mid = (low + high) // 2
            totalHours =  self.computeTotalHours(piles, mid)
            if totalHours <= h:
                minSpeed = mid
                high = mid - 1
            elif totalHours > h:
                low = mid + 1
        return minSpeed

    def computeTotalHours(self, piles, k):
        totalHours = 0
        for pile in piles:
            totalHours += math.ceil(pile / k)
        return totalHours
    
