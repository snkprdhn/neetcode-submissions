class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        len_t = len(t)
        dp = [0] * (len_t+1)
        dp[-1] = 1

        for i in range(n-1, -1, -1):
            new_dp = [0] * (len_t+1)
            new_dp[-1] = 1
            for j in range(len_t-1, -1, -1):
                if s[i] == t[j]:
                    new_dp[j] += dp[j+1]
                new_dp[j] += dp[j]
            dp = new_dp
        
        #print(dp)
        return dp[0]

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
