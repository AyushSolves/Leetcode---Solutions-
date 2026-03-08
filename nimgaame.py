class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0


# For VS Code / Local Testing
if __name__ == "__main__":
    sol = Solution()

    n1 = 4
    n2 = 1
    n3 = 2
    n4 = 8

    print("Input:", n1, "Output:", sol.canWinNim(n1))  # False
    print("Input:", n2, "Output:", sol.canWinNim(n2))  # True
    print("Input:", n3, "Output:", sol.canWinNim(n3))  # True
    print("Input:", n4, "Output:", sol.canWinNim(n4))  # False