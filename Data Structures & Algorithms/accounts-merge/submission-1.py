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
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsu = DSU(n)

        e_to_n = {}

        for i, account in enumerate(accounts):
            name = account[0]
            for email in account[1:]:
                if email in e_to_n:
                    dsu.union(e_to_n[email], i)
                else:
                    e_to_n[email] = i
        
        
        n_to_e = defaultdict(list)
        for email, name in e_to_n.items():
            parent = dsu.find(name)
            n_to_e[parent].append(email)
        
        res = []
        for name, emails in n_to_e.items():
            res.append([accounts[name][0]] + sorted(emails))
        
        return res