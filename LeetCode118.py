class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            element = [1]*(i+1)
            if(i >= 2):
                for j in range(1, i):
                    element[j] = result[i-1][j-1] + result[i-1][j]
            result.append(element)

        return result
