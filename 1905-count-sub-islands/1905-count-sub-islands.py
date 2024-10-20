class Solution:
    def isSubIsland(self, i, j, grid1, grid2, visited):
        l = len(grid2)
        w = len(grid2[0])
        queue = []
        queue.append((i, j))

        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        rslt = True
        while len(queue) > 0:
            x, y = queue[0]
            queue = queue[1:]
            visited.add((x, y))

            if grid1[x][y] != grid2[x][y]:
                rslt = rslt and False
            
            for n in neighbours:
                nx, ny = n[0] + x, n[1] + y
                if (nx>=0 and nx<l and ny>=0 and ny<w):
                    if (nx, ny) not in visited and grid2[nx][ny] == 1:
                        if grid1[nx][ny] != grid2[nx][ny]:
                            rslt = rslt and False
                        queue.append((nx, ny))
                visited.add((nx, ny))
        
        return rslt
                  
            

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        visited = set()
        count = 0

        for i, row in enumerate(grid2):
            for j, col in enumerate(row):
                if (i, j) not in visited and col == 1:
                    if self.isSubIsland(i, j, grid1, grid2, visited):
                        count += 1 
                    
                visited.add((i, j))
                # print(visited)

        return count