class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = {}
        tickets.sort()
        for src, dst in tickets[::-1]:
            if src not in adj:
                adj[src] = []
            adj[src].append(dst)
        
        res = []
        def dfs(src):
            if src in adj:
                while adj[src]:
                    dst = adj[src].pop()
                    dfs(dst)
            res.append(src)
        
        dfs("JFK")
        return res[::-1]