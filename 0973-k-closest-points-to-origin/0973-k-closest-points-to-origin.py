import heapq as hq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []

        for p in points:
            hq.heappush(distance, ((p[0] ** 2 + p[1] ** 2), p[0], p[1]))
        
        rslt = []
        for i in range(k):
            dist, x, y = hq.heappop(distance)
            rslt.append((x, y))

        return rslt