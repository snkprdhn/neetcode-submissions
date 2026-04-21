class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        max_area = 0
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def dfs(i, j):
            if i<0 or j<0 or i==n or j==m or grid[i][j]==0:
                return 0

            grid[i][j] = 0
            area = 1
            for r, c in dirs:
                area += dfs(i+r, j+c)         
            return area

        for i in range(n):
            for j in range(m):
                if grid[i][j]==1:
                    area = dfs(i, j)
                    max_area = max(max_area, area)
        
        return max_area