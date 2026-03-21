class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        count = [0] * 26
        
        for c in s:
            count[ord(c) - ord('a')] += 1
        
        for i in range(len(s)):
            if count[ord(s[i]) - ord('a')] == 1:
                return i
        
        return -1

if __name__ == "__main__":
    sol = Solution()

    s1 = "leetcode"
    s2 = "loveleetcode"
    s3 = "aabb"

    print("Input:", s1, "Output:", sol.firstUniqChar(s1))  # 0
    print("Input:", s2, "Output:", sol.firstUniqChar(s2))  # 2
    print("Input:", s3, "Output:", sol.firstUniqChar(s3))  # -1