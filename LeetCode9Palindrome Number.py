class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        i = 1
        j =10
        if(x<0):
            return False

        while(x/j >=1):
            j = j*10
            i = i + 1
        if(i == 1):
            return True
        for j in range(1,i/2+1):
            if( x%(10**j)/ 10**(j-1) != x/(10**(i-j)) %10 ):
                return False
        return True

        
