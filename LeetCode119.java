public class Solution {
    public List<Integer> getRow(int rowIndex) {
        List<Integer> ans = new ArrayList<Integer>(rowIndex + 1);
        List<int[]> result = new ArrayList<int[]>();
        for(int i =0;i <= rowIndex;++i){
        int []element = new int[i+1];
          for(int k =0;k<i+1;++k){
            element[k] = 1;
          }
          if( i>=2){
            for(int j =1;j<i;++j)
              element[j] = (result.get(i-1))[j-1]+ (result.get(i-1))[j];
          }
          result.add(element);
          if(i == rowIndex)
          {

            for(int q =0;q<rowIndex +1 ;++q){
              ans.add(element[q]);
            }
            return ans;
          }
        }

        return ans;

    }
}
