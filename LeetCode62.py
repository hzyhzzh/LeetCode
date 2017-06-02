class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a=1
        b=1
        for i in range(n-1):
            a = a*(i+1)
        for j in range(m, m+n-1):
            b = b*j
        return b/a