class Node:
    def __init__(self, key: int, value: int, left = None, right = None):
        self.key = key 
        self.value = value 
        self.next = left
        self.prev = right

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = None
        self.tail = None
        self.lookup = {}
    
    def log(self):
        pass
        # print("------------")
        # print("lookup")
        # for x, v in self.lookup.items():
        #     print(f"\t{x}:({v.key}:{v.value})")
        # print("------------")
        # print("list")
        # s = ""
        # tt = self.head
        # while tt!=None:
        #     s =  s + "->" + str(tt.key)
        #     tt = tt.next
        # print(s)

    def get(self, key: int) -> int:
        # print("------------")
        # print("get", key)
        if key not in self.lookup:
            # self.log()
            return -1
        
        curr = self.lookup[key] 
        if curr == self.head:
            # self.log()
            return curr.value
        
        if curr == self.tail:
            self.tail = curr.prev

        p = curr.prev
        curr.prev = None

        n = curr.next
        curr.next = self.head
        
        self.head.prev = curr
        self.head = curr
        
        p.next = n
        if n:
            n.prev = p
        
        
        # self.log()
        return curr.value

    def put(self, key: int, value: int) -> None:
        # print("------------")
        # print("put", key, value)
        if self.head == None:
            # print("\t head is none")
            self.head = Node(key, value)
            self.tail = self.head
            self.lookup[key] = self.head
            # self.log()
            return
        
        if key in self.lookup:
            # print("\t key exists")
            curr = self.lookup[key]
            curr.value = value
            if curr == self.head:
                # self.log()
                return
            if curr == self.tail:
                self.tail= curr.prev

            p = curr.prev
            n = curr.next
        
            p.next = n
            if n:
                n.prev = p

            curr.prev = None
            curr.next = self.head
            self.head.prev = curr
            self.head = curr
            # self.log()
            return

        # print("\t key not found")
        curr = Node(key, value)
        curr.next = self.head
        self.head.prev = curr
        self.head = curr

        if len(self.lookup) == self.capacity:
            del self.lookup[self.tail.key]

            pt = self.tail.prev
            if pt != None:
                pt.next = None
            self.tail = pt

        self.lookup[key] = curr
        # self.log()

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)