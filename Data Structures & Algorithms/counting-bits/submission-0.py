class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n+1):
            ans = 0
            while i:
                i &= (i-1)
                ans+=1
            res.append(ans)
        
        return res