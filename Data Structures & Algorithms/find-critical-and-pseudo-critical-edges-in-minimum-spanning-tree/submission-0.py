class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.components = n
    
    def find(self, i):
        if self.parent[i] == i:
            return self.parent[i]
        
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]
    
    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)

        if root_i == root_j:
            return False
        
        if self.size[root_i] > self.size[root_j]:
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
        else:
            self.parent[root_i] = root_j
            self.size[root_j] += self.size[root_i]
        
        self.components -= 1
        return True

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        for i , e in enumerate(edges):
            # e = [u, v, w, i]
            e.append(i)
        
        edges.sort(key = lambda x:x[2])

        # Find mst_weight
        mst_weight = 0
        dsu = DSU(n)
        for u, v, w, i in edges:
            if dsu.union(u, v):
                mst_weight += w
            
            if dsu.components == 1:
                break
        
        # Check if each edge is critical or pseudo critical
        critical = []
        pseudo_critical = []
        for u1, v1, edge_w, i in edges:
            # Check Critical, try without curr edge
            dsu = DSU(n)
            cur_weight = 0
            for u2, v2, w, j in edges:
                if i != j and dsu.union(u2, v2):
                    cur_weight += w
                
            if dsu.components != 1 or cur_weight > mst_weight:
                critical.append(i)
                continue
            
            # Check Pseudo critical, try with curr edge
            dsu = DSU(n)
            cur_weight = edge_w
            dsu.union(u1, v1)
            for u3, v3, w, j in edges:
                if i!= j and dsu.union(u3, v3):
                    cur_weight += w
                
            if cur_weight == mst_weight:
                pseudo_critical.append(i)

        return [critical, pseudo_critical]
