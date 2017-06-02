# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = 0
        num2 = 0
        digit = 0
        while(l1 != None):
            num1 =  num1 + l1.val*10**digit
            l1 = l1.next
            digit = digit +1
        digit = 0
        while(l2 !=None):
            num2 = num2 +l2.val*10**digit
            l2 = l2.next
            digit = digit +1
        num1 = num2 + num1
        now = ListNode(0)
        result = now
        if(num1 == 0):
            return result
        while(num1 != 0):
            now.next = ListNode(num1 % 10)
            num1 = num1 / 10
            now = now.next
        return result.next
