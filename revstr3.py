class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        for i in range(len(words)):
            words[i] = words[i][::-1]

        return " ".join(words)

if __name__ == "__main__":
    sol = Solution()
    print(sol.reverseWords("Let's take LeetCode contest"))

    print(sol.reverseWords("Mr Ding"))
