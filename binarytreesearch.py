class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root):
        freq = {}

        def dfs(node):
            if not node:
                return

            freq[node.val] = freq.get(node.val, 0) + 1

            dfs(node.left)
            dfs(node.right)

        dfs(root)

        max_freq = max(freq.values())

        result = []
        for key in freq:
            if freq[key] == max_freq:
                result.append(key)

        return result

if __name__ == "__main__":
    sol = Solution()

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.left = TreeNode(2)

    print(sol.findMode(root))   # Output: [2]