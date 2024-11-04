class Node:
    def __init__(self, key, value, prev = None, next = None):
        self.key = key
        self.val = value
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.lookup = {}
        self.head = None
        self.tail = None
        self.cap = capacity

    def get(self, key: int) -> int:
        if key not in self.lookup:
            return -1
        
        curr = self.lookup[key]
        prev = curr.prev
        next = curr.next

        if curr == self.tail:
            self.tail = prev

        if prev != None:
            prev.next = next
        
        if next != None:
            next.prev = prev
        
        if self.head != None:
            self.head.prev = curr
        
        curr.next = self.head
        self.head = curr

        return curr.val

    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            node.val = value
            self.get(key)
            return
        
        if len(self.lookup) < self.cap:
            node = Node(key, value)
            self.lookup[key] = node
            node.next = self.head
            if self.head == None:
                self.head = node
                self.tail = node
                return 

            self.head.prev = node
            self.head = node

            return
        
        del self.lookup[self.tail.key]
        self.tail = self.tail.prev
        self.tail.next = None

        node = Node(key, value)
        self.lookup[key] = node
        node.next = self.head
        self.head.prev = node
        self.head = node
        



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)