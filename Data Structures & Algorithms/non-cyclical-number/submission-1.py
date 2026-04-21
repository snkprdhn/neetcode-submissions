class Solution:
    def isHappy(self, n: int) -> bool:
        res = set()
        while True:
            sq = 0
            while n:
                sq += pow((n%10),2)
                n //= 10
            # print(sq)
            if sq==1:
                return True
            
            if sq in res:
                return False
            res.add(sq)
            n=sq
