class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        j = 3
        if(n == 1):
            return 1
        if (n == 2):
            return 2
        if(n == 3):
            return 3
        L1 = [1,2,3]
        index = [1,1,0]
        while(True):
            j+=1
            tmp = L1[j-2]
            min2 = L1[index[0]]*2
            min3 = L1[index[1]]*3
            min5 = L1[index[2]]*5
            min_number = min(min2,min3,min5)
            if(min_number == min2):
                index[0] += 1
            if(min_number == min3):
                index[1] +=1
            if(min_number == min5):
                index[2] +=1
            L1.append(min_number)
            if(j == n):
                return L1[j-1]
