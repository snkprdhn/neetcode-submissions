class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        e_to_n = defaultdict(set)
        e_to_e = defaultdict(set)
        for account in accounts:
            name = account[0]
            for i in range(1, len(account)):
                email1 = account[i]
                if i+1 < len(account):
                    email2 = account[i+1]
                    e_to_e[email1].add(email2)
                    e_to_e[email2].add(email1)      
        
        # print(e_to_n)
        # print(e_to_e)
        
        def dfs(node, cur):
            if node in visited:
                return False
            
            if node in cur:
                return True
            cur.add(node)

            for nxt in e_to_e[node]:
                if not dfs(nxt, cur):
                    return False
            return True

        visited = set()
        res = []
        for account in accounts:
            cur = set()
            name = account[0]
            email = account[1]  
            if dfs(email, cur):
                visited.update(cur)
                res.append([name] + sorted(list(cur)))
            
        
        return res
