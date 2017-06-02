class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        res = []
		find = False
		for i in xrange(len(nums)):
			if(nums[i] == target):
				if(len(res) == 0):
					res=[i,i]
				else:
					res[1] = i
				find = True
		if(find == False):
			res=[-1,-1]
		return res