# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        prev = head
        current = head
        if(not prev):return head
        while(current):
            if(head.val == val):
                head = head.next
                prev = head
                current = prev
            elif(current.val == val and current.next is not None):
                prev.next = current.next
                current = current.next
            elif(current.val == val and current.next == None):
                prev.next = None
                current = current.next
            else:
                prev = current
                current = current.next
        return head
