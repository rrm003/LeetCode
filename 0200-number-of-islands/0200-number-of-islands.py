class Solution:
    def bfs(self, grid, i, j, visited):
        l = len(grid)
        w = len(grid[0])

        queue = []
        queue.append((i, j))
        neighbours = [[1, 0], [0, 1], [-1, 0], [0, -1]]

        while len(queue) > 0:
            x, y = queue[0]
            queue = queue[1:]
            visited.add((x, y))
            
            for n in neighbours:
                nx, ny = x+n[0], y+n[1]
                if (nx >=0 and nx < l and ny>=0 and ny<w):
                    if  grid[nx][ny] == "1" and  (nx, ny) not in visited:
                        queue.append((nx, ny))
                        visited.add((nx, ny))


    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        islands = 0

        for i, row in enumerate(grid):
            for j, col in enumerate(row):
                if grid[i][j] == "1" and (i, j) not in visited:
                    self.bfs(grid, i, j, visited)
                    # print(visited)
                    islands+=1
        
        return islands
        