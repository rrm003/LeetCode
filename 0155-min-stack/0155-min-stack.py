class MinStack:
    stack = []
    min = 0
    
    def __init__(self):
        self.stack = []
        self.min = 0

    def push(self, val: int) -> None: 
        l = len(self.stack)
        if l > 0:
            if val < self.stack[self.min]:
                self.min = l
        self.stack.append(val)

    def pop(self) -> None:
        l = len(self.stack)
        if l>0:
            i=0
            m = self.stack[0]
            while i<l-1:
                # print("pop :", i, m, self.stack[i], self.stack, self.min)
                if m >= self.stack[i]:
                    self.min = i
                    m = self.stack[i]
                i += 1

            t = self.stack[l-1]
            self.stack = self.stack[:l-1]
            return t

    def top(self) -> int:
        l = len(self.stack)
        if len(self.stack) >0:
            return self.stack[l-1]

    def getMin(self) -> int:
        if len(self.stack) >0:
            return self.stack[self.min]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()