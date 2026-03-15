class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        s = list(s)

        left = 0
        right = len(s) - 1

        while left < right:

            while left < right and s[left] not in vowels:
                left += 1

            while left < right and s[right] not in vowels:
                right -= 1

            s[left], s[right] = s[right], s[left]

            left += 1
            right -= 1

        return "".join(s)

if __name__ == "__main__":
    sol = Solution()

    s1 = "IceCreAm"
    s2 = "leetcode"

    print("Input:", s1, "Output:", sol.reverseVowels(s1))
    print("Input:", s2, "Output:", sol.reverseVowels(s2))