class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol = [], []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, n_sum):
            if n_sum == target:
                res.append(sol[:])
                return
            if i == n or n_sum>target:
                return

            sol.append(candidates[i])
            backtrack(i+1, n_sum+candidates[i])
            sol.pop()
            
            # don't pick
            while i+1 < n and candidates[i] == candidates[i+1]:
                i+=1
            backtrack(i+1, n_sum)
            

        
        backtrack(0,0)
        return res
