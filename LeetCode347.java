public class Solution {
    public List<Integer> topKFrequent(int[] nums, int k) {
        Map<int,int> count = new HashMap(int,int);
        for(int i =0;i<nums.length;++i)
        {
          Integer num = (Integer)count.get(nums[i]);
          if(num == null)
            num =0;
          count.put(nums[i], num+1);
        }


    }
}
