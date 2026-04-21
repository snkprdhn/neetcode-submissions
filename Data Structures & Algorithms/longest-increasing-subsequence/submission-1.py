class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1] * (n)
        dp[-1] = 1
        def dfs(i):
            if dp[i]!=-1:
                return dp[i]
            
            lis = 1
            for j in range(i+1, n):
                if nums[j] > nums[i]:
                    lis = max(lis, 1+dfs(j))
            dp[i] = lis
            return lis
        
        max_len = 0
        for i in range(n):
            max_len = max(max_len, dfs(i))
        return max_len