class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        s3_len = len(s3)
        if n+m != s3_len:
            return False


        dp = {}
        def dfs(i, j, k):
            if i==n and j==m:
                return True
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            c1 = c2 = False
            if i < n and s1[i] == s3[k]:
                c1 = dfs(i+1, j, k+1)

            if j < m and s2[j] == s3[k]:
                c2 = dfs(i, j+1, k+1)
            
            dp[(i,j)] = c1 or c2
            return dp[(i,j)]
        
        return dfs(0,0,0)
            
