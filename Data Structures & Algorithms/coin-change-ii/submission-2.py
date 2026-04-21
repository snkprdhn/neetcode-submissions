class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        self.total_count = 0

        dp = {}

        def dfs(i ,amount):
            if amount == 0:
                return 1
            
            if (i, amount) in dp:
                return dp[(i, amount)]
            
            options = 0
            for j in range(i, n):
                coin = coins[j]
                if amount - coin >= 0:
                    options += dfs(j, amount - coin)
            
            dp[(i, amount)] = options
            return options

        return dfs(0, amount)
        #return self.total_count
            

            