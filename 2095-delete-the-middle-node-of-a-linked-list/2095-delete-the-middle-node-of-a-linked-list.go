/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func deleteMiddle(head *ListNode) *ListNode {
    if head == nil || head.Next == nil {
        return nil
    }

    slow, fast := head, head
    var prev *ListNode

    for fast != nil {
        fast = fast.Next
        if fast != nil {
            fast = fast.Next
            prev = slow
            slow = slow.Next
        }
    }   

    if prev != nil && prev.Next != nil {
        prev.Next = prev.Next.Next
    }

    return head
}