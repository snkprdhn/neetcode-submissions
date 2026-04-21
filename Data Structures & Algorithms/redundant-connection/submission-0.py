class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        edge_map = {}
        for i in range(1, len(edges)+1):
            edge_map[i] = set()
        
        def dfs(i, prev):
            if i in visited:
                return False
            
            visited.add(i)
            for edge in edge_map[i]:
                if edge == prev:
                    continue
                if not dfs(edge, i):
                    return False            
            return True

        for node, edge in edges:
            edge_map[node].add(edge)
            edge_map[edge].add(node)
            visited = set()
            if not dfs(node, None):
                return [node, edge]
        
        return [] 