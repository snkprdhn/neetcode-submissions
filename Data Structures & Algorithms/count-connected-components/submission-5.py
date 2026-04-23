class dsu:
    def __init__(self, n):
        self.parent = list(range(n))
        self.components = n
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return

        self.parent[root_j] = root_i
        self.components -= 1


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = dsu(n)
        for i, j in edges:
            graph.union(i, j)
        
        return graph.components