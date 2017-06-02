class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        first_odd = 0
        tested = []
        if_odd = False
        for char in s:
            if(char not in tested):
                result += s.count(char)
            else:
                continue
            if(s.count(char) % 2 == 1 and char not in tested):
                first_odd += 1
                if_odd = True
            tested.append(char)

        if(if_odd):
            result = result- (first_odd - 1)
        return result
