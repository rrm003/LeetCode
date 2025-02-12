# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if l1 == None: return l2
        if l2 == None: return l1
        
        rslt_head = None
        rslt = None
        carry = 0
        while l1 != None and l2 != None:
            sum = ((l1.val + l2.val + carry) % 10)
            carry =  (l1.val + l2.val + carry) // 10
            l1 = l1.next
            l2 = l2.next
            if rslt == None:
                rslt_head = ListNode(sum)
                rslt = rslt_head
            else:
                rslt.next = ListNode(sum)
                rslt = rslt.next
        
        while l1 != None:
            sum = ((l1.val + carry) % 10) 
            carry = (l1.val + carry) // 10
            l1 = l1.next
            rslt.next = ListNode(sum)
            rslt = rslt.next

        while l2 != None:
            sum = ((l2.val + carry) % 10)
            carry = (l2.val + carry )// 10
            l2 = l2.next
            rslt.next = ListNode(sum)
            rslt = rslt.next

        if carry > 0 :
            rslt.next = ListNode(carry)
            rslt = rslt.next

        return rslt_head