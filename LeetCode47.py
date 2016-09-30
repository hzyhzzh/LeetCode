from itertools import permutations
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        iter = itertools.permutations(nums,len(nums))


        return list(set((list(iter))))
