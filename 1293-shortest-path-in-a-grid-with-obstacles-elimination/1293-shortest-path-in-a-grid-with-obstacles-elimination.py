from collections import deque

class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        l = len(grid) - 1
        w = len(grid[0]) - 1

        queue = deque()
        visited = set()
        moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        queue.append((0, 0, k, 0))

        rslt = math.inf
        while len(queue) > 0:
            x, y, o, d = queue.popleft()
            
            if (x, y, o) in visited:
                continue
            
            visited.add((x, y, o))
            if x == l and y == w:
                rslt = min(rslt, d)

            for move in moves:
                x1 = x + move[0]
                y1 = y + move[1]

                if (x1, y1) in visited:
                    continue
    
                if (x1 >=0 and x1 <= l and y1>=0 and y1 <= w):
                    val = grid[x1][y1]
                    if val == 1 and o ==0:
                        continue
                    
                    o1 = o
                    if val == 1 and o > 0:
                        o1 = o1 - 1 

                    queue.append((x1, y1, o1, d + 1))
            
        return -1 if rslt == math.inf else rslt

