class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for sr, ds, cost in flights:
            adj[sr].append((ds, cost))

        heap = [(0, src, 0)]

        while heap:
            total_cost, node, stops = heapq.heappop(heap)

            if node == dst:
                return total_cost
            
            if (stops == k + 1) or (node not in adj):
                continue

            for edge, e_cost in adj[node]:
                heapq.heappush(heap, (total_cost+e_cost, edge, stops+1))
        
        return -1