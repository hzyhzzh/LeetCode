class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        width = board[0].__len__()
        height = board.__len__()
        flag = [[0]*width]*height
        for i in xrange(height):
            for j in xrange(width):
                flag = True
                if( board[i][j] == "o"):
                    '''
                    ：不考虑边界
                    '''
                    if(board[i+1][j] == "o" or flag[i+1][j] == 1):
                        flag =False
                    if(board[i][j+1] == "o" or flag[i][j+1] == 1):
                        flag =False
                    if(board[i-1][j] == "o" or flag[i-1][j] == 1):
                        flag =False
                    if(board[i][j-1] == "o" or flag[i][j-1] == 1):
                        flag =False
                        
                    if(not flag):
                       board[i][j] = "x" 
                       flag[i][j] = 1