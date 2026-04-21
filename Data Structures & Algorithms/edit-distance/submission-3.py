class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)
        dp = [[0] * (m+1) for _ in range(n+1)]
        for i in range(n+1):
            dp[i][m] = n - i

        for j in range(m+1):
            dp[n][j] = m - j
        
        for i in range(n-1, -1, -1):
            for j in range(m-1, -1, -1):
                if word1[i] == word2[j]:
                    ans = dp[i+1][j+1]
                else:
                    insert = 1 + dp[i][j+1]
                    delete = 1 + dp[i+1][j]
                    replace = 1 + dp[i+1][j+1]
                    ans = min(insert, delete, replace)
                dp[i][j] = ans
        
        return dp[0][0]

        # dp = [[-1] * m for _ in range(n)]
        # def dfs(i, j):
        #     if j == m:
        #         return n-i
        #     if i == n:
        #         return m-j
            
        #     if dp[i][j] != -1:
        #         return dp[i][j]
            
        #     changes = float("inf")
        #     if word1[i] == word2[j]:
        #         # no change
        #         changes = min(changes, dfs(i+1, j+1))
        #     else:
        #         # insert
        #         changes = min(changes, 1 + dfs(i, j+1))

        #         # delete
        #         changes = min(changes, 1 + dfs(i+1, j))

        #         # replace
        #         changes = min(changes, 1 + dfs(i+1, j+1))
            
        #     dp[i][j] = changes
        #     return changes
        
        # ans = dfs(0, 0)
        # print(dp)
        # return ans



