class Solution:
    def dfs(self, graph, course, visited, sequence):
        if len(graph[course]) == 0:
            if course not in sequence:  
                sequence.append(course) 
            return True
        if course in visited: 
            return visited[course]
        
        satisfied = True
        visited[course] = False 
        for i in graph[course]:
            visited[i] = self.dfs(graph, i, visited, sequence)
            satisfied = satisfied and visited[i]

        if satisfied:
            if course not in sequence:  
                sequence.append(course)
        visited[course] = satisfied

        return satisfied   


    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {}
        visited = {}
        for i in range(numCourses):
            graph[i] = []

        for p in prerequisites:
            graph[p[0]].append(p[1])
        
        sequence = []
        for i in range(numCourses):
            if i not in visited:
                if not self.dfs(graph, i, visited, sequence):
                    return []

        return sequence