class Solution:
    def sumOfLeftLeaves(self, root):
        return self.helper(root, False)

    def helper(self, node, is_left):
        if not node:
            return 0

        if not node.left and not node.right:
            return node.val if is_left else 0

        return self.helper(node.left, True) + self.helper(node.right, False)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print("Output:", sol.sumOfLeftLeaves(root))  # 24