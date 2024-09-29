class Heap:
    def __init__(self):
        self.heap = []
    
    def insert(self, val: int):
        self.heap.append(val)
        i = len(self.heap) - 1
        root = i // 2

        while root >= 0 and self.heap[root] < self.heap[i]:
            self.heap[root], self.heap[i] = self.heap[i], self.heap[root]
            i = root
            root = i // 2
            
    def delete(self) -> int:
        if len(self.heap) == 0: return -1

        l = len(self.heap)
        rslt = self.heap[0]
        self.heap[0] = self.heap[l-1]
        self.heap = self.heap[:l-1]

        root = 0
        left = root * 2
        right = root * 2 + 1

        while right < l-1 and (self.heap[root] < self.heap[left] or self.heap[root] < self.heap[right]):
            t = root
            if self.heap[right] < self.heap[left]:
                t = left
            else:
                t = right

            self.heap[root], self.heap[t] = self.heap[t], self.heap[root]
            root = t
            left = root * 2
            right = root * 2 + 1
        
        return rslt


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = Heap()
        freq = {}
        for x in nums:
            if x not in freq:
                freq[x] = 0
            freq[x] += 1

        for x in set(nums):
            h.insert(x)
        
        # k = k % len(nums)
        rslt = 0
        f = 0
        while f < k:
            v = h.delete()
            f += freq[v]
            if f >= k : return v
            rslt = v
        
        return rslt
        