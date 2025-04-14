class Solution:
    def findReachable(self, graph, k, visited):
        if k[0] in visited: return []
        # if len(graph[k[0]]) == 0:
        #     return []
        
        rslt = [k]
        visited.append(k[0])
        for neighbour in graph[k[0]]:
            rslt.extend(self.findReachable(graph, (neighbour[0], k[1]*neighbour[1]), visited))

        return rslt

    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}

        for i, equation in enumerate(equations):
            if equation[0] not in graph:
                graph[equation[0]] = []

            graph[equation[0]].append((equation[1], values[i]))
            
            if equation[1] not in graph:
                graph[equation[1]] = []
                
            graph[equation[1]].append((equation[0], 1 /values[i]))

        # print(graph)

        reachable = {}
        for key in graph.keys():
            reachable[key] = self.findReachable(graph, (key, 1), [])
        
        # print(reachable)

        rslt = []
        for a, b in queries:
            if a not in reachable:
                rslt.append(-1)
            else:
                found = False
                for bi in reachable[a]:
                    if bi[0] == b:
                        found = True
                        rslt.append(bi[1])

                if not found:
                    rslt.append(-1)

        return rslt