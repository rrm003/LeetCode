class Solution:
    def dfs(self, graph, curr, completed, visits) -> bool:
        if len(graph[curr]) == 0: return True
        if completed[curr]: return True
        if curr in visits: return False

        rslt = True
        visits.append(curr)
        for deps in graph[curr]:
            rslt = rslt and self.dfs(graph, deps, completed, visits)
        visits = visits[:-1]

        completed[curr] = rslt
        return rslt


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        completed = {}

        for i in range(numCourses):
            graph[i] = [] 
            completed[i] = False
        
        for preq in prerequisites:
            graph[preq[0]].append(preq[1])

        rslt = True
        for i in range(numCourses):
            rslt = rslt and self.dfs(graph, i, completed, [])
        
        return rslt