class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = nums[1] + nums[0]+ nums[len(nums)-1]
        j = len(nums) - 1
        for i in range(0, j-1):
            if(nums[i] == nums[i-1] and i>0):
                continue
            begin= i+1
            end = j
            while(begin < end):
                if(abs(nums[i] + nums[begin] + nums[end] - target) <= abs(res - target)):
                    res = nums[i] + nums[begin] + nums[end] 
                if( nums[i] + nums[begin] + nums[end] - target <0):
                    begin+=1
                elif(nums[i] + nums[begin] + nums[end] - target >0):
                    end-=1
                elif( nums[i] + nums[begin] + nums[end] - target ==0):
                    return res
        return res