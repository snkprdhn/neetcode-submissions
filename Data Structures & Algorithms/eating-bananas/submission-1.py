class Solution:
    def get_h(self, piles, k):
        h = 0
        for b in piles:
            h+= -(-b//k)
        return h

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = max(piles)
        l,r = 1, min_k
        piles.sort()
        print(piles)
        while(l<=r):
            mid = l + ((r-l)//2)
            t = self.get_h(piles, mid)
            print(f"mid={mid}, t={t}")
            if t<=h:
                min_k = min(min_k, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return min_k