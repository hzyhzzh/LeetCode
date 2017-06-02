class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs) == 0):
            return ""
        result = ""
        if(len(strs) == 1):
            return strs[0]
        prefix = 0
        while(True):
            for i in range(1, len(strs)):
                if( prefix >= len(strs[0]) or prefix >= len(strs[i]) or strs[0][prefix] != strs[i][prefix]):
                    return result
            result = result + strs[0][prefix]
            prefix = prefix + 1

        return result


            
