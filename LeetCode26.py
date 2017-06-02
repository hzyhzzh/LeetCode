class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if(len(nums) == 0):
            return 0
        count = 1
        now = nums[0]
        dup_pos = -1
        for i in range(1,len(nums)):
            if(nums[i] != now):
                now = nums[i]
                if(dup_pos >= 0):
                    nums[dup_pos] = nums[i]
                count = count+1
            elif(nums[i] == now):
                dup_pos = i
        return count
