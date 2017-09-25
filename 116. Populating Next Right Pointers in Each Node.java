/**
 * Definition for binary tree with next pointer.
 * public class TreeLinkNode {
 *     int val;
 *     TreeLinkNode left, right, next;
 *     TreeLinkNode(int x) { val = x; }
 * }
 */
public class Solution {
    public void connect(TreeLinkNode root) {
        if(root == null){
            return ;
        }
        curlev = new TreeLinkNode();
        while(root.left!= null){
            curlev = root;
            while(curlev != null) {
                curlev.left.next = curlev.right;
                if(curlev.next!=null) {
                    curlev.right.next = curlev.next.left;
                    
                }
                curlev = curlev.next;
            }
            root = root.left;
        }
    }
}