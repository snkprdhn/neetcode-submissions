class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        perimeter = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    for r, c in dirs:
                        nr = i+r
                        nc = j+c
                        if 0<=nr<m and 0<=nc<n and grid[nr][nc]:
                            continue
                        perimeter += 1

        
        return perimeter
