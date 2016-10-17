public class Solution {
    public boolean isValidSudoku(char[][] board) {
        for(int i =0;i<9;++i)
        {
          String s = "";
          for(int j=0;j<9;++j)
          {

              if(board[j][i] != '.' && (s.indexOf(board[j][i]) != -1))
                return false;
              s += board[j][i];
          }
        }
        for(int i =0;i<9;++i)
        {
          String s = "";
          for(int j=0;j<9;++j)
          {

              if(board[i][j] != '.' && (s.indexOf(board[i][j]) != -1))
                return false;
              s += board[i][j];
          }
        }
        for(int i =0;i<9;++i)
        {
          String s = "";
          int row = (i / 3)*3;
          int col = (i % 3)*3;
          for(int j=0;j<9;++j)
          {
            if(board[row + j/3 ][col+ j%3] != '.' && (s.indexOf(board[row + j/3][col+ j%3]) != -1))
              return false;
              s += board[row + j/3][col+ j%3];

          }
        }

        return true;
    }
}
