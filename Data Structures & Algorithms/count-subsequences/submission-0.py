class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        len_t = len(t)
        dp = [[-1] * len_t for _ in range(n)]

        def dfs(i, j):
            if j == len_t:
                return 1
            if i == n:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            options = 0
            if s[i] == t[j]:
                #pick i
                options += dfs(i+1, j+1)

            #don't pick i
            options += dfs(i+1, j)
            dp[i][j] = options
            return options

        return dfs(0, 0)
