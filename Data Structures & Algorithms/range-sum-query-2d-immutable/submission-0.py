class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.mat = matrix
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.area = [[0] * self.n for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                self.area[i][j] += self.mat[i][j]
                if i>0:
                    self.area[i][j] += self.area[i-1][j]
                if j>0:
                    self.area[i][j] += self.area[i][j-1]
                if i>0 and j>0:
                    self.area[i][j] -= self.area[i-1][j-1]
        #print(self.area)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        base_area = self.area[row2][col2]
        #print("0", base_area)
        if row1>0:
            base_area -= self.area[row1-1][col2]
            #print("1", base_area, self.area[row1-1][col2])
        if col1>0:
            base_area -= self.area[row2][col1-1]
            #print("2", base_area, self.area[row2][col1-1])
        if row1>0 and col1>0:
            base_area += self.area[row1-1][col1-1]
            #print("3", base_area, self.area[row1-1][col1-1])
        
        return base_area

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)