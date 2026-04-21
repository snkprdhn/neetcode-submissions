class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)

        dp = {}

        def dfs(i,j):
            print(i,j)
            if i == n and j == m:
                return True
            if j == m:
                return False
            
            if i == n:
                if j < m-1 and p[j+1] == "*":
                    return dfs(i, j+2)
                return False
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            ans = False
            if j < m-1 and p[j+1] == "*":
                if p[j] == s[i] or p[j] == ".":
                    ans = dfs(i+1, j)  or dfs(i, j+2)
                else:
                    ans = dfs(i, j+2)
            elif s[i] == p[j]:
                ans = dfs(i+1, j+1)
            elif p[j] == ".":
                ans = dfs(i+1, j+1)

            dp[(i,j)] = ans
            return ans

        return dfs(0,0)

            

