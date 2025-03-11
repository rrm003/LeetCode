class Solution:
    def dfs(self, course: int, graph: dict, satisfied: List[bool], stack: List[int]) -> bool:
        if len(graph[course]) == 0 or satisfied[course]: return True
        if course in stack: return False

        stack.append(course)

        rslt = True
        for pr in graph[course]:
            rslt = rslt and self.dfs(pr, graph, satisfied, stack)
        
        satisfied[course] = rslt

        return rslt


    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = {}
        satisfied = {}
        for i in range(numCourses):
            graph[i] = []
            satisfied[i] = True
        
        for prerequisite in prerequisites:
            graph[prerequisite[0]].append(prerequisite[1])
            satisfied[prerequisite[0]] = False
        
        print(graph)

        rslt = True
        for i in range(numCourses):
            if satisfied[i]:
                continue

            stack = []
            rslt = rslt and self.dfs(i, graph, satisfied, stack)

        return rslt