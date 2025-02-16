class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        area = 0 
        queue = []
        visited = set()
        neighbours = [(1, 0), (0, -1), (-1, 0), (0, 1)]

        for i in range(r):
            for j in range(c):
                if (i, j) not in visited:
                    if grid[i][j] == 0: continue

                    print(f"({i} {j}) : {area}")
                    queue.append((i, j))
                    curr_area = 0
                    while queue:
                        x, y = queue[0]
                        queue = queue[1:]
                        if grid[x][y] == 0 or (x, y) in visited: continue
                        
                        curr_area += 1
                        visited.add((x,y))
                        
                        for n in neighbours:
                            cx, cy = x + n[0], y + n[1]
                            if cx < 0 or cx >= r or cy < 0 or cy >= c: continue
                            if grid[cx][cy] == 0 or (cx, cy) in visited: continue

                            print(f"\t{cx} {cy}")
                            queue.append((cx, cy))
                
                    area = max(area, curr_area)
        
        return area