import heapq as hq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}
        for num in nums:
            if num not in lookup:
                lookup[num] = 0
            lookup[num] += 1

        item_with_freq = [(-f, v) for v, f in lookup.items()]
        hq.heapify(item_with_freq)
        
        rslt = []
        for i in range(k):
            _, item =  hq.heappop(item_with_freq)
            rslt.append(item)

        return rslt