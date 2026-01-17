class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str = "Hello world"
        str.strip()
        words = s.split()
        return len(words[-1])
       