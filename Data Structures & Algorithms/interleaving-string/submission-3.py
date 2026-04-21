class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        s3_len = len(s3)
        dp = {}
        def dfs(i,j,k,s):
            if k == s3_len:
                if "".join(s) == s3 and i==n and j==m:
                    return True
                return False
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            c1 = c2 = False
            if i < n and s1[i] == s3[k]:
                s.append(s1[i])
                c1 = dfs(i+1, j, k+1, s)
                s.pop()

            if j < m and s2[j] == s3[k]:
                s.append(s2[j])
                c2 = dfs(i, j+1, k+1, s)
            
            dp[(i,j)] = c1 or c2
            return dp[(i,j)]
        
        return dfs(0,0,0,[])
            
