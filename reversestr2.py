class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)

        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])

        return "".join(s)


# Testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseStr("abcdefg", 2))  # bacdfeg
    print(sol.reverseStr("abcd", 2))     # bacd