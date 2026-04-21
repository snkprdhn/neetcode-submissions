class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n+2)]

        for i in range(n-1, -1, -1):
            # buying
            buy = dp[i+1][1] - prices[i]
            cooldown = dp[i+1][0]
            dp[i][0] = max(buy, cooldown)

            # selling
            sell = dp[i+2][0] + prices[i]
            cooldown = dp[i+1][1]
            dp[i][1] = max(sell, cooldown)

        return dp[0][0]
            