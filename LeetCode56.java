/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        if(postorder.length == 0)
          return null;
        TreeNode root = create(inorder, postorder);
        return root;
    }
    public  TreeNode create(int []inorder, int [] postorder){

          TreeNode root = new TreeNode(postorder[postorder.length -1 ]);
          if(postorder.length == 1)
            return root;
          int point = postorder[postorder.length -1];
          int mid = 0;
          for(int i = 0;i < inorder.length;++i)
          {
            if(inorder[i] == point)
              {
                mid = i;
                break;
              }
          }
          int left_start =0;
          int left_end = mid -1;
          int right_start = mid + 1;
          int right_end = inorder.length-1;
          int []left_inorder =  Arrays.copyOfRange(inorder, left_start, left_end+1);
          int []left_postorder = Arrays.copyOfRange(postorder, left_start, left_end+1);
          int []right_inorder =  Arrays.copyOfRange(inorder, right_start, right_end+1);
          int []right_postorder =  Arrays.copyOfRange(postorder, left_end + 1, right_end);

          if(left_postorder.length >= 1)
          {
              root.left = create(left_inorder, left_postorder);
          }
          if(right_postorder.length >= 1)
          {
            root.right = create(right_inorder, right_postorder);
          }
          return root;


    }
}
