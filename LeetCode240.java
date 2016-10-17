public class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int i = 0;
        while(i < matrix.length){
          if(matrix[0][0] > target)
              return false;
          if(i == matrix.length - 1){
              for(int j =0; j< matrix[0].length;++j)
                 {
                     if(matrix[i][j] == target)
                        return true;
                 }
                 i++;
          }
          else if( matrix[i][matrix[0].length-1] < target)
              i+=1;
          else if(matrix[i][0] <= target && matrix[i][matrix[0].length-1] >= target)
          {
            int len = matrix[0].length;
            for(int j =0; j< len;++j){
              if(matrix[i][j] == target)
                return true;
            }
            i++;
          }
          else
                i+=1;
        }
        return  false;
    }
}
