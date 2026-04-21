class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        s3_len = len(s3)
        if n+m != s3_len:
            return False
        
        if m < n:
            n, m = m, n
            s1, s2 = s2, s1

        dp = [False] * (m+1)
        dp[-1] = True

        for i in range(n, -1, -1):
            new_dp = [False] * (m+1)
            if i == n:
                new_dp[-1] = True
            for j in range(m, -1, -1):
                if i<n and s1[i] == s3[i+j] and dp[j]:
                    new_dp[j] = True
                if j<m and s2[j] == s3[i+j] and new_dp[j+1]:
                    new_dp[j] = True
            dp = new_dp
        
        return dp[0]


        # dp = {}
        # def dfs(i, j):
        #     if i==n and j==m:
        #         return True
            
        #     if (i,j) in dp:
        #         return dp[(i,j)]
            
        #     k = i+j
        #     c1 = c2 = False
        #     if i < n and s1[i] == s3[k]:
        #         c1 = dfs(i+1, j)

        #     if j < m and s2[j] == s3[k]:
        #         c2 = dfs(i, j+1)
            
        #     dp[(i,j)] = c1 or c2
        #     return dp[(i,j)]
        
        # return dfs(0,0)
            
