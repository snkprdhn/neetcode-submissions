class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]

        q = deque()
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    q.append((i,j))
                    visited.add((i,j))

        perimeter = 0

        while q:
            i, j = q.popleft()
            for r, c in dirs:
                nr = i+r
                nc = j+c

                if (nr, nc) not in visited:
                    if 0<=nr<m and 0<=nc<n and grid[nr][nc]:
                        visited.add((nr, nc))
                        q.append((nr, nc))
                    else:
                        perimeter += 1
        
        return perimeter
