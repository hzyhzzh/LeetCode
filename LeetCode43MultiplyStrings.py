class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if(num1.__len__() ==1):
            if(int(num1)==0):
                return "0"
        if(num2.__len__() ==1):
            if(int(num2)==0):
                return "0"
        longer = num1
        shorter = num2
        if(len(num1)<len(num2)):
            longer = num2
            shorter = num1
        res = "0"
        count = 1
        count_zero = 0
        str_store = []
        while(count <= len(shorter)):
            down = int(shorter[len(shorter)-count])
            carry = 0
            ele = "0"*count_zero
            for i in range(0,len(longer))[::-1]:
                up = int(longer[i])
                back = (up*down +carry)%10
                carry = (up*down +carry)/10
                ele += str(back)
            if(carry > 0):
                ele += str(carry)
            count_zero += 1
            str_store.append(ele)
            count +=1
        for i in xrange(str_store.__len__()):
            tmp = str_store[i]
            if(res.__len__() < tmp.__len__()):
                tmp1 = res
                res = tmp
                tmp = tmp1
            carry = 0
            element = ""
            for i in xrange(tmp.__len__()):
                bit = str( (int(tmp[i])+ int(res[i]) +carry) % 10)
                carry = (int(tmp[i])+ int(res[i]) +carry)/10
                element +=bit
            if(res.__len__() > tmp.__len__() ):
                for j in range(tmp.__len__(), res.__len__()):
                    element += str((int(res[j])+carry) % 10)
                    carry = (int(res[j])+carry) / 10
            if(carry > 0):
                element += str(carry)
            res = element
        return res[::-1]



                
