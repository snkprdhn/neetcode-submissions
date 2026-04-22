class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        INF = 2147483647
        m = len(grid)
        n = len(grid[0])
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        def bfs(q):
            visited = set()
            while q:
                level_len = len(q)
                for _ in range(level_len):
                    i, j, dist = q.popleft()
                    visited.add((i,j))
                    grid[i][j] = min(grid[i][j], dist)
                    for r, c in dirs:
                        new_r = i+r
                        new_c = j+c
                        if (0 <= new_r < m) and (0 <= new_c < n) and ((new_r, new_c) not in visited) and (grid[new_r][new_c] != -1) and (grid[new_r][new_c] != 0):
                            q.append((new_r, new_c, dist+1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    q = deque()
                    q.append((i,j,0))
                    bfs(q)

        