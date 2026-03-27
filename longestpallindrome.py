class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        count = [0] * 128  # ASCII
        
        # Count frequency
        for c in s:
            count[ord(c)] += 1
        
        length = 0
        has_odd = False
        
        for freq in count:
            length += (freq // 2) * 2
            if freq % 2 == 1:
                has_odd = True
        
        # Add one odd character in center
        if has_odd:
            length += 1
        
        return length


# For VS Code / Local Testing
if __name__ == "__main__":
    sol = Solution()

    s1 = "abccccdd"
    s2 = "a"

    print("Input:", s1, "Output:", sol.longestPalindrome(s1))  # 7
    print("Input:", s2, "Output:", sol.longestPalindrome(s2))  # 1