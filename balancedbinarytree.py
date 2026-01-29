class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root):
        return self.checkHeight(root) != -1

    def checkHeight(self, node):
        if not node:
            return 0

        left = self.checkHeight(node.left)
        if left == -1:
            return -1

        right = self.checkHeight(node.right)
        if right == -1:
            return -1

        if abs(left - right) > 1:
            return -1

        return 1 + max(left, right)


if __name__ == "__main__":
    sol = Solution()
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    print("Is Balanced:", sol.isBalanced(root))  
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.left.left = TreeNode(3)

    print("Is Balanced:", sol.isBalanced(root2)) 
