class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = None
        length = len(s)
        dp = [ [False]*length for i in range(length)]
        #print(dp)
        for i in range(0,length)[::-1]:
            for j in range(i,length):
                dp[i][j] = (s[i]== s[j] and ( j - i <3 or dp[i+1][j-1]))

                if(dp[i][j] and ( result == None or j-i+1> len(result))):
                    result = s[i:j+1]


        return result
