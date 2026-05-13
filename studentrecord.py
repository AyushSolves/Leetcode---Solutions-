class Solution:
    def checkRecord(self, s: str) -> bool:
        # Less than 2 'A' and no "LLL"
        return s.count('A') < 2 and "LLL" not in s


# Testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.checkRecord("PPALLP"))  # True
    print(sol.checkRecord("PPALLL"))  # False