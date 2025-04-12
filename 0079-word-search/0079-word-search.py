class Solution:
    def dfs(self, board, i, j, w, word, visited) -> bool:
        if w == len(word) -1 : return True
        if visited[i][j]: return True

        m = len(board)
        n = len(board[0])
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited[i][j] = True
        for neighbour in neighbours:
            x1, y1 = i + neighbour[0], j + neighbour[1]
            if x1 >= 0 and x1 < m and y1 >= 0 and y1 < n and not visited[x1][y1]:
                if w < len(word) - 1 and board[x1][y1] == word[w+1]:
                    rslt = self.dfs(board, x1, y1, w + 1, word, visited)
                    if rslt: return True
        
        visited[i][j] = False
        return False

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = [[False for _ in range(n)] for _ in range(m)]
                    if self.dfs(board, i, j, 0, word, visited):
                        return True
        
        return False
