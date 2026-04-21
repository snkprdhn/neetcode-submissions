class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def dfs(i, cur_sum, ans):
            if cur_sum == target:
                res.append(ans[:])
                return
            
            for j in range(i, len(candidates)):
                if cur_sum + candidates[j] > target:
                    break
                
                if j > i and candidates[j] == candidates[j-1]:
                    continue

                ans.append(candidates[j])
                dfs(j+1, cur_sum + candidates[j], ans)
                ans.pop()
        
        dfs(0,0,[])
        return res
