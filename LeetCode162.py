class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if(len(nums) == 1 or (i == 0 and nums[0] > nums[1])):
                return 0
            elif(i == len(nums) - 1 and nums[i] > nums[i-1]):
                return i
            elif(nums[i] > nums[i-1] and nums[i] > nums[i+1]):
                return i
