class Node: 
    def __init__(self, data:int):
        self.data = data
        self.next = None
        self.prev = None 

class MyCircularQueue:

    def __init__(self, k: int):
        self.head = None
        self.tail = None
        self.size = k

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        self.size -= 1
        
        if self.head == None:
            self.head = Node(value)
            self.tail = self.head
            self.head.prev = self.tail 
            self.tail.next = self.head
            
        else:
            temp = Node(value)
            self.tail.next = temp
            temp.prev = self.tail
            self.tail = temp
            self.tail.next = self.head
            self.head.prev = self.tail
        
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        self.size += 1

        if self.head == self.tail : 
            self.head = None
            self.tail = None
            return True

        self.head = self.head.next
        self.head.prev = self.tail
        self.tail.next = self.head

        return True

    def Front(self) -> int:
        if self.head == None : return -1
        return self.head.data

    def Rear(self) -> int:
        if self.tail == None: return -1
        return self.tail.data

    def isEmpty(self) -> bool:
        return self.head == None
        

    def isFull(self) -> bool:
        return self.size == 0
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()