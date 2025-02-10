class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        m = len(boxGrid)
        n = len(boxGrid[0])

        transform = [([''] * m) for i in range(n)]
        i = 0 
        while i < m:
            j = 0
            while j < n:
                transform[j][m-i-1] = boxGrid[i][j]
                j += 1
            i+=1

        print(transform)

        i = 0
        while i < m:
            j = n - 1
            while j >=0:
                print(j, i)
                if transform[j][i] == "#":
                    k = j
                    while (k+1) < n and transform[k+1][i] == ".":
                        k += 1

                    transform[j][i] = "."
                    transform[k][i] = "#"
                j -= 1
            
            i+=1

        return transform

# [".","#"],
# ["#","#"],
# ["*","*"],
# [".","."]

# ["#","#","."],
# ["#","#","."],
# ["*","#","#"],
# [".","*","#"],
# ["*",".","#"],
# [".",".","#"]

['#', '#', '#'], 
['#', '#', '#'], 
['*', '#', '#'], 
['.', '*', '.'], 
['*', '.', '#'], 
['.', '.', '.']