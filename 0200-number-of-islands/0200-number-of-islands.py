class Solution:
    def traverse(self, grid, x, y, lookup):
        row = len(grid)
        col = len(grid[0])
        neighbors = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        queue = []
        queue.append((x, y))

        while len(queue) > 0:
            curr = queue[0]
            queue = queue[1:]
            lookup[curr[0]][curr[1]] = True

            for n in neighbors:
                i, j = curr[0] + n[0], curr[1] + n[1]
                if i < 0 or i >= row or j < 0 or j >= col:
                    continue

                if lookup[i][j] or grid[i][j] == "0":
                    continue

                queue.append((i, j))
                lookup[i][j] = True

    def numIslands(self, grid: List[List[str]]) -> int:
        row = len(grid)
        col = len(grid[0])

        lookup = [ [False for x in range(col)] for y in range(row)]
        print(lookup)

        island = 0
        for i in range(row):
            for j in range(col):
                if lookup[i][j] or grid[i][j] == "0":
                    continue
                else:
                    self.traverse(grid, i, j, lookup)
                    island += 1
        return island