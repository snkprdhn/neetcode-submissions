class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        total_count = 0
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins[::-1]:
            temp = list(dp)
            for i in range(1, amount+1):
                if coin > i:
                    temp[i] += 0
                else:
                    remain = i - coin
                    temp[i] += temp[remain]
            # print(coin, temp)
            dp = temp

        return dp[-1] 


        # def dfs(i ,amount):
        #     if amount == 0:
        #         return 1
            
        #     if (i, amount) in dp:
        #         return dp[(i, amount)]
            
        #     options = 0
        #     for j in range(i, n):
        #         coin = coins[j]
        #         if amount - coin >= 0:
        #             options += dfs(j, amount - coin)
            
        #     dp[(i, amount)] = options
        #     return options
        
        # return dfs(0, amount)
        # print(dp)
            

            