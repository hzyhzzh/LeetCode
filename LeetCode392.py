class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        index = -1
        i = 0
        while(i < len(s)):
            index = t.find(s[i],index+1)
            if(index ==  -1):
                return False
            i += 1
        if(i == len(s)):
            return True
        return False
