class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        adj = defaultdict(set)
        n = len(words)

        for i in range(n-1):
            w1 = words[i]
            w2 = words[i+1]

            min_len = min(len(w1), len(w2))
            if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
                return False
            
            for j in range(min_len):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break

        visited = set()
        for ch in order:
            if ch in adj:
                for val in adj[ch]:
                    if val in visited:
                        return False
            visited.add(ch)
        return True
