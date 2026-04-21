class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        queens = [["."]*n for _ in range(n)]

        cols = set()
        diag_1 = set()
        diag_2 = set()

        def backtrack(r):
            if r == n:
                res.append(["".join(row) for row in queens])
                return

            for c in range(n):
                if c in cols or r+c in diag_1 or r-c in diag_2:
                    continue
                
                cols.add(c)
                diag_1.add(r+c)
                diag_2.add(r-c)
                queens[r][c] = "Q"
                backtrack(r+1)
                queens[r][c] = "."
                cols.remove(c)
                diag_1.remove(r+c)
                diag_2.remove(r-c)

        backtrack(0)
        return res

        
        


