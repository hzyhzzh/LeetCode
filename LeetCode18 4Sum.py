class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        res = []
        j = len(nums) - 1
        for k in xrange(0,j-2):
            if(nums[k] == nums[k-1] and k>0):
                continue
            for i in range(k+1, j-1):
                if(nums[i] == nums[i-1] and i>k+1):
                    continue
                begin= i+1
                end = j
                while(begin < end):
                    if(nums[i] + nums[begin] + nums[end] +nums[k] == target):
                        res.append([nums[k],nums[i] ,nums[begin] , nums[end]])
                        while(begin < end and nums[begin] == nums[begin+1]):
                            begin +=1
                        begin +=1
                        while(begin < end and nums[end] == nums[end-1]):
                            end -=1
                        end -=1
                    elif(nums[i] + nums[begin] + nums[end] <target - nums[k]):
                        begin+=1
                    elif(nums[i] + nums[begin] + nums[end] >target - nums[k]):
                        end-=1
        return res
