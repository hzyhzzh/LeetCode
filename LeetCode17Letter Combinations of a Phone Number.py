class Solution(object):
    dict1 = {'1':['*'], '2':['a','b','c'], '3':['d','e','f'],
    	'4':['g','h','i'],'5':['j','k','l'],'6':['m','n','o'],
    	'7':['p','q','r','s'],'8':['t','u','v'],'9':['w','x','y','z'],'0':[' ']	}
    res = []
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if(not len(digits)):
            return self.res
        ans = ""
    	self.dfs(ans,digits,0,len(digits))
    	return self.res
    	
    def dfs(self,ans,digits,current_level,level):
        for i in xrange(len(self.dict1[digits[current_level]])):
        	ans1 =ans
        	ans1 += self.dict1[digits[current_level]][i]
        	if(current_level <level-1):
        	    self.dfs(ans1,digits,current_level+1,level)
        	else:
        	    self.res.append(ans1)
        	
        	
    
    	
    	
    	
    				