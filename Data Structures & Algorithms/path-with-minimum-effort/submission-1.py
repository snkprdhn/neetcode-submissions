class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, i):
        if self.parent[i] == i:
            return i
        
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
        
        return True

class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        dirs = [(1, 0), (0, 1)]

        m = len(heights)
        n = len(heights[0])  

        def get_index(i, j):
            return (i*n) + j      

        edges = []
        for i in range(m):
            for j in range(n):
                cur = heights[i][j]
                for r, c in dirs:
                    nr = i+r
                    nc = j+c
                    if 0<=nr<m and 0<=nc<n:
                        h_diff = abs(cur - heights[nr][nc])
                        edges.append([h_diff, get_index(i, j), get_index(nr, nc)])

        edges.sort()
        dsu = DSU(m*n)
        last_idx = get_index(m-1, n-1)

        for effort, u, v in edges:
            dsu.union(u, v)
            if dsu.find(0) == dsu.find(last_idx):
                return effort
        
        return 0

