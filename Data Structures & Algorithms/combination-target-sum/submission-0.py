class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res, sol = [], []
        nums.sort()
        n = len(nums)
        def backtracking(i, n_sum):
            if n_sum == target:
                res.append(sol[:])
                return
            if i==n or n_sum > target:
                return
            
            # don't pick
            backtracking(i+1, n_sum)

            # pick
            sol.append(nums[i])
            backtracking(i, n_sum + nums[i])
            sol.pop()

        backtracking(0, 0)
        return res