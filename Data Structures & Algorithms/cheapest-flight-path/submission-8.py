class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        prices = [float("inf")] * n
        prices[src] = 0
        
        adj = defaultdict(list)
        for sr, ds, cost in flights:
            adj[sr].append((ds, cost))

        q = deque([(0, src, 0)])

        while q:
            total_cost, node, stops = q.popleft()
            
            if stops > k:
                continue

            for edge, e_cost in adj[node]:
                new_cost = total_cost + e_cost
                if prices[edge] > new_cost:
                    prices[edge] = new_cost
                    q.append((new_cost, edge, stops+1))
        
        return prices[dst] if prices[dst] != float("inf") else -1