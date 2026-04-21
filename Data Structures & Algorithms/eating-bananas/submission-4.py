class Solution:
    def get_h(self, piles, k):
        h = 0
        for p in piles:
            h += -(-p//k)
        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = -(-sum(piles) // h)
        r = max(piles)

        while l<=r:
            mid = -(-(l+r) // 2)
            new_h = self.get_h(piles, mid)
            if new_h <= h:
                r = mid - 1
            else:
                l = mid + 1
        
        return l
                