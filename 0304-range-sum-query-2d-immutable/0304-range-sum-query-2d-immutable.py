class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        l = len(matrix)
        self.prefix = [[]] * l
        for i, row in enumerate(matrix):
            self.prefix[i] = []
            for j, col in enumerate(row):
                n = [col]
                if i > 0:
                    n.append(self.prefix[i-1][j])

                if j > 0:
                    n.append(self.prefix[i][j-1])
                
                if i>0 and j>0:
                    n.append(self.prefix[i-1][j-1]*-1)
                
                self.prefix[i].append(sum(n))
                print(self.prefix[i][j], end=" ")
            print()

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.prefix[row2][col2]
        if row1 > 0:
            total -= self.prefix[row1-1][col2]
        if col1 > 0:
            total -= self.prefix[row2][col1-1]
        if row1>0 and col1>0:
            total += self.prefix[row1-1][col1-1] 
        return total

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)