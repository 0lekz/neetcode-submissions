class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.prefix = [[0] * len(matrix[0]) for _ in range(len(matrix))] 
        for row in range(len(matrix)):
            total = 0
            for col in range(len(matrix[0])):
                total += matrix[row][col]
                self.prefix[row][col] = total


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        res = 0
        
        for i in range(row1, row2 + 1):
            R = self.prefix[i][col2]
            L = self.prefix[i][col1 - 1] if col1 > 0 else 0
            res += R - L

        return res


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)