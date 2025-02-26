# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq as hq

class HeapNode:  
    def __init__(self, node: 'ListNode'):
        self.node = node
    
    def __lt__(self, other: 'HeapNode'):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        elements = []
        for ll in lists:
            if ll :
                hq.heappush(elements, HeapNode(ll))

        rslt = None
        temp = None
        while elements:
            curr = hq.heappop(elements)
            if curr.node.next:
                hq.heappush(elements, HeapNode(curr.node.next))

            if rslt == None:
                rslt = curr.node
                temp = rslt
                continue

            temp.next = curr.node
            temp = temp.next
        
        return rslt