from math import isqrt
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
        if n == 1:
            return True
        if 1 in nums:
            return False

        max_num = max(nums)

        # primes up to sqrt(max_num)
        limit = isqrt(max_num)
        is_prime = [True] * (limit + 1)
        primes = []
        for i in range(2, limit + 1):
            if is_prime[i]:
                primes.append(i)
                for j in range(i * i, limit + 1, i):
                    is_prime[j] = False

        def get_factors(x):
            factors = set()
            for p in primes:
                if p * p > x:
                    break
                if x % p == 0:
                    factors.add(p)
                    while x % p == 0:
                        x //= p
            if x > 1:
                factors.add(x)
            return factors

        # group indices by value
        pos = defaultdict(list)
        for i, x in enumerate(nums):
            pos[x].append(i)

        dsu = DSU(n)
        owner = {}  # prime factor -> one index that has it
        factor_cache = {}

        for val, indices in pos.items():
            if val not in factor_cache:
                factor_cache[val] = get_factors(val)

            rep = indices[0]

            # connect duplicates of the same value
            for idx in indices[1:]:
                dsu.union(rep, idx)

            # connect this value through its prime factors
            for f in factor_cache[val]:
                if f in owner:
                    dsu.union(rep, owner[f])
                else:
                    owner[f] = rep

            if dsu.components == 1:
                return True

        return dsu.components == 1