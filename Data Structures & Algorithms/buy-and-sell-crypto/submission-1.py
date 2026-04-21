class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        max_profit = 0
        for sell_price in prices:
            profit = sell_price-buy_price
            max_profit = max(max_profit, profit)
            if sell_price <= buy_price:
                buy_price = sell_price
        return max_profit
