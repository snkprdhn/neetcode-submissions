class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        cost_list = [float("inf")] * n
        total_cost = 0
        visited = set()
        node = 0
        cost_list[0] = 0

        while len(visited) < n:
            visited.add(node)
            total_cost += cost_list[node]
            
            x1, y1 = points[node]
            min_cost = float("inf")
            next_point = -1
            for i in range(n):
                if i == node:
                    continue
                if i in visited:
                    continue
                x2, y2 = points[i]
                cost = abs(x1-x2) + abs(y1-y2)
                cost_list[i] = min(cost_list[i], cost)
                if cost_list[i] < min_cost:
                    min_cost = cost_list[i]
                    next_point = i
            node = next_point

        return total_cost
