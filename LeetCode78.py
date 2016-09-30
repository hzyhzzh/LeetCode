import itertools
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        for num in nums:
            tmp = []
            tmp.appen(num)
            result.append(tmp)
        if(len(nums) >= 2):
            for i in range(2,len(nums)+1)[::-1]:
                iter = itertools.combinations(nums,i)
                for element in list(iter):
                    result.append(element)


        tmp = []
        result.append(tmp)
        return result
