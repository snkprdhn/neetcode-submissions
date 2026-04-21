class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Check rows
        for i in range(len(board)):
            val = [0] * 10
            for j in range(len(board[0])):
                ele = board[i][j]
                if ele != ".":
                    if val[int(ele)] != 0:
                        return False
                    val[int(ele)] = 1
        
        # Check columns
        for j in range(len(board[0])):
            val = [0] * 10
            for i in range(len(board)):
                ele = board[i][j]
                if ele != ".":
                    if val[int(ele)] != 0:
                        return False
                    val[int(ele)] = 1
        
        # Check 3x3 sub-boxes
        for i in range(0, len(board), 3):
            for j in range(0, len(board[0]), 3):
                val = [0] * 10
                for m in range(i, i+3):
                    for n in range(j, j+3):
                        # print(m, n)
                        ele = board[m][n]
                        if ele != ".":
                            if val[int(ele)] != 0:
                                return False
                            val[int(ele)] = 1

        return True