class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cost_list = [(0, 0)]
        visited = set()
        total_cost = 0
        while len(visited) < len(points):
            cost, i = heapq.heappop(cost_list)
            if i in visited:
                continue
            
            visited.add(i)
            total_cost+=cost
            x1, y1 = points[i]
            for j in range(len(points)):
                if j in visited:
                    continue

                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                heapq.heappush(cost_list, (cost, j))
        
        return total_cost

