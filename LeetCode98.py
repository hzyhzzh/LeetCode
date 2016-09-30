# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.result = []
        self.LVR(root)
        for i in range(0,len(result)-1):
            if( result[i] >= result[i+1]):
                return False
        return True

    def LVR(self, root):
        if(root == None):
            return
        LVR(root.left)
        self.result.append(root.val)
        LVR(root.right)
