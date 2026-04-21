class Solution:
    def numDecodings(self, s: str) -> int:
        # split into sub numbers less than 27 without any leading 0s
        n = len(s)
        dp = {
            n:1
        }
        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0
            
            res = dfs(i+1)
            if i+1 < n and (s[i]=="1" or (s[i]=="2" and s[i+1] in "0123456")):
                res += dfs(i+2)

            dp[i] = res
            return res
        
        return dfs(0)