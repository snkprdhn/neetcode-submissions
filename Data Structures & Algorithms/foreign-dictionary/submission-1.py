class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        for w in words:
            for c in w:
                adj[c] = set()
        
        n = len(words)
        for i in range(n-1):
            min_len = min(len(words[i]), len(words[i+1]))
            if words[i][:min_len] == words[i+1][:min_len] and len(words[i]) > len(words[i+1]):
                return ""
            for j in range(min_len):
                if words[i][j] != words[i+1][j]:
                    adj[words[i][j]].add(words[i+1][j])
                    break
        
        #print(adj)
        visited = {}
        res = []
        def dfs(c):
            #print(f"got: {c}", visited, res)
            if c in visited:
                return visited[c]
            
            visited[c] = True
            for edge in adj[c]:
                #print(f"edge:{edge}")
                if dfs(edge):
                    return True
            res.append(c)
            visited[c] = False
            return False
        
        for c in adj.keys():
            if dfs(c):
                return ""
        
        #print(res)
        return "".join(res[::-1])