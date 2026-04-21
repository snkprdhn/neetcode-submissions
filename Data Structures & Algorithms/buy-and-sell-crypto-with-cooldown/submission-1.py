class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [[0]*2 for _ in range(n+2)]
        dp_1 = [0,0]
        dp_2 = [0,0]

        for i in range(n-1, -1, -1):
            cur = [0, 0]
            # buying
            buy = dp_1[1] - prices[i]
            cooldown = dp_1[0]
            cur[0] = max(buy, cooldown)

            # selling
            sell = dp_2[0] + prices[i]
            cooldown = dp_1[1]
            cur[1] = max(sell, cooldown)

            dp_1, dp_2 = cur, dp_1

        return dp_1[0]
            