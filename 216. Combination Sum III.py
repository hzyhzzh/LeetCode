class Solution(object):
    result = []
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        ele = []
        self.backtracking(1,k,n,ele)
        
    def backtracking(self, level, k,s,ele):
        for i in xrange(1,10):
            if(level == k and i == s and i not in ele):
                ele.append(i)
                tmp = ele[:]
                self.result.append(tmp)
                ele = []
            elif(level < k and i <s and i not in ele):
                level += 1
                ele.append(i)
                s = s-i
                self.backtracking(level, k,s,ele)
            else:
                break
        