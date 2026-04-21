class Solution:
    def myPow(self, x: float, n: int) -> float:
        dp = {0:1, 1:x}
        def find_pow(x, n):
            if n in dp:
                return dp[n]
            
            if n%2:
                dp[n] = x * find_pow(x, n//2) * find_pow(x, n//2)
            else:
                dp[n] = find_pow(x, n//2) * find_pow(x, n//2)

            return dp[n]
        
        res =  find_pow(x, abs(n))
        if n < 0:
            res = 1 / res
        return res