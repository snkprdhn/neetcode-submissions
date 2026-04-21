class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge_map = {}
        visited = set()

        for i in range(n):
            edge_map[i] = set()
        
        for node, edge in edges:
            edge_map[node].add(edge)
            edge_map[edge].add(node)
            
        components = 0
        for i in range(n):
            if i not in visited:
                q = deque()
                q.append(i)
                components+=1
                while q:
                    node = q.popleft()
                    if node in visited:
                        continue
                    visited.add(node)
                    for edge in edge_map[node]:
                        q.append(edge)
                        
        return components