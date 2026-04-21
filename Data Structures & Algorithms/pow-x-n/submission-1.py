class Solution:
    def myPow(self, x: float, n: int) -> float:
        def find_pow(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x
             
            half = find_pow(x, n//2) * find_pow(x, n//2)
            
            if n%2:
                return x * half
            return half
        
        res =  find_pow(x, abs(n))
        if n < 0:
            res = 1 / res
        return res