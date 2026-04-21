class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        n = len(grid)
        m = len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        visited = set()
        q = deque()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 0:
                    q.append((i,j))
                    visited.add((i,j))
        
        def add_cell(i,j):
            if i<0 or j<0 or i==n or j==m or grid[i][j]==-1 or (i,j) in visited:
                return
            visited.add((i,j))
            q.append((i,j))

        dist = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                grid[i][j] = dist
                for r, c in dirs:
                    add_cell(i+r, j+c)
            dist+=1
