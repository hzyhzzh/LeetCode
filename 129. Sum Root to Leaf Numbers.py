# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        result = []
        if(root ==  None):
            return 0
        self.getleafnumber(root, root.val,result)
        sum = 0
        print result
        for each in result:
            sum += each
        return sum
    def getleafnumber(self, root, num,result):
        if(root.left == None and root.right == None):
            result.append(num)
            return 
        if(root.left!= None):
            temp = num*10 + root.left.val
            self.getleafnumber(root.left,temp ,result)
        if(root.right != None):
            temp  = num*10 + root.right.val
            self.getleafnumber(root.right,temp ,result)