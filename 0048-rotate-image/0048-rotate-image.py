class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            j = 0
            while i > j:
                temp = matrix[i][j]
                matrix[i][j] =  matrix[j][i]
                matrix[j][i] = temp
                j = j+1
        
        for x in matrix:
            x.reverse()