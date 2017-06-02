class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length= len(nums)
        result = nums[0]
        local = nums[0]
        for i in xrange(length):
            local = max(A[i],local+A[i])
            result = max(result,local)
        return result
