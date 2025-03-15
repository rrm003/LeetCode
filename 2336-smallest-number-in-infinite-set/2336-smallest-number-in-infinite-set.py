import heapq as hq

class SmallestInfiniteSet:

    def __init__(self):
        self.arr = [i for i in range(1,1001)]
        hq.heapify(self.arr)

    def popSmallest(self) -> int:
        rslt = hq.heappop(self.arr)
        return rslt

    def addBack(self, num: int) -> None:
        if num not in self.arr:
            hq.heappush(self.arr, num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)