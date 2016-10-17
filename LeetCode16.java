### wrong answer
public class Solution {
    public int threeSumClosest(int[] nums, int target) {
        int gap = nums[0] + nums[1] + nums[2] - target;
        int sum = nums[0] + nums[1] + nums[2] ;
        if(nums.length == 3)
          return nums[0] + nums[1] + nums[2] ;
        int a1 = nums[0];
        int a2 = nums[1];
        int a3 = nums[2];



        return sum;
    }
}
