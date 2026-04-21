class Solution:
    def solve(self, board: List[List[str]]) -> None:
        q = deque()
        n, m = len(board), len(board[0])
        visited = set()
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]

        for i in range(n):
            if board[i][0] == "O":
                q.append((i,0))
                visited.add((i,0))
                board[i][0] = "T"
            if board[i][m-1] == "O":
                q.append((i,m-1))
                visited.add((i,m-1))
                board[i][m-1] = "T"
        
        for j in range(1,m-1):
            if board[0][j] == "O":
                q.append((0,j))
                visited.add((0,j))
                board[0][j] = "T"
            if board[n-1][j] == "O":
                q.append((n-1,j))
                visited.add((n-1,j))
                board[n-1][j] = "T"
        
        while q:
            i, j = q.popleft()
            for r, c in dirs:
                nr = i+r
                nc = j+c

                if (0<=nr<n) and (0<=nc<m) and (nr, nc) not in visited and board[nr][nc]=="O":
                    board[nr][nc] = "T"
                    visited.add((nr, nc))
                    q.append((nr,nc))
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"
        

            