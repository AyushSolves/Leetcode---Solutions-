class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # If lengths differ, cannot be anagram
        if len(s) != len(t):
            return False
        
        count = [0] * 26  # For lowercase English letters
        
        # Count characters
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        
        # If all values are 0 → anagram
        for num in count:
            if num != 0:
                return False
        
        return True