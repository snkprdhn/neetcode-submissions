class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res, sol = [], []
        n = len(s)

        def is_palin(i,j):
            while i < j:
                if s[i]!=s[j]:
                    return False
                i+=1
                j-=1
            return True

        def backtrack(i):
            if i == n:
                res.append(sol[:])
                return
                
            for j in range(i, n):
                if is_palin(i,j):
                    sol.append(s[i:j+1])
                    backtrack(j+1)
                    sol.pop()
                    
        
        backtrack(0)
        return res
