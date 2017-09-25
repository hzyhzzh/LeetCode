class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        s = 0
        e = len(numbers)-1
        while(numbers[s] + numbers[e]!= target):
            if(numbers[s] + numbers[e] > target):
                e-=1
            elif(numbers[s] + numbers[e] < target):
                s+=1
            
        result = [s+1,e+1]
        return result