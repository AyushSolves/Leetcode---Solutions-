class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTilt(self, root):
        self.tilt = 0

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            self.tilt += abs(left_sum - right_sum)

            return node.val + left_sum + right_sum

        dfs(root)
        return self.tilt

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

sol = Solution()
print("Tilt of tree:", sol.findTilt(root))