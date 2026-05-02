class DSU:
    def __init__(self):
        self.parent = {}
        self.weight = {}
    
    def add(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.weight[x] = 1
        
    def find(self, x):
        if self.parent[x] == x:
            return x
        
        org_parent = self.parent[x]
        self.parent[x] = self.find(self.parent[x])
        self.weight[x] *= self.weight[org_parent]

        return self.parent[x]
    
    def union(self, x, y, val):
        self.add(x)
        self.add(y)
        root_x, root_y = self.find(x), self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y
            self.weight[root_x] = val * ( self.weight[y] / self.weight[x])
    
    def get_ratio(self, x, y):
        if x not in self.parent or y not in self.parent or self.find(x)!=self.find(y):
            return -1
        
        return self.weight[x] / self.weight[y]

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dsu = DSU()
        
        for i, (a, b) in enumerate(equations):
            dsu.union(a, b, values[i])
        
        return [dsu.get_ratio(a, b) for a, b in queries]
        