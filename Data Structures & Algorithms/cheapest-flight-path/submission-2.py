class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = {}
        for sr, ds, cost in flights:
            if sr not in adj:
                adj[sr] = []
            adj[sr].append((ds, cost))

        print(adj)
        heap = [(0, src, 0, 0)]
        visited = set()
        final_cost = float("inf")
        while heap:
            cost, node, stops, total_cost = heapq.heappop(heap)
            print(cost, node, stops, total_cost)
            
            if stops > k + 1:
                continue
            total_cost += cost
            if node == dst:
                final_cost = min(final_cost, total_cost)

            if node not in adj:
                continue
            for edge, e_cost in adj[node]:
                heapq.heappush(heap, (e_cost, edge, stops+1, total_cost))
        
        if final_cost != float("inf"): return final_cost
        return -1