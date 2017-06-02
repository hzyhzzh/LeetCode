class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        start = 0
        for i in range(0,len(nums)-1):
            flag = True
            if (nums[i]==0):
                for j in range(0,i):
                    if(nums[j] > i-j):
                        flag =False
                        break
                if(flag):
                    return False
            flag = True
        return True
