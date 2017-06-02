public class Solution {
    public int lengthOfLongestSubstring(String s) {
      if(s.length() == 0)
        return 0;
       int right =0;
       int left = 0;
       int max = 1;
       boolean flag[] = new boolean [128];
       while(right < s.length())
       {
         if (flag[s.charAt(right)] == false)
          {  flag[s.charAt(right)] = true;

          right ++;
          max = max >( right -left)?max: right - left;
          }
        else
        {
          flag[s.charAt(left)] = false;
          left ++ ;
        }


       }
        return max;
    }
}
