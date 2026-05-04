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
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
        else:
            self.parent[root_i] = root_j
            self.size[root_j] += self.size[root_i]
        
        self.components -= 1
        return True

class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        n = len(nums)
        if n > 1 and 1 in nums:
            return False

        dsu = DSU(n)

        max_num = max(nums)
        seive = list(range(max_num+1))

        for i in range(2, int(max_num ** 0.5) + 1):
            if seive[i] == i:
                for j in range(i*i, max_num+1, i):
                    if seive[j] == j:
                        seive[j] = i
        
        def get_factors(x):
            factor_set = set()
            while x>1:
                factor_set.add(seive[x])
                x //= seive[x]
            return factor_set

        factor_map = {}
        for i in range(n):
            for f in get_factors(nums[i]):
                if f in factor_map:
                    dsu.union(factor_map[f], i)
                else:
                    factor_map[f] = i
 
        return dsu.components == 1
