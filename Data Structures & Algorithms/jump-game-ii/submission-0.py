class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [(False, 0)] * n
        dp[-1] = (True, 0)

        for i in range(n-2, -1, -1):
            jump_limit = min(i + nums[i] + 1, n)
            dp[i] = (False, 0)
            min_jumps = float("inf")
            for j in range(i+1, jump_limit):
                can_jump, jumps = dp[j]
                if can_jump:
                    min_jumps = min(min_jumps, jumps)
            
            if min_jumps != float("inf"):
                dp[i] = (True, min_jumps+1)
        #print(dp)
        can_jump, min_jumps = dp[0]
        return min_jumps