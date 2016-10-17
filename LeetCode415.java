public class Solution {
    public String addStrings(String num1, String num2) {
        int l1 = num1.length();
        int l2 = num2.length();
        String longer;
        String shorter;
        int len = Math.max(l1, l2);
        int len_s = Math.min(l1, l2);
        if(l1 > l2)
        {
          longer = num1;
          shorter = num2;
        }
        else
        {
          longer = num2;
          shorter = num1;
        }
        String result="";
        int flag = 0;
        for(int i = 0;i<len;++i)
        {
            int a = longer.charAt(len - i - 1) -   48;
            int b = 0;
            if(i < len_s)
              b = shorter.charAt(len_s-i-1) - 48;
            int c = (a+b+flag)% 10;

            result = c + flag  + result;
            flag = (a+b+flag) / 10;
        }
        if(flag == 1)
          result = flag + result;

        return result;
    }
}
