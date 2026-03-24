class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i = 0  # pointer for s
        
        for char in t:
            if i < len(s) and s[i] == char:
                i += 1
        
        return i == len(s)


# For VS Code / Local Testing
if __name__ == "__main__":
    sol = Solution()

    s1, t1 = "abc", "ahbgdc"
    s2, t2 = "axc", "ahbgdc"

    print("Input:", s1, t1, "Output:", sol.isSubsequence(s1, t1))  # True
    print("Input:", s2, t2, "Output:", sol.isSubsequence(s2, t2))  # False