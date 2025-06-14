/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func pairSum(head *ListNode) int {
    if head == nil {
        return 0
    }

    slow := head
    fast := head

    stack := []int{head.Val}
    for fast != nil {
        slow = slow.Next
        stack = append(stack, slow.Val)
        fast = fast.Next

        if fast != nil {
            fast = fast.Next
        }
    }

    stack = stack[:len(stack) - 1]

    rslt := 0
    for slow != nil && len(stack) > 0 {
        s := stack[len(stack) - 1] + slow.Val
        rslt = int(math.Max(float64(rslt), float64(s)))

        slow = slow.Next
        stack = stack[:len(stack)-1]
    }
   
    return rslt
}