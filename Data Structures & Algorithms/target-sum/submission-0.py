class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}
        def dfs(i, amount):
            if i == n:
                if amount == 0:
                    return 1
                return 0
            
            if (i, amount) in dp:
                return dp[(i, amount)]
            
            dp[(i, amount)] = 0
            num = nums[i]
            dp[(i, amount)] += dfs(i+1, amount - num) + dfs(i+1, amount + num)

            return dp[(i, amount)]
        
        return dfs(0, target)

                