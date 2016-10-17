***///题目理解错误**

public class Solution {
    public int[] maxNumber(int[] nums1, int[] nums2, int k) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int []result = new int[k];
        int len1 = nums1.length;
        int len2 = nums2.length;
        int i =0;
        int index1 = len1;
        int index2 = len2;
        while(i < k){
          if(index1 ==-1){
            result[i] = nums2[index2];
            index2 --;
            i++;
          }
          else if(index2 == -1){
            result[i] = nums1[index1];
            index1 --;
            i++;
          }

          else if(nums1[index1] > nums2[index2])
          {

                result[i] = nums1[index1];
                index1--;
                i++;
          }
          else if(nums1[index1] < nums2[index2])
          {
                result[i] = nums2[index2];
                index2--;
                i++;
          }
          else if(nums1[index1] ==  nums2[index2]){
               if(i == k-1){
                result[i] = nums2[index2];
                 return result;
               }
               else{
                  result[i] = nums2[index2];
                  i++;
                  result[i] = nums2[index2];
                   i+=1;
               }
          }
        }
        return result;
    }
}
