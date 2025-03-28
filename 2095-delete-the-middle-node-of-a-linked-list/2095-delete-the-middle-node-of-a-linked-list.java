/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;
        ListNode prev = null;

        if (fast == null) {return null;}
        if (fast.next == null) {return null;}
        
        while (fast != null) {
            fast = fast.next;
            if (fast == null) {
               break;
            }

            fast = fast.next;
            prev = slow;
            slow = slow.next;
        }

        if (prev!=null) {
            if (prev.next!= null){
                prev.next = prev.next.next;
            }else{
                prev.next = null;
            }
        }

        return head;
    }
}