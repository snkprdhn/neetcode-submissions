class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        top_down = matrix[0][0]

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    if j == 0:
                        top_down = 0
                    else:
                        matrix[0][j] = 0


        # print(matrix)
        # print(top_down)

        # vertical
        for j in range(1, len(matrix[0])):
            if matrix[0][j] == 0:
                for i in range(len(matrix)):
                    matrix[i][j] = 0
        
        # horizontal
        for i in range(0, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(len(matrix[0])):
                    matrix[i][j] = 0
        
        # top-left
        if top_down == 0:
            for i in range(len(matrix)):
                matrix[i][0] = 0