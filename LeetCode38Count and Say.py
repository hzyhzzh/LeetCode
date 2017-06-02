class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """,
        res=["1","11","21","1211","111221"]
        if(n<=5):
            return res[n-1]
        tmp = res[4]
        for i in range(0,n-5):
            count = 1
            say = ""
            for j in xrange(len(tmp)-1):
                if(tmp[j] == tmp[j+1] and j+1 == len(tmp)-1):
                    say = say + str(count+1) +tmp[j]
                if(tmp[j] != tmp[j+1]):
                    say = say + str(count) +tmp[j]
                    count = 1
                else:
                    count += 1
            if(tmp[len(tmp)-1] != tmp[len(tmp)-2]):
                say = say + '1' +tmp[len(tmp)-1]
            tmp =say
        return tmp
