class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        m = len(matrix[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        def dfs(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            steps = 1
            for r, c in dirs:
                new_r = i+r
                new_c = j+c
                if (0 <= new_r < n) and (0 <= new_c < m) and matrix[new_r][new_c] > matrix[i][j]:
                    steps = max(steps, 1+dfs(new_r, new_c))

            dp[i][j] = steps
            return steps
        
        max_len = 0
        for i in range(n):
            for j in range(m):
                max_len = max(max_len, dfs(i, j))
        
        return max_len
                
