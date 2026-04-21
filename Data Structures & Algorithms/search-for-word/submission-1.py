class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n,m = len(board),len(board[0])
        char_req = len(word)
        def backtrack(i, j, char_found):
            if char_found == char_req:
                return True
            
            if i<0 or j<0 or i==n or j==m or board[i][j] != word[char_found]:
                return False
            
            temp = board[i][j]
            board[i][j] = "#"

            found = (
                backtrack(i+1, j, char_found+1) or
                backtrack(i-1, j, char_found+1) or
                backtrack(i, j+1, char_found+1) or
                backtrack(i, j-1, char_found+1)
            )
            board[i][j] = temp
            return found
        
        for i in range(n):
            for j in range(m):
                if backtrack(i,j,0):
                    return True
        
        return False