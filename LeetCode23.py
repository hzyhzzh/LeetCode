# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0: return
        elif len(lists) == 1: return lists[0]
        else:
            mid = (len(lists) - 1) / 2
            l1 = self.mergeKLists(lists[0:mid+1])
            l2 = self.mergeKLists(lists[mid+1 : len(lists)])
            return self.merge_couple(l1, l2)

    def merge_couple(self, ListNode1, ListNode2):
        i =0
        j =0
        start = ListNode(-1)
        current = start
        while(ListNode1 != None or ListNode2 != None ):
            node = ListNode(-1)     
            if(ListNode2 == None):
                node.val = ListNode1.val
                ListNode1 = ListNode1.next
            elif(ListNode1 ==  None):
                node.val = ListNode2.val
                ListNode2 = ListNode2.next
            elif( ListNode1.val < ListNode2.val or ListNode2 == None ):
                node.val = ListNode1.val
                ListNode1 = ListNode1.next
            else:
                node.val = ListNode2.val
                ListNode2 = ListNode2.next
            current.next = node
            current =current.next
        return start.next
