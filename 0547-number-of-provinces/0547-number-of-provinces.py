class Solution:
    def dfs(self, adjacencyList, city, visited):
        if city in visited: return 

        for i in adjacencyList[city]:
            visited[i] = True
            self.dfs(adjacencyList, i, visited) 


    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adjacencyList = {}
        m = len(isConnected)
        n = len(isConnected[0])

        for i in range(m):
            adjacencyList[i] = []
        
        for i in range(m):
            for j in range(n):
                if i == j or isConnected[i][j] == 0: continue
                adjacencyList[i].append(j)
                
        print(adjacencyList)

        province = 0
        visited = {}
        for i in range(m):
            if i not in visited:
                province += 1
                self.dfs(adjacencyList, i, visited)

        return province
        