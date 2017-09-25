class Solution {
    public boolean isHappy(int n) {
        while( broke(n) != 1) {
            n = broke(n);
            if(n == 20)
                return false;
        }
        return true;
    }
    public int broke(int n) {
        int sum = 0;
        while(n != 0) {
            sum = sum + (n%10) * (n%10);
            n = n / 10;
        }
        return sum;
    }
}