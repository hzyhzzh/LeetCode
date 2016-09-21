class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return 0
        maxnumber = nums[0]
        minnumber = nums[0]

        for i in nums:
            if (i < minnumber):
                minnumber = i
            elif(i > maxnumber):
                maxnumber = i
                ##len of bucket
        length = (maxnumber - minnumber)/len(nums) + 1
        bucket = [-1]*len(nums)
        for num in nums:
            i = (num - minnumber)/length
            if(bucket[i] == -1):
                bucket[i] =[num,num]
            else:
                if(bucket[i][0] > num ):
                    bucket[i][0] =num
                elif(bucket[i][1] <num):
                    bucket[i][1] = num

        gap = -1
        prev = 0
        for i in range( 1, (maxnumber - minnumber)/length + 1 ):
            while(bucket[i] == -1):
                i+=1
            prev = i - 1
            while(bucket[prev] == -1):
                prev += 1
            gap = max(gap, bucket[i][1] - bucket[prev][0]);

        return gap
