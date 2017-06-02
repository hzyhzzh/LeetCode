# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        less = ListNode(0)
        bigger = ListNode(0)
        ref = less
        start = bigger
        
        while(head is not None):
            if(head.val >=x):
               tmp = ListNode(head.val)
               bigger.next = tmp
               bigger = bigger.next
            else:
               tmp = ListNode(head.val)
               less.next = tmp
               less = less.next
            head = head.next
        
        less.next = start.next
       
        return ref.next
                
        
        