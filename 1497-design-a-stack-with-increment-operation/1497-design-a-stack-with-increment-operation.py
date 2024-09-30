class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == self.size:
            return

        self.stack.append(x)

    def pop(self) -> int:
        l = len(self.stack)
        if l == 0 : return -1
        
        top = self.stack[l-1]
        self.stack = self.stack[:l-1]
        return top
        

    def increment(self, k: int, val: int) -> None:
        l = len(self.stack)
        till = min(l, k)

        i = 0
        while i < till:
            self.stack[i] += val
            i+=1
        
 

# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)