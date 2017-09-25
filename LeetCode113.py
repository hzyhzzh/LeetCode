# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import copy
class Solution(object):
    def __init__(self):
        """Constructor"""
        self.result = []
    def pathSum(self, root, sum1):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        
        if(root == None):
            return self.result
        self.Dfs(root,sum1,[])
        return self.result
        
    def Dfs(self,root,sum1,ele):
        ele.append(root.val)
        if(root.left== None and root.right==None):
            if(sum1 == root.val):
                self.result.append(copy.copy(ele))
        if(root.left!= None): 
            self.Dfs(root.left, sum1-root.val, ele)
        if(root.right!= None):
            self.Dfs(root.right, sum1-root.val, ele)
        ele.pop()
        
            