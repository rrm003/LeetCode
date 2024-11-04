class Solution:
    def dfs(self, dependency, curr, visited, schedule) -> bool:
        if curr in visited:
            return visited[curr]
        
        visited[curr] = False
        rslt = True
        for n in dependency[curr]:
            if n not in visited:
                visited[n] = self.dfs(dependency, n, visited, schedule)
                
            rslt = rslt and visited[n]
        
        if rslt:
            schedule.append(curr)

        visited[curr] = rslt
        return rslt

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dependency = {}
        visited = {}

        for cn in range(numCourses):
            dependency[cn] = []
        
        for info in prerequisites:
            dependency[info[0]].append(info[1])
        
        rslt = True
        schedule = []
        for x in dependency:
            if x not in visited or not visited[x]:
                visited[x] = self.dfs(dependency, x, visited, schedule)
            
            rslt = rslt and visited[x]
        
        if len(schedule) < numCourses:
            return []

        return schedule 
    