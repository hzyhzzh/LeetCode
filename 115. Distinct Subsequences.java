public class Solution {  
    public int numDistinct(String S, String T) {  
        if(S==null||T==null) {  
            return 0;  
        }  
        if(S.length()<T.length()) {  
            return 0;  
        }  
    //递推公式用的  
        int [][] dp = new int[S.length()+1][T.length()+1];  
        dp[0][0] = 1;  
        //任意一个字符串变换成一个空串都只有一种变换方法  
        for(int i=0;i<S.length();i++) {  
            dp[i][0] = 1;      
        }  
        //递推公式  
        for(int i=1;i<=S.length();i++) {  
            for(int j=1;j<=T.length();j++) {  
                //如果S和T的当前字符相等，那么有两种选法；否则S的当前字符不能要  
                dp[i][j] = dp[i-1][j];  
                if(S.charAt(i-1)==T.charAt(j-1)) {  
                    dp[i][j] += dp[i-1][j-1];  
                }  
            }  
        }  
        return dp[S.length()][T.length()];  
    }  
} 