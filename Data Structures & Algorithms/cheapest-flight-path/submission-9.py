class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        
        for i in range(k+1):
            temp_prices = prices.copy()
            for sr, ds, cost in flights:
                if prices[sr] == float("inf"):
                    continue
                
                new_price = prices[sr] + cost
                if new_price < temp_prices[ds]:
                    temp_prices[ds] = new_price
        
            prices = temp_prices
        
        return prices[dst] if prices[dst] != float("inf") else -1