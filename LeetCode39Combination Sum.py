class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        for i in xrange(len(candidates)):
            tmp = candidates[i]
            element = []
            while(target>tmp)：
                find(candidates[i+1:len(candidates)],target - tmp,element)
                tmp +=tmp
                if(len(element)):
                    res.append(element)
        return res
    def find(self, list, target, element):
        
