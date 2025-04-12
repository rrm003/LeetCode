class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        queue = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        neighbours = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        rslt = 0
        while queue:
            curr = queue[0]
            rslt = max(rslt, curr[2])
            queue = queue[1:]

            for neighbour in neighbours:
                x1, y1 = curr[0] + neighbour[0], curr[1] + neighbour[1]
                if x1 < 0 or x1 >= m or y1 < 0 or y1 >= n:
                    continue
                
                if grid[x1][y1] == 1:
                    grid[x1][y1] = 2
                    queue.append((x1, y1, curr[2] + 1))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1

        return rslt