class Solution:
    def findWords(self, words):
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")

        result = []

        for word in words:
            w = word.lower()

            if set(w).issubset(row1) or set(w).issubset(row2) or set(w).issubset(row3):
                result.append(word)

        return result

if __name__ == "__main__":
    sol = Solution()

    words = ["Hello", "Alaska", "Dad", "Peace"]
    print(sol.findWords(words))   # Output: ['Alaska', 'Dad']