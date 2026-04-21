class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj = {}
        indegree = {}
        for word in words:
            for c in word:
                adj[c] = set()
                indegree[c] = 0

        for i in range(len(words)-1):
            word_1 = words[i]
            word_2 = words[i+1]

            min_len = min(len(word_1), len(word_2))
            if word_1[:min_len] == word_2[:min_len] and len(word_1) > len(word_2):
                return ""

            for j in range(min_len):
                if word_1[j] != word_2[j]:
                    # if word_1[j] not in indegree:
                    #     indegree[word_1[j]] = 0
                    # if word_2[j] not in indegree:
                    #     indegree[word_2[j]] = 0

                    if word_1[j] not in adj:
                        adj[word_1[j]] = set()
                    if word_2[j] not in adj[word_1[j]]:
                        adj[word_1[j]].add(word_2[j])
                        indegree[word_2[j]] += 1
                    break
        
        print(adj)
        print(indegree)

        q = deque()
        for c, degree in indegree.items():
            if degree == 0:
                q.append(c)


        ans = []
        while q:
            c = q.popleft()
            if c in adj:
                for edge in adj[c]:
                    indegree[edge] -= 1
                    if indegree[edge] == 0:
                        q.append(edge)
            ans.append(c)
        
        if len(ans) != len(indegree):
            return ""
        return "".join(ans)

