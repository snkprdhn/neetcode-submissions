class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(conditions):
            conditions = set(tuple(c) for c in conditions)
            adj = defaultdict(set)
            indegree = {i:0 for i in range(1, k+1)}

            for u, v in conditions:
                adj[u].add(v)
                indegree[v] += 1

            q = deque()
            for i, count in indegree.items():
                if not count:
                    q.append(i)

            order = []
            while q:
                u = q.popleft()
                order.append(u)

                for v in adj[u]:
                    indegree[v] -= 1
                    if not indegree[v]:
                        q.append(v)
            
            return order if len(order) == k else []

        row_order = topo_sort(rowConditions)
        col_order = topo_sort(colConditions)

        if not row_order or not col_order:
            return []

        idx_map = defaultdict(list)
        for i, val in enumerate(row_order):
            idx_map[val].append(i)

        for j, val in enumerate(col_order):
            idx_map[val].append(j)

        res = [[0]*k for _ in range(k)]
        for val, idx in idx_map.items():
            res[idx[0]][idx[1]] = val
        
        return res

            
            