class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        # Trick: check in (s + s)
        return s in (s + s)[1:-1]

if __name__ == "__main__":
    sol = Solution()

    s1 = "abab"
    s2 = "aba"
    s3 = "abcabcabcabc"

    print(sol.repeatedSubstringPattern(s1))  # True
    print(sol.repeatedSubstringPattern(s2))  # False
    print(sol.repeatedSubstringPattern(s3))  # True