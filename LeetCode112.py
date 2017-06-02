# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def hasPathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if(root == None):
            return False
        if (not root.left and not root.right and root.val == sum1):
            return True
        return self.hasPathSum(root.left,sum1-root.val) or self.hasPathSum(root.right,sum1-root.val)
