class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = []
        j = len(nums) - 1
        for i in range(0, j-1):
            if(nums[i] == nums[i-1] and i>0):
                continue
            begin= i+1
            end = j
            while(begin < end):
                if(nums[i] + nums[begin] + nums[end] == 0):
                    res.append([nums[i] ,nums[begin] , nums[end]])
                    while(begin < end and nums[begin] == nums[begin+1]):
                        begin +=1
                    begin +=1
                    while(begin < end and nums[end] == nums[end-1]):
                        end -=1
                    end -=1
                elif(nums[i] + nums[begin] + nums[end] <0):
                    begin+=1
                elif(nums[i] + nums[begin] + nums[end] >0):
                    end-=1
        return res
