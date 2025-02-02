class Solution:
    def iterate(self, board, x, y, word, visited) -> bool:
        l = len(board)
        w = len(board[0])

        if len(word) == 0:
            return True
        
        neighours = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        
        ch = word[0]
        rslt = False
        for i, j in neighours:
            x1 = x + i
            y1 = y + j
            if x1<0 or x1>=l or y1<0 or y1 >= w:
                continue

            if board[x1][y1] == ch and (x1, y1) not in visited:
                visited.append((x1, y1))
                # print("found", ch)
                rslt = rslt or self.iterate(board, x1, y1, word[1:], visited)
                visited = visited[:-1]
                if rslt: return True
        
        return False
            
    def exist(self, board: List[List[str]], word: str) -> bool:
        l = len(board)
        w = len(board[0])
        ch = word[0]

        starting_points = []

        i = 0
        while i < l:
            j = 0 
            while j < w:
                visited = [(i, j)]
                if board[i][j] == ch:
                    if self.iterate(board, i, j, word[1:], visited): return True
                j+=1
            i+=1
        
        return False