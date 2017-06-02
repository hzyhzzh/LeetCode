class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if(not x):
            return 0
        flag = True
        if(x < 0):
            flag = False
        x= abs(x)
        res = []
        result =0
        while(x!=0):
            res.append(x % 10)
            x = x/10
        for i in range(0,len(res))[::-1]:
            if(flag):
                result = result + res[i]*10**(len(res)-1 - i)
            else:
                result = result - res[i]*10**(len(res)-1 - i)
        if(abs(result) >2**31):
            return 0
        return result
        
