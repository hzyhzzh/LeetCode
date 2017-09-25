class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = ""
        begin = 0
        end = len(s)-1
        while(begin < end):
            while(s[begin].lower() not in "abcdefghijklmnopqrstuvwxyz0123456789"):
                begin +=1
                if(begin >= len(s)):
                    break
            while(s[end].lower() not in "abcdefghijklmnopqrstuvwxyz0123456789"):
                end -=1
                if(end < 0):
                    break
            if(begin <  end and s[begin].lower() != s[end].lower()):
                return False
            begin +=1
            end -= 1
                
        return True
            
        