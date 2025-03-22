# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq as hq

class HeapNode:
    def __init__(self, node):
        self.node = node
    
    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue = []
        l = len(lists)

        for head in lists:
            if head:
                hq.heappush(queue, HeapNode(head))
        
        if not queue : return

        node = hq.heappop(queue)
        if node.node.next:
            hq.heappush(queue, HeapNode(node.node.next))

        head = ListNode(node.node.val)
        temp = head

        while queue:
            node = hq.heappop(queue)
            temp.next = ListNode(node.node.val)
            temp = temp.next

            if node.node.next:
                hq.heappush(queue, HeapNode(node.node.next))
        
        return head