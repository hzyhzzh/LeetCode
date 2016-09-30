class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i = 0
        while(True):
            if(s[:len(s)-i] == s[len(s)-i-1::-1]):
                break
            i += 1
            if(i == len(s)):
                break
        print i
        s = s[len(s) - 1:len(s) - 1-j:-1] + s
        return s
