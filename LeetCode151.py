class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """

        wordlist = s.split()
        if len(wordlist) == 0:
            return ""
        wordlist = wordlist[::-1]
        result = ""
        for i in range(len(wordlist)):
            if i != len(wordlist)-1:
                result += wordlist[i] + ' '
            else:
                result += wordlist[i]
        return result
