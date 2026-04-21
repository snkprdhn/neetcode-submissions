class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        node = 0
        cost_list = [float("inf")] * n
        cost_list[0] = 0
        visited = set()
        total_cost = 0
        while len(visited) < n:
            visited.add(node)
            node_cost = cost_list[node]
            total_cost+=node_cost
            x1, y1 = points[node]
            min_cost, min_node = float("inf"), node
            for j in range(len(points)):
                if j in visited:
                    continue

                x2, y2 = points[j]
                cost = abs(x1-x2) + abs(y1-y2)
                cost_list[j] = min(cost_list[j] , cost)
                if cost_list[j] < min_cost:
                    min_cost = cost_list[j]
                    min_node = j
            
            node = min_node
        
        return total_cost

