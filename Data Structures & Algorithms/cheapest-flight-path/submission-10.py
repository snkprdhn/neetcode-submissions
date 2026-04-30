class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, p in flights:
            adj[u].append((p, v))
        
        prices = [float("inf")] * n
        q = deque()
        q.append((src, 0))
        stops = 0
        while q and stops <= k:
            for _ in range(len(q)):
                node, cur_price = q.popleft()
                for price, nxt in adj[node]:
                    new_price = cur_price + price
                    if new_price < prices[nxt]:
                        prices[nxt] = new_price
                        q.append((nxt, new_price))
            stops += 1
            
        return prices[dst] if prices[dst] != float("inf") else -1
