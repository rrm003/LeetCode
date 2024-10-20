class Solution:
    def traverse(self, curr: int, visited: dict, graph: dict, order: list):
        # print("processing", curr)
        if len(visited) == len(graph):
            return graph[curr]

        neighbor = graph[curr]
        if len(neighbor) == 0:
            # order.append(curr)
            return True
        
        visited[curr] = False
        is_possible = True
        for x in neighbor:
            if x not in visited:
                rslt = self.traverse(x, visited, graph, order)
                visited[x] = rslt
                order.append(x)
                is_possible = is_possible and rslt
            else:
                is_possible = visited[x] and is_possible

        visited[curr] = is_possible
        # order.append(curr)
        # print("rslt", is_possible)
        return is_possible

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        lookup = {}
        for x in range(numCourses):
            lookup[x] = []
        
        for pre in prerequisites:
            lookup[pre[1]].append(pre[0])
        
        visited = {}
        is_possible = True
        order = []
        for x in range(numCourses):
            # print(visited)
            if x not in visited:
                rslt = self.traverse(x, visited, lookup, order)
                visited[x] = rslt
                order.append(x)
                is_possible = is_possible and rslt 
            else:
                is_possible = visited[x] and is_possible
        
        order.reverse()
        return order if is_possible else []