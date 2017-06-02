class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if (len(a) < len(b)):
            s = b
            b = a
            a = s
        along = int(a)
        bshort = int(b)
        i=0;j=0
        while(along / 10**i >0):
            i+=1
        while(bshort / 10**j >0):
            j+=1
        k = 1
        result = ""
        c= 0
        if(not j ):
            j=1
        if(not i ):
            i = 1
  
  
        while(k<=i):
            if(k<=j):
                result += str(((along % 10 + bshort % 10 + c)%2))
                c = ( along% 10 + bshort% 10 +c) / 2
                along = along / 10
                bshort = bshort / 10
            else:
                result +=str(((along % 10 + c)%2))
                c = ( along% 10 +c ) / 2
                along = along / 10
            k+=1
        if(c ==1):
                result += "1"
        return result[::-1]
        