class DisjointSet():
    def __init__(self, n):
        self.size = [1] * (n+1)
        self.par = [i for i in range(n+1)] 
    
    def find_par(self, i):
        if self.par[i] != i:
            self.par[i] = self.find_par(self.par[i])        
        return self.par[i]
    
    def union(self, i, j):
        par_i = self.find_par(i)
        par_j = self.find_par(j)

        if par_i == par_j:
            return False
        
        if self.size[par_j] > self.size[par_i]:
            self.par[par_i] = par_j
            self.size[par_j] += self.size[par_i]
        else:
            self.par[par_j] = par_i
            self.size[par_i] += self.size[par_j]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        u_set = DisjointSet(n)
        for i, j in edges:
            if not u_set.union(i, j):
                return [i, j]
        return []
