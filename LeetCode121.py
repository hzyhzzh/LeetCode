class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        maxp = 0
        subed = prices[0]
        if(not len(prices)):
            return
        for i in range(1,len(prices)):
            if(prices[i] < subed):
                subed = prices[i]
            else:
                maxp = max(maxp, prices[i] - subed)

        return maxp
