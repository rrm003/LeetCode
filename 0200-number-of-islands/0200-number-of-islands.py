from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        i = 0 
        visited = set()
        island_count = 0
        while i < m :
            j = 0
            while j < n:
                if grid[i][j] == "1" and (i, j) not in visited:
                    queue = deque([])
                    queue.append((i, j))
                    visited.add((i, j))
                    island_count += 1
                    while queue:
                        x, y = queue.popleft()
                        for (nx, ny) in neighbours:
                            x1, y1 = x+nx, y+ny
                            if x1 < 0 or x1>=m or y1<0 or y1>=n:
                                continue
                            if (x1, y1) not in visited and grid[x1][y1] == "1":
                                queue.append((x1, y1))
                                visited.add((x1, y1))
                j += 1
            i += 1
        return island_count