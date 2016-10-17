public class NumArray {
    private int[]num;
    public NumArray(int[] nums) {
        num = new int[nums.length];
        for(int i =0;i<nums.length;++i){
          num[i] = nums[i];
        }
    }

    public int sumRange(int i, int j) {
        int sum =0;
        for(int k =i;k<=j;++k){
          sum += num[k];
        }
        return sum;
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);
