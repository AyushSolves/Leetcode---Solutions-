class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # check power of two and correct position
        return (n & (n - 1)) == 0 and (n - 1) % 3 == 0


# For VS Code / Local Testing
if __name__ == "__main__":
    sol = Solution()

    nums = [16, 5, 1, 64, 20]

    for n in nums:
        print(f"Input: {n} -> Output: {sol.isPowerOfFour(n)}")