from collections import deque
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root):
        result = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            result.append(node.val)

        dfs(root)
        return result

def build_tree(arr):
    if not arr:
        return None

    root = TreeNode(arr[0])
    queue = deque([root])
    i = 1

    while queue and i < len(arr):
        node = queue.popleft()

        if i < len(arr) and arr[i] is not None:
            node.left = TreeNode(arr[i])
            queue.append(node.left)
        i += 1

        if i < len(arr) and arr[i] is not None:
            node.right = TreeNode(arr[i])
            queue.append(node.right)
        i += 1

    return root

if __name__ == "__main__":
    arr = [1, None, 2, 3]

    root = build_tree(arr)

    sol = Solution()
    print(sol.postorderTraversal(root))
