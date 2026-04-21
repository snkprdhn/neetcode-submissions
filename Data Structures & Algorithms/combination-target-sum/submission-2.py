class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        n = len(candidates)
        candidates.sort()
        def dfs(i, cur_sum, ans):
            if cur_sum == target:
                res.append(ans.copy())
                return 
            
            for j in range(i, n):
                if cur_sum + candidates[j] > target:
                    break
                
                ans.append(candidates[j])
                dfs(j, cur_sum + candidates[j], ans)
                ans.pop()

        
        dfs(0, 0, [])
        return res