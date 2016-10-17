/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode deleteDuplicates(ListNode head) {
        ListNode tmp = head;
        if(tmp ==  null)return head;
        while(tmp.next!= null){
          if(tmp.next.val == tmp.val){
            ListNode tag = tmp;
            while(tmp.next !=null && tmp.val == tag.val ){
              tmp = tmp.next;
            }
            if(tag.val == tmp.val){tag.next = null;break;}
            else tag.next = tmp;

          }
          else  tmp = tmp.next;

        }
        return head;
    }
}
