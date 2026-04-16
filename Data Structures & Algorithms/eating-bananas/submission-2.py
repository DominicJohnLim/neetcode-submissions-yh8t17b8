import math

class Solution:

    def check(self, x, piles, h):
        if x <= 0: return False

        amt = 0
        for pile in piles:
            amt += math.ceil(pile / x)
        
        return amt <= h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 0
        hi = sum(piles) 

        while lo <= hi:
            mid = lo + (hi - lo) // 2

            if not self.check(mid, piles, h):
                lo = mid + 1
            else:
                hi = mid - 1
        
        # print(lo, hi)

        return lo