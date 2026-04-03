class Solution:
    def countSegments(self, s: str) -> int:
        
        count = 0
        
        for i in range(len(s)):
            # Start of a new word
            if s[i] != ' ' and (i == 0 or s[i - 1] == ' '):
                count += 1
        
        return count

if __name__ == "__main__":
    sol = Solution()

    s1 = "Hello, my name is John"
    s2 = "Hello"
    s3 = "   fly me   to   the moon  "

    print(sol.countSegments(s1))  # 5
    print(sol.countSegments(s2))  # 1
    print(sol.countSegments(s3))  # 5