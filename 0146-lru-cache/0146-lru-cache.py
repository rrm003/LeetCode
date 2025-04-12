class Node:
    def __init__ (self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None 


class LRUCache:

    def __init__(self, capacity: int):
        self.Size = capacity
        self.Head = Node(-1, -1)
        self.Tail = Node(-1, -1)
        self.Head.next = self.Tail
        self.Tail.prev = self.Head
        self.Lookup = {}

    def get(self, key: int) -> int:
        if key not in self.Lookup:
            return -1
        
        node = self.Lookup[key]
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

        first = self.Head.next 
        self.Head.next = node 
        node.prev = self.Head
        node.next = first
        first.prev = node

        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.Lookup:
            self.Lookup[key].val = value
            self.get(key)
            return
        
        if len(self.Lookup) == self.Size:
            evict = self.Tail.prev
            prev = evict.prev
            prev.next = self.Tail
            self.Tail.prev = prev
            del self.Lookup[evict.key]
        
        new_node = Node(key, value)
        self.Lookup[key] = new_node
        next = self.Head.next
        self.Head.next = new_node
        new_node.prev = self.Head 
        new_node.next = next
        next.prev = new_node



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)