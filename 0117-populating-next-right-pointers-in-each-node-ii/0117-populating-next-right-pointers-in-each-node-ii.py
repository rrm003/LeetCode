"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root == None:
            return None
        
        level = 0 
        queue = [(root, level)]
        lookup = {}

        while len(queue) > 0:
            curr, lvl = queue[0]
            queue = queue[1:]

            if curr == None:
                continue

            if lvl not in lookup:
                lookup[lvl] = []
            
            lookup[lvl].append(curr)

            queue.append((curr.left, lvl+1))
            queue.append((curr.right, lvl+1))

        for key, val in lookup.items():
            i = 0
            while i + 1 < len(val):
                val[i].next = val[i+1] 
                i+=1
            
        return root