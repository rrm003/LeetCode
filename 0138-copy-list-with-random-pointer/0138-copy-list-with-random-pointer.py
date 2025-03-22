"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head : return 
        
        lookup = {}
        temp = head
        while temp :
            lookup[temp] = Node(temp.val)
            temp = temp.next
        
        temp = head
        while temp:
            if temp.next:
                lookup[temp].next = lookup[temp.next]
            
            if temp.random:
                lookup[temp].random = lookup[temp.random]
            
            temp = temp.next

        return lookup[head]