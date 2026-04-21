class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = cost.copy()
        dp.extend([0,0])

        for i in range(n-1, -1, -1):
            print(i)
            dp[i] = dp[i] + min(dp[i+1], dp[i+2])
            
        print(dp)
        return min(dp[0], dp[1])