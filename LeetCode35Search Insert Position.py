class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if(target =< nums[0]):
            return 0
        if(target > nums[len(nums)-1]):
            return len(nums)
        for i in xrange(len(nums)-1):
            if(target>nums[i] and nums[i+1]>=target):
                return i
