class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res, sol = [], []

        def backtracking(i):
            if i==len(nums):
                res.append(sol[:])
                return
            
            # don't pick
            backtracking(i+1)

            # pick
            sol.append(nums[i])
            backtracking(i+1)
            sol.pop()
        
        backtracking(0)
        return res