class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        result =[]
        for token in tokens:
            if(token not in ["+","-","*","/"]):
                result.append(token)
            else:
                a2 = int(result.pop())
                a1 = int(result.pop())
                if(token == "+"):
                    result.append(str(a1+a2))
                elif(token == "-"):
                    result.append(str(a1-a2))
                elif(token == "*"):
                        result.append(str(a1*a2))
                elif(token == "/"):
                    result.append(str(a1/a2))
                    if((a1 < 0 and a2 >= 0) or (a1 >= 0 and a2 < 0) ):
                        result.pop()
                        result.append(str(-(-a1/a2)))
        return int(result[0])