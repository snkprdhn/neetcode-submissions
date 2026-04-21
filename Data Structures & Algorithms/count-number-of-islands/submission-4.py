class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_island = 0
        n,m = len(grid), len(grid[0])
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(i,j):
            if i<0 or j<0 or i==n or j==m or grid[i][j]=="0":
                return
            
            grid[i][j] = "0"
            for r, c in dirs:
                dfs(i+r,j+c)
        
        for i in range(n):
            for j in range(m):
                if grid[i][j]=="1":
                    dfs(i,j)
                    print(i,j)
                    num_island+=1
        
        return num_island
