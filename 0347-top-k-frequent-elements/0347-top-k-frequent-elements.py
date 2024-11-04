class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lookup = {}

        for x in nums:
            if x not in lookup:
                lookup[x] = 0
        
            lookup[x] += 1
        
        val_freq = [[x, lookup[x]] for x in lookup]
        val_freq.sort(key=lambda x:[-x[1]])

        print(val_freq[:k])
        rslt = []
        for v in val_freq[:k]:
            rslt.append(v[0])

        return rslt