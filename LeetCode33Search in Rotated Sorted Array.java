public class Solution {
    public int search(int[] nums, int target) {
		int pivot = -1;
		if(nums.length == 0)
			return -1;
		if(nums.length == 1)
		    if(nums[0] == target)
		        return 0;
		    else
		        return -1;
		for(int i =0;i< nums.length-1;++i){
			if(nums[i] > nums[i+1])
			{
				pivot = i; 
				break;
				}
		}
		if(pivot == -1){
		    return binarysearch(nums,0,nums.length-1,target);
		}
		
		if(target > nums[pivot] || target < nums[pivot+1])
			return -1;
		if(target == nums[pivot])
		    return pivot;
			

		if(target < nums[pivot] && target >nums[nums.length-1])
			return binarysearch(nums,0,pivot,target);
		else if(target>= nums[pivot+1] && target <= nums[nums.length-1])
			return binarysearch(nums,pivot+1, nums.length-1, target);
			
		return -1;
    }
    	public int binarysearch(int[] nums,int begin, int end, int target)
		{
			while(begin<=end){
			    int mid = begin +(end-begin)/2;
			    if(nums[mid] == target)
			        return mid;
			     if(target > nums[mid])
			        begin = mid +1;
			     else
			        end = mid -1;
			      
			}
			return -1;
		}
}