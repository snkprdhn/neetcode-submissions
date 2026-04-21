class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount+1] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1+dp[i-coin])
        
        return -1 if dp[amount] == (amount+1) else dp[amount]

        
        # def dfs(amount):
        #     if amount in dp:
        #         return dp[amount]
            
        #     res = float("inf")
        #     for coin in coins:
        #         if amount - coin >= 0:
        #             res = min(res, 1 + dfs(amount - coin))
        #     dp[amount] = res
        #     return res
        
        # res = dfs(amount)
        # return -1 if res == float("inf") else res