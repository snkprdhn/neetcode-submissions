class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        q = deque()
        visited = set()
        self.fresh = 0
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        for i in range(n):
            for j in range(m):
                if grid[i][j]==2:
                    q.append((i,j))
                    visited.add((i,j))
                if grid[i][j]==1:
                    self.fresh += 1
        
        if not self.fresh:
            return 0
        
        def add_cell(i, j):
            if min(i,j)<0 or i==n or j==m or (i,j) in visited or grid[i][j]==0:
                return
            q.append((i,j))
            visited.add((i,j))
            self.fresh -= 1

        minute = 0
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                for r, c in dirs:
                    add_cell(i+r, j+c)
            minute += 1
        print(self.fresh)
        return minute-1 if self.fresh==0 else -1