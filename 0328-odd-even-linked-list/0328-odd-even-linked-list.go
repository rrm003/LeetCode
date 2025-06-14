/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func oddEvenList(head *ListNode) *ListNode {
    if head == nil {
        return nil
    }
    
    var oHead, oTemp *ListNode
    var eHead, eTemp *ListNode

    temp := head
    for temp != nil {
        // odd 
        if oHead == nil {
            oHead = temp
            oTemp = oHead
            temp = temp.Next
            oTemp.Next = nil
        }else {
            oTemp.Next = temp
            oTemp = oTemp.Next
            temp = temp.Next
            oTemp.Next = nil
        }

        if temp == nil {
            break
        }

        // even        
        if eHead == nil {
            eHead = temp
            eTemp = eHead
            temp = temp.Next
            eTemp.Next = nil
        }else {
            eTemp.Next = temp
            eTemp = eTemp.Next
            temp = temp.Next
            eTemp.Next = nil
        }
    }

    oTemp.Next = eHead
    return oHead
}