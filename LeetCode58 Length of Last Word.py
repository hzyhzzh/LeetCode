class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        leng = len(s)
        while(s[leng-1]==' '):
            leng-=1
        for i in range(0,leng)[::-1]:
            if(s[i] == ' '):
                break
            count +=1
        return count
