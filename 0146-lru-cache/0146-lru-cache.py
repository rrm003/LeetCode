class Node:
    def __init__(self, key, val):
        self.key = key
        self.value = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.lookup = {}
        self.head = Node(-1, 0)
        self.tail = Node(-1, 0)
        self.head.next = self.tail
        self.tail.prev = self.head 
        self.size = capacity

    def get(self, key: int) -> int:
        if key not in self.lookup: return -1
        node = self.lookup[key]
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

        f = self.head.next
        f.prev = node
        node.next = f

        self.head.next = node
        node.prev = self.head
        
        return node.value


    def put(self, key: int, value: int) -> None:
        if key in self.lookup:
            node = self.lookup[key]
            node.value = value

            prev, next = node.prev, node.next
            prev.next = next
            next.prev = prev

            f = self.head.next
            f.prev = node
            node.next = f

            self.head.next = node
            node.prev = self.head

            return node.value
        
        if len(self.lookup) == self.size:
            p = self.tail.prev
            del self.lookup[p.key]
            p.prev.next = p.next
            p.next.prev = p.prev
        
        node = Node(key, value)
        self.lookup[key] = node

        f = self.head.next
        f.prev = node
        node.next = f

        self.head.next = node
        node.prev = self.head

        return


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# (4, 1) (2, 3) 