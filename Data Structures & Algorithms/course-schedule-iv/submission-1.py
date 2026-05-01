class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = defaultdict(set)
        indegree = [0] * numCourses
        for u, v in prerequisites:
            adj[u].add(v)
            indegree[v] += 1

        q = deque([i for i in range(numCourses) if indegree[i]==0])
        preq = defaultdict(set)

        while q:
            cur = q.popleft()

            for nxt in adj[cur]:
                preq[nxt].add(cur)
                preq[nxt].update(preq[cur])

                indegree[nxt] -= 1
                if not indegree[nxt]:
                    q.append(nxt)
                    
        res = []
        for u, v in queries:
            res.append(u in preq[v])
        
        return res