class Solution:

    def depth(self, graph, curr, visited, dist) -> int:
        if curr in visited: return dist
        if len(graph[curr]) == 0: return dist

        visited.add(curr)

        height = 0
        for n in graph[curr]:
            height = max(height, self.depth(graph, n, visited, dist + 1))
        
        return height

    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 0: return []
        if n == 1: return [0]
        
        adj_list = {}
        for i in range(n):
            adj_list[i] = []
            
        for e in edges:
            adj_list[e[0]].append(e[1])
            adj_list[e[1]].append(e[0])
        
        heights = []
        min_height = math.inf
        for k in range(n):
            if len(adj_list[k]) == 0:  continue
            visited = set()
            h = self.depth(adj_list, k, visited, 0)
            min_height = min(min_height, h)
            heights.append((h, k))
        
        rslt = []
        for h in heights:
            if h[0] == min_height:
                rslt.append(h[1])

        return rslt