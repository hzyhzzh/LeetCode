class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        result = [0]
        if(n ==0):
            return result
        
        for i in range(0,n):
            tmp = result[:]
            result.reverse()
            print tmp
            for j in range(len(result)):
                result[j] += 2**i
            result = tmp[:] + result[:]

        return result