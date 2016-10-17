public class Solution {
public int lengthOfLIS(int[] nums) {
int n=nums.length;
int max = 0;
int I[]= new int[n+1];
Arrays.fill(I,Integer.MAX_VALUE);
I[0] = Integer.MIN_VALUE;
for(int i=0;i<n;i++){
int ind = Arrays.binarySearch(I ,nums[i]);
if(ind <0)
ind = -ind-1;
I[ind] = nums[i];
if(max < ind)
max =ind;
}
return max;
}
}
