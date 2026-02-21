from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root):
        if root is None:
            return None
        
        # swap left and right
        root.left, root.right = root.right, root.left
        
        # invert subtrees
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root

# Function to print tree (level order)
def printTree(root):
    if not root:
        return
    
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        print(node.val, end=" ")
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Create example tree [4,2,7,1,3,6,9]
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(9)

# Invert tree
sol = Solution()
root = sol.invertTree(root)

# Print output
print("Output:")
printTree(root)