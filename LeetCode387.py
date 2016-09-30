class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        i =0
        tmp = []
        if not s :
            return -1
        for ch in s:
            if( s.find(ch,i+1,len(s)) == -1 and ch not in tmp):
                return i
            tmp.append(s[i])
            i += 1
        return -1
