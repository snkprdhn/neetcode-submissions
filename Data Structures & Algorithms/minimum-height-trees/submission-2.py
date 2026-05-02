class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]
        
        adj = defaultdict(list)
        for u, v in edges:
            adj[v].append(u)
            adj[u].append(v)
        
        q = deque()
        neigh_map = defaultdict(int)
        for u, neighbours in adj.items():
            neigh_map[u] = len(neighbours)
            if len(neighbours) == 1:
                q.append(u)
        
        while q:
            if n <= 2:
                return list(q)
            
            for _ in range(len(q)):
                u = q.popleft()
                n -= 1
                for nxt in adj[u]:
                    neigh_map[nxt] -= 1
                    if neigh_map[nxt] == 1:
                        q.append(nxt)
                