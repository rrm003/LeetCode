class Solution:
    def dfs(self, dependency, curr, visited) -> bool:
        if curr in visited:
            return visited[curr]
        
        visited[curr] = False
        rslt = True
        for n in dependency[curr]:
            if n not in visited:
                visited[n] = self.dfs(dependency, n, visited)
                
            rslt = rslt and visited[n]
        
        visited[curr] = rslt
        return rslt

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dependency = {}
        visited = {}

        for cn in range(numCourses):
            dependency[cn] = []
        
        for info in prerequisites:
            dependency[info[0]].append(info[1])
        
        rslt = True
        for x in dependency:
            if x not in visited or not visited[x]:
                visited[x] = self.dfs(dependency, x, visited)
                
            rslt = rslt and visited[x]

        return rslt 
        