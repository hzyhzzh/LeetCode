class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 1
        for i in range(1,n/2+1):
            fenzi = 1
            fenmu = 1
            for j in range(1, i+1):
                fenzi = fenzi*j
            for k in range(n-2*i+1, n-i+1):
                fenmu = fenmu*k
            result = fenmu / fenzi + result
        return result
