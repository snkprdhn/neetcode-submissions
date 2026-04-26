class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m = len(grid)
        n = len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        q = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q.append((0,i,j))
        
        while q:
            dist, i, j = q.popleft()
            for r, c in dirs:
                new_r = i+r
                new_c = j+c
                if 0<=new_r<m and 0<=new_c<n and grid[new_r][new_c] != "-1":
                    if grid[new_r][new_c] > (dist+1):
                        grid[new_r][new_c] = dist+1
                        q.append((dist+1, new_r, new_c))