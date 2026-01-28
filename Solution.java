class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode(int val) {
        this.val = val;
    }
}

class Solution 
{

    public TreeNode sortedArrayToBST(int[] nums) 
    {
        return buildBST(nums, 0, nums.length - 1);
    }

    private TreeNode buildBST(int[] nums, int left, int right) 
    {
        if (left > right) return null;

        int mid = left + (right - left) / 2;
        TreeNode root = new TreeNode(nums[mid]);

        root.left = buildBST(nums, left, mid - 1);
        root.right = buildBST(nums, mid + 1, right);

        return root;
    }

    public void inorder(TreeNode root) 
    {
        if (root == null) return;
        inorder(root.left);
        System.out.print(root.val + " ");
        inorder(root.right);
    }

    public static void main(String[] args) 
    {
        Solution sol = new Solution();

        int[] nums = {-10, -3, 0, 5, 9};

        TreeNode root = sol.sortedArrayToBST(nums);

        System.out.print("Inorder Traversal of BST: ");
        sol.inorder(root);
    }
}
