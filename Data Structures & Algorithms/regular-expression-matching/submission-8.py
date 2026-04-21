class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        dp = {}

        def dfs(i,j):
            if (i,j) in dp:
                return dp[(i,j)]

            if j == m: 
                return i == n

            match = i < n and (p[j] == s[i] or p[j] == ".")
            
            if j < m-1 and p[j+1] == "*":
                dp[(i,j)] = dfs(i, j + 2) or (match and dfs(i + 1, j))
            else:
                dp[(i,j)] = match and dfs(i+1, j+1)

            return dp[(i,j)]

        return dfs(0,0)

            

