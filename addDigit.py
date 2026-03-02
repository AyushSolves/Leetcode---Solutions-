class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9


# For VS Code / local testing
if __name__ == "__main__":
    sol = Solution()
    
    num1 = 38
    num2 = 0

    print(f"Input: {num1} -> Output:", sol.addDigits(num1))  # 2
    print(f"Input: {num2} -> Output:", sol.addDigits(num2))  # 0