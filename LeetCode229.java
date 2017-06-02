//摩尔投票法
public class Solution {
    public List<Integer> majorityElement(int[] nums) {
         List<Integer> result = new ArrayList<Integer>();
        if(nums.length == 0)
            return result;
        if(nums.length == 1)
        {
            result.add((Integer)nums[0]);
            return result;
        }
        if(nums.length == 2)
        {
            result.add((Integer)nums[0]);
            if(nums[0] != nums[1])
            result.add((Integer)nums[1]);
            return result;
        }
        int num1=0, num2 =0, num1_c = 0, num2_c = 0;
        for(int num : nums)
        {
          if(num == num1)num1_c++;
          else if(num == num2)num2_c++;
          else if(num1_c == 0) {num1= num;num1_c=1;}
          else if(num2_c == 0) {num2 =num;num2_c=1;}
          else {num1_c--;num2_c--;}
        }
        num1_c = num2_c = 0;
        for(int num : nums)
        {
          if(num == num1)num1_c++;
          else if(num == num2)num2_c++;
        }

        if( num1_c > (nums.length/3) ) result.add((Integer)num1_c);
        if( num2_c > (nums.length/3) ) result.add((Integer)num2_c);

          return result;
    }
}
