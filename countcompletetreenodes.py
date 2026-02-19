class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root):

        def leftHeight(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height

        def rightHeight(node):
            height = 0
            while node:
                height += 1
                node = node.right
            return height

        if not root:
            return 0

        lh = leftHeight(root)
        rh = rightHeight(root)

        if lh == rh:
            return (1 << lh) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)

    sol = Solution()

    print("Number of nodes:", sol.countNodes(root))
