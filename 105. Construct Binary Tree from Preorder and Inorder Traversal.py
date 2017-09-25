# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if(preorder.__len__() == 0):
            return []
        root = TreeNode(0)
        self.construct(root,preorder,inorder)
        
        return root
        
        
    def construct(self,root,preorder,inorder):
        if(preorder.__len__()==0 or inorder.__len__()==0):
            return 
        mid = inorder.index(preorder[0])
        lpreorder = preorder[1:mid+1]
        rpreorder = preorder[mid+1:]
        linorder = inorder[:mid]
        rinorder = inorder[mid+1:]
        root.val = preorder[0]
        if(lpreorder.__len__()>0):
            root.left = TreeNode(0)
        if(rpreorder.__len__()>0):
            root.right = TreeNode(0)
        self.construct(root.left,lpreorder,linorder)
        self.construct(root.right,rpreorder,rinorder)