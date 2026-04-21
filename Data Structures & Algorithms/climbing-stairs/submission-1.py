class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [float("inf")] * n
        def dfs(i):
            if i > n:
                return 0
            if i==n:
                return 1

            if dp[i] != float("inf"):
                return dp[i]
            
            dp[i] = dfs(i+1) + dfs(i+2)
            return dp[i]
        
        return dfs(0)

