class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        return max(len(a), len(b))


# Testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.findLUSlength("aba", "cdc"))  # 3
    print(sol.findLUSlength("aaa", "bbb"))  # 3
    print(sol.findLUSlength("aaa", "aaa"))  #-1