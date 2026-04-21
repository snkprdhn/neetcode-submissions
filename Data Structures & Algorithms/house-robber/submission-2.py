class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * n

        def dfs(i):
            if i >= n:
                return 0

            if dp[i] != -1:
                return dp[i]

            dp[i] = max(
                nums[i] + dfs(i+2),   # rob
                dfs(i+1)             # skip
            )

            return dp[i]
        
        return dfs(0)