class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*n for _ in range(m)]
        dp[m-1][n-1] = 1

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 and j == n-1:
                    continue
                
                down = right = 0
                if i < m-1:
                    down = dp[i+1][j]
                if j < n-1:
                    right = dp[i][j+1]

                dp[i][j] = down + right
    
        return dp[0][0]