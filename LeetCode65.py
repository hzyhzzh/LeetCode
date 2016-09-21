class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s =s.strip()
        if(' ' in s):
            return False

        elif( 'e' in s):
            index = s.index('e')
            before = s[:index]
            last = s[index+1:len(s)]

            try:
                int(last)
            except(ValueError):
                return False
            if(before.isdigit() ):
                return True
            elif(not before.isdigit()):
                try:
                    float(before)
                    return True
                except(ValueError):
                    return False
            else:
                return False

        elif('.' in s):
            try:
                float(s)
                return True
            except(ValueError):
                return False
        else:
            try:
                int(s)
                return True
            except(ValueError):
                return False
