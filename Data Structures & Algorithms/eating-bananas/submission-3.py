class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        min_rate = high

        while low <= high:
            mid = (low + high) // 2

            # Calculate time taken to finish eating bananas with eating rate of `mid`
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
            
            # If eating rate is viable, save it and try reducing it further
            if time <= h:
                high = mid - 1
                min_rate = mid
            else:
                low = mid + 1
        
        return min_rate