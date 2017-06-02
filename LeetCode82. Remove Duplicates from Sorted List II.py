# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head == None):
            return None
        if(head.next == None):
            return head
        result = ListNode(-1)
        tag = result
        now = head.val
        if(now != head.next.val):
            tmp = ListNode(now)
            tag.next = tmp
            tag = tmp
        pre = now
        head = head.next
        while(head.next!=None):
            if (pre != head.val and head.val != head.next.val):
                tmp = ListNode(head.val)
                tag.next = tmp
                tag = tmp
                
            pre = head.val
            head = head.next
        if(pre != head.val):
            tmp = ListNode(head.val)
            tag.next = tmp
            tag = tmp
            
        return result.next
            
        