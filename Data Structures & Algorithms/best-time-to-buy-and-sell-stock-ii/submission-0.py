class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = float('inf')
        for price in prices:
            buy = min(price, buy)
            if buy < price:
                profit += price-buy
                buy = price
        return profit