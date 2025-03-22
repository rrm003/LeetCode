class Solution:
    def bfs(self, grid, i, j, visited):
        m = len(grid)
        n = len(grid[0])

        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        queue = []
        queue.append((i, j))

        while queue:
            x, y = queue[0]
            queue = queue[1:]

            visited[x][y] = True

            for neighbour in neighbours:
                nx, ny = x + neighbour[0], y + neighbour[1]
                if nx < 0 or nx >= m or ny < 0 or ny >= n: continue

                if grid[nx][ny] == "1" and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
    
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False for _ in range(cols)] for _ in range(rows)]

        island = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == "1" and visited[i][j] == False:
                    self.bfs(grid, i, j, visited)
                    island += 1

        return island