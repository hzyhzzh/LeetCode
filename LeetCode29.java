public class Solution {
    public int divide(int i_dividend, int i_divisor) {
      long x,y;
      long ans=0;
      int sign = 1;
      long dividend = (long)i_dividend;
      long divisor = (long)i_divisor;
      if(dividend == 0)
      return 0;
      if(dividend < 0 && divisor >0 )
        {
          sign = -1;
          dividend = -dividend;
        }
      else if( dividend >0 && divisor < 0)
        {
          divisor = -divisor;
          sign = -1;
        }
      else if(dividend <0 && divisor < 0)
      {
        divisor = -divisor;
        dividend = -dividend;
      }
      while(dividend>=divisor){
          x=divisor;
          y=1;
          while(dividend>=(x<<1)){
              x<<=1;
              y<<=1;
          }
          dividend-=x;
          ans+=y;
          if(ans == Integer.MAX_VALUE)
            return Integer.MAX_VALUE;
      }
      if(sign == -1)
        ans = -ans;

      if(ans>Integer.MAX_VALUE) return Integer.MAX_VALUE;
      else if(ans <Integer.MIN_VALUE) return Integer.MIN_VALUE;
      return (int)ans;
    }
  }
