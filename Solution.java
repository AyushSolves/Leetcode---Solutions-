import java.util.*;

public class Solution {

    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode(int val) { this.val = val; }
    }

    public List<String> binaryTreePaths(TreeNode root) {
        List<String> result = new ArrayList<>();
        
        if (root == null) {
            return result;
        }

        dfs(root, "", result);
        return result;
    }

    private void dfs(TreeNode node, String path, List<String> result) {

        if (node == null) return;

        if (node.left == null && node.right == null) {
            result.add(path + node.val);
            return;
        }

        dfs(node.left, path + node.val + "->", result);
        dfs(node.right, path + node.val + "->", result);
    }

    public static void main(String[] args) 
    {

        Solution sol = new Solution();
        TreeNode root = new TreeNode(1);
        root.left = new TreeNode(2);
        root.right = new TreeNode(3);
        root.left.right = new TreeNode(5);

        List<String> result = sol.binaryTreePaths(root);
        System.out.println(result);
    }
}