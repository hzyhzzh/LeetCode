class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        max = -1
        if(len(nums) == 0):
            return False
        if(len(nums) == 1):
            return nums[0]==target
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                max = i 
        if(max == -1):#not rotated
            for i in range(0,len(nums)):
                if nums[i] ==  target:
                    return True
            return False
            
        if target >= nums[0] and target <= nums[max]:
            for i in range(0,max+1):
                if nums[i] ==  target:
                    return True
            return False
        if target >= nums[max+1] and target <= nums[len(nums) - 1]:
            for i in range(max+1, len(nums)):
                if nums[i] ==  target:
                    return True
            return False
                
        return False
            