class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        n = len(words)
        adj = {c: set() for w in words for c in w}
        indegree = {c: 0 for c in adj}

        for i in range(n-1):
            word1 = words[i]
            word2 = words[i+1]

            min_len = min(len(word1), len(word2))
            if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
                return ""

            for j in range(min_len):
                if word1[j] != word2[j]:
                    if word2[j] not in adj[word1[j]]:
                        adj[word1[j]].add(word2[j])
                        indegree[word2[j]] += 1
                    break

        res = []
        q = deque()

        for ch, count in indegree.items():
            if not count:
                q.append(ch)

        while q:
            ch = q.popleft()
            res.append(ch)

            for nxt in adj[ch]:
                indegree[nxt] -= 1
                if not indegree[nxt] :
                    q.append(nxt)
        


        return "".join(res) if len(res) == len(adj) else ""
                    
        
