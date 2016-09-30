# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.result = []
        self.traverse(root)
        if(len(self.result)):
            tmp = TreeNode(self.result[0])
            root = tmp
            for i in range( 1,len(self.result) ):
                tmp.right = TreeNode(self.result[i])
                print tmp.right.val
                tmp.left = None
                tmp = tmp.right

    def traverse(self, root):
        if(not root):
            return
        self.result.append(root.val)
        self.traverse(root.left)
        self.traverse(root.right)
