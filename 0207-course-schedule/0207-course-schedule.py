class Solution:
    def dfs(self, graph, curr, completed) -> bool:
        if len(graph[curr]) == 0: return True
        if curr in completed: return completed[curr]

        rslt = True
        completed[curr] = False
        for deps in graph[curr]:
            rslt = rslt and self.dfs(graph, deps, completed)

        completed[curr] = rslt
        return rslt

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        completed = {}

        for i in range(numCourses):
            graph[i] = [] 
        
        for preq in prerequisites:
            graph[preq[0]].append(preq[1])

        rslt = True
        for i in range(numCourses):
            rslt = rslt and self.dfs(graph, i, completed)
        
        return rslt