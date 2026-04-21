class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = {}
        def dfs(i, j):
            if j == m:
                return n-i
            if i == n:
                return m-j
            
            if (i,j) in dp:
                return dp[(i,j)]
            
            changes = float("inf")
            if word1[i] == word2[j]:
                # no change
                changes = min(changes, dfs(i+1, j+1))
            else:
                # insert
                changes = min(changes, 1 + dfs(i, j+1))
                
                # delete
                changes = min(changes, 1 + dfs(i+1, j))

                # replace
                changes = min(changes, 1 + dfs(i+1, j+1))
            
            dp[(i,j)] = changes
            return changes
        
        return dfs(0, 0)



