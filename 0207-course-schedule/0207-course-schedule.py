class Solution:
    def dfs(self, course, graph, satisfied, stack)-> bool:
        if satisfied[course]: return True
        if course in stack: return False
        
        stack.append(course)
        rslt = True
        for neighbour in graph[course]:
            rslt = rslt and self.dfs(neighbour, graph, satisfied, stack)

        satisfied[course] = rslt
        return rslt

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        satisfied = {}
        for i in range(0, numCourses):
            graph[i] = []
            satisfied[i] = False
        
        for c1, c2 in prerequisites:
            graph[c1].append(c2)

        for i in range(0, numCourses):
            if not satisfied[i]:
                rslt = self.dfs(i, graph, satisfied, [])
                if not rslt : return False
                satisfied[i] = rslt
        
        return True
