import heapq as hq

class Solution:

    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        a = 0
        b = 0
        combinations = []
        hq.heappush(combinations, (nums1[a] + nums2[b], a, b))
        
        rslt = []
        visited = set()
        while combinations:
            s, x, y = hq.heappop(combinations)
            if (x, y) in visited: continue
            visited.add((x, y))
            
            rslt.append((nums1[x], nums2[y]))
            if len(rslt)>=k:
                break

            if len(nums1) > x+1:
                hq.heappush(combinations, (nums1[x+1] + nums2[y], x+1, y))
            
            if len(nums2) > y+1:
                hq.heappush(combinations, (nums1[x] + nums2[y+1], x, y+1))

        return rslt