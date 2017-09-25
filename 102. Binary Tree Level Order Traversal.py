# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    queue = []
    tree = []
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if(root==None):
            return []
        if(root!=None):
            self.queue.append(root)
        
        while(len(self.queue) > 0):
            node = self.queue[0]
            if(node == 'a'):
                self.tree.append(node)
                del self.queue[0]
                continue    
            if(node!='a'):
                self.tree.append(node.val)
            if(node.left!=None):
                self.queue.append(node.left)
            elif(node.left==None):
                self.queue.append('a')
            if(node.right != None):
                self.queue.append(node.right)
            elif(node.right== None):
                self.queue.append('a')
            del self.queue[0]
        result = []
        power = 0
        index = 0
        while(index < self.tree.__len__()):
            element = []
            for i in xrange(2**power):
                if(self.tree[index] != 'a'):
                    element.append(self.tree[index])
                index += 1
                if(index >= self.tree.__len__()):
                    break
            result.append(element)
            power += 1
        return result[:-1]
            
            