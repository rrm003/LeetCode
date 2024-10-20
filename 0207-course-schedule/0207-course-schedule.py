class Solution:
    def traverse(self, curr: int, visited: dict, graph: dict):
        # print("processing", curr)
        if len(visited) == len(graph):
            return  graph[curr]

        neighbor = graph[curr]
        if len(neighbor) == 0:
            return True
        
        visited[curr] = False
        is_possible = True
        for x in neighbor:
            if x not in visited:
                rslt = self.traverse(x, visited, graph)
                visited[x] = rslt
                is_possible = is_possible and rslt
            else:
                is_possible = visited[x] and is_possible

        visited[curr] = is_possible
        # print("rslt", is_possible)
        return is_possible

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        lookup = {}
        for x in range(numCourses):
            lookup[x] = []
        
        for pre in prerequisites:
            lookup[pre[1]].append(pre[0])
        
        visited = {}
        is_possible = True
        for x in range(numCourses):
            # print(visited)
            if x not in visited:
                rslt = self.traverse(x, visited, lookup)
                visited[x] = rslt
                is_possible = is_possible and rslt 
            else:
                is_possible = visited[x] and is_possible

        return is_possible