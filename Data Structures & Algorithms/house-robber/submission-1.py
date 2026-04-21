class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = {}
        
        def dfs(i, pick):
            if i >= n:
                return 0

            if (i, pick) in dp :
                return dp[(i, pick)]

            if pick:
                dp[(i, pick)] = nums[i] + dfs(i+1, False)
            else:
                dp[(i, pick)] = max(dfs(i+1, True), dfs(i+1, False))
            return dp[(i, pick)]
        
        return max(dfs(0, True), dfs(0, False))
        