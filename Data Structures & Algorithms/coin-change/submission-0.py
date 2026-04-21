class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n = len(coins)
        dp = {0:0}
        def dfs(amount):
            if amount in dp:
                return dp[amount]
            
            res = float("inf")
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            dp[amount] = res
            return res
        
        min_coins = dfs(amount)
        return -1 if min_coins == float("inf") else min_coins
            
            