class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        carry = 0
        result = []

        while i >= 0 or j >= 0 or carry:
            total = carry

            if i >= 0:
                total += int(a[i])
                i -= 1

            if j >= 0:
                total += int(b[j])
                j -= 1

            result.append(str(total % 2))
            carry = total // 2

        return "".join(result[::-1])

if __name__ == "__main__":
    sol = Solution()

    a = "1010"
    b = "1011"

    print("Binary A:", a)
    print("Binary B:", b)

    ans = sol.addBinary(a, b)

    print("Sum in Binary:", ans)
