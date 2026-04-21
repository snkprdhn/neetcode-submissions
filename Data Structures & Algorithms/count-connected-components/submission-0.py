class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        edge_map = {}
        visited = set()
        for i in range(n):
            edge_map[i] = set()
        
        for node, edge in edges:
            edge_map[node].add(edge)
            edge_map[edge].add(node)
        
        def dfs(node):
            if not edge_map[node]:
                return

            if node in visited:
                return
            
            visited.add(node)
            for edge in edge_map[node]:
                dfs(edge)
            
        components = 0
        for i in range(n):
            if i not in visited:
                components+=1
                dfs(i)
        
        return components