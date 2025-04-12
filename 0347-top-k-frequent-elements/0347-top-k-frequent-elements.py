from collections import Counter
import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        freq_list = [ (-v, k) for (k, v) in freq.items() ]

        hq.heapify(freq_list)
        
        rslt = []
        for i in range(k):
            k, v = hq.heappop(freq_list)
            rslt.append(v)

        return rslt