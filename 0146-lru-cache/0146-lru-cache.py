class Node :
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = None
        self.tail = None
        self.lookup = {}
    
    def print(self):
        temp = self.head
        while temp:
            print(f"({temp.key} : {temp.val})", end = " ")
            temp = temp.next
        print()

    def get(self, key: int) -> int:
        if key not in self.lookup: return -1

        node = self.lookup[key]
        if node == self.head: return node.val
    
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        
        if node == self.tail:
            self.tail = self.tail.prev
            if self.tail: self.tail.next = None
        
        node.next = self.head
        node.prev = None
        if self.head: self.head.prev = node
        self.head = node

        return node.val

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.lookup:
            node = self.lookup[key]
            node.val = value
            self.get(node.key)
            return
        
        node = Node(key, value)
        self.lookup[key] = node

        node.next = self.head
        if self.head: self.head.prev = node
        self.head = node
        if not self.tail: self.tail = self.head
        
        # capacity check
        if len(self.lookup)>self.cap:
            if self.tail:
                print(self.tail.key, self.tail.val)
                del self.lookup[self.tail.key]
                self.tail = self.tail.prev
                if self.tail:
                    self.tail.next = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)