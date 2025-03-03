import heapq as hq

class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        if not self.max_heap or num <= -self.max_heap[0]:
            hq.heappush(self.max_heap, -num)
        else:
            hq.heappush(self.min_heap, num)

        if len(self.max_heap) > len(self.min_heap) + 1:
            curr = hq.heappop(self.max_heap)
            hq.heappush(self.min_heap, -curr)
        elif len(self.min_heap) > len(self.max_heap) + 1:
            curr = hq.heappop(self.min_heap)
            hq.heappush(self.max_heap, -curr)
        
        return

    def findMedian(self) -> float:
        print(self.min_heap, self.max_heap)
        
        if not self.min_heap and not self.max_heap : return 0

        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] - self.max_heap[0]) / 2
        elif len(self.min_heap) < len(self.max_heap):
            return -self.max_heap[0]

        return self.min_heap[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()