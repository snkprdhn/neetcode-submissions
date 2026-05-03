class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
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
            return False
        
        if self.size[root_i] > self.size[root_j]:
            self.parent[j] = root_i
            self.size[root_i] += self.size[root_j]
        else:
            self.parent[i] = root_j
            self.size[root_j] += self.size[root_i]
        
        self.components -= 1
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        dsu = DSU(n)

        def gcd(a, b):
            if not b:
                return a
            return gcd(b, a % b)

        for i in range(n):
            for j in range(i+1, n):
                if gcd(nums[i], nums[j]) > 1:
                    dsu.union(i, j)
                    if dsu.components == 1:
                        return True
        
        return False
