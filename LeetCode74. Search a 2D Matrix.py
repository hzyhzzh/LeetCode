class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m = len(matrix)
        if(not m ):
            return False
        n = len(matrix[0])
        if(not n ):
            return False
        for i in range(m):
            if( matrix[i][n-1] >= target and matrix[i][0] <= target):
                    for j in range(n):
                        if (matrix[i][j] ==  target):
                            return True
                    return False
            
        return False