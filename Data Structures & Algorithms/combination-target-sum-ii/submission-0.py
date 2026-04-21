class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res,sol = set(), []
        n = len(candidates)
        candidates.sort()

        def backtrack(i, n_sum):
            if n_sum == target:
                res.add(tuple(sol))
                return
            if i == n or n_sum>target:
                return
            
            # don't pick
            backtrack(i+1, n_sum)
            
            sol.append(candidates[i])
            backtrack(i+1, n_sum+candidates[i])
            sol.pop()
        
        backtrack(0,0)
        return [list(ans) for ans in res]
