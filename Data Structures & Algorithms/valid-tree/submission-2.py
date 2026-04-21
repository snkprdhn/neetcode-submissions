class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False
            
        edge_map = {}
        visited = set()

        for node in range(n):
            edge_map[node] = set()
        
        for node, edge in edges:
            edge_map[node].add(edge)
            edge_map[edge].add(node)
        
        def dfs(node, prev):
            if node in visited:
                return False
            
            visited.add(node)
            for i in edge_map[node]:
                if i==prev:
                    continue

                if not dfs(i, node):
                    return False
            return True

        return dfs(0, None) and n==len(visited)