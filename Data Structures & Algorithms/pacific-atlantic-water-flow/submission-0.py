class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        n, m = len(heights), len(heights[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        pac_q = deque()
        atl_q = deque()
        pac = set()
        atl = set()

        for i in range(n):
            pac_q.append((i,0))
            pac.add((i,0))

        for j in range(1, m):
            pac_q.append((0,j))
            pac.add((0,j))

        for i in range(n):
            atl_q.append((i, m-1))
            atl.add((i, m-1))

        for j in range(m-1):     # skip bottom-right only
            atl_q.append((n-1, j))
            atl.add((n-1, j))
        
        def bfs(q, visited):
            while q:
                i, j = q.popleft()
                for r, c in dirs:
                    nr = i+r
                    nc = j+c
                    if (0<=nr<n) and (0<=nc<m) and heights[nr][nc]>=heights[i][j] and (nr, nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))

        bfs(pac_q, pac)       
        bfs(atl_q, atl)
        
        return list(pac & atl)