class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        n = len(s)
        res = ['']* n
        if(numRows == 1):
            return s
        if( not n ):
            return res

        start = -1
        #array = [ ['']*(n/(2*numRows-2)*(numRows-1)+ numRows) for i in range(numRows)]
        for i in xrange(numRows):
            for j in range(i,n)[::2*numRows-2]:
                start = start +1
                res[start] = s[j]
                if(i !=0 and i != numRows-1  and j+ 2*numRows-2-2*i <n):
                    start = start +1
                    res[start] = s[j+ 2*numRows-2-2*i]
                if(j+2*numRows-2 >= n):
                    continue

        s =''.join(res)
        return s
