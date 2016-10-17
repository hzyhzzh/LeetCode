class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if(k> len(nums)):
            k = k % len(nums)
        b= nums + nums
        a = b[len(b)/2 - k: len(b)-k]
        for i in range(len(nums)):
            nums[i] = a[i]
