class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        len_t = len(t)
        dp = [[0] * (len_t+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][len_t] = 1
        #print(dp)

        for i in range(n-1, -1, -1):
            for j in range(len_t-1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] += dp[i+1][j+1]
                dp[i][j] += dp[i+1][j]
        
        #print(dp)
        return dp[0][0]

        # def dfs(i, j):
        #     if j == len_t:
        #         return 1
        #     if i == n:
        #         return 0
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     options = 0
        #     if s[i] == t[j]:
        #         #pick i
        #         options += dfs(i+1, j+1)

        #     #don't pick i
        #     options += dfs(i+1, j)
        #     dp[i][j] = options
        #     return options

        # res = dfs(0, 0)
        # print(dp)
        # return res
