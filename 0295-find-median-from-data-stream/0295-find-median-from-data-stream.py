import heapq as hq

class MedianFinder:
    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        hq.heappush(self.left, -num)
        hq.heappush(self.right, -heappop(self.left))
        if len(self.left) < len(self.right):
            hq.heappush(self.left, -hq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.right) == len(self.left) and self.right:
            return (self.right[0] - self.left[0]) / 2
        elif len(self.left) > len(self.right): 
            return -self.left[0]
        
        return 0

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()